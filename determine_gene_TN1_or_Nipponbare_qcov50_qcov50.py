import os

"""
Nipponbare_gene1=["Os12g0640600","Os12g0640800","Os12g0640900","Os12g0641100","Os12g0641300","Os12g0641400","Os12g0641500","Os12g0641600"]
Nipponbare_gene2=["OsTNG_gene1","OsTNG_gene2","OsTNG_gene2","OsTNG_gene2","OsTNG_gene2","OsTNG_gene1","OsTNG_gene3","OsTNG_gene4"]
Nipponbare_qcov=[85.00,67.00,95.00,98.00,99.00,86.00,89.00,66.00]
Nipponbare_qaln=[80.00,45.00,95.00,68.00,95.00,82.00,93.00,84.00]




TN1_gene1=["OsTN.1_gene_1","OsTN.1_gene_2","OsTN3_gene_3","OsTN.1_gene_4","OsTN.1_gene_5","OsTN.1_gene_6","OsTN.1_gene_7"]
TN1_gene2=["OsTNG_gene1","OsTNG_gene2","OsTNG_gene2","OsTNG_gene2","OsTNG_gene3","OsTNG_gene4","OsTNG_gene5"]
TN1_qcov=[100.00,90.00,50.00,90.00,80.00,50.00,55.00]
TN1_qaln=[100.00,90.00,50.00,70.00,92.00,52.00,56.00]
"""


var_qcov=50.00
var_qaln=50.00

Nipponbare_gene1=[]
Nipponbare_gene2=[]
Nipponbare_qcov=[]
Nipponbare_qaln=[]



TNG67_in_Nipponbare_gene1=[]
TNG67_in_Nipponbare_gene2=[]
TNG67_in_Nipponbare_qcov=[]
TNG67_in_Nipponbare_qaln=[]


TN1_gene1=[]
TN1_gene2=[]
TN1_qcov=[]
TN1_qaln=[]



TNG67_in_TN1_gene1=[]
TNG67_in_TN1_gene2=[]
TNG67_in_TN1_qcov=[]
TNG67_in_TN1_qaln=[]





with open('/home/jpanibe/CLC_Data/TNG67_annotation/TNG67_annotation/Nipponbare_v_TNG67_forsnpeff.nucmer1.filter.showcoords_Nipponbaregene.txt', 'r') as Nipponbare_gene1_file:
        for line in Nipponbare_gene1_file:
        # remove linebreak which is the last character of the string
                current_Nipponbare_gene1Place = line[:-1]

                Nipponbare_gene1.append(current_Nipponbare_gene1Place)


with open('/home/jpanibe/CLC_Data/TNG67_annotation/TNG67_annotation/Nipponbare_v_TNG67_forsnpeff.nucmer1.filter.showcoords_TNG67gene.txt', 'r') as Nipponbare_gene2_file:
        for line in Nipponbare_gene2_file:
                current_Nipponbare_gene2Place = line[:-1]

                Nipponbare_gene2.append(current_Nipponbare_gene2Place)



with open('/home/jpanibe/CLC_Data/TNG67_annotation/TNG67_annotation/Nipponbare_v_TNG67_forsnpeff.nucmer1.filter.showcoords_qcov.txt', 'r') as Nipponbare_qcov_file:
        for line in Nipponbare_qcov_file:
        # remove linebreak which is the last character of the string
                current_Nipponbare_qcovPlace = line[:-1]

                Nipponbare_qcov.append(float(current_Nipponbare_qcovPlace))


with open('/home/jpanibe/CLC_Data/TNG67_annotation/TNG67_annotation/Nipponbare_v_TNG67_forsnpeff.nucmer1.filter.showcoords_qaln.txt', 'r') as Nipponbare_qaln_file:
        for line in Nipponbare_qaln_file:
                current_Nipponbare_qalnPlace = line[:-1]

                Nipponbare_qaln.append(float(current_Nipponbare_qalnPlace))



with open('/home/jpanibe/CLC_Data/TNG67_annotation/TNG67_annotation/TN1_v_TNG67_forsnpeff.nucmer1.filter.showcoords_TN1gene.txt', 'r') as TN1_gene1_file:
        for line in TN1_gene1_file:
        # remove linebreak which is the last character of the string
                current_TN1_gene1Place = line[:-1]

                TN1_gene1.append(current_TN1_gene1Place)


