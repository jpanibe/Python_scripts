import os

files=['final.genome.scf_TNG67_MiSeq_Nanopore_cabogis1.fasta', \
'final.genome.scf_TNG67_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1.fasta', \
'Flye_assembly_Nanopore_only_assembly.fasta', \
'flye_assembly_TNG67_MiSeq_Nanopore.fasta', \
'TNG67_Canu_rice.contigs.fasta', \
'TNG67_smartdenovo_Nanopore_only.fasta']
reads=['LGC-IS01_604bp_GATCAG_L001_trimmomatic_minlen150_basecorrected.fastq','SG_DE51_351bp_CGATGT_L001_trimmomatic_minlen75_basecorrected.fastq']

os.system('/home/jpanibe/CLC_Data')

i=0
while i<len(files):
	j=0
	while j<len(reads):
		os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index %s' % files[i])
		os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p %s %s > %s_%s_mapall_mem.sam' % (files[i],reads[j],files[i],reads[j]))
		os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_%s_mapall_mem.sam > %s_%s_mapall_mem.bam' % (files[i],reads[j],files[i],reads[j]))
		os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_%s_mapall_mem_sort.bam  %s_%s_mapall_mem.bam' % (files[i],reads[j],files[i],reads[j]))
		os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_%s_mapall_mem_sort.bam' % (files[i],reads[j]))
		j+=1
	i+=1

