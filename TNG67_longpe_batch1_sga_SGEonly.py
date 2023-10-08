import os

files_pe=['SG_DE01_C_1062bp_GATCAG_L001_trimmomatic', \
'SG-DE01-C-1062bp_GATCAG_L001_trimmomatic', \
'SG_DE01_D_1700bp_GTCCGC_L001_trimmomatic', \
'SG-DE01-D-1700bp_GTCCGC_L001_trimmomatic']

#os.system('export LD_LIBRARY_PATH=/usr/local/lib64:$LD_LIBRARY_PATH')
#os.system('export PATH=/SDATA/tools/anaconda-1.9.0/bin/:$PATH')

#os.environ["LD_LIBRARY_PATH"]="/usr/local/lib64:$LD_LIBRARY_PATH"
#os.environ["PATH"]="/SDATA/tools/anaconda-1.9.0/bin/:$PATH"


i=0
while i<len(files_pe):
	os.system('sga preprocess --pe-mode 1 %s_R1.fastq %s_R2.fastq > %s.sga.fastq'% (files_pe[i],files_pe[i],files_pe[i]))
	os.system('sga index -a ropebwt -t 16 --no-reverse %s.sga.fastq' % files_pe[i])
	os.system('sga preqc -t 16 %s.sga.fastq > %s.preqc' % (files_pe[i],files_pe[i]))
       # os.system('sga-preqc-report.py %s.preqc *.preqc' % files_pe[i]
	os.system('sga correct --learn -t 16 -o %s_basecorrected.fastq %s.sga.fastq'% (files_pe[i],files_pe[i]))
	i+=1
