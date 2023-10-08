#####################################################################
# Date: August 2, 2014                                               #
# Author: Jerome P. Panibe                                          #
#                                                                   #
# This script will remove the adapters in raw TNG67 mate-pair data  #
#                                                                   #
#####################################################################

import os

files150=['ec']

i=0
while i<len(files150):
        os.chdir('/home/jpanibe/CLC_Data')
        os.system('java -jar /home/jpanibe/CLC_Data/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 16 -trimlog %s_trimmomatic_minlen215_trimlog_withpalindrome_forREAPR.txt %s.f.fq %s.r.fq %s_trimmomatic_minlen215_ec.f_forREAPR.fastq %s_trimmomatic_minlen215_ec.f_forREAPR.fastq_noadapter_s1_se %s_trimmomatic_minlen215_ec.r_forREAPR.fastq %s_trimmomatic_minlen215_ec.r_forREAPR.fastq_noadapter_s2_se MINLEN:215 CROP:215' % (files150[i],files150[i],files150[i],files150[i],files150[i],files150[i],files150[i]))	
	i+=1
