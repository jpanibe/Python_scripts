import os


protein_TNG67=['OsTNG07t000985.1']
protein_TN1=['OsTN7t001067.1']
protein_Nipponbare=['Os07t0261200-01']


enzyme_name='Ghd7'


i=0
while i<len(protein_TNG67):
	os.system("samtools faidx TNG67_proteins.fasta '%s' > %s_%s.fasta" %(protein_TNG67[i],enzyme_name,protein_TNG67[i]))
	i=i+1


i=0
while i<len(protein_TN1):
	os.system("samtools faidx TN1_proteins.fasta '%s' > %s_%s.fasta" % (protein_TN1[i],enzyme_name,protein_TN1[i]))
	i=i+1

i=0
while i<len(protein_Nipponbare):
	os.system("samtools faidx IRGSP-1.0_protein_2022-03-11.fasta '%s' > %s_%s.fasta" % (protein_Nipponbare[i],enzyme_name,protein_Nipponbare[i]))
	i=i+1


os.system("cat %s_*.fasta > %s_protein_sequences.fasta" % (enzyme_name,enzyme_name))
os.system("/home/jpanibe/CLC_Data/clustalw/clustalw-2.1-linux-x86_64-libcppstatic/clustalw2 -infile=%s_protein_sequences.fasta -type=protein -output=FASTA -align" % enzyme_name)


#os.system("mkdir %s_gff" % enzyme_name)
os.system("mv %s*.fasta %s_gff" % (enzyme_name,enzyme_name))


