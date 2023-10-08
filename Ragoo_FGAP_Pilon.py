import os

files=['ec']

os.chdir('/home/jpanibe/CLC_Data')

i=0

while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index TN1_ragoo_combined_FGAP.final.fasta')
        os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p TN1_ragoo_combined_FGAP.final.fasta %s.fq > %s_TN1_ragoo_combined_FGAP.final_mem.sam' % (files[i],files[i]))
        os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_TN1_ragoo_combined_FGAP.final_mem.sam > %s_TN1_ragoo_combined_FGAP.final_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_TN1_ragoo_combined_FGAP.final_mem_sort.bam %s_TN1_ragoo_combined_FGAP.final_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_TN1_ragoo_combined_FGAP.final_mem_sort.bam' % files[i])
	i+=1

os.system('java -Xmx100g -jar pilon-1.23.jar --genome TN1_ragoo_combined_FGAP.final.fasta --frags ec_TN1_ragoo_combined_FGAP.final_mem_sort.bam --output TN1_ragoo_combined_FGAP.final_Pilon --outdir /home/jpanibe/CLC_Data/TN1_ragoo_combined_FGAP.final_Pilon_results --changes --tracks --diploid --threads 16 --K 125 --fix all')


