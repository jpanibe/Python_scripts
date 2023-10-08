import os

files=["ERR635473", \
"ERR635484", \
"ERR635483", \
"ERR635482", \
"ERR635481", \
"ERR635480", \
"ERR635479", \
"ERR635478", \
"ERR635477", \
"ERR635476", \
"ERR635475", \
"ERR635474"]


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
ERR635473_mapall_mem_sort.bam \
ERR635484_mapall_mem_sort.bam \
ERR635483_mapall_mem_sort.bam \
ERR635482_mapall_mem_sort.bam \
ERR635481_mapall_mem_sort.bam \
ERR635480_mapall_mem_sort.bam \
ERR635479_mapall_mem_sort.bam \
ERR635478_mapall_mem_sort.bam \
ERR635477_mapall_mem_sort.bam \
ERR635476_mapall_mem_sort.bam \
ERR635475_mapall_mem_sort.bam \
ERR635474_mapall_mem_sort.bam')


os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o TN1_other_NCBI_other_reads_sorted.bam TN1_other_NCBI_other_reads.bam')
os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index TN1_other_NCBI_other_reads_sorted.bam')
