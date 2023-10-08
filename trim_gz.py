import os

fileread=['LGZ17-MQ01_550bp_1_S6_L002',\
'LGZ17-MQ01_550bp_2_S7_L002',\
'LGZ17-MQ01_550bp_3_S8_L002',\
'LGZ17-MQ01_550bp_4_S9_L002',\
'LGZ17-MQ01_550bp_S1_L002']

reads2=['LGZ18_MQ01_550bp_01_GGTTTACT_L002',\
'LGZ18_MQ01_550bp_02_CTAAACGG_L002',\
'LGZ18_MQ01_550bp_03_TCGGCGTC_L002',\
'LGZ18_MQ01_550bp_04_AACCGTAA_L002']


os.chdir('/home/jpanibe/CLC_Data/TN1')

i=0
while i<len(fileread):
	os.system('java -jar /home/jpanibe/CLC_Data/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 16 -trimlog log.txt %s_R1_001.fastq.gz %s_R2_001.fastq.gz %s_minlen150_R1.fastq.gz %s_minlen75_R1.fastq_noadapter_s1_se.gz %s_minlen150_R2.fastq.gz %s_minlen75_R2.fastq_noadapter_s2_se.gz CROP:150' % (fileread[i],fileread[i],fileread[i],fileread[i],fileread[i],fileread[i]))
	i+=1


i=0
while i<len(reads2):
	os.system('java -jar /home/jpanibe/CLC_Data/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 16 -trimlog log.txt %s_R1.fastq.gz %s_R2.fastq.gz %s_minlen150_R1.fastq.gz %s_minlen75_R1.fastq_noadapter_s1_se.gz %s_minlen150_R2.fastq.gz %s_minlen75_R2.fastq_noadapter_s2_se.gz CROP:150' % (reads2[i],reads2[i],reads2[i],reads2[i],reads2[i],reads2[i]))
	i+=1
