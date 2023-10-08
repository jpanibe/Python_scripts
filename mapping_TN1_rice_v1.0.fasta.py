import os

files=['TN1_rice_v1.0.fasta']

os.system('/home/jpanibe/CLC_Data')

i=0
while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index %s' % files[i])
        os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p %s ec.fq > %s_mapall_mem.sam' % (files[i],files[i]))
        os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_mapall_mem.sam > %s_mapall_mem.bam' % (files[i],files[i]))
        os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_mapall_mem_sort.bam %s_mapall_mem.bam' % (files[i],files[i]))
        os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_mapall_mem_sort.bam' % files[i])
	i+=1

