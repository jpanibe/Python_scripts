import os

os.system('/home/jpanibe/CLC_Data')


os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools faidx Pilon.fasta')
os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index Pilon.fasta')


os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t16 -p -C Pilon.fasta barcoded.fastq | /home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@16 -tBX -o Pilon_rerun.fasta.reads.sortbx.bam')
os.system('/home/jpanibe/CLC_Data/tigmint/tigmint/bin/tigmint-molecule Pilon_rerun.fasta.reads.sortbx.bam | sort -k1,1 -k2,2n -k3,3n >  Pilon_rerun.fasta.reads.molecule.bed')

os.system('/home/jpanibe/CLC_Data/tigmint/tigmint/bin/tigmint-cut -p16 -o Pilon_rerun.tigmint.fa Pilon.fasta Pilon_rerun.fasta.reads.molecule.bed')