with open('/home/jpanibe/CLC_Data/TNG67_annotation/TNG67_annotation/TN1_v_TNG67_forsnpeff.nucmer1.filter.showcoords_TNG67gene.txt', 'r') as TN1_gene2_file:
        for line in TN1_gene2_file:
                current_TN1_gene2Place = line[:-1]

                TN1_gene2.append(current_TN1_gene2Place)


with open('/home/jpanibe/CLC_Data/TNG67_annotation/TNG67_annotation/TN1_v_TNG67_forsnpeff.nucmer1.filter.showcoords_qcov.txt', 'r') as TN1_qcov_file:
        for line in TN1_qcov_file:
        # remove linebreak which is the last character of the string
                current_TN1_qcovPlace = line[:-1]

                TN1_qcov.append(float(current_TN1_qcovPlace))


with open('/home/jpanibe/CLC_Data/TNG67_annotation/TNG67_annotation/TN1_v_TNG67_forsnpeff.nucmer1.filter.showcoords_qaln.txt', 'r') as TN1_qaln_file:
        for line in TN1_qaln_file:
                current_TN1_qalnPlace = line[:-1]
		
                TN1_qaln.append(float(current_TN1_qalnPlace))


print Nipponbare_qaln

TNG67_not_assigned_gene1=[]
TNG67_not_assigned_gene2=[]
TNG67_not_assigned_qcov=[]
TNG67_not_assigned_qaln=[]


TNG67_uniquely_assigned_to_Nipponbare_gene1=[]
TNG67_uniquely_assigned_to_Nipponbare_gene2=[]
TNG67_uniquely_assigned_to_Nipponbare_qcov=[]
TNG67_uniquely_assigned_to_Nipponbare_qaln=[]

TNG67_uniquely_assigned_to_TN1_gene1=[]
TNG67_uniquely_assigned_to_TN1_gene2=[]
TNG67_uniquely_assigned_to_TN1_qcov=[]
TNG67_uniquely_assigned_to_TN1_qaln=[]


index=0


print "Nipponbare_gene2:\n"
print Nipponbare_gene2 

