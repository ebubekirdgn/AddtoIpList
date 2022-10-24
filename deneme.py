import ipaddress

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        print("IP address {} is valid. The object returned is {}".format(address, ip))
    except ValueError:
        print("IP address {} is not valid".format(address)) 


## Adding
dosya = open("fihrist.txt","r+")
numbers= []
for satir in dosya:
   satir = satir.replace("\n","")
   numbers.append(satir)

## Sorting
for ip in sorted(numbers, key = lambda ip: [int(ip) for ip in ip.split(".")] ):
            print(ip)
