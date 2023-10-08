import os

fileread=['LGZ17-MQ01_550bp_1_S1_L002']
"""
reads2=['TN1_1_S1_L002',\
'TN1_2_S2_L002',\
'TN1_3_S3_L002',\
'TN1_4_S4_L002']
"""

os.chdir('/home/jpanibe/CLC_Data/TN1_10x_correctdata/TN1_10x_correctdata')

i=0
while i<len(fileread):
	os.system('java -jar /home/jpanibe/CLC_Data/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 16 -trimlog log.txt %s_R1_001.fastq.gz %s_R2_001.fastq.gz %s_minlen150_R1.fastq.gz %s_minlen75_R1.fastq_noadapter_s1_se %s_minlen150_R2.fastq.gz %s_minlen75_R2.fastq_noadapter_s2_se CROP:150' % (fileread[i],fileread[i],fileread[i],fileread[i],fileread[i],fileread[i]))
	i+=1

"""
i=0
while i<len(reads2):
	os.system('java -jar /home/jpanibe/CLC_Data/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 16 -trimlog log.txt %s_R1_001.fastq.gz %s_R2_001.fastq.gz %s_minlen150_R1.fastq.gz %s_minlen75_R1.fastq_noadapter_s1_se %s_minlen150_R2.fastq.gz %s_minlen75_R2.fastq_noadapter_s2_se CROP:150' % (reads2[i],reads2[i],reads2[i],reads2[i],reads2[i],reads2[i]))
	i+=1
"""
