import os

kmersize=["SRR8652337_minlen75", \
"SRR3056114_minlen75", \
"SRR3075258_and_SRR3056468_minlen75", \
"SRR3056278_minlen75", \
"SRR3056466_minlen75"]

os.chdir("/home/jpanibe/CLC_Data/SRA_data")

i=0
while i<len(kmersize):
	os.system("/home/jpanibe/CLC_Data/Jellyfish/jellyfish-2.3.0/bin/jellyfish histo -t 16 %s_kmer21.jf > %s_kmer21.histo" % (kmersize[i],kmersize[i]))
	i+=1

