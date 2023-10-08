import os

genome=['Pilon_tigmint_platanusscaffoldwith10x_consensusScaffold_medusaR498andHGAP.fasta']

os.chdir('/home/jpanibe/CLC_Data')

os.system('/home/jpanibe/CLC_Data/REAPR/Reapr_1.0.18/reapr facheck %s' % genome[0])
os.system('/home/jpanibe/CLC_Data/REAPR/Reapr_1.0.18/reaper perfectmap %s ec_trimmomatic_minlen215_ec.f_forREAPR.fastq ec_trimmomatic_minlen215_ec.r_forREAPR.fastq 407 perfect' % genome[0])
os.system('/home/jpanibe/CLC_Data/REAPR/Reapr_1.0.18/reapr smaltmap %s ec_trimmomatic_minlen215_ec.f_forREAPR.fastq ec_trimmomatic_minlen215_ec.r_forREAPR.fastq ec_trimmomatic_minlen215_ec_mapped.bam' % genome[0])
os.system('/home/jpanibe/CLC_Data/REAPR/Reapr_1.0.18/reapr pipeline %s ec_trimmomatic_minlen215_ec_mapped.bam output_directory perfect' % genome[0])
