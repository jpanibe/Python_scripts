import os

files=['ec_trimmomatic_minlen215_ec']

os.chdir('/home/jpanibe/CLC_Data')


i=0

while i<len(files):
	os.system('java -jar /home/jpanibe/CLC_Data/picard_tools/picard/build/libs/picard.jar CollectInsertSizeMetrics I=%s_mem_sort.bam O=%s_mem_sort_insert_size_metrics.txt H=%s_mem_sort_insert_size_histogram.pdf M=0.5' %(files[i],files[i],files[i]))
	i+=1


