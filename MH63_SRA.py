import os

fileread=['SRR1743093',\
'SRR1743095',\
'SRR1743097',\
'SRR1743098']


os.chdir('/home/jpanibe/SRA_data')

i=0
while i<len(fileread):
	os.system('java -jar /home/jpanibe/CLC_Data/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 16 -trimlog log_MH63_SRA.txt %s.fastq %s.fastq %s_minlen90_R1.fastq %s_minlen90_R1.fastq_noadapter_s1_se %s_minlen90_R2.fastq %s_minlen90_R2.fastq_noadapter_s2_se ILLUMINACLIP:/home/jpanibe/CLC_Data/Trimmomatic-0.39/adapters/adapters.fa:2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:4:20 MINLEN:90 CROP:100' % (fileread[i],fileread[i],fileread[i],fileread[i],fileread[i],fileread[i]))
	i+=1



