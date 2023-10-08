import os

data=["ERR619929", \
"ERR619928", \
"ERR619927", \
"ERR619926", \
"ERR619925", \
"ERR619924", \
"ERR619923", \
"ERR619922", \
"ERR619921", \
"ERR619920", \
"ERR619919", \
"ERR619918", \
"ERR619917", \
"ERR619916"]

os.chdir('/home/jpanibe/SRA_data')

i=0
while i<len(data):
	os.system('/home/jpanibe/CLC_Data/sratoolkit/sratoolkit.2.10.5-centos_linux64/bin/fastq-dump --split-files %s' % data[i])
	i+=1

