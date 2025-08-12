import subprocess

def list_networks():
    print("Scanning for networks...\n");
    result = subprocess.check_output(["nmcli", "-t", "-f", "SSID,SIGNAL", "dev", "wifi", "list"]).decode()
    networks = []
    for line in result.strip().split("\n"):
        if line:
            ssid, signal = line.split(":")
            networks.append((ssid, signal))
    for i, (ssid, signal) in enumerate(networks,start=1):
        print(f"{i}. {ssid} ({signal}%)")
        
    return networks


def connect_to_network(ssid,password):
    try:
        subprocess.run(["nmcli", "dev", "wifi", "connect", ssid, "password",password],check=True)
        print(f"connected to {ssid}")
    except subprocess.CalledProcessError:
        print(f"Failed to connect {ssid}")

if __name__ == "__main__":
    networks = list_networks()

    if not networks:
        print("No networks found.")
    else:
        choice = int(input("\nSelect network number: "))
        ssid = networks[choice - 1][0]
        password = input("Enter password: ")
        connect_to_network(ssid,password)









