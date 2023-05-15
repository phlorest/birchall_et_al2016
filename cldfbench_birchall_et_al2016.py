import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "birchall_et_al2016"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree(
                'relaxed-binary-simple.time.mcct.trees', detranslate=True),
            self.metadata,
            args.log)

        args.writer.add_posterior(
            self.raw_dir.read_trees(
                'relaxed-binary-simple.time.trees.gz',
                burnin=10000,
                sample=1000,
                detranslate=True),
            self.metadata, 
            args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('Chapacuran_Swadesh207-2019-labelled.nex'),
            self.characters, 
            args.log)
