import os

subreads=['subreads_pd017_1',\
'subreads_pd018_0',\
'subreads_pd018_1',\
'subreads_pd019_2',\
'subreads_pd019_3',\
'subreads_pd021_2',\
'subreads_pd021_3',\
'subreads_pd021_4',\
'subreads_pd021_5',\
'subreads_pd021_6',\
'subreads_pd021_7']

os.chdir('/home/jpanibe/CLC_Data')

i=0
while i<len(subreads):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index %s.fasta' % subreads[i])
        os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p %s.fasta ec.fq > %s_mem.sam' % (subreads[i],subreads[i]))
        os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_mem.sam > %s_mem.bam' % (subreads[i],subreads[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_mem_sort.bam %s_mem.bam' % (subreads[i],subreads[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_mem_sort.bam' % subreads[i])
	os.system('java -Xmx100g -jar pilon-1.23.jar --genome %s.fasta --frags %s_mem_sort.bam --output %s_Pilon --outdir /home/jpanibe/CLC_Data/Pilon_%s_results --changes --tracks --diploid --threads 16 --K 125 --fix all' %(subreads[i],subreads[i],subreads[i],subreads[i]))
	i+=1


