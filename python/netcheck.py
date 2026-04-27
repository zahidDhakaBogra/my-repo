
import subprocess
 
sites=["google.com","facebook.com","192.168.101.101","twitter.com","github.com","8.8.8.8"]
    
ln=len(sites)
print("Sites:",ln)
timeOutSite=""

try:
   for site in sites:
        timeOutSite=site
        cmd = ["ping", site]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        status = "✅ ONLINE" if result.returncode == 0 else "❌ OFFLINE"
        print(f"{site}: {status}")
            
except subprocess.TimeoutExpired:
    print(f"{timeOutSite} is ⏰ Timeout – network unreachable")

