import os

os.system('/home/jpanibe/CLC_Data')


os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools faidx Pilon.medusa_R498only.fasta')
os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index Pilon.medusa_R498only.fasta')


os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t16 -p -C Pilon.medusa_R498only.fasta barcoded.fastq | /home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@16 -tBX -o Pilon.medusa_R498only.fasta.reads.sortbx.bam')
os.system('/home/jpanibe/CLC_Data/tigmint/tigmint/bin/tigmint-molecule Pilon.medusa_R498only.fasta.reads.sortbx.bam | sort -k1,1 -k2,2n -k3,3n >  Pilon.medusa_R498only.fasta.reads.molecule.bed')

os.system('/home/jpanibe/CLC_Data/tigmint/tigmint/bin/tigmint-cut -p16 -o Pilon.medusa_R498only.tigmint.fa Pilon.medusa_R498only.fasta Pilon.medusa_R498only.fasta.reads.molecule.bed')

