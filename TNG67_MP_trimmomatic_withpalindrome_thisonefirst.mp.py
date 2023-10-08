#####################################################################
# Date: August 2, 2014                                               #
# Author: Jerome P. Panibe                                          #
#                                                                   #
# This script will remove the adapters in raw TNG67 mate-pair data  #
#                                                                   #
#####################################################################

import os

files150=['SG_DE01_MP2_4kb_AGTTCC_L002', \
'SG_DE01_MP4_6kb_GTGAAA_L002', \
'SG_DE01_MP6_10kb_TGACCA_L002']



i=0
while i<len(files150):
	os.chdir('/home/jpanibe/CLC_Data')
	os.system('java -jar /home/jpanibe/CLC_Data/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 16 -trimlog %s_trimmomatic_trimlog_withpalindrome_NxTrim_thisonefirst.txt %s.mp.f.fastq %s.mp.r.fastq %s_trimmomatic.mp.f.fastq %s_trimmomatic.mp.f.fastq_noadapter_s1_se %s_trimmomatic.mp.r.fastq %s_trimmomatic.mp.r.fastq_noadapter_s2_se ILLUMINACLIP:/home/jpanibe/CLC_Data/Trimmomatic-0.39/adapters/adapters.fa:2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:4:20 MINLEN:30 CROP:150' % (files150[i],files150[i],files150[i],files150[i],files150[i],files150[i],files150[i]))
	i+=1



