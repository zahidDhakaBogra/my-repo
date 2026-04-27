import os



file_path="D:\SOC_Training_monitoring\Advanced_Scripting\python"
errFileName="error.log"

try: 
    with open("activity.log", "r") as f: 
        print(f.read()) 
except Exception as e: 
    with open(errFileName, "a") as err: 
        err.write(f"{e}\n")

print("Current user:", os.environ.get("USER", "Unknown")) 
print("Home directory:", os.environ.get("HOME", "Unknown"))         

  