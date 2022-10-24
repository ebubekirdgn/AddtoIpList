import ipaddress

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        print("IP address {} is valid. The object returned is {}".format(address, ip))
    except ValueError:
        print("IP address {} is not valid".format(address)) 


## Adding
dosya = open("bizimliste.txt","r+")
bizimliste = []
for satir in dosya:
   satir = satir.replace("\n","")
   bizimliste.append(satir)

dosya2 = open("eklenecekliste.txt","r+")
eklenecekliste = []
for satir in dosya2:
   satir = satir.replace("\n","")
   eklenecekliste.append(satir)

print(bizimliste)
print(eklenecekliste)

for eleman in eklenecekliste: 
    if not(eleman in bizimliste):
        print(eleman)

## Sorting
for ip in sorted(bizimliste, key = lambda ip: [int(ip) for ip in ip.split(".")] ):
            print(ip)
