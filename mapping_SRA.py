import os


ref=['TN1','oryza_indicair8-toplevel-20180831_UPPERCASE','MH63RS2.LNNK00000000_UPPERCASE']
files=['SRR1743093_minlen90','SRR1743098_minlen90']


os.system('/home/jpanibe/CLC_Data')

#os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index TN1.fasta')
#os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index oryza_indicair8-toplevel-20180831_UPPERCASE.fasta')
#os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index MH63RS2.LNNK00000000_UPPERCASE.fasta')


"""
i=0
while i<len(ref):
	j=0
	while j<len(files):
        	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 %s.fasta %s_R1.fastq %s_R2.fastq > %s_%s_mapall_mem.sam' % (ref[i],files[j],files[j],ref[i],files[j]))
        	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_%s_mapall_mem.sam > %s_%s_mapall_mem.bam' % (ref[i],files[j],ref[i],files[j]))
        	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_%s_mapall_mem_sort.bam %s_%s_mapall_mem.bam' % (ref[i],files[j],ref[i],files[j]))
        	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_%s_mapall_mem_sort.bam' % (ref[i],files[j]))
		j+=1	
	i+=1
"""



i=0
while i<len(ref):
        j=0
        while j<len(files):
		os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -f2 -q 20 -b %s_%s_mapall_mem_sort.bam > %s_%s_mapall_mem_sort.q20.bam' % (ref[i],files[j],ref[i],files[j]))
                os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_%s_mapall_mem_sort.q20.bam %s_%s_mapall_mem_sort.q20.sort.bam' % (ref[i],files[j],ref[i],files[j]))
                os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_%s_mapall_mem_sort.q20.sort.bam' % (ref[i],files[j]))
                j+=1
        i+=1



