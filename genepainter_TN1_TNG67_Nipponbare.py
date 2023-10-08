import os

gene_TN1=['OsTN7g001067']
protein_TN1=['OsTN7t001067.1']

gene_TNG67=['OsTNG07g000985']
protein_TNG67=['OsTNG07t000985.1']

gene_Nipponbare=['Os07g0261200']
protein_Nipponbare=['Os07t0261200-01']

enzyme_name='Ghd7'

i=0
while i<len(gene_TN1):
	os.system("grep '%s' TN1_genome.maker.pass2.maker_model.rename.gff > %s_%s_genepainter.gff" % (gene_TN1[i],enzyme_name,gene_TN1[i]))
	i+=1

i=0
while i<len(gene_TN1):
        os.system("grep '%s' TN1_genome.maker.pass2.maker_model.rename.gff > %s_%s_genepainter.gff" % (protein_TN1[i],enzyme_name,protein_TN1[i]))
        os.system("cat %s_%s_genepainter.gff %s_%s_genepainter.gff > %s_%s.gff" % (enzyme_name,gene_TN1[i],enzyme_name,protein_TN1[i],enzyme_name,protein_TN1[i]))
        i=i+1



i=0
while i<len(gene_TNG67):
	os.system("grep '%s' TNG67_assembly.maker.pass2.maker_model.rename.gff > %s_%s_genepainter.gff" % (gene_TNG67[i],enzyme_name,gene_TNG67[i]))
	i=i+1


i=0
while i<len(gene_TNG67):
	os.system("grep '%s' TNG67_assembly.maker.pass2.maker_model.rename.gff > %s_%s_genepainter.gff" % (protein_TNG67[i],enzyme_name,protein_TNG67[i]))
	os.system("cat %s_%s_genepainter.gff %s_%s_genepainter.gff > %s_%s.gff" % (enzyme_name,gene_TNG67[i],enzyme_name,protein_TNG67[i],enzyme_name,protein_TNG67[i])) 
	i=i+1

i=0
while i<len(gene_Nipponbare):
	os.system("grep '%s' locus.gff > %s_%s_genepainter.gff" % (gene_Nipponbare[i],enzyme_name,gene_Nipponbare[i]))
	i=i+1

i=0
while i<len(protein_Nipponbare):
	os.system("grep '%s' transcripts_exon.gff > %s_%s_transcripts_exon_genepainter.gff" % (protein_Nipponbare[i],enzyme_name,protein_Nipponbare[i]))
	os.system("grep '%s' transcripts.gff > %s_%s_transcripts_genepainter.gff" %(protein_Nipponbare[i],enzyme_name,protein_Nipponbare[i]))
	os.system("cat %s_%s_genepainter.gff %s_%s_transcripts_exon_genepainter.gff %s_%s_transcripts_genepainter.gff > %s_%s.gff" % (enzyme_name,gene_Nipponbare[0],enzyme_name,protein_Nipponbare[i],enzyme_name,protein_Nipponbare[i],enzyme_name,protein_Nipponbare[i]))
	i=i+1

os.system("mkdir %s_gff" % enzyme_name)

os.system("mv %s*.gff %s_gff" % (enzyme_name,enzyme_name))

os.chdir("/home/jpanibe/CLC_Data/TNG67_ClusterVenn/%s_gff" % enzyme_name)

i=0
while i<len(protein_Nipponbare):
	os.system("mv %s_%s.gff %s.gff" % (enzyme_name,protein_Nipponbare[i],protein_Nipponbare[i]))
	i=i+1

i=0
while i<len(protein_TN1):
        os.system("mv %s_%s.gff %s.gff" % (enzyme_name,protein_TN1[i],protein_TN1[i]))
        i=i+1

i=0
while i<len(protein_TNG67):
        os.system("mv %s_%s.gff %s.gff" % (enzyme_name,protein_TNG67[i],protein_TNG67[i]))
        i=i+1

