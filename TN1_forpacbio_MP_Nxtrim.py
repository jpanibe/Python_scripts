#####################################################################
# Date: August 2, 2014                                               #
# Author: Jerome P. Panibe                                          #
#                                                                   #
# This script will remove the adapters in raw TNG67 mate-pair data  #
#                                                                   #
#####################################################################

import os

files150=['LGM17-LS01_12K_CTTGTA_L002', \
'LGM17-LS01_1K_TGACCA_L002', \
'LGM17-LS01_20K_GTGAAA_L002', \
'LGM17-LS01_3K_ACAGTG_L002', \
'LGM17-LS01_5K_GCCAAT_L002', \
'LGM17-LS01_8K_CAGATC_L002']



i=0
while i<len(files150):
	os.chdir('/home/jpanibe/CLC_Data')
	os.system('/home/jpanibe/CLC_Data/NxTrim/NxTrim/nxtrim -1 %s_R1.fastq -2 %s_R2.fastq --rf -O %s' % (files150[i],files150[i],files150[i]))	
	i+=1








"""
files150=['LGM17-LS01_1K_TGACCA_L002_NxTrim_thisonefirst', \
'LGM17-LS01_3K_ACAGTG_L002_NxTrim_thisonefirst', \
'LGM17-LS01_5K_GCCAAT_L002_NxTrim_thisonefirst', \
'LGM17-LS01_8K_CAGATC_L002_NxTrim_thisonefirst', \
'LGM17-LS01_12K_CTTGTA_L002_NxTrim_thisonefirst', \
'LGM17-LS01_20K_GTGAAA_L002_NxTrim_thisonefirst']
"""
