import socket

def get_ip_details(ip_address):
  try:
    # Get the hostname for the IP address
    hostname = socket.gethostbyaddr(ip_address)[0]
  except:
    hostname = "Unable to resolve hostname"
  
  # Get the IP address details
  ip_details = socket.gethostbyaddr(ip_address)
  
  print(f"IP address: {ip_address}")
  print(f"Hostname: {hostname}")
  print(f"IP details: {ip_details}")

# Test the function with a few IP addresses
ip_addresses = ["8.8.8.8", "1.1.1.1", "172.217.5.206"]
for ip in ip_addresses:
  get_ip_details(ip)
  print()
