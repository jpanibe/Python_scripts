import os

os.chdir('/home/jpanibe/CLC_Data')
"""
os.system('/home/jpanibe/CLC_Data/blast/ncbi-blast-2.10.0+/bin/blastp -query TN1_genome.maker.pass2.maker_proteins.rename.fasta -db oryza_indicair8_maker_gene.protein.fasta -num_threads 24 -evalue 1e-10 -max_target_seqs 5 -outfmt 6 -out for_MCScanX_TN1q_vs_IR8db.blast')

os.system('/home/jpanibe/CLC_Data/blast/ncbi-blast-2.10.0+/bin/blastp -query oryza_indicair8_maker_gene.protein.fasta -db TN1_genome.maker.pass2.maker_proteins.rename.fasta -num_threads 24 -evalue 1e-10 -max_target_seqs 5 -outfmt 6 -out for_MCScanX_IR8q_vs_TN1db.blast')

os.system('nohup /home/jpanibe/CLC_Data/blast/ncbi-blast-2.10.0+/bin/blastp -query oryza_indicair8_maker_gene.protein.fasta -db oryza_indicair8_maker_gene.protein.fasta -num_threads 24 -evalue 1e-10 -max_target_seqs 5 -outfmt 6 -out for_MCScanX_IR8q_vs_IR8db.blast')

os.system('/home/jpanibe/CLC_Data/blast/ncbi-blast-2.10.0+/bin/blastp -query TN1_genome.maker.pass2.maker_proteins.rename.fasta -db TN1_genome.maker.pass2.maker_proteins.rename.fasta -num_threads 24 -evalue 1e-10 -max_target_seqs 5 -outfmt 6 -out for_MCScanX_TN1q_vs_TN1db.blast')
"""

####

os.system('/home/jpanibe/CLC_Data/blast/ncbi-blast-2.10.0+/bin/makeblastdb -in MH63RS2.LNNK00000000.pro.v2.fa -dbtype prot')

os.system('/home/jpanibe/CLC_Data/blast/ncbi-blast-2.10.0+/bin/makeblastdb -in IR64_proteins.fasta -dbtype prot')

os.system('/home/jpanibe/CLC_Data/blast/ncbi-blast-2.10.0+/bin/blastp -query MH63RS2.LNNK00000000.pro.v2.fa -db MH63RS2.LNNK00000000.pro.v2.fa -num_threads 32 -evalue 1e-10 -max_target_seqs 5 -outfmt 6 -out for_MCScanX_MH63q_vs_MH63db.blast')


os.system('/home/jpanibe/CLC_Data/blast/ncbi-blast-2.10.0+/bin/blastp -query TN1_genome.maker.pass2.maker_proteins.rename.fasta -db MH63RS2.LNNK00000000.pro.v2.fa -num_threads 32 -evalue 1e-10 -max_target_seqs 5 -outfmt 6 -out for_MCScanX_TN1q_vs_MH63db.blast')


os.system('/home/jpanibe/CLC_Data/blast/ncbi-blast-2.10.0+/bin/blastp -query MH63RS2.LNNK00000000.pro.v2.fa -db TN1_genome.maker.pass2.maker_proteins.rename.fasta -num_threads 32 -evalue 1e-10 -max_target_seqs 5 -outfmt 6 -out for_MCScanX_MH63q_vs_TN1db.blast')


os.system('/home/jpanibe/CLC_Data/blast/ncbi-blast-2.10.0+/bin/blastp -query IR64_proteins.fasta -db IR64_proteins.fasta -num_threads 32 -evalue 1e-10 -max_target_seqs 5 -outfmt 6 -out for_MCScanX_IR64q_vs_IR64db.blast')


os.system('/home/jpanibe/CLC_Data/blast/ncbi-blast-2.10.0+/bin/blastp -query TN1_genome.maker.pass2.maker_proteins.rename.fasta -db IR64_proteins.fasta -num_threads 32 -evalue 1e-10 -max_target_seqs 5 -outfmt 6 -out for_MCScanX_TN1q_vs_IR64db.blast')


os.system('/home/jpanibe/CLC_Data/blast/ncbi-blast-2.10.0+/bin/blastp -query IR64_proteins.fasta -db TN1_genome.maker.pass2.maker_proteins.rename.fasta -num_threads 32 -evalue 1e-10 -max_target_seqs 5 -outfmt 6 -out for_MCScanX_IR64q_vs_TN1db.blast')



