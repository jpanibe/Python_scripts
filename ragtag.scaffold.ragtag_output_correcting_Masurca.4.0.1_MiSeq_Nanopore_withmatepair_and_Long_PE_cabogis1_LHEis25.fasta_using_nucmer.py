import os

files=['TNG67_forPilonreads']

os.chdir('/home/jpanibe/CLC_Data')

i=0

while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index ragtag.scaffold.ragtag_output_correcting_Masurca.4.0.1_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1_LHEis25.fasta_using_nucmer.fasta')
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p ragtag.scaffold.ragtag_output_correcting_Masurca.4.0.1_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1_LHEis25.fasta_using_nucmer.fasta %s.fastq > %s_ragtag.scaffold.ragtag_output_correcting_Masurca.4.0.1_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1_LHEis25.fasta_using_nucmer_mem.sam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_ragtag.scaffold.ragtag_output_correcting_Masurca.4.0.1_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1_LHEis25.fasta_using_nucmer_mem.sam > %s_ragtag.scaffold.ragtag_output_correcting_Masurca.4.0.1_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1_LHEis25.fasta_using_nucmer_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_ragtag.scaffold.ragtag_output_correcting_Masurca.4.0.1_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1_LHEis25.fasta_using_nucmer_mem_sort.bam %s_ragtag.scaffold.ragtag_output_correcting_Masurca.4.0.1_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1_LHEis25.fasta_using_nucmer_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_ragtag.scaffold.ragtag_output_correcting_Masurca.4.0.1_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1_LHEis25.fasta_using_nucmer_mem_sort.bam' % files[i])
	i+=1

os.system('java -Xmx100g -jar pilon-1.23.jar --genome ragtag.scaffold.ragtag_output_correcting_Masurca.4.0.1_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1_LHEis25.fasta_using_nucmer.fasta --frags %s_ragtag.scaffold.ragtag_output_correcting_Masurca.4.0.1_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1_LHEis25.fasta_using_nucmer_mem_sort.bam --output ragtag.scaffold.ragtag_output_correcting_Masurca.4.0.1_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1_LHEis25.fasta_using_nucmer_Pilon --outdir /home/jpanibe/CLC_Data/ragtag.scaffold.ragtag_output_correcting_Masurca.4.0.1_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1_LHEis25.fasta_using_nucmer_Pilon_results --changes --tracks --diploid --threads 16 --fix all' % files[0])


