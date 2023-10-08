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
TN1_qcov=[55,67,100,90]
TN1_qaln=[60,45,100,70]
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
					print ("i:%d" % i)
					print ("j:%d" % j)
					
						
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
					print ("i:%d" % i)
					print ("j:%d" % j)
													
			else:
				print "ewan"					



		elif Nipponbare_gene2[i]==TN1_gene2[j] and TN1_qcov[j]>Nipponbare_qcov[i] and TN1_qaln[j]>Nipponbare_qaln[i]:
			if TN1_qcov[j]>50 and TN1_qaln[j]>50:
				if TN1_gene2[j] not in TNG67_in_TN1_gene2:
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
				else:
					index=TNG67_in_TN1_gene2.index(TN1_gene2[j])
					print ("index:%s" % index)
					if TN1_qcov[j]>TNG67_in_TN1_qcov[index] and Nipponbare_qaln[i]>TNG67_in_TN1_qaln[index]:
						TNG67_in_TN1_gene1[index]=TN1_gene1[j]
						TNG67_in_TN1_gene2[index]=TN1_gene2[j]
						TNG67_in_TN1_qcov[index]=TN1_qcov[j]
						TNG67_in_TN1_qaln[index]=TN1_qaln[j]
					elif TN1_qcov[j]>TNG67_in_TN1_qcov[index] and TN1_qaln[j]<TNG67_in_TN1_qaln[index]:
						TNG67_in_TN1_gene1[index]=TN1_gene1[j]
						TNG67_in_TN1_gene2[index]=TN1_gene2[j]
						TNG67_in_TN1_qcov[index]=TN1_qcov[j]
						TNG67_in_TN1_qaln[index]=TN1_qaln[j]
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
			else:
				print "ewan"

		j=j+1
	i=i+1	


"""
i=0
while i<len(TNG67_in_Nipponbare_gene2):
	j=0
	while i<len(TNG67_in_TN1_gene2):

		  if TN1_qcov[j]>50 and TN1_qaln[j]>50:
                                if TN1_gene2[j] not in TNG67_in_TN1_gene2:
                                        TNG67_in_TN1_gene1.append(TN1_gene1[j])
                                        TNG67_in_TN1_gene2.append(TN1_gene2[j])
                                        TNG67_in_TN1_qcov.append(TN1_qcov[j])
                                        TNG67_in_TN1_qaln.append(TN1_qaln[j])

"""
"""
index=0
	
    
                        

	

                                if TNG67_in_TN1_gene2[j] in TNG67_in_Nipponbare_gene2:
 					index=TNG67_in_TN1_gene2.index(TNG67_in_TN1_gene2[j])                                       
	
					if (TNG67_in_Nipponbare_qcov[i]>TNG67_in_TN1_qcov[j] and TNG67_in_Nipponbare_qaln[i]>TNG67_in_TN1_qaln[j]) or (TNG67_in_Nipponbare_qcov[i]>TNG67_in_TN1_qcov[j] and TNG67_in_Nipponbare_qaln[i]<=TNG67_in_TN1_qaln[j])

					TNG67_in_TN1_gene1.pop(TNG67_in_TN1_gene1[index])
                                        TNG67_in_TN1_gene2.pop(TNG67_in_TN1_gene2[index])
                                        TNG67_in_TN1_qcov.pop(TNG67_in_TN1_qcov[index])
                                        TNG67_in_TN1_qaln.pop(TNG67_in_TN1_qaln[index])



				elif:
					j=j+1

				elif TNG67_in_Nipponbare_gene2[j] in TNG67_in_TN1_gene2:
                                        index=TNG67_in_Nipponbare_gene2.index(TNG67_in_Nipponbare_gene2[j])

                                        if (TNG67_in_TN1_qcov[i]>TNG67_in_Nipponbare_qcov[j] and TNG67_in_TN1_qaln[i]>TNG67_in_Nipponbare_qaln[j]) or (TNG67_in_TN1_qcov[i]>TNG67_in_Nipponbare_qcov[j] and TNG67_in_TN1_qaln[i]<=TNG67_in_Nipponbare_qaln[j])

                                        TNG67_in_Nipponbare_gene1.pop(TNG67_in_Nipponbare_gene1[index])
                                        TNG67_in_Nipponbare_gene2.pop(TNG67_in_Nipponbare_gene2[index])
                                        TNG67_in_Nipponbare_qcov.pop(TNG67_in_Nipponbare_qcov[index])
                                        TNG67_in_Nipponbare_qaln.pop(TNG67_in_Nipponbare_qaln[index])  


"""


	
                                         
						
						
					
						


###

		
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


