import json 

filename="server.json"
data = { 
"Server": "Prod-1", 
"Status": "Running", 
"IP": "192.168.1.10" 
} 
with open(filename, "w") as f: 
    json.dump(data, f, indent=4) 
print("Data written to server.json")

with open(filename, "r") as f: 
    info = json.load(f) 
print(info["Server"], info["Status"], info["IP"])
