import os

kmersize=['17','21','25','31']

i=0

while i<len(kmersize):
	os.system("/home/jpanibe/CLC_Data/Jellyfish/jellyfish-2.3.0/bin/jellyfish count -C -m %s -s 1000000000 -t 16 allreads.fastq -o allreads_kmer%s.jf " % (kmersize[i],kmersize[i]))
	i+=1

