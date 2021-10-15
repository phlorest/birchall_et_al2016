import gzip
import pathlib

import nexus
from pydplace import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "birchall_et_al2016"

    def cmd_makecldf(self, args):
        self.init(args)

        with phlorest.NexusFile(self.cldf_dir / 'summary.trees') as nex:
            f = nexus.NexusReader(self.raw_dir / 'relaxed-binary-simple.time.mcct.trees')
            f.trees.detranslate()
            assert len(f.trees.trees) == 1
            self.add_tree(args, f.trees.trees[0], nex, 'summary', 'summary')

        with gzip.open(self.raw_dir / 'relaxed-binary-simple.time.trees.gz') as f:
            posterior = nexus.NexusReader.from_string(
                self.sample(self.remove_burnin(f.read().decode('utf8'), 10000), detranslate=True))

        with phlorest.NexusFile(self.cldf_dir / 'posterior.trees') as nex:
            for i, tree in enumerate(posterior.trees.trees, start=1):
                self.add_tree(
                    args, tree, nex, 'posterior-{}'.format(i), 'sample')

        self.add_data(args, self.raw_dir / 'Chapacuran_Swadesh207-2019-labelled.nex')