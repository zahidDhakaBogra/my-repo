
logfile = "system.log" 
def write_log(msg): 
    with open(logfile, "a") as f: 
        f.write(f"{msg}\n") 
write_log("System started successfully.") 
write_log("Security scan completed.") 

with open("system.log", "r") as f: 
    content = f.read() 
print(content) 