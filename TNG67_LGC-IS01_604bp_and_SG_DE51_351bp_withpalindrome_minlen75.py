#####################################################################
# Date: August 2, 2014                                               #
# Author: Jerome P. Panibe                                          #
#                                                                   #
# This script will remove the adapters in raw TNG67 mate-pair data  #
#                                                                   #
#####################################################################

import os

files150=['SG_DE51_351bp_CGATGT_L001']
files300=['LGC-IS01_604bp_GATCAG_L001']

i=0
while i<len(files150):
	os.chdir('/home/jpanibe/CLC_Data')
	os.system('java -jar /home/jpanibe/CLC_Data/Trimmomatic-0.39/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 16 -trimlog %s_trimmomatic_minlen75_trimlog_withpalindrome.txt %s_R1.fastq %s_R2.fastq %s_trimmomatic_minlen75_R1.fastq %s_trimmomatic_minlen75_R1.fastq_noadapter_s1_se %s_trimmomatic_minlen75_R2.fastq %s_trimmomatic_minlen75_R2.fastq_noadapter_s2_se ILLUMINACLIP:/home/jpanibe/CLC_Data/Trimmomatic-0.39/Trimmomatic-0.39/adapters/adapters.fa:2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:4:20 MINLEN:75 CROP:150' % (files150[i],files150[i],files150[i],files150[i],files150[i],files150[i],files150[i]))
	i+=1


i=0
while i<len(files300):
	os.chdir('/home/jpanibe/CLC_Data')
	os.system('java -jar /home/jpanibe/CLC_Data/Trimmomatic-0.39/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 16 -trimlog %s_trimmomatic_minlen150_trimlog_withpalindrome.txt %s_R1.fastq %s_R2.fastq %s_trimmomatic_minlen150_R1.fastq %s_trimmomatic_minlen150_R1.fastq_noadapter_s1_se %s_trimmomatic_minlen150_R2.fastq %s_trimmomatic_minlen150_R2.fastq_noadapter_s2_se ILLUMINACLIP:/home/jpanibe/CLC_Data/Trimmomatic-0.39/Trimmomatic-0.39/adapters/adapters.fa:2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:4:20 MINLEN:150 CROP:300' % (files300[i],files300[i],files300[i],files300[i],files300[i],files300[i],files300[i]))
	i+=1

