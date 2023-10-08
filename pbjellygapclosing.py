import os

os.chdir('/home/jpanibe/CLC_Data')

os.system('/home/jpanibe/CLC_Data/PBJelly/PBSuite_15.8.24/pbsuite/jelly/Jelly.py setup Protocol_TN1.xml')
os.system('/home/jpanibe/CLC_Data/PBJelly/PBSuite_15.8.24/pbsuite/jelly/Jelly.py mapping Protocol_TN1.xml')
os.system('/home/jpanibe/CLC_Data/PBJelly/PBSuite_15.8.24/pbsuite/jelly/Jelly.py support Protocol_TN1.xml -x "--minMapq 20"')
os.system('/home/jpanibe/CLC_Data/PBJelly/PBSuite_15.8.24/pbsuite/jelly/Jelly.py extraction Protocol_TN1.xml')
os.system('/home/jpanibe/CLC_Data/PBJelly/PBSuite_15.8.24/pbsuite/jelly/Jelly.py assembly Protocol_TN1.xml -x "-n 16"')
os.system('/home/jpanibe/CLC_Data/PBJelly/PBSuite_15.8.24/pbsuite/jelly/Jelly.py output Protocol_TN1.xml')
