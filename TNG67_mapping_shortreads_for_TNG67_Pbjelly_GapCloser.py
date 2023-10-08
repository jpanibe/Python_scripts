import os

files=['SG_DE51_351bp_CGATGT_L001_trimmomatic_minlen75_basecorrected', \
'LGC-IS01_604bp_GATCAG_L001_trimmomatic_minlen150_basecorrected']        

os.chdir('/home/jpanibe/CLC_Data')

i=0

while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index TNG67_Pbjelly_GapCloser.fasta')
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p TNG67_Pbjelly_GapCloser.fasta %s.fastq > %s_TNG67_Pbjelly_GapCloser_mem.sam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_TNG67_Pbjelly_GapCloser_mem.sam > %s_TNG67_Pbjelly_GapCloser_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_TNG67_Pbjelly_GapCloser_mem_sort.bam %s_TNG67_Pbjelly_GapCloser_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_TNG67_Pbjelly_GapCloser_mem_sort.bam' % files[i])
	i+=1