i=0
while i<len(Nipponbare_gene2):
	j=0
	while j<len(TN1_gene2):
		if Nipponbare_gene2[i]==TN1_gene2[j] and Nipponbare_qcov[i]>TN1_qcov[j] and Nipponbare_qaln[i]>TN1_qaln[j]:
			if Nipponbare_qcov[i]>var_qcov and Nipponbare_qaln[i]>var_qaln:
				if Nipponbare_gene2[i] not in TNG67_in_Nipponbare_gene2 and Nipponbare_gene2[i] not in TNG67_in_TN1_gene2:
					TNG67_in_Nipponbare_gene1.append(Nipponbare_gene1[i])
					TNG67_in_Nipponbare_gene2.append(Nipponbare_gene2[i])
					TNG67_in_Nipponbare_qcov.append(Nipponbare_qcov[i])
					TNG67_in_Nipponbare_qaln.append(Nipponbare_qaln[i])				
					print "\n"		
					print "TNG67_in_Nipponbare_gene1:"
					print TNG67_in_Nipponbare_gene1
					print "TNG67_in_Nipponbare_gene2:"
					print TNG67_in_Nipponbare_gene2
					print "TNG67_in_Nipponbare_qcov:"
					print TNG67_in_Nipponbare_qcov
					print "TNG67_in_Nipponbare_qaln:"
					print TNG67_in_Nipponbare_qaln
					print ("i:%d" % i)
					print ("j:%d" % j)	
				
				elif Nipponbare_gene2[i] in TNG67_in_TN1_gene2:
					index=TNG67_in_TN1_gene2.index(Nipponbare_gene2[i])
					print ("index:%s" % index)
					if Nipponbare_qcov[i]>TNG67_in_TN1_qcov[index] and TNG67_in_TN1_qcov[index]>50.00 and (Nipponbare_qaln[i]>TNG67_in_TN1_qaln[index] or Nipponbare_qaln[i]<TNG67_in_TN1_qaln[index]):
                                                TNG67_in_TN1_gene1[index]=Nipponbare_gene1[i]
                                                TNG67_in_TN1_gene2[index]=Nipponbare_gene2[i]
                                                TNG67_in_TN1_qcov[index]=Nipponbare_qcov[i]
                                                TNG67_in_TN1_qaln[index]=Nipponbare_qaln[i]
						print "\n"
						print "TNG67_in_Nipponbare_gene1:"
						print TNG67_in_Nipponbare_gene1
						print "TNG67_in_Nipponbare_gene2:"
						print TNG67_in_Nipponbare_gene2
						print "TNG67_in_Nipponbare_qcov:"
						print TNG67_in_Nipponbare_qcov
						print "TNG67_in_Nipponbare_qaln:"
						print TNG67_in_Nipponbare_qaln
						print ("i:%d" % i)
						print ("j:%d" % j)

						
				elif TN1_gene2[j] in TNG67_in_Nipponbare_gene2:
					index=TNG67_in_Nipponbare_gene2.index(TN1_gene2[j])
					print ("index:%s" % index)
					if TN1_qcov[j]>TNG67_in_Nipponbare_qcov[index] and TNG67_in_Nipponbare_qcov[index]>50.00 and (TN1_qaln[j]>TNG67_in_Nipponbare_qaln[index] or TN1_qaln[j]<TNG67_in_Nipponbare_qaln[index]):
						TNG67_in_Nipponbare_gene1[index]=TN1_gene1[j]
						TNG67_in_Nipponbare_gene2[index]=TN1_gene2[j]
						TNG67_in_Nipponbare_qcov[index]=TN1_qcov[j]
						TNG67_in_Nipponbare_qaln[index]=TN1_qaln[j]
						print "\n"
						print "TNG67_in_Nipponbare_gene1:"
						print TNG67_in_Nipponbare_gene1
						print "TNG67_in_Nipponbare_gene2:"
						print TNG67_in_Nipponbare_gene2
						print "TNG67_in_Nipponbare_qcov:"
						print TNG67_in_Nipponbare_qcov
						print "TNG67_in_Nipponbare_qaln:"
						print TNG67_in_Nipponbare_qaln
						print ("i:%d" % i)
						print ("j:%d" % j)					
				else:
					print "ewan"					



		elif Nipponbare_gene2[i]==TN1_gene2[j] and TN1_qcov[j]>Nipponbare_qcov[i] and TN1_qaln[j]>Nipponbare_qaln[i]:
			if TN1_qcov[j]>var_qcov and TN1_qaln[j]>var_qaln:
				if TN1_gene2[j] not in TNG67_in_TN1_gene2 and TN1_gene2[j] not in TNG67_in_Nipponbare_gene2:
					TNG67_in_TN1_gene1.append(TN1_gene1[j])
					TNG67_in_TN1_gene2.append(TN1_gene2[j])
					TNG67_in_TN1_qcov.append(TN1_qcov[j])
					TNG67_in_TN1_qaln.append(TN1_qaln[j])                 
					print "\n"
					print "TNG67_in_TN1_gene1:"
					print TNG67_in_TN1_gene1
					print "TNG67_in_TN1_gene2:"
					print TNG67_in_TN1_gene2
					print "TNG67_in_TN1_qcov:"
					print TNG67_in_TN1_qcov
					print "TNG67_in_TN1_qaln:"
					print TNG67_in_TN1_qaln
					print ("i:%d" % i)
					print ("j:%d" % j)
					print "ewan"
				elif Nipponbare_gene2[i] in TNG67_in_TN1_gene2:
					index=TNG67_in_TN1_gene2.index(Nipponbare_gene2[i])
					print ("index:%s" % index)
					if Nipponbare_qcov[i]>TNG67_in_TN1_qcov[index] and TNG67_in_TN1_qcov[index]>50.00 and (Nipponbare_qaln[i]>TNG67_in_TN1_qaln[index] or Nipponbare_qaln[i]<TNG67_in_TN1_qaln[index]):
						TNG67_in_TN1_gene1[index]=Nipponbare_gene1[i]
						TNG67_in_TN1_gene2[index]=Nipponbare_gene2[i]
						TNG67_in_TN1_qcov[index]=Nipponbare_qcov[i]
						TNG67_in_TN1_qaln[index]=Nipponbare_qaln[i]
						print "\n"
						print "TNG67_in_TN1_gene1:"
						print TNG67_in_TN1_gene1
						print "TNG67_in_TN1_gene2:"
						print TNG67_in_TN1_gene2
						print "TNG67_in_TN1_qcov:"
						print TNG67_in_TN1_qcov
						print "TNG67_in_TN1_qaln:"
						print TNG67_in_TN1_qaln
						print ("i:%d" % i)
						print ("j:%d" % j)
				elif TN1_gene2[j] in TNG67_in_Nipponbare_gene2:
					index=TNG67_in_Nipponbare_gene2.index(TN1_gene2[j])
					print ("index:%s" % index)
					if TN1_qcov[j]>TNG67_in_Nipponbare_qcov[index] and TNG67_in_Nipponbare_qcov[index]>50.00 and (TN1_qaln[j]>TNG67_in_Nipponbare_qaln[index] or TN1_qaln[j]<TNG67_in_Nipponbare_qaln[index]):
						TNG67_in_Nipponbare_gene1[index]=TN1_gene1[j]
						TNG67_in_Nipponbare_gene2[index]=TN1_gene2[j]
						TNG67_in_Nipponbare_qcov[index]=TN1_qcov[j]
						TNG67_in_Nipponbare_qaln[index]=TN1_qaln[j]
						print "\n"
						print "TNG67_in_TN1_gene1:"
						print TNG67_in_TN1_gene1
						print "TNG67_in_TN1_gene2:"
						print TNG67_in_TN1_gene2
						print "TNG67_in_TN1_qcov:"
						print TNG67_in_TN1_qcov
						print "TNG67_in_TN1_qaln:"
						print TNG67_in_TN1_qaln
						print ("i:%d" % i)
						print ("j:%d" % j)

			
			else:
				print "ewan"

		
		j=j+1
	i=i+1	


