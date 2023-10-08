import os

os.system('/home/jpanibe/CLC_Data')

os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools faidx HGAP_contigs_Pilon.fasta')
os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index HGAP_contigs_Pilon.fasta')

os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t16 -p -C HGAP_contigs_Pilon.fasta barcoded.fastq | /home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@16 -tBX -o HGAP_contigs_Pilon.fasta.reads.sortbx.bam')
os.system('/home/jpanibe/CLC_Data/tigmint/tigmint/bin/tigmint-molecule HGAP_contigs_Pilon.fasta.reads.sortbx.bam | sort -k1,1 -k2,2n -k3,3n > HGAP_contigs_Pilon.fasta.reads.molecule.bed')

os.system('/home/jpanibe/CLC_Data/tigmint/tigmint/bin/tigmint-cut -p16 -o HGAP_contigs_Pilon.tigmint.fa HGAP_contigs_Pilon.fasta HGAP_contigs_Pilon.fasta.reads.molecule.bed')

