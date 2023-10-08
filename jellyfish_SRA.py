import os

fileread=['SRR8652337',\
'SRR3056114',\
'SRR3056468',\
'SRR3056278',\
'SRR3056466']


os.chdir('/home/jpanibe/CLC_Data/SRA_data')

i=0
while i<len(fileread):
	os.system('java -jar /home/jpanibe/CLC_Data/Trimmomatic-0.39/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 16 -trimlog log_jellyfish_SRA.txt %s_R1.fastq %s_R2.fastq %s_minlen75_R1.fastq %s_minlen75_R1.fastq_noadapter_s1_se %s_minlen75_R2.fastq %s_minlen75_R2.fastq_noadapter_s2_se ILLUMINACLIP:/home/jpanibe/CLC_Data/Trimmomatic-0.39/Trimmomatic-0.39/adapters/adapters.fa:2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:4:20 MINLEN:75' % (fileread[i],fileread[i],fileread[i],fileread[i],fileread[i],fileread[i]))
	i+=1