j=0
while j<len(TN1_gene2):
	if TN1_gene2[j] not in Nipponbare_gene2 and TN1_qcov[j]>var_qcov and TN1_qaln[j]>var_qaln:
		TNG67_uniquely_assigned_to_TN1_gene1.append(TN1_gene1[j])
		TNG67_uniquely_assigned_to_TN1_gene2.append(TN1_gene2[j])
		TNG67_uniquely_assigned_to_TN1_qcov.append(TN1_qcov[j])
		TNG67_uniquely_assigned_to_TN1_qaln.append(TN1_qaln[j])
	j=j+1



j=0
while j<len(Nipponbare_gene2):
	if Nipponbare_gene2[j] not in TN1_gene2 and Nipponbare_qcov[j]>var_qcov and Nipponbare_qaln[j]>var_qaln:
		TNG67_uniquely_assigned_to_Nipponbare_gene1.append(Nipponbare_gene1[j])
		TNG67_uniquely_assigned_to_Nipponbare_gene2.append(Nipponbare_gene2[j])
		TNG67_uniquely_assigned_to_Nipponbare_qcov.append(Nipponbare_qcov[j])
		TNG67_uniquely_assigned_to_Nipponbare_qaln.append(Nipponbare_qaln[j])
	j=j+1



print "\n"
print "TNG67_in_Nipponbare_gene1:"
print TNG67_in_Nipponbare_gene1
print "TNG67_in_Nipponbare_gene2:"
print TNG67_in_Nipponbare_gene2
print "TNG67_in_Nipponbare_qcov:"
print TNG67_in_Nipponbare_qcov
print "TNG67_in_Nipponbare_qaln:"
print TNG67_in_Nipponbare_qaln
print "\n"
print "TNG67_in_TN1_gene1:"
print TNG67_in_TN1_gene1
print "TNG67_in_TN1_gene2:"
print TNG67_in_TN1_gene2
print "TNG67_in_TN1_qcov:"
print TNG67_in_TN1_qcov
print "TNG67_in_TN1_qaln:"
print TNG67_in_TN1_qaln

print "hello"

index_A=0
index_B=0


#only 1 while loop, because the previos list contain unique members. So 1 round lang.


merged_TNG67_in_NipandTN1_gene1 = TNG67_in_Nipponbare_gene1 + TNG67_in_TN1_gene1

merged_TNG67_in_NipandTN1_gene2 = TNG67_in_Nipponbare_gene2 + TNG67_in_TN1_gene2

merged_TNG67_in_NipandTN1_qcov = TNG67_in_Nipponbare_qcov + TNG67_in_TN1_qcov

merged_TNG67_in_NipandTN1_qaln = TNG67_in_Nipponbare_qaln + TNG67_in_TN1_qaln



print merged_TNG67_in_NipandTN1_gene1 
print merged_TNG67_in_NipandTN1_gene2 
print merged_TNG67_in_NipandTN1_qcov 
print merged_TNG67_in_NipandTN1_qaln


import re

#word_to_use_Nip_gene = r'Os([0-9][0-9].*?)'
#word_to_use_TN1_gene = r'OsTN.(.*?)'

