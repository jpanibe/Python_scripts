import os

kmersize=['65','69','71','75']

i=0

while i<len(kmersize):
	os.system("/home/jpanibe/CLC_Data/Jellyfish/jellyfish-2.3.0/bin/jellyfish count -C -m %s -s 1000000000 -t 16 TNG67_allreads.fastq -o TNG67_allreads_kmer%s.jf" % (kmersize[i],kmersize[i]))
	i+=1

