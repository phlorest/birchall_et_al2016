import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "birchall_et_al2016"

    def cmd_makecldf(self, args):
        self.init(args)

        with phlorest.NexusFile(self.cldf_dir / 'summary.trees') as nex:
            self.add_tree_from_nexus(
                args,
                self.raw_dir / 'relaxed-binary-simple.time.mcct.trees',
                nex,
                'summary',
                'summary',
                detranslate=True,
            )

        posterior = self.sample(
            self.remove_burnin(
                self.read_gzipped_text(self.raw_dir / 'relaxed-binary-simple.time.trees.gz'),
                10000),
            detranslate=True,
            as_nexus=True)

        with phlorest.NexusFile(self.cldf_dir / 'posterior.trees') as nex:
            for i, tree in enumerate(posterior.trees.trees, start=1):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i), 'sample')

        self.add_data(args, self.raw_dir / 'Chapacuran_Swadesh207-2019-labelled.nex')