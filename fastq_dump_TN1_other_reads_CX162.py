import os

#data=["ERR635478", \
#"ERR635477", \
#"ERR635476", \
#"ERR635475", \
#"ERR635474"]


#data=["ERR635479", \
#"ERR635480", \
#"ERR635481", \
#"ERR635482", \
#"ERR635483", \
#"ERR635484"]


data=["ERR635473"]

os.chdir('/home/jpanibe/SRA_data')

i=0
while i<len(data):
	os.system('/home/jpanibe/CLC_Data/sratoolkit/sratoolkit.2.10.5-centos_linux64/bin/fastq-dump --split-files %s' % data[i])
	i+=1

