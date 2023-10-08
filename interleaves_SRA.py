import os

fileread=['ERR619929', \
'ERR619928', \
'ERR619927', \
'ERR619926', \
'ERR619925', \
'ERR619924', \
'ERR619923', \
'ERR619922', \
'ERR619921', \
'ERR619920', \
'ERR619919', \
'ERR619918', \
'ERR619917', \
'ERR619916']

os.chdir("/home/jpanibe/SRA_data")

i=0
while i<len(fileread):
	os.system("/home/jpanibe/CLC_Data/BBMap/bbmap/reformat.sh \
in1=%s_trimmomatic_minlen50_R1.fastq \
in2=%s_trimmomatic_minlen50_R2.fastq \
out=%s_trimmomatic_minlen50.fastq" % (fileread[i],fileread[i],fileread[i]))
	i+=1
