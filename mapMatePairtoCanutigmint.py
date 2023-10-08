import os

files=['LGM17-LS01_12K_CTTGTA_L002_trimmomatic.mp.ec', \
'LGM17-LS01_1K_TGACCA_L002_trimmomatic.mp.ec', \
'LGM17-LS01_20K_GTGAAA_L002_trimmomatic.mp.ec', \
'LGM17-LS01_3K_ACAGTG_L002_trimmomatic.mp.ec', \
'LGM17-LS01_5K_GCCAAT_L002_trimmomatic.mp.ec', \
'LGM17-LS01_8K_CAGATC_L002_trimmomatic.mp.ec']


os.chdir('/home/jpanibe/CLC_Data')


i=0

while i<len(files):
	os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa index Pilon.tigmint.fa')
        os.system('/home/jpanibe/CLC_Data/bwa/bwa-0.7.17/bwa mem -t 16 -p Pilon.tigmint.fa %s.fq > %s_mem.sam' % (files[i],files[i]))
        os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools view -h -b -S %s_mem.sam > %s_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools sort -@ 16 -O bam -T tmp_ -o %s_mem_sort.bam %s_mem.bam' % (files[i],files[i]))
	os.system('/home/jpanibe/CLC_Data/samtools/samtools-1.9/samtools index %s_mem_sort.bam' % files[i])
	i+=1


