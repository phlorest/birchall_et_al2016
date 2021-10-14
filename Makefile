all: summary.trees posterior.trees data.nex

summary.nex: raw/relaxed-binary-simple.time.mcct.trees
	cp $< cldf/$@

posterior.nex: raw/relaxed-binary-simple.time.trees.gz
	# remove 10000 (50%), sample 1000 from remainder
	gunzip -c $< > tmp
	nexus trees -c -d 1-10000 tmp -o tmp2
	nexus trees --random-seed 12345 -t -n 1000 tmp2 -o cldf/$@
	rm tmp tmp2

data.nex:
	cp raw/Chapacuran_Swadesh207-2019-labelled.nex cldf/$@
