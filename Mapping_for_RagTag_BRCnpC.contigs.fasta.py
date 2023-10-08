import os

files=['TNG67_forPilonreads']

os.chdir('/home/jpanibe/CLC_Data')

i=0

while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index BRCnpC.contigs.fasta')
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p BRCnpC.contigs.fasta %s.fastq > %s_BRCnpC.contigs_mem.sam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_BRCnpC.contigs_mem.sam > %s_BRCnpC.contigs_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmpA_ -o %s_BRCnpC.contigs_mem_sort.bam %s_BRCnpC.contigs_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_BRCnpC.contigs_mem_sort.bam' % files[i])
	i+=1


