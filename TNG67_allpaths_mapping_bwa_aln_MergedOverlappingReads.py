##########################################################################################################
# Date created: March 30, 2015                                                                           #
# Author: Jerome P. Panibe                                                                               #
#                                                                                                        #
# This is a combo script that will perform:                                                              #
# 1. perform bwa aln mapping of                                                                          #
# 2. convert sam to bam                                                                                  #
# 3. remove unmapped reads and multi-mappers below mapq of 30                                            #
# 4. merge bam files                                                                                     #
# 4. sort bam                                                                                            #
#                                                                                                        #
##########################################################################################################                                      
 
import os

files2=['HS2_correct.filled','HS4_correct.filled','HS5_correct.filled','HS6_correct.filled','MS3_correct.filled','HS2_correct.unpaired','HS4_correct.unpaired','HS5_correct.unpaired','HS6_correct.unpaired','MS3_correct.unpaired']
files3=['IRGSP_techin']



#bwa aln and sampe mapping   
#single-end
'''
os.system('/home/jpanibe/Bioinformatics/BWA/bwa-0.7.7/bwa index /home/jpanibe/TNG67/techin/IRGSP-1.0_genome.fasta')


i=0
while i<len(files2):	
	os.chdir('/home/jpanibe/TNG67/techin')	
        os.system('/home/jpanibe/Bioinformatics/BWA/bwa-0.7.7/bwa aln -t 50 -n 0.01 /home/jpanibe/TNG67/techin/IRGSP-1.0_genome.fasta %s.fastq > %s_%s_sa.sai' % (files2[i],files2[i],files3[0]))
                
        os.system('/home/jpanibe/Bioinformatics/BWA/bwa-0.7.7/bwa samse -n 100000000 /home/jpanibe/TNG67/techin/IRGSP-1.0_genome.fasta %s_%s_sa.sai %s.fastq > %s_%s_aln.sam' % (files2[i],files3[0],files2[i],files2[i],files3[0]))
	i+=1
'''

'''
##convert sam to bam

i=0
while i<len(files2):
        os.chdir('/home/jpanibe/TNG67/techin')
        os.system('samtools view -h -b -S %s_%s_aln.sam > %s_%s_aln.bam' % (files2[i],files3[0],files2[i],files3[0]))
        i+=1


#filter multi-mapper and unmapped reads
i=0
while i<len(files2):
	os.chdir('/home/jpanibe/TNG67/techin')
	os.system('samtools view -h -bF 4 -q 30 %s_%s_aln.bam > %s_%s_aln_bF4_q30.bam'  % (files2[i],files3[0],files2[i],files3[0]))
	i+=1
'''



#merge bam files
os.chdir('/home/jpanibe/TNG67/techin')
os.system('nohup java -jar /home/jpanibe/Bioinformatics/picard_tools/picard-tools-1.113/MergeSamFiles.jar \
INPUT=HS2_correct.filled_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded.bam \
INPUT=HS4_correct.filled_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded.bam \
INPUT=HS5_correct.filled_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded.bam \
INPUT=HS6_correct.filled_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded.bam \
INPUT=MS3_correct.filled_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded.bam \
INPUT=HS2_correct.unpaired_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded.bam \
INPUT=HS4_correct.unpaired_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded.bam \
INPUT=HS5_correct.unpaired_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded.bam \
INPUT=HS6_correct.unpaired_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded.bam \
INPUT=MS3_correct.unpaired_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded.bam \
OUTPUT=HS2+HS4+HS5+HS6+MS3[correct.filled+correct.unpaired]_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded.bam &> nohup.HS2+HS4+HS5+HS6+MS3[correct.filled+correct.unpaired]_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded.bam.out')


##sort bam 


os.chdir('/home/jpanibe/TNG67/techin')
os.system('java -jar /home/jpanibe/Bioinformatics/picard_tools/picard-tools-1.113/SortSam.jar INPUT=HS2+HS4+HS5+HS6+MS3[correct.filled+correct.unpaired]_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded.bam OUTPUT=HS2+HS4+HS5+HS6+MS3[correct.filled+correct.unpaired]_IRGSP_techin_aln_bF4_q30_coordinate_sorted_ReadGroupsadded_coordinate_sorted.bam SORT_ORDER=coordinate')

       
     







