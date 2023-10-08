import os

os.chdir("/home/jpanibe/CLC_Data")

file1='LGC17-LS01_585bp_CGATGT_L002_trimmomatic_minlen75_R1.fastq'
file2='LGC17-LS01_585bp_CGATGT_L002_trimmomatic_minlen75_R2.fastq'

os.system('bash -c "/home/jpanibe/CLC_Data/BFC/bfc/bfc -s 400m -t 16 <(/home/jpanibe/CLC_Data/seqtk/seqtk/seqtk mergepe %s %s) <(/home/jpanibe/CLC_Data/seqtk/seqtk/seqtk mergepe %s %s) | gzip -1 > ec.fq.gz"' % (file1,file2,file1,file2))
