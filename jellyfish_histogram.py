import os

kmersize=['17','21','25']

i=0

while i<len(kmersize):
	os.system("/home/jpanibe/CLC_Data/Jellyfish/jellyfish-2.3.0/bin/jellyfish histo -t 16 allreads_kmer%s.jf > reads_kmer%s.histo" % (kmersize[i],kmersize[i]))
	i+=1

