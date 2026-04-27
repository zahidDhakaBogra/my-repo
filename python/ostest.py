import subprocess,platform

result=subprocess.run(["whoami"],capture_output=True,text=True)
print("Current User:",result.stdout.strip())

system_os=platform.system()
command=["systeminfo"] if system_os=="Windows" else ["uname","-a"]

result=subprocess.run(command,capture_output=True,text=True)
print(f"System Information ({system_os}):")

print("system info:",result.stdout[:320])
print("="*2)



