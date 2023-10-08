import os

os.chdir('/home/jpanibe/CLC_Data/TN1_proteins')

threshold=1.0e-50
col_1=[]
col_3=[]
col_14=[]
col_15=[]
gene_in_TN1=[]
gene_in_Nipponbare=[]
gene_neither=[]

with open('TNG67_cds_sequence.fasta_to_TN1_and_IRGSP_cds.fasta_col_1.txt', 'r') as col_1_file:
	for line in col_1_file:
	# remove linebreak which is the last character of the string
		current_col_1 = line[:-1]

		col_1.append(current_col_1)


with open('TNG67_cds_sequence.fasta_to_TN1_and_IRGSP_cds.fasta_col_3.txt', 'r') as col_3_file:
	for line in col_3_file: 
		current_col_3 = line[:-1]
		
		col_3.append(current_col_3)	




with open('TNG67_cds_sequence.fasta_to_TN1_and_IRGSP_cds.fasta_col_14.txt', 'r') as col_14_file:
        for line in col_14_file:
                current_col_14 = line[:-1]

                col_14.append(current_col_14)




with open('TNG67_cds_sequence.fasta_to_TN1_and_IRGSP_cds.fasta_col_15.txt', 'r') as col_15_file:
        for line in col_15_file:
                current_col_15 = line[:-1]

                col_15.append(current_col_15)


counter=len(col_1)





i=0
while i<(len(col_1)-1):
	if "OsTN" in col_3[i] and "OsTN" in col_3[i+1]:
		gene_in_TN1.append(col_1[i])
	elif "OsTN" not in col_3[i] and "OsTN" not in col_3[i+1]:
		gene_in_Nipponbare.append(col_1[i])
	elif "OsTN" in col_3[i] and "OsTN" not in col_3[i+1]:
		if (float(col_14[i+1])-float(col_14[i])==float(0)) and (float(col_15[i])-float(col_15[i+1])>0):
			gene_in_TN1.append(col_1[i])		
		elif (float(col_14[i+1])-float(col_14[i])>float(0)) and (float(col_15[i])-float(col_15[i+1])>0):
			gene_in_TN1.append(col_1[i])						
		elif (float(col_14[i+1])-float(col_14[i])==float(0)) and (float(col_15[i])-float(col_15[i+1])<0):
			gene_in_Nipponbare.append(col_1[i])
		elif (float(col_14[i+1])-float(col_14[i])==float(0)) and (float(col_15[i])-float(col_15[i+1])==0):
			gene_neither.append(col_1[i])
	elif "OsTN" not in col_3[i] and "OsTN" in col_3[i+1]:	
		if (float(col_14[i+1])-float(col_14[i])==float(0)) and (float(col_15[i])-float(col_15[i+1])>0):
			gene_in_Nipponbare.append(col_1[i])
		elif (float(col_14[i+1])-float(col_14[i])>float(0)) and (float(col_15[i])-float(col_15[i+1])>0):	
			gene_in_Nipponbare.append(col_1[i])
		elif (float(col_14[i+1])-float(col_14[i])==float(0)) and (float(col_15[i])-float(col_15[i+1])<0):
			gene_in_TN1.append(col_1[i])
		elif (float(col_14[i+1])-float(col_14[i])==float(0)) and (float(col_15[i])-float(col_15[i+1])==0):
			gene_neither.append(col_1[i])
	i=i+2



#unique_count_TN1=len(set(gene_in_TN1))
#unique_count_Nipponbare=len(set(gene_in_Nipponbare))

#print "number of unique count of TN1 cds:%d" % unique_count_TN1
#print "number of unique count of Nipponbare cds:%d" % unique_count_Nipponbare
print "number of TN1 cds:%d" % len(gene_in_TN1)
print "number of Nipponbare cds:%d" % len(gene_in_Nipponbare)
print "number of neither genes:%d" % len(gene_neither)

total=len(gene_in_TN1)+len(gene_in_Nipponbare)+len(gene_neither)

print "total:%d" % total
print "number of blast hits:%d" % len(col_1)


print "number of unique TN1 cds:%d" % len(set(gene_in_TN1))
print "number of unique Nipponbare cds:%d" % len(set(gene_in_Nipponbare))


