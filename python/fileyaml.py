import yaml 

data = { 
"app": "web-server", 
"port": 8080, 
"status": "active" 
} 
with open("config.yaml", "w") as f: 
    yaml.dump(data, f) 
with open("config.yaml", "r") as f: 
    config = yaml.safe_load(f) 
print(config["app"], config["port"], config["status"])
# This code writes a dictionary to a YAML file and then reads it back, printing the values.
# This code requires the PyYAML library. You can install it using: pip install pyyaml



