#GMAO_FP.20240320T000000.MET.NRT.nc
#GMAO_FP.20240320T000000.PROFILE.NRT.nc

import re



def check(fileName):
    date = re.search(r"\d{8}T\d{6}",fileName)
    print((date.group()))
    

# print(check("GMAO_FP.20240320T000000.PROFILE.NRT.nc"))

def check_file_date(event_file):
    e_file=event_file.rsplit('.', 3)[0]
    e_file=e_file.split('_', 4)[2]
    e_file=e_file.split('T', 1)[0]
    print(e_file)

name1 = "GMAO_FP.55555520240320T0000003333.PROFILE.NRT.nc"
# check_file_date(name1)

check(name1)