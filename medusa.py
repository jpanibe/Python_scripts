import os

os.chdir('/home/jpanibe/CLC_Data')

os.system('java -jar /home/jpanibe/CLC_Data/medusa/medusa.jar -f referencegenomes_folder -i Pilon_tigmint_platanusscaffoldwith10x_consensusScaffold.fa -o Pilon_tigmint_platanusscaffoldwith10x_consensusScaffold_medusa.fasta -v')
