import os

files_pe=['JA98KOB01', \
'JA98KOB02', \
'JBYCXRI01', \
'JBYCXRI02', \
'JCGURSI01', 
'JCGURSI02']

#os.system('export LD_LIBRARY_PATH=/usr/local/lib64:$LD_LIBRARY_PATH')
#os.system('export PATH=/SDATA/tools/anaconda-1.9.0/bin/:$PATH')

#os.environ["LD_LIBRARY_PATH"]="/usr/local/lib64:$LD_LIBRARY_PATH"
#os.environ["PATH"]="/SDATA/tools/anaconda-1.9.0/bin/:$PATH"


i=0
while i<len(files_pe):
	os.system('sga preprocess --pe-mode 1 %s.sff.OUT.Forward.trimmomatic.fastq %s.sff.OUT.Reverse.trimmomatic.fastq > %s.sga.fastq'% (files_pe[i],files_pe[i],files_pe[i]))
	os.system('sga index -a ropebwt -t 16 --no-reverse %s.sga.fastq' % files_pe[i])
	os.system('sga preqc -t 16 %s.sga.fastq > %s.preqc' % (files_pe[i],files_pe[i]))
       # os.system('sga-preqc-report.py %s.preqc *.preqc' % files_pe[i]
	os.system('sga correct --learn -t 16 -o %s_basecorrected.fastq %s.sga.fastq'% (files_pe[i],files_pe[i]))
	i+=1
