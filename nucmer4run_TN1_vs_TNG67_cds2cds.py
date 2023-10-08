import os

os.chdir('/home/jpanibe/CLC_Data/TN1_proteins')

os.system('/home/jpanibe/CLC_Data/MUMmer/mummer-4.0.0beta2/nucmer --maxmatch -c 200 -l 100 -p cds2cds_TN1_vs_TNG67_forsnpeff.nucmer1 -t 16 TN1_cds_sequence.fasta TNG67_cds_sequence.fasta')
os.system('/home/jpanibe/CLC_Data/MUMmer/mummer-4.0.0beta2/delta-filter -1 cds2cds_TN1_vs_TNG67_forsnpeff.nucmer1.delta > cds2cds_TN1_vs_TNG67_forsnpeff.nucmer1.filter')

#os.system('/home/jpanibe/CLC_Data/MUMmer/mummer-4.0.0beta2/dnadiff -d Nipponbare_v_TNG67_forsnpeff.nucmer1.filter -p Nipponbare_v_TNG67_forsnpeff.nucmer1.dnadiff')
#os.system('/home/jpanibe/CLC_Data/MUMmer/mummer-4.0.0beta2/show-snps -ClrT Nipponbare_v_TNG67_forsnpeff.nucmer1.filter > Nipponbare_v_TNG67_forsnpeff.nucmer1.filter.snps')
	





