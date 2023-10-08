#####################################################################
# Date: August 2, 2014                                               #
# Author: Jerome P. Panibe                                          #
#                                                                   #
# This script will remove the adapters in raw TNG67 mate-pair data  #
#                                                                   #
#####################################################################

import os

files150=["ERR635473", \
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



i=0
while i<len(files150):
	os.chdir('/home/jpanibe/SRA_Data')
	os.system('java -jar /home/jpanibe/CLC_Data/Trimmomatic-0.39/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 16 -trimlog %s_trimmomatic_TN1_other_NCBI_reads.txt %s_1.fastq %s_2.fastq %s_trimmomatic_minlen50_R1.fastq %s_trimmomatic_minlen50_R1.fastq_noadapter_s1_se %s_trimmomatic_minlen50_R2.fastq %s_trimmomatic_minlen50_R2.fastq_noadapter_s2_se ILLUMINACLIP:/home/jpanibe/CLC_Data/Trimmomatic-0.39/Trimmomatic-0.39/adapters/adapters.fa:2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:4:20 MINLEN:50 CROP:82' % (files150[i],files150[i],files150[i],files150[i],files150[i],files150[i],files150[i]))
	i+=1



