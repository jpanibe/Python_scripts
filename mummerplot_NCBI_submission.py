import os

os.chdir('/home/jpanibe/CLC_Data')

#os.system('/home/jpanibe/CLC_Data/Mummer/mummer-4.0.0beta2/nucmer -t 16 R498_Chr_M.fasta TN1_rice_v1.0_seqA.fasta -p R498_Chr_M_with_TN1_rice_v1.0_seqA')
os.system('/home/jpanibe/CLC_Data/Mummer/mummer-4.0.0beta2/delta-filter -m -l 1000 R498_Chr_M_with_TN1_rice_v1.0_seqA.delta > R498_Chr_M_with_TN1_rice_v1.0_seqA.delta.m.l5000')
os.system('/home/jpanibe/CLC_Data/Mummer/mummer-4.0.0beta2/mummerplot --color --png --large --layout R498_Chr_M_with_TN1_rice_v1.0_seqA.delta.m.l5000 -p R498_Chr_M_with_TN1_rice_v1.0_seqA.delta.m.l5000_plot') 


#os.system('/home/jpanibe/CLC_Data/Mummer/mummer-4.0.0beta2/nucmer -t 16 R498_Chr_C.fasta TN1_rice_v1.0_seqB.fasta -p R498_Chr_C_with_TN1_rice_v1.0_seqB')

os.system('/home/jpanibe/CLC_Data/Mummer/mummer-4.0.0beta2/delta-filter -m -l 1000 R498_Chr_C_with_TN1_rice_v1.0_seqB.delta > R498_Chr_C_with_TN1_rice_v1.0_seqB.delta.m.l5000')

os.system('/home/jpanibe/CLC_Data/Mummer/mummer-4.0.0beta2/mummerplot --color --png --large --layout R498_Chr_C_with_TN1_rice_v1.0_seqB.delta.m.l5000 -p R498_Chr_C_with_TN1_rice_v1.0_seqB.delta.m.l5000_plot')

