import os

os.chdir('/home/jpanibe/CLC_Data/Mauve_run_Nipponbare_TNG67')

files=['01','02','03','04','05','06','07','08','09','10','11','12']

i=0
while i<len(files):
	os.system('/home/jpanibe/CLC_Data/Mauve/mauve_snapshot_2015-02-13/linux-x64/progressiveMauve --output=progMauve_IRGSP_chr%s_and_TNG67_chr%s.xmfa --output-guide-tree=progMauve_IRGSP_chr%s_and_TNG67_chr%s.tree --backbone-output=progMauve_IRGSP_chr%s_and_TNG67_chr%s.backbone IRGSP_chr%s.fasta TNG67_chr%s.fasta' % (files[i],files[i],files[i],files[i],files[i],files[i],files[i],files[i]))
	i+=1