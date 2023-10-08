import os

Nipponbare_gene1=["Nip_gene_A","Nip_gene_B","Nip_gene_C","Nip_gene_D","Nip_gene_E","Nip_gene_F"]
Nipponbare_gene2=["TNG67_gene1","TNG67_gene2","TNG67_gene2","TNG67_gene2","TNG67_gene2","TNG67_gene1"]
Nipponbare_qcov=[85,90,95,98,99,86]
Nipponbare_qaln=[80,90,95,68,95,82]
TNG67_in_Nipponbare_gene1=[]
TNG67_in_Nipponbare_gene2=[]
TNG67_in_Nipponbare_qcov=[]
TNG67_in_Nipponbare_qaln=[]


TN1_gene1=["TN1_gene_A","TN1_gene_B","TN1_gene_C","TN1_gene_D"]
TN1_gene2=["TNG67_gene1","TNG67_gene2","TNG67_gene2","TNG67_gene2"]
TN1_qcov=[55,67,80,90]
TN1_qaln=[60,45,55,70]
TNG67_in_TN1_gene1=[]
TNG67_in_TN1_gene2=[]
TNG67_in_TN1_qcov=[]
TNG67_in_TN1_qaln=[]
index=0

"""
with open('', 'r') as Nipponbare_gene1_file:
        for line in Nipponbare_gene1_file:
        # remove linebreak which is the last character of the string
                current_Nipponbare_gene1Place = line[:-1]

                Nipponbare_gene1.append(current_Nipponbare_gene1Place)


with open('', 'r') as Nipponbare_gene2_file:
        for line in Nipponbare_gene2_file:
                current_Nipponbare_gene2Place = line[:-1]

                Nipponbare_gene2.append(current_Nipponbare_gene2Place)



with open('', 'r') as Nipponbare_qcov_file:
        for line in Nipponbare_qcov_file:
        # remove linebreak which is the last character of the string
                current_Nipponbare_qcovPlace = line[:-1]

                Nipponbare_qcov.append(current_Nipponbare_qcovPlace)


with open('', 'r') as Nipponbare_qaln_file:
        for line in Nipponbare_qaln_file:
                current_Nipponbare_qalnPlace = line[:-1]

                Nipponbare_qaln.append(current_Nipponbare_qalnPlace)


with open('', 'r') as TN1_gene1_file:
        for line in TN1_gene1_file:
        # remove linebreak which is the last character of the string
                current_TN1_gene1Place = line[:-1]

                TN1_gene1.append(current_TN1_gene1Place)


with open('', 'r') as TN1_gene2_file:
        for line in querylist_file:
                current_TN1_gene2Place = line[:-1]

                TN1_gene2.append(current_TN1_gene2Place)


with open('', 'r') as TN1_qcov_file:
        for line in TN1_qcov_file:
        # remove linebreak which is the last character of the string
                current_TN1_qcovPlace = line[:-1]

                TN1_qcov.append(current_TN1_qcovPlace)


with open('', 'r') as TN1_qaln_file:
        for line in TN1_qaln_file:
                current_TN1_qalnPlace = line[:-1]

                TN1_qaln.append(current_TN1_qalnPlace)
"""

print Nipponbare_gene2 

i=0

TNG67_in_Nipponbare_gene1=[Nipponbare_gene1[i]]
TNG67_in_Nipponbare_gene2=[Nipponbare_gene1[i]]
TNG67_in_Nipponbare_qcov=[Nipponbare_qcov[i]]
TNG67_in_Nipponbare_qaln=[Nipponbare_qaln[i]]


TNG67_in_TN1_gene1=[TN1_gene1[i]]
TNG67_in_TN1_gene2=[TN1_gene1[i]]
TNG67_in_TN1_qcov=[TN1_qcov[i]]
TNG67_in_TN1_qaln=[TN1_qaln[i]]

while i<len(Nipponbare_gene2):

	print ("i:%d" % i)

	if Nipponbare_gene2[i]==TNG67_in_Nipponbare_gene2 and Nipponbare_qcov[i]>TN1_qcov[j] and Nipponbare_qaln[i]>TN1_qaln[j]:
		if Nipponbare_qcov[i]>50 and Nipponbare_qaln[i]>50:
			if Nipponbare_gene2[i] not in TNG67_in_Nipponbare_gene2:
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

						
			else:
				index=TNG67_in_Nipponbare_gene2.index(Nipponbare_gene2[i])
				print ("index:%s" % index)
				if Nipponbare_qcov[i]>TNG67_in_Nipponbare_qcov[index] and Nipponbare_qaln[i]>TNG67_in_Nipponbare_qaln[index]:
					TNG67_in_Nipponbare_gene1[index]=Nipponbare_gene1[i]
					TNG67_in_Nipponbare_gene2[index]=Nipponbare_gene2[i]
					TNG67_in_Nipponbare_qcov[index]=Nipponbare_qcov[i]
					TNG67_in_Nipponbare_qaln[index]=Nipponbare_qaln[i]
				elif Nipponbare_qcov[i]>TNG67_in_Nipponbare_qcov[index] and Nipponbare_qaln[i]<TNG67_in_Nipponbare_qaln[index]:
					TNG67_in_Nipponbare_gene1[index]=Nipponbare_gene1[i]
					TNG67_in_Nipponbare_gene2[index]=Nipponbare_gene2[i]
					TNG67_in_Nipponbare_qcov[index]=Nipponbare_qcov[i]
					TNG67_in_Nipponbare_qaln[index]=Nipponbare_qaln[i]
					print "\n"
					print "TNG67_in_Nipponbare_gene1:"
					print TNG67_in_Nipponbare_gene1
					print "TNG67_in_Nipponbare_gene2:"
					print TNG67_in_Nipponbare_gene2
					print "TNG67_in_Nipponbare_qcov:"
					print TNG67_in_Nipponbare_qcov
					print "TNG67_in_Nipponbare_qaln:"
					print TNG67_in_Nipponbare_qaln
	
			
				

	#no append, just replace via sub in index. Also no need for counter because append is the method to add the new gene in the list	
		
					
												
			
	i=i+1

"""				
		elif Nipponbare_gene2[i]==TN1_gene2[j] and TN1_qcov[j]>Nipponbare_qcov[i] and TN1_qaln[j]>Nipponbare_qaln[i]:
			if TN1_qcov[j]>50 and TN1_qaln[j]>50:								
				if TN1_gene2[j] not in TNG67_in_TN1_gene2:
					TNG67_in_TN1_gene1.append(Nipponbare_gene1[i])
                                        TNG67_in_TN1_gene2.append(Nipponbare_gene2[i])
                                        TNG67_in_TN1_qcov.append(Nipponbare_qcov[i])
                                        TNG67_in_TN1_qaln.append(Nipponbare_qcov[i]) 


					j=j+1
				else:
					index=TNG67_in_TN1_gene2.index(TN1_gene2[j])
					if TN1_qcov[j]>TN1_qcov[index] and TN1_qaln[j]>TN1_qaln[index]:
						TNG67_in_TN1_gene1[index]=TN1_gene2[j]
						TNG67_in_TN1_gene2[index]=TN1_gene2[j]
						TNG67_in_TN1_qcov[index]=TN1_gene2[j]
						TNG67_in_TN1_qaln[index]=TN1_gene2[j]
					j=j+1
			else:
				j=j+1
"""
	
		
#		i=i+1

		
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


