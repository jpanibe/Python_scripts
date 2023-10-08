import os

files=['ERR619929', \
'ERR619928', \
'ERR619927', \
'ERR619926', \
'ERR619925', \
'ERR619924', \
'ERR619923', \
'ERR619922', \
'ERR619921', \
'ERR619920', \
'ERR619919', \
'ERR619918', \
'ERR619917', \
'ERR619916']


os.chdir('/home/jpanibe/SRA_Data')

os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index /home/jpanibe/CLC_Data/TN1_rice_v1.0.fasta')

i=0
while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p /home/jpanibe/CLC_Data/TN1_rice_v1.0.fasta %s_trimmomatic_minlen50.fastq > %s_mapall_mem.sam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -S -h -b %s_mapall_mem.sam > %s_mapall_mem.bam'  % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_mapall_mem_sort.bam %s_mapall_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_mapall_mem_sort.bam' % files[i])
	i+=1


os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools merge -f -h ERR619916_mapall_mem.sam --output-fmt BAM --threads 16 \
TN1_other_NCBI_other_reads.bam \
ERR619929_mapall_mem_sort.bam \
ERR619928_mapall_mem_sort.bam \
ERR619927_mapall_mem_sort.bam \
ERR619926_mapall_mem_sort.bam \
ERR619925_mapall_mem_sort.bam \
ERR619924_mapall_mem_sort.bam \
ERR619923_mapall_mem_sort.bam \
ERR619922_mapall_mem_sort.bam \
ERR619921_mapall_mem_sort.bam \
ERR619920_mapall_mem_sort.bam \
ERR619919_mapall_mem_sort.bam \
ERR619918_mapall_mem_sort.bam \
ERR619917_mapall_mem_sort.bam \
ERR619916_mapall_mem_sort.bam')


os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o TN1_other_NCBI_other_reads_sorted.bam TN1_other_NCBI_other_reads.bam')
os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index TN1_other_NCBI_other_reads_sorted.bam')
