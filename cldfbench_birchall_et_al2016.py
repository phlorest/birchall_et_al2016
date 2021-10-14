import gzip
import shutil
import pathlib

import nexus
from pydplace import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "birchall_et_al2016"

    def cmd_makecldf(self, args):
        self.add_schema(args)
        shutil.copy(self.raw_dir / 'source.bib', self.cldf_dir / 'sources.bib')
        lids = self.add_taxa(args)

        f = nexus.NexusReader(self.raw_dir / 'relaxed-binary-simple.time.mcct.trees')
        f.trees.detranslate()

        assert len(f.trees.trees) == 1
        summary = f.trees.trees[0]
        phlorest.check_tree(summary, lids, args.log)

        with phlorest.NexusFile(self.cldf_dir / 'summary.nex') as nex:
            nex.append(summary)

            args.writer.objects['trees.csv'].append(dict(
                ID='summary',
                Name=summary.name,
                Nexus_File=nex.path.name,
                rooted=summary.rooted,
                type='summary',
                method='Consensus tree from a bayesian analysis',
                scaling=self.metadata.scaling,
                Source=['Birchall_et_al2016'],
            ))

        with gzip.open(self.raw_dir / 'relaxed-binary-simple.time.trees.gz') as f:
            posterior = f.read().decode('utf8')
            posterior = self.run_nexus('--log-level WARNING trees -c -d 1-10000', posterior)
            # FIXME: set random seed!?
            posterior = nexus.NexusReader.from_string(
                self.run_nexus('trees --random-seed 12345 -t -n 1000', posterior))

        with phlorest.NexusFile(self.cldf_dir / 'posterior.nex') as nex:
            for i, tree in enumerate(posterior.trees.trees, start=1):
                phlorest.check_tree(tree, lids, args.log)
                nex.append(tree)

                args.writer.objects['trees.csv'].append(dict(
                ID='posterior-{}'.format(i),
                Name=tree.name,
                Nexus_File=nex.path.name,
                rooted=tree.rooted,
                type='sample',
                method='Sample from posterior of a bayesian analysis',
                scaling=self.metadata.scaling,
                Source=['Birchall_et_al2016'],
            ))
