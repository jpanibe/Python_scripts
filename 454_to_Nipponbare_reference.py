import os


ref=['IRGSP-1.0_genome_UPPERCASE']
files=['JA98KOB01_basecorrected', \
'JA98KOB02_basecorrected', \
'JBYCXRI01_basecorrected', \
'JBYCXRI02_basecorrected', \
'JCGURSI01_basecorrected', \
'JCGURSI02_basecorrected']

os.system('/home/jpanibe/CLC_Data')

#os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index IRGSP-1.0_genome_UPPERCASE.fasta')

i=0
while i<len(ref):
	j=0
	while j<len(files):
		os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 %s.fasta %s_R1.fastq %s_R2.fastq> %s_%s_mapall_mem.sam' % (ref[i],files[j],files[j],ref[i],files[j]))
		os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_%s_mapall_mem.sam > %s_%s_mapall_mem.bam' % (ref[i],files[j],ref[i],files[j]))
		os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_%s_mapall_mem_sort.bam %s_%s_mapall_mem.bam' % (ref[i],files[j],ref[i],files[j]))
		os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_%s_mapall_mem_sort.bam' % (ref[i],files[j]))
		j+=1	
	i+=1

