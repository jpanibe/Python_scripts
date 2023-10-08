########################################################################################################
# Date created: March 31, 2014                                                                         #
# Author: Jerome P. Panibe                                                                             #
#                                                                                                      #
# This python script will perform sga preqc for all the readsets of the adapter and linker free TNG67  #
#                                                                                                      #
########################################################################################################

import os

files_pe=['HS1']
'''
files_pe=['GA1','GA2','HS1','HS2','HS3','HS4','HS5','HS6','MS1','MS2','L1','L2']
files_mp=['MP2','MP3','MP4','MP5','MP6','MP7','MP8','MP9']
'''

#os.system('export LD_LIBRARY_PATH=/usr/local/lib64:$LD_LIBRARY_PATH')
#os.system('export PATH=/SDATA/tools/anaconda-1.9.0/bin/:$PATH')

os.environ["LD_LIBRARY_PATH"]="/usr/local/lib64:$LD_LIBRARY_PATH"
os.environ["PATH"]="/SDATA/tools/anaconda-1.9.0/bin/:$PATH"


i=0
while i<len(files_pe):
        os.chdir('/home/jpanibe/TNG67/PE/HS1')
	os.system('/SDATA/tools/sga/bin/sga preprocess --pe-mode 1 %s_trimmed_1.fastq %s_trimmed_2.fastq > %s_trimmed10bp.fastq'% (files_pe[i],files_pe[i],files_pe[i]))
        os.system('/SDATA/tools/sga/bin/sga index -a ropebwt -t 8 --no-reverse %s_trimmed10bp.fastq' % files_pe[i])
        os.system('/SDATA/tools/sga/bin/sga preqc -t 8 %s_trimmed10bp.fastq > %s_trimmed10bp.preqc' % (files_pe[i],files_pe[i]))
        os.system('/SDATA/tools/sga/src/bin/sga-preqc-report.py %s_trimmed10bp.preqc *.preqc' % files_pe[i])
	os.system('/SDATA/tools/sga/bin/sga correct --learn -t 8 -o %s_trimmed10bp_basecorrected.fastq %s_trimmed10bp.fastq'% (files_pe[i],files_pe[i]))
        i+=1


'''
i=0
while i<len(files_mp):
        os.chdir('/home/jpanibe/TNG67/MP')
        os.system('/SDATA/tools/sga/bin/sga preprocess --pe-mode 1 %s_trimmed_1.fastq %s_trimmed_2.fastq > %s_trimmed10bp.fastq'% (files_mp[i],files_mp[i],files_mp[i]))
        os.system('/SDATA/tools/sga/bin/sga index -a ropebwt -t 8 --no-reverse %s_trimmed10bp.fastq' % files_mp[i])
        os.system('/SDATA/tools/sga/bin/sga preqc -t 8 %s_trimmed10bp.fastq > %s_trimmed10bp.preqc' % (files_mp[i],files_mp[i]))
        os.system('/SDATA/tools/sga/src/bin/sga-preqc-report.py %s_trimmed10bp.preqc *.preqc' % files_mp[i])
	os.system('/SDATA/tools/sga/bin/sga correct --learn -t 8 -o %s_trimmed10bp_basecorrected.fastq %s_trimmed10bp.fastq'% (files_mp[i],files_mp[i]))
	i+=1
'''    












 

