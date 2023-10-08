import os

files=['SG_DE01_MP2_4kb_AGTTCC_L002_trimmomatic.mp_basecorrected', \
'SG_DE01_MP4_6kb_GTGAAA_L002_trimmomatic.mp_basecorrected', \
'SG_DE01_MP6_10kb_TGACCA_L002_trimmomatic.mp_basecorrected', \
'SG_DE01_C_1062bp_GATCAG_L001_trimmomatic_basecorrected', \
'SG-DE01-C-1062bp_GATCAG_L001_trimmomatic_basecorrected', \
'SG_DE01_D_1700bp_GTCCGC_L001_trimmomatic_basecorrected', \
'SG-DE01-D-1700bp_GTCCGC_L001_trimmomatic_basecorrected']


os.chdir('/home/jpanibe/CLC_Data')

i=0

while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index IRGSP-1.0_genome_UPPERCASE.fasta')
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p IRGSP-1.0_genome_UPPERCASE.fasta %s.fastq > %s_IRGSP-1.0_genome_UPPERCASE_mem.sam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_IRGSP-1.0_genome_UPPERCASE_mem.sam > %s_IRGSP-1.0_genome_UPPERCASE_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_IRGSP-1.0_genome_UPPERCASE_mem_sort.bam %s_IRGSP-1.0_genome_UPPERCASE_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_IRGSP-1.0_genome_UPPERCASE_mem_sort.bam' % files[i])
	i+=1

