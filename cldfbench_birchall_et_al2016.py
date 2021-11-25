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

        posterior = self.sample(
            self.remove_burnin(
                self.raw_dir.read('relaxed-binary-simple.time.trees.gz'),
                10000),
            detranslate=True,
            as_nexus=True)

        args.writer.add_posterior(
            posterior.trees.trees, 
            self.metadata, 
            args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('Chapacuran_Swadesh207-2019-labelled.nex'),
            self.characters, 
            args.log)

