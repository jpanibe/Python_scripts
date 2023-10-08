import os

files=['TN1_canu_default.contigs.fasta','Pilon.fasta','Pilon_rerun.tigmint.fa','Pilon_rerun_tigmint_pacbioonly_consensusScaffold.fa','Pilon_rerun_ARKS_result.fa','Pilon_rerun_ARKS_result_SSPACE.final.scaffolds.fasta','Pilon_rerun_ARKS_RAILSwithsupernova.fa','pbjelly_rerun.fasta','pbjelly_rerun_linear_AfterRAILS_UPPERCASE.fasta','pbjelly_rerun_linear_AfterRAILS_UPPERCASE_GapCloser.fasta','pbjelly_rerun_linear_AfterRAILS_UPPERCASE_GapCloser_GapFiller_iter3.gapfilled.final.fa','TN1_ragoo_combined.fasta','TN1_ragoo_combined_FGAP.final.fasta','TN1_ragoo_combined_FGAP.final_Pilon.fasta']

os.system('/home/jpanibe/CLC_Data')

i=0
while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index %s' % files[i])
        os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p %s ec.fq > %s_mapall_mem.sam' % (files[i],files[i]))
        os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_mapall_mem.sam > %s_mapall_mem.bam' % (files[i],files[i]))
        os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_mapall_mem_sort.bam %s_mapall_mem.bam' % (files[i],files[i]))
        os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_mapall_mem_sort.bam' % files[i])
	i+=1

