import os

files=['LGC_EU52_381bp_TGACCA_L002_trimmomatic_minlen75_trimmed_basecorrected']

os.chdir('/home/jpanibe/TNG67/Nanopore/BRCnpC002_mutant_assembly/output')

i=0
"""
while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index mutant.contigs.fasta')
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p mutant.contigs.fasta %s.fastq > %s_mutant.contigs_mem.sam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_mutant.contigs_mem.sam > %s_mutant.contigs_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_mutant.contigs_mem_sort.bam %s_mutant.contigs_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_mutant.contigs_mem_sort.bam' % files[i])
	i+=1
"""

os.system('java -Xmx100g -jar /home/jpanibe/CLC_Data/Pilon/pilon-1.23.jar --genome mutant.contigs.fasta --frags %s_mutant.contigs_mem_sort.bam --output mutant.contigs_Pilon --outdir /home/jpanibe/TNG67/Nanopore/BRCnpC002_mutant_assembly/output/mutant.contigs_Pilon_results --changes --tracks --diploid --threads 16 --fix all' % files[0])


