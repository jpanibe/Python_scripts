import os

#set to path: /home/jpanibe/CLC_Data/GATK/gatk-4.1.7.0



os.chdir('')



#Step1

os.system('bwa mem \
-K 100000000 \
-Y \
-R '@RG\tID:%s\tLB:%s\tPL:ILLUMINA\tPM:HISEQ\tSM:%s' \
TN1.fasta \
%s_R1.fq \
%s_R2.fq \
> aligned_reads.sam' % (files[i],files[i],files[i],files[i],files[i]))

#Step2


os.system('MarkDuplicatesSpark \
	-I aligned_reads.sam \
	-M dedup_metrics.txt \
	-O sorted_dedup_reads.bam')


#Step3

os.system('java -jar picard.jar \
        CollectAlignmentSummaryMetrics \
        R=TN1.fasta \
        I=sorted_dedup_reads.bam \
        O=alignment_metrics.txt')

os.system('java -jar picard.jar \
CollectInsertSizeMetrics \
        INPUT=sorted_dedup_reads.bam \
        OUTPUT=insert_metrics.txt \
        HISTOGRAM_FILE=insert_size_histogram.pdf')

os.system('samtools depth -a sorted_dedup_reads.bam > depth_out.txt')


#Step4

os.system('gatk HaplotypeCaller \
        -R TN1.fasta \
        -I sorted_dedup_reads.bam \
        -o raw_variants.vcf')



#Step5


os.system('gatk SelectVariants \
        -R TN1.fasta \
        -V raw_variants.vcf \
        -selectType SNP \
        -o raw_snps.vcf')

os.system('gatk SelectVariants \
        -R TN1.fasta \
        -V raw_variants.vcf \
        -selectType INDEL \
        -o raw_indels.vcf')


#Step6


os.system('gatk VariantFiltration \
        -R TN1.fasta \
        -V raw_snps.vcf \
        -O filtered_snps.vcf \
        -filter-name "QD_filter" -filter "QD < 2.0" \
        -filter-name "FS_filter" -filter "FS > 60.0" \
        -filter-name "MQ_filter" -filter "MQ < 40.0" \
        -filter-name "SOR_filter" -filter "SOR > 4.0" \
        -filter-name "MQRankSum_filter" -filter "MQRankSum < -12.5" \
        -filter-name "ReadPosRankSum_filter" -filter "ReadPosRankSum < -8.0"')


#Step7


os.system('gatk VariantFiltration \
        -R TN1.fasta \
        -V raw_indels.vcf \
        -O filtered_indels.vcf \
        -filter-name "QD_filter" -filter "QD < 2.0" \
        -filter-name "FS_filter" -filter "FS > 200.0" \
        -filter-name "SOR_filter" -filter "SOR > 10.0"')


#Step8

os.system('gatk SelectVariants \
        --exclude-filtered \
        -V filtered_snps.vcf \
        -O bqsr_snps.vcf')



os.system('gatk SelectVariants \
        --exclude-filtered \
        -V filtered_indels.vcf \
        -O bqsr_indels.vcf')



#Step9


os.system('gatk BaseRecalibrator \
        -R TN1.fasta \
        -I sorted_dedup_reads.bam \
        --known-sites bqsr_snps.vcf \
        --known-sites bqsr_indels.vcf \
        -O recal_data.table')


#Step10


os.system('gatk ApplyBQSR \
        -R TN1.fasta \
        -I sorted_dedup_reads.bam \
        -bqsr recal_data.table \
        -O recal_reads.bam')



#Step11


os.system('gatk BaseRecalibrator \
        -R TN1.fasta \
        -I recal_reads.bam \
        --known-sites bqsr_snps.vcf \
        --known-sites bqsr_indels.vcf \
        -O post_recal_data.table')


#Step12

os.system('gatk AnalyzeCovariates \        
       -before recal_data.table \
        -after post_recal_data.table \
        -plots recalibration_plots.pdf')



#Step13

os.system('gatk HaplotypeCaller \
        -R TN1.fasta \
        -I recal_reads.bam \
        -o raw_variants_recal.vcf')


#Step14



os.system('gatk SelectVariants \
        -R TN1.fasta \
        -V raw_variants_recal.vcf \
        -selectType SNP \
        -o raw_snps_recal.vcf')


os.system('gatk SelectVariants \
        -R TN1.fasta \
        -V raw_variants.vcf \
        -selectType INDEL \
        -o raw_indels_recal.vcf')


#Step15


os.system('gatk VariantFiltration \       
-R TN1.fasta \
        -V raw_snps_recal.vcf \
        -O filtered_snps_final.vcf \
        -filter-name "QD_filter" -filter "QD < 2.0" \
        -filter-name "FS_filter" -filter "FS > 60.0" \
        -filter-name "MQ_filter" -filter "MQ < 40.0" \
        -filter-name "SOR_filter" -filter "SOR > 4.0" \
        -filter-name "MQRankSum_filter" -filter "MQRankSum < -12.5" \
        -filter-name "ReadPosRankSum_filter" -filter "ReadPosRankSum < -8.0"')


#Step16


os.system('gatk VariantFiltration \        
	-R TN1.fasta \
        -V raw_indels_recal.fa \
        -O filtered_indels_final.vcf \
        -filter-name "QD_filter" -filter "QD < 2.0" \
        -filter-name "FS_filter" -filter "FS > 200.0" \
        -filter-name "SOR_filter" -filter "SOR > 10.0"')


#Step17


os.system('java -jar snpEff.jar -v \        
	<snpeff_db> \
        filtered_snps_final.vcf > $filtered_snps_final.ann.vcf')

#Step18

os.system('parse_metrics.sh sample_id > sample_id_report.csv')



