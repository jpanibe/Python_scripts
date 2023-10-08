import os

files=['ec']

os.chdir('/home/jpanibe/CLC_Data')

i=0

while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index R498_UPPERCASE.fasta')
        os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p R498_UPPERCASE.fasta %s.fq > %s_R498_UPPERCASE_mem.sam' % (files[i],files[i]))
        os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_R498_UPPERCASE_mem.sam > %s_R498_UPPERCASE_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_R498_UPPERCASE_mem_sort.bam %s_R498_UPPERCASE_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_R498_UPPERCASE_mem_sort.bam' % files[i])
	i+=1


