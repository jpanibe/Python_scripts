import os

Nipponbare_gene1=["Nip_gene_A","Nip_gene_B","Nip_gene_C","Nip_gene_D","Nip_gene_E","Nip_gene_F","Nip_gene_G","Nip_gene_H"]
Nipponbare_gene2=["TNG67_gene1","TNG67_gene2","TNG67_gene2","TNG67_gene2","TNG67_gene2","TNG67_gene1","TNG67_gene3","TNG67_gene4"]
Nipponbare_qcov=[85,67,95,98,99,86,89,66]
Nipponbare_qaln=[80,45,95,68,95,82,93,84]
TNG67_in_Nipponbare_gene1=[]
TNG67_in_Nipponbare_gene2=[]
TNG67_in_Nipponbare_qcov=[]
TNG67_in_Nipponbare_qaln=[]


TN1_gene1=["TN1_gene_1","TN1_gene_2","TN1_gene_3","TN1_gene_4","TN1_gene_5","TN1_gene_6","TN1_gene_7"]
TN1_gene2=["TNG67_gene1","TNG67_gene2","TNG67_gene2","TNG67_gene2","TNG67_gene3","TNG67_gene4","TNG67_gene5"]
TN1_qcov=[100,90,50,90,80,50,55]
TN1_qaln=[100,90,50,70,92,52,56]
TNG67_in_TN1_gene1=[]
TNG67_in_TN1_gene2=[]
TNG67_in_TN1_qcov=[]
TNG67_in_TN1_qaln=[]
index=0


print Nipponbare_gene2 

i=0
while i<len(Nipponbare_gene2):
	j=0
	while j<len(TN1_gene2):
		if Nipponbare_gene2[i]==TN1_gene2[j] and Nipponbare_qcov[i]>TN1_qcov[j] and Nipponbare_qaln[i]>TN1_qaln[j]:
			if Nipponbare_qcov[i]>50 and Nipponbare_qaln[i]>50:
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
					if Nipponbare_qcov[i]>TNG67_in_TN1_qcov[index] and (Nipponbare_qaln[i]>TNG67_in_TN1_qaln[index] or Nipponbare_qaln[i]<TNG67_in_TN1_qaln[index]):
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
					if TN1_qcov[j]>TNG67_in_Nipponbare_qcov[index] and (TN1_qaln[j]>TNG67_in_Nipponbare_qaln[index] or TN1_qaln[j]<TNG67_in_Nipponbare_qaln[index]):
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
			if TN1_qcov[j]>50 and TN1_qaln[j]>50:
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
					if Nipponbare_qcov[i]>TNG67_in_TN1_qcov[index] and (Nipponbare_qaln[i]>TNG67_in_TN1_qaln[index] or Nipponbare_qaln[i]<TNG67_in_TN1_qaln[index]):
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
					if TN1_qcov[j]>TNG67_in_Nipponbare_qcov[index] and (TN1_qaln[j]>TNG67_in_Nipponbare_qaln[index] or TN1_qaln[j]<TNG67_in_Nipponbare_qaln[index]):
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

word_to_use_Nip_gene = r'Nip_gene_(.*?)'
word_to_use_TN1_gene = r'TN1_gene_(.*?)'


filtered_TNG67_in_Nip_gene1 = list(filter(lambda x: re.match(word_to_use_Nip_gene, x), merged_TNG67_in_NipandTN1_gene1))
filtered_TNG67_in_TN1_gene1 = list(filter(lambda x: re.match(word_to_use_TN1_gene, x), merged_TNG67_in_NipandTN1_gene1))


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


