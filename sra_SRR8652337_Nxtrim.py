#####################################################################
# Date: August 2, 2014                                               #
# Author: Jerome P. Panibe                                          #
#                                                                   #
# This script will remove the adapters in raw TNG67 mate-pair data  #
#                                                                   #
#####################################################################

import os

files150=['SRR8652337']


i=0
while i<len(files150):
	os.chdir('/home/jpanibe/CLC_Data/SRA_data')
	os.system('/home/jpanibe/CLC_Data/NxTrim/NxTrim/nxtrim -1 %s_R1.fastq -2 %s_R2.fastq --rf -O %s' % (files150[i],files150[i],files150[i]))	
	i+=1