#word_to_use_Nip_gene = r'Os([0-9].*?)'
word_to_use_TN1_gene = r'OsTN(.*?)'


#filtered_TNG67_in_Nip_gene1 = list(filter(lambda x: re.match(word_to_use_Nip_gene, x), merged_TNG67_in_NipandTN1_gene1))
filtered_TNG67_in_TN1_gene1 = list(filter(lambda x: re.match(word_to_use_TN1_gene, x), merged_TNG67_in_NipandTN1_gene1))



#filtered_TNG67_in_Nip_gene1=merged_TNG67_in_NipandTN1_gene1-filtered_TNG67_in_TN1_gene1


set1 = set(merged_TNG67_in_NipandTN1_gene1)
set2 = set(filtered_TNG67_in_TN1_gene1)
set3 = set1.difference(set2)
filtered_TNG67_in_Nip_gene1 = list(set3)






print "filtered_TNG67_in_Nip_gene1:"
print(filtered_TNG67_in_Nip_gene1)
print "filtered_TNG67_in_TN1_gene1"
print(filtered_TNG67_in_TN1_gene1)


final_filtered_TNG67_in_Nip_gene1=[]
final_filtered_TNG67_in_Nip_gene2=[]
final_filtered_TNG67_in_Nip_qcov=[]
final_filtered_TNG67_in_Nip_qaln=[]

final_filtered_TNG67_in_TN1_gene1=[]
final_filtered_TNG67_in_TN1_gene2=[]
final_filtered_TNG67_in_TN1_qcov=[]
final_filtered_TNG67_in_TN1_qaln=[]

index_C=0

i=0
while i<len(filtered_TNG67_in_Nip_gene1):
	index_C=merged_TNG67_in_NipandTN1_gene1.index(filtered_TNG67_in_Nip_gene1[i])
	final_filtered_TNG67_in_Nip_gene1.append(merged_TNG67_in_NipandTN1_gene1[index_C])
	final_filtered_TNG67_in_Nip_gene2.append(merged_TNG67_in_NipandTN1_gene2[index_C])
	final_filtered_TNG67_in_Nip_qcov.append(merged_TNG67_in_NipandTN1_qcov[index_C])
	final_filtered_TNG67_in_Nip_qaln.append(merged_TNG67_in_NipandTN1_qaln[index_C])
	print i
	i=i+1



print "final_filtered_TNG67_in_Nip_gene1\n"
print final_filtered_TNG67_in_Nip_gene1
print final_filtered_TNG67_in_Nip_gene2
print final_filtered_TNG67_in_Nip_qcov
print final_filtered_TNG67_in_Nip_qaln 



index_D=0
i=0
while i<len(filtered_TNG67_in_TN1_gene1):
        index_D=merged_TNG67_in_NipandTN1_gene1.index(filtered_TNG67_in_TN1_gene1[i])
	final_filtered_TNG67_in_TN1_gene1.append(merged_TNG67_in_NipandTN1_gene1[index_D])
	final_filtered_TNG67_in_TN1_gene2.append(merged_TNG67_in_NipandTN1_gene2[index_D])
	final_filtered_TNG67_in_TN1_qcov.append(merged_TNG67_in_NipandTN1_qcov[index_D])
	final_filtered_TNG67_in_TN1_qaln.append(merged_TNG67_in_NipandTN1_qaln[index_D])
	print i
	i=i+1

print "final_filtered_TNG67_in_TN1_gene1\n"
print final_filtered_TNG67_in_TN1_gene1
print final_filtered_TNG67_in_TN1_gene2
print final_filtered_TNG67_in_TN1_qcov
print final_filtered_TNG67_in_TN1_qaln


print "TNG67_uniquely_assigned_to_Nipponbare_gene2"
print TNG67_uniquely_assigned_to_Nipponbare_gene2

print "TNG67_uniquely_assigned_to_TN1_gene2"
print TNG67_uniquely_assigned_to_TN1_gene2

print "\n\n"
print "number of TNG67 genes assigned to Nipponbare: %d" % len(final_filtered_TNG67_in_Nip_gene1)
print "number of TNG67 genes assigned to TN1: %d" % len(final_filtered_TNG67_in_TN1_gene1)
print "number of TNG67 genes uniquely assigned to Nipponbare: %d" % len(TNG67_uniquely_assigned_to_Nipponbare_gene2)
print "number of TNG67 genes uniquely assigned to TN1: %d" % len(TNG67_uniquely_assigned_to_TN1_gene2)



