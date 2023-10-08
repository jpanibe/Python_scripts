import os

files=['ec']

os.chdir('/home/jpanibe/CLC_Data')

i=0

while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index HGAP_contigs.fasta')
        os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p HGAP_contigs.fasta %s.fq > %s_HGAP_contigs_mem.sam' % (files[i],files[i]))
        os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_HGAP_contigs_mem.sam > %s_HGAP_contigs_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_HGAP_contigs_mem_sort.bam %s_HGAP_contigs_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_HGAP_contigs_mem_sort.bam' % files[i])
	i+=1

os.system('java -Xmx100g -jar pilon-1.23.jar --genome HGAP_contigs.fasta --frags ec_HGAP_contigs_mem_sort.bam --output HGAP_contigs_Pilon --outdir /home/jpanibe/CLC_Data/HGAP_contigs_Pilon_results --changes --tracks --diploid --threads 16 --K 125 --fix all')


