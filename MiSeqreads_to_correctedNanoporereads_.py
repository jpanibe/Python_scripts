import os


ref=['prefix.correctedReads','TNG67_Canu_rice.contigs']
files=['LGC-IS01_604bp_GATCAG_L001_trimmomatic_minlen150_basecorrected','SG_DE51_351bp_CGATGT_L001_trimmomatic_minlen75_basecorrected']

os.system('/home/jpanibe/CLC_Data')

#os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index prefix.correctedReads.fasta')
#os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index TNG67_Canu_rice.contigs.fasta')



i=0
while i<len(ref):
	j=0
	while j<len(files):
		os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -p -t 16 %s.fasta %s.fastq > %s_%s_mapall_mem.sam' % (ref[i],files[j],ref[i],files[j]))
		os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_%s_mapall_mem.sam > %s_%s_mapall_mem.bam' % (ref[i],files[j],ref[i],files[j]))
		os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_%s_mapall_mem_sort.bam %s_%s_mapall_mem.bam' % (ref[i],files[j],ref[i],files[j]))
		os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_%s_mapall_mem_sort.bam' % (ref[i],files[j]))
		j+=1	
	i+=1

