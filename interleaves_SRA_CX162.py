import os

fileread=["ERR635473", \
"ERR635484", \
"ERR635483", \
"ERR635482", \
"ERR635481", \
"ERR635480", \
"ERR635479", \
"ERR635478", \
"ERR635477", \
"ERR635476", \
"ERR635475", \
"ERR635474"]


os.chdir("/home/jpanibe/SRA_data")

i=0
while i<len(fileread):
	os.system("/home/jpanibe/CLC_Data/BBMap/bbmap/reformat.sh \
in1=%s_trimmomatic_minlen50_R1.fastq \
in2=%s_trimmomatic_minlen50_R2.fastq \
out=%s_trimmomatic_minlen50.fastq" % (fileread[i],fileread[i],fileread[i]))
	i+=1
