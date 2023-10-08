import os

files_pe=['LGC_EU02_301bp_TGACCA_L008_trimmomatic_minlen50','LGC_EU52_381bp_TGACCA_L002_trimmomatic_minlen75']

#os.system('export LD_LIBRARY_PATH=/usr/local/lib64:$LD_LIBRARY_PATH')
#os.system('export PATH=/SDATA/tools/anaconda-1.9.0/bin/:$PATH')

os.environ["LD_LIBRARY_PATH"]="/usr/local/lib64:$LD_LIBRARY_PATH"
os.environ["PATH"]="/SDATA/tools/anaconda-1.9.0/bin/:$PATH"


i=0
while i<len(files_pe):
        os.chdir('/home/jpanibe/TNG67/TW/SA0169')
	os.system('/SDATA/tools/sga/bin/sga preprocess --pe-mode 1 %s_R1.fastq %s_R2.fastq > %s_trimmed.fastq' % (files_pe[i],files_pe[i],files_pe[i]))
        os.system('/SDATA/tools/sga/bin/sga index -a ropebwt -t 8 --no-reverse %s_trimmed.fastq' % files_pe[i])
        os.system('/SDATA/tools/sga/bin/sga preqc -t 8 %s_trimmed.fastq > %s_trimmed.preqc' % (files_pe[i],files_pe[i]))
        os.system('/SDATA/tools/sga/src/bin/sga-preqc-report.py %s_trimmed.preqc *.preqc' % files_pe[i])
	os.system('/SDATA/tools/sga/bin/sga correct --learn -t 8 -o %s_trimmed_basecorrected.fastq %s_trimmed.fastq'% (files_pe[i],files_pe[i]))
        i+=1















 

