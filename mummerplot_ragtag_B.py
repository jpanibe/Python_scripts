import os

os.chdir('/home/jpanibe/CLC_Data/ragtag.scaffold.ragtag_output_correcting_Masurca.4.0.1_MiSeq_Nanopore_withmatepair_and_Long_PE_cabogis1_LHEis25.fasta_using_nucmer_Pilon_results')

i=0
while i<13:
	os.system('/home/jpanibe/CLC_Data/Mummer/mummer-4.0.0beta2/nucmer -t 16 IRGSP-1.0_genome_UPPERCASE_chr%d.fasta ragtag_B.chr%d.fasta -p Nipponbare_chr_%d_with_TNG67_ragtag_B_chr_%d' % (i+1,i+1,i+1,i+1))
	os.system('/home/jpanibe/CLC_Data/Mummer/mummer-4.0.0beta2/delta-filter -m -l 5000 Nipponbare_chr_%d_with_TNG67_ragtag_B_chr_%d.delta > Nipponbare_chr_%d_with_TNG67_ragtag_B_chr_%d.m.l5000' % (i+1,i+1,i+1,i+1))
	os.system('/home/jpanibe/CLC_Data/Mummer/mummer-4.0.0beta2/mummerplot --color --png --large --layout Nipponbare_chr_%d_with_TNG67_ragtag_B_chr_%d.m.l5000 -p Nipponbare_chr_%d_with_TNG67_ragtag_B_chr_%d.m.l5000_plot' % (i+1,i+1,i+1,i+1))
	i+=1
