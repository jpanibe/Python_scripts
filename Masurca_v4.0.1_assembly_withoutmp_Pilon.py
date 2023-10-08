import os

files=['TNG67_forPilonreads']

os.chdir('/home/jpanibe/CLC_Data')

i=0

while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index Masurca_v4.0.1_assembly_withoutmp.fasta')
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p Masurca_v4.0.1_assembly_withoutmp.fasta %s.fastq > %s_Masurca_v4.0.1_assembly_withoutmp_mem.sam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_Masurca_v4.0.1_assembly_withoutmp_mem.sam > %s_Masurca_v4.0.1_assembly_withoutmp_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_Masurca_v4.0.1_assembly_withoutmp_mem_sort.bam %s_Masurca_v4.0.1_assembly_withoutmp_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_Masurca_v4.0.1_assembly_withoutmp_mem_sort.bam' % files[i])
	i+=1

os.system('java -Xmx100g -jar pilon-1.23.jar --genome Masurca_v4.0.1_assembly_withoutmp.fasta --frags %s_Masurca_v4.0.1_assembly_withoutmp_mem_sort.bam --output Masurca_v4.0.1_assembly_withoutmp_Pilon --outdir /home/jpanibe/CLC_Data/Masurca_v4.0.1_assembly_withoutmp_Pilon_results --changes --tracks --diploid --threads 16 --fix all' % files[0])


