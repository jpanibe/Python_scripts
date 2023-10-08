import os

os.chdir('/home/jpanibe/CLC_Data/TNG67_annotation/TNG67_annotation/')

os.system('/home/jpanibe/CLC_Data/MUMmer/mummer-4.0.0beta2/nucmer --maxmatch -c 200 -l 100 -p TN1_v_Nipponbare_g2g_forsnpeff.nucmer1 -t 16 IRGSP-1.0_all_58_UPPERCASE.fasta TN1_rice_v1.0.fasta')
os.system('/home/jpanibe/CLC_Data/MUMmer/mummer-4.0.0beta2/delta-filter -1 TN1_v_Nipponbare_g2g_forsnpeff.nucmer1.delta > TN1_v_Nipponbare_g2g_forsnpeff.nucmer1.filter')
os.system('/home/jpanibe/CLC_Data/MUMmer/mummer-4.0.0beta2/dnadiff -d TN1_v_Nipponbare_g2g_forsnpeff.nucmer1.filter -p TN1_v_Nipponbare_g2g_forsnpeff.nucmer1.dnadiff')
os.system('/home/jpanibe/CLC_Data/MUMmer/mummer-4.0.0beta2/show-snps -ClrT TN1_v_Nipponbare_g2g_forsnpeff.nucmer1.filter > TN1_v_Nipponbare_g2g_forsnpeff.nucmer1.filter.snps')
	





