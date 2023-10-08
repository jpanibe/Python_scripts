import os

data=["SRR8652337_minlen75", \
"SRR3056114_minlen75", \
"SRR3075258_and_SRR3056468_minlen75", \
"SRR3056278_minlen75", \
"SRR3056466_minlen75"]

os.chdir('/home/jpanibe/CLC_Data/SRA_data')

i=0
while i<len(data):
	os.system("/home/jpanibe/CLC_Data/Jellyfish/jellyfish-2.3.0/bin/jellyfish count -C -m 21 -s 1000000000 -t 16 %s.fastq -o %s_kmer21.jf" % (data[i],data[i]))
	i+=1

