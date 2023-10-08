import os

os.chdir('/home/jpanibe/CLC_Data/for_Mauve_run')

files=['1','2','3','4','5','6','7','8','9','10','11','12']

i=0
while i<len(files):
	os.system('/home/jpanibe/CLC_Data/Mauve/mauve_snapshot_2015-02-13/linux-x64/progressiveMauve --output=progMauve_IR8_chr%s_and_TN1_chr%s.xmfa --output-guide-tree=progMauve_IR8_chr%s_and_TN1_chr%s.tree --backbone-output=progMauve_IR8_chr%s_and_TN1_chr%s.backbone oryza_indicair8-toplevel-20180831_UPPERCASE_rename_chr%s.fasta TN1_chr%s.fasta' % (files[i],files[i],files[i],files[i],files[i],files[i],files[i],files[i]))
	i+=1
