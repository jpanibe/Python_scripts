import os

"""
files=['pbjelly_rerun_linear_AfterRAILS_UPPERCASE_GapCloser_GapFiller_iter3.gapfilled.final.fa_mapall_mem_sort',
'Pilon.fasta_mapall_mem_sort',
'Pilon_rerun_ARKS_RAILSwithsupernova.fa_mapall_mem_sort',
'Pilon_rerun_ARKS_result.fa_mapall_mem_sort',
'Pilon_rerun_ARKS_result_SSPACE.final.scaffolds.fasta_mapall_mem_sort',
'Pilon_rerun.tigmint.fa_mapall_mem_sort',
'Pilon_rerun_tigmint_pacbioonly_consensusScaffold.fa_mapall_mem_sort',
'TN1_canu_default.contigs.fasta_mapall_mem_sort',
'TN1_ragoo_combined.fasta_mapall_mem_sort',
'TN1_ragoo_combined_FGAP.final.fasta_mapall_mem_sort']
"""


files=['pbjelly_rerun.fasta_mapall_mem_sort',
'pbjelly_rerun_linear_AfterRAILS_UPPERCASE.fasta_mapall_mem_sort',
'pbjelly_rerun_linear_AfterRAILS_UPPERCASE_GapCloser.fasta_mapall_mem_sort',
'TN1_ragoo_combined_FGAP.final_Pilon.fasta_mapall_mem_sort']


i=0

while i<len(files):
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools flagstat %s.bam > flagstat_%s.txt' % (files[i],files[i]))
	i+=1
