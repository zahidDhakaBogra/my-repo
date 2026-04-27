import os
from datetime import datetime


print (datetime.now())




file_path="D:\SOC_Training_monitoring\Advanced_Scripting\python"


if(os.path.exists(file_path)):
    print("The file or directory exists.")
else:
    print("The file or directory does not exist."   )
    