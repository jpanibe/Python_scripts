import os

os.chdir('/home/jpanibe/CLC_Data/TNG67_annotation/TNG67_annotation/')


reference=[]
query=[]

with open('TN1_v_TNG67_forsnpeff.nucmer1.filter.gene_pairing_TN1_genes.txt', 'r') as reflist_file:
	for line in reflist_file:
	# remove linebreak which is the last character of the string
		current_refPlace = line[:-1]

		reference.append(current_refPlace)


with open('TN1_v_TNG67_forsnpeff.nucmer1.filter.gene_pairing_TNG67_genes.txt', 'r') as querylist_file:
	for line in querylist_file: 
		current_queryPlace = line[:-1]
		
		query.append(current_queryPlace)	


i=0
while i<len(reference):
	os.system('/home/jpanibe/CLC_Data/MUMmer/mummer-4.0.0beta2/show-aligns TN1_v_TNG67_forsnpeff.nucmer1.filter %s %s' % (reference[i],query[i]))
	i=i+1	





