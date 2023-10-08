import os

files=['ec']

os.chdir('/home/jpanibe/CLC_Data')

i=0

while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index supernova_RAILS_HGAP_RAILS_linear_GapCloser_GapFiller_iter3.gapfilled.final.fa')
        os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p supernova_RAILS_HGAP_RAILS_linear_GapCloser_GapFiller_iter3.gapfilled.final.fa %s.fq > %s_supernova_RAILS_HGAP_RAILS_linear_GapCloser_GapFiller_iter3.gapfilled.final.fa_mem.sam' % (files[i],files[i]))
        os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_supernova_RAILS_HGAP_RAILS_linear_GapCloser_GapFiller_iter3.gapfilled.final.fa_mem.sam > %s_supernova_RAILS_HGAP_RAILS_linear_GapCloser_GapFiller_iter3.gapfilled.final.fa_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_supernova_RAILS_HGAP_RAILS_linear_GapCloser_GapFiller_iter3.gapfilled.final.fa_mem_sort.bam %s_supernova_RAILS_HGAP_RAILS_linear_GapCloser_GapFiller_iter3.gapfilled.final.fa_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_supernova_RAILS_HGAP_RAILS_linear_GapCloser_GapFiller_iter3.gapfilled.final.fa_mem_sort.bam' % files[i])
	i+=1


