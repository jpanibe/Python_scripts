import os

os.chdir('/home/jpanibe/CLC_Data/TNG67_annotation/TNG67_annotation/')

os.system('/home/jpanibe/CLC_Data/MUMmer/mummer-4.0.0beta2/nucmer --maxmatch -c 200 -l 100 -p Nipponbare_v_TNG67_forsnpeff.nucmer1 -t 16 Nipponbare_genes.fasta TNG67_assembly.maker.pass2.maker_model.rename.gene.fasta')
os.system('/home/jpanibe/CLC_Data/MUMmer/mummer-4.0.0beta2/delta-filter -1 Nipponbare_v_TNG67_forsnpeff.nucmer1.delta > Nipponbare_v_TNG67_forsnpeff.nucmer1.filter')
os.system('/home/jpanibe/CLC_Data/MUMmer/mummer-4.0.0beta2/dnadiff -d Nipponbare_v_TNG67_forsnpeff.nucmer1.filter -p Nipponbare_v_TNG67_forsnpeff.nucmer1.dnadiff')
os.system('/home/jpanibe/CLC_Data/MUMmer/mummer-4.0.0beta2/show-snps -ClrT Nipponbare_v_TNG67_forsnpeff.nucmer1.filter > Nipponbare_v_TNG67_forsnpeff.nucmer1.filter.snps')
	





