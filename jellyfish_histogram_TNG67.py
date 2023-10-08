import os


kmersize=['65','69','71','75']

i=0

while i<len(kmersize):
	os.system("/home/jpanibe/CLC_Data/Jellyfish/jellyfish-2.3.0/bin/jellyfish histo -t 16 TNG67_allreads_kmer%s.jf > TNG67_reads_kmer%s.histo" % (kmersize[i],kmersize[i]))
	i+=1

