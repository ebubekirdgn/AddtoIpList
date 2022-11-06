import ipaddress

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        return True
    except ValueError:
        return False        
## Sorting        
def sorting(ipList):
    for ip in sorted(ipList, key = lambda ip: [int(ip) for ip in ip.split(".")] ):
         print(ip)

## Difference Two List 
def difference(list1,list2):
    s = set(list2)
    temp3 = [x for x in list1 if x not in s]
    return temp3

#TODO : Dosya okuma islemleri teke dusurulecek.
#def list(filename,listof):
#    file = open(filename,"r+")
#    for row in file:
#        row = row.replace("\n","")
#        listof.append(row)

## Adding
dosya = open("bizimliste.txt","r+")
bizimliste = []
for satir in dosya:
    satir = satir.replace("\n","")
    if(validate_ip_address(f"{satir}")):
        bizimliste.append(satir)
    else:
        print("Invalid Ip Address Please Control Ip Addres")

print("Bizim Liste : \n " ,bizimliste)
#sorting(bizimliste)
