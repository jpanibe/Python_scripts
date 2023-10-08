import os

files=['TNG67_forPilonreads']

os.chdir('/home/jpanibe/CLC_Data')

i=0

while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index TNG67_Masurca_v4.0.1.fasta')
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p TNG67_Masurca_v4.0.1.fasta %s.fastq > %s_TNG67_Masurca_v4.0.1_mem.sam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_TNG67_Masurca_v4.0.1_mem.sam > %s_TNG67_Masurca_v4.0.1_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_TNG67_Masurca_v4.0.1_mem_sort.bam %s_TNG67_Masurca_v4.0.1_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_TNG67_Masurca_v4.0.1_mem_sort.bam' % files[i])
	i+=1

os.system('java -Xmx100g -jar pilon-1.23.jar --genome TNG67_Masurca_v4.0.1.fasta --frags %s_TNG67_Masurca_v4.0.1_mem_sort.bam --output TNG67_Masurca_v4.0.1_Pilon --outdir /home/jpanibe/CLC_Data/TNG67_Masurca_v4.0.1_Pilon_results --changes --tracks --diploid --threads 16 --fix all' % files[0])


