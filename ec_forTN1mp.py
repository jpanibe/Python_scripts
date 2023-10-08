import os

os.chdir("/home/jpanibe/CLC_Data")

file1=['LGM17-LS01_12K_CTTGTA_L002_trimmomatic', \
'LGM17-LS01_1K_TGACCA_L002_trimmomatic', \
'LGM17-LS01_20K_GTGAAA_L002_trimmomatic', \
'LGM17-LS01_3K_ACAGTG_L002_trimmomatic', \
'LGM17-LS01_5K_GCCAAT_L002_trimmomatic', \
'LGM17-LS01_8K_CAGATC_L002_trimmomatic']


i=0
while i<len(file1):
	os.system('bash -c "/home/jpanibe/CLC_Data/BFC/bfc/bfc -s 400m -t 16 <(/home/jpanibe/CLC_Data/seqtk/seqtk/seqtk mergepe %s.mp.f.fastq %s.mp.r.fastq) <(/home/jpanibe/CLC_Data/seqtk/seqtk/seqtk mergepe %s.mp.f.fastq %s.mp.r.fastq) | gzip -1 > %s.mp.ec.fq.gz"' % (file1[i],file1[i],file1[i],file1[i],file1[i]))
	i+=1


