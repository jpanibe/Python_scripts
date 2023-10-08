import os



os.chdir('/home/jpanibe/CLC_Data')

#i=0
#while i<len(files):
#	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index Pilon.tigmint.fa')
#        os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p Pilon.tigmint.fa %s.fq > %s_Pilon.tigmint_mem.sam' % (files[i],files[i]))
#        os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_Pilon.tigmint_mem.sam > %s_Pilon.tigmint_mem.bam' % (files[i],files[i]))
#	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_Pilon.tigmint_mem_sort.bam %s_Pilon.tigmint_mem.bam' % (files[i],files[i]))
#	@os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_Pilon.tigmint_mem_sort.bam' % files[i])
#	i+=1



#os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index Pilon.tigmint.fa')

os.system('/home/jpanibe/CLC_Data/OPERA-LG/OPERA-LG_v2.0.6/bin/OPERA-long-read.pl --contig-file /home/jpanibe/CLC_Data/Pilon.tigmint.fa --long-read-file /home/jpanibe/CLC_Data/subreads_pdALL.fasta --output-prefix Pilontigmintopera --output-directory /home/jpanibe/CLC_Data/opera-lg_result_new3 --num-of-processors 16 --short-read-maptool bwa --illumina-read1 /home/jpanibe/CLC_Data/ec.f.fastq --illumina-read2 /home/jpanibe/CLC_Data/ec.r.fastq')
