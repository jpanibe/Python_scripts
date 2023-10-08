import os

subreads=['subreads_pd017_1',\
'subreads_pd018_0',\
'subreads_pd018_1',\
'subreads_pd019_2',\
'subreads_pd019_3',\
'subreads_pd021_2',\
'subreads_pd021_3',\
'subreads_pd021_4',\
'subreads_pd021_5',\
'subreads_pd021_6',\
'subreads_pd021_7']

os.chdir('/home/jpanibe/CLC_Data')

i=0
while i<len(subreads):
	os.system("gunzip -c ec_copy2.fq.gz | awk 'NR % 4 == 2' | sort | gzip > ec.sorted.txt.gz")
	os.system("gunzip -c ec.sorted.txt.gz | tr NT TN | /home/jpanibe/CLC_Data/ropebwt2/ropebwt2/ropebwt2 -LR | tr NT TN | /home/jpanibe/CLC_Data/fmlrc/fmlrc/fmlrc-convert /home/jpanibe/CLC_Data/fmlrc/fmlrc/comp_msbwt.npy")
	os.system("/home/jpanibe/CLC_Data/fmlrc/fmlrc/fmlrc -p 16 /home/jpanibe/CLC_Data/fmlrc/fmlrc/comp_msbwt.npy %s.fasta %s_fmlrccorrected.fasta" %(subreads[i],subreads[i]))
	i+=1
