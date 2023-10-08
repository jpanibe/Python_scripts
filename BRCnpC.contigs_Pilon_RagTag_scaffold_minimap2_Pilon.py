import os

files=['TNG67_forPilonreads']

os.chdir('/home/jpanibe/CLC_Data')

i=0

while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index BRCnpC.contigs_Pilon_RagTag_scaffold_minimap2.fasta')
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p BRCnpC.contigs_Pilon_RagTag_scaffold_minimap2.fasta %s.fastq > %s_BRCnpC.contigs_Pilon_RagTag_scaffold_minimap2_mem.sam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_BRCnpC.contigs_Pilon_RagTag_scaffold_minimap2_mem.sam > %s_BRCnpC.contigs_Pilon_RagTag_scaffold_minimap2_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_BRCnpC.contigs_Pilon_RagTag_scaffold_minimap2_mem_sort.bam %s_BRCnpC.contigs_Pilon_RagTag_scaffold_minimap2_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_BRCnpC.contigs_Pilon_RagTag_scaffold_minimap2_mem_sort.bam' % files[i])
	i+=1

os.system('java -Xmx100g -jar pilon-1.23.jar --genome BRCnpC.contigs_Pilon_RagTag_scaffold_minimap2.fasta --frags %s_BRCnpC.contigs_Pilon_RagTag_scaffold_minimap2_mem_sort.bam --output BRCnpC.contigs_Pilon_RagTag_scaffold_minimap2_Pilon --outdir /home/jpanibe/CLC_Data/BRCnpC.contigs_Pilon_RagTag_scaffold_minimap2_Pilon_results --changes --tracks --diploid --threads 16 --fix all' % files[0])


