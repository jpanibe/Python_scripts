import os

os.chdir('/home/jpanibe/CLC_Data/mummerplot')

i=0
j=0
while i<13:
        j=0
        while j<13:
#                os.system('/home/jpanibe/CLC_Data/Mummer/mummer-4.0.0beta2/nucmer -t 16 R498_chr_%d.fasta TN1_chr_%d.fasta -p R498_chr_%d_with_TN1_chr_%d' % (i+1,j+1,i+1,j+1))
                os.system('/home/jpanibe/CLC_Data/Mummer/mummer-4.0.0beta2/delta-filter -m -l 5000 R498_chr_%d_with_TN1_chr_%d.delta > R498_chr_%d_with_TN1_chr_%d.delta.m.l5000' % (i+1,j+1,i+1,j+1))
#                os.system('/home/jpanibe/CLC_Data/Mummer/mummer-4.0.0beta2/mummerplot --color --png --large --layout R498_chr_%d_with_TN1_chr_%d.delta.m.l1000 -p R498_chr_%d_with_TN1_chr_%d.delta.m.l1000_plot' % (i+1,j+1,i+1,j+1))
                j+=1
        i+=1
