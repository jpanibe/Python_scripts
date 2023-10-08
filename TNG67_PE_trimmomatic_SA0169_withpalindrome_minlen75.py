import os

files100=['LGC_EU02_301bp_TGACCA_L008']
files150=['LGC_EU52_381bp_TGACCA_L002']


i=0
while i<len(files150):
        os.chdir('/home/jpanibe/TNG67/TW/SA0169')
        os.system('java -jar /home/jpanibe/CLC_Data/Trimmomatic-0.39/from_bioinfoX/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 16 -trimlog %s_trimmomatic_minlen75_trimlog_withpalindrome.txt %s_R1.fastq %s_R2.fastq %s_trimmomatic_minlen75_R1.fastq %s_trimmomatic_minlen75_R1.fastq_noadapter_s1_se %s_trimmomatic_minlen75_R2.fastq %s_trimmomatic_minlen75_R2.fastq_noadapter_s2_se ILLUMINACLIP:/home/jpanibe/CLC_Data/Trimmomatic-0.39/from_bioinfoX/Trimmomatic-0.39/adapters/adapters.fa:2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:4:20 MINLEN:75 CROP:150' % (files150[i],files150[i],files150[i],files150[i],files150[i],files150[i],files150[i]))	
	i+=1


i=0
while i<len(files100):
        os.chdir('/home/jpanibe/TNG67/TW/SA0169')
        os.system('java -jar /home/jpanibe/CLC_Data/Trimmomatic-0.39/from_bioinfoX/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 16 -trimlog %s_trimmomatic_minlen50_trimlog_withpalindrome.txt %s_R1.fastq %s_R2.fastq %s_trimmomatic_minlen50_R1.fastq %s_trimmomatic_minlen50_R1.fastq_noadapter_s1_se %s_trimmomatic_minlen50_R2.fastq %s_trimmomatic_minlen50_R2.fastq_noadapter_s2_se ILLUMINACLIP:/home/jpanibe/CLC_Data/Trimmomatic-0.39/from_bioinfoX/Trimmomatic-0.39/adapters/adapters.fa:2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:4:20 MINLEN:50 CROP:100' % (files100[i],files100[i],files100[i],files100[i],files100[i],files100[i],files100[i]))
        i+=1






