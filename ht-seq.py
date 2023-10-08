import os

os.chdir('/home/jpanibe/CLC_Data')

#os.system('/home/jpanibe/CLC_Data/htseq/HTSeq-0.12.4/scripts/htseq-count --format bam --order pos --type CDS --minaqual 30 TN1_SRR1743093_minlen90_mapall_mem_sort.bam TN1_genome.maker.pass2.maker_model.rename.gtf > TN1_SRR1743093_minlen90_mapall_mem_sort_htseq.txt')

os.system('/home/jpanibe/CLC_Data/htseq/HTSeq-0.12.4/scripts/htseq-count --format bam --order pos --type CDS --minaqual 20 TN1_SRR1743093_minlen90_mapall_mem_sort.bam TN1_genome.maker.pass2.maker_model.rename.gtf > TN1_SRR1743093_minlen90_mapall_mem_sort_htseq_q20.txt')
