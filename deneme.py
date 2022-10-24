import ipaddress

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        print("IP address {} is valid. The object returned is {}".format(address, ip))
    except ValueError:
        print("IP address {} is not valid".format(address)) 



dosya = open("fihrist.txt","r+")
numbers= []
for satir in dosya:
   satir = satir.replace("\n","")
   numbers.append(satir)

print(numbers[0])
validate_ip_address(numbers[0])