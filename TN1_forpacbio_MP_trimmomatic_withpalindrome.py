#####################################################################
# Date: August 2, 2014                                               #
# Author: Jerome P. Panibe                                          #
#                                                                   #
# This script will remove the adapters in raw TNG67 mate-pair data  #
#                                                                   #
#####################################################################

import os

files150=['LGM17-LS01_1K_TGACCA_L002', \
'LGM17-LS01_3K_ACAGTG_L002', \
'LGM17-LS01_5K_GCCAAT_L002', \
'LGM17-LS01_8K_CAGATC_L002', \
'LGM17-LS01_12K_CTTGTA_L002', \
'LGM17-LS01_20K_GTGAAA_L002']


i=0
while i<len(files150):
        os.chdir('/home/jpanibe/TNG67/PE')
        os.system('java -jar /home/jpanibe/Bioinformatics/bago-Trimmomatic/trimmomatic-Binary_0.36/Trimmomatic-0.36/trimmomatic-0.36.jar PE -threads 16 -trimlog %s_trimmomatic_trimlog_withpalindrome.txt %s_R1.fastq %s_R2.fastq %s_trimmomatic_R1.fastq %s_trimmomatic_R1.fastq_noadapter_s1_se %s_trimmomatic_R2.fastq %s_trimmomatic_R2.fastq_noadapter_s2_se ILLUMINACLIP:/home/jpanibe/Bioinformatics/bago-Trimmomatic/trimmomatic-0.36/adapters/all.fa:2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:4:20 CROP:250' % (files150[i],files150[i],files150[i],files150[i],files150[i],files150[i],files150[i]))                   
        i+=1



