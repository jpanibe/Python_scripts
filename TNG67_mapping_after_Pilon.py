import os

files=['SG_DE51_351bp_CGATGT_L001_trimmomatic_minlen75_basecorrected', \
'LGC-IS01_604bp_GATCAG_L001_trimmomatic_minlen150_basecorrected']        

genome=['IRGSP-1.0_genome_UPPERCASE.fasta']

os.chdir('/home/jpanibe/CLC_Data')

i=0
while i<len(genome):
	j=0
	while j<len(files):
		os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index %s' % genome[i])
		os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p %s %s.fastq > %s_%s_mem.sam' % (genome[i],files[j],genome[i],files[j]))
		os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_%s_mem.sam > %s_%s_mem.bam' % (genome[i],files[j],genome[i],files[j]))
		os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_%s_mem_sort.bam %s_%s_mem.bam' % (genome[i],files[j],genome[i],files[j]))
		os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_%s_mem_sort.bam' % (genome[i],files[j]))
		j+=1	
	i+=1

