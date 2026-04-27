
import os 
def count_log_files(directory): 
    files = os.listdir(directory) 
    log_files = [f for f in files if f.endswith(".py")] 
    return len(log_files) 
path = "D:\SOC_Training_monitoring\Advanced_Scripting\python" 
print("Total .py files:", count_log_files(path)) 

