##########################################################################################################
# Date created: Aug. 13, 2014                                                                            #
# Author: Jerome P. Panibe                                                                               #
#                                                                                                        #
# This is a combo script that will perform:                                                              #
# 1. perform bwa mem mapping of raw sga base corrected trimmed reads of TNG67 to the ALLPATHS assembly   #
# 2. convert sam to bam                                                                                  #
# 3. sort bam                                                                                            #
#                                                                                                        #
#                                                                                                        #
##########################################################################################################                                      
 
import os

files2=['HS2_correct.unpaired_grabe']
files3=['IRGSP_techin']

print len(files2)

#bwa aln and sampe mapping   
#single-end
'''
os.system('/home/jpanibe/Bioinformatics/BWA/bwa-0.7.7/bwa index /home/jpanibe/TNG67/techin/IRGSP-1.0_genome_renamed.fasta')
'''

i=0
while i<len(files2):	
	os.chdir('/home/jpanibe/TNG67/techin')	
        os.system('/home/jpanibe/Bioinformatics/BWA/bwa-0.7.7/bwa aln -t 40 -n 0.01 /home/jpanibe/TNG67/techin/IRGSP-1.0_genome_renamed.fasta %s.fastq > %s_%s_sa.sai' % (files2[i],files2[i],files3[0]))
                
        os.system('/home/jpanibe/Bioinformatics/BWA/bwa-0.7.7/bwa samse -n 100000000 /home/jpanibe/TNG67/techin/IRGSP-1.0_genome_renamed.fasta %s_%s_sa.sai %s.fastq > %s_%s_mem.sam' % (files2[i],files3[0],files2[i],files2[i],files3[0]))
	i+=1



##convert sam to bam

i=0
while i<len(files2):
        os.chdir('/home/jpanibe/TNG67/techin')
        os.system('samtools view -b -S %s_%s_mem.sam > %s_%s_mem.bam' % (files2[i],files3[0],files2[i],files3[0]))
        i+=1


#filter multi-mapper and unmapped reads
i=0
while i<len(files2):
	os.chdir('/home/jpanibe/TNG67/techin')
	os.system('samtools view -bF 4 -q 1 %s_%s_mem.bam > %s_%s_bFq1_mem.bam'  % (files2[i],files3[0],files2[i],files3[0]))
	i+=1

i=0 
while i<len(files2):
        os.chdir('/home/jpanibe/TNG67/techin')
        os.system('samtools view -bq 30 %s_%s_bFq1_mem.bam > %s_%s_bFq1_q30_mem.bam'  % (files2[i],files3[0],files2[i],files3[0]))
        i+=1


#merge bam
os.system('nohup java -jar /home/jpanibe/Bioinformatics/picard_tools/picard-tools-1.113/MergeSamFiles.jar \
INPUT=HS2_correct.filled_IRGSP_techin_mem_coordinate_sorted.bam \
INPUT=HS4_correct.filled_IRGSP_techin_mem_coordinate_sorted.bam \
INPUT=HS5_correct.filled_IRGSP_techin_mem_coordinate_sorted.bam \
INPUT=HS6_correct.filled_IRGSP_techin_mem_coordinate_sorted.bam \
INPUT=MS3_correct.filled_IRGSP_techin_mem_coordinate_sorted.bam \
INPUT=HS2_correct.unpaired_IRGSP_techin_mem_coordinate_sorted.bam \
INPUT=HS4_correct.unpaired_IRGSP_techin_mem_coordinate_sorted.bam \
INPUT=HS5_correct.unpaired_IRGSP_techin_mem_coordinate_sorted.bam \
INPUT=HS6_correct.unpaired_IRGSP_techin_mem_coordinate_sorted.bam \
INPUT=MS3_correct.unpaired_IRGSP_techin_mem_coordinate_sorted.bam \
OUTPUT=HS2+HS4+HS5+HS6+MS3[correct.filled+correct.unpaired]_IRGSP_techin_mem_coordinate_sorted.bam &> nohup.HS2+HS4+HS5+HS6+MS3[correct.filled+correct.unpaired]_IRGSP_techin_mem_coordinate_sorted.bam.out')


##sort bam

i=0
while i<len(files2):
        os.chdir('/home/jpanibe/TNG67/techin')
        os.system('java -jar /home/jpanibe/Bioinformatics/picard_tools/picard-tools-1.113/SortSam.jar INPUT=%s_%s_bFq1_q30_mem.bam OUTPUT=%s_%s_mem_coordinate_sorted.bam SORT_ORDER=coordinate' % (files2[i],files3[0],files2[i],files3[0]))
        i+=1
     

'''
#collect insert size metrics
i=0
while i<len(files2):
        os.chdir('/home/jpanibe/TNG67/techin')
        os.system('java -Xmx128M -jar /home/jpanibe/Bioinformatics/picard_tools/picard-tools-1.113/CollectInsertSizeMetrics.jar INPUT=%s_%s_mem_coordinate_sorted.bam OUTPUT=%s_%s.metrics HISTOGRAM_FILE=%s_%s.hist' % (files2[i],files3[0],files2[i],files3[0],files2[i],files3[0]))
        i+=1
'''







