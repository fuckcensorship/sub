import base64
import json
import random
import string
import requests

def generate_random_string(size):
    # Define the set of characters to choose from
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
     
    # Generate a random string
    return ''.join(random.choices(characters, k=size))

def generate_vmess_config(add, aid, host, id, net, path, port, ps, scy, sni, tls, type, v):
    config = {
        "add": add,
        "aid": aid,
        "host": host,
        "id": id,
        "net": net,
        "path": path,
        "port": port,
        "ps": ps,
        "scy": scy,
        "sni": sni,
        "tls": tls,
        "type": type,
        "v": v
    }

    config_json = json.dumps(config)
    base64_config = base64.urlsafe_b64encode(config_json.encode()).decode()

    return "vmess://" + base64_config

def writer(ips, fileName):
    #Clean Configs.txt file
    with open( fileName, "w") as f:
        f.write("")
    
    randomstr = generate_random_string(4)
    host = randomstr + ".iraniancp.autos"
    for add in ips:
        aid = "0"
        id = "3365caca-abaa-47ba-ed1d-7e81c753fabe"
        net = "ws"
        path = "/?ed=2048"
        port = "443"
        ps = "sex"
        scy = "chacha20-poly1305"
        sni = randomstr + ".iraniancp.autos"
        tls = "tls"
        type = ""
        v = "2"
        
        config = generate_vmess_config(add, aid, host, id, net, path, port, ps, scy, sni, tls, type, v)
        
        # Add config to Configs.txt
        with open(fileName, "a") as f:
            f.write(config + "\n")

# Fech ircf domains
ircf = requests.get("https://raw.githubusercontent.com/fuckcensorship/best-cf-ip-iran/main/ircf.txt").text.splitlines()
# Generate configs for ircf
writer(ircf, "ircf.txt")
# URL of ip list
#url = "https://" 
# Fech ip list from URL
#ips = requests.get(url).text.splitlines()
# Generate configs for ips
#writer(ips, "ips.txt")
