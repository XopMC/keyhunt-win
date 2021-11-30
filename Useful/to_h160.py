import base58
from bitcoinlib.encoding import addr_bech32_to_pubkeyhash,change_base

def bech32_to_hash160(address):
	h1 = addr_bech32_to_pubkeyhash(address)
	h2=change_base(h1, 256, 16)	
	return h2

with open("minikey.txt","r") as f:
    content = f.readlines()
content = [x.strip() for x in content]
f.close()
outfile = open("hash160.txt","a")
for x in content:
    if x.find("-") != 1:
        if len(x) > 25 and len(x) < 36:
            address=base58.b58decode_check(x).hex()[2:]
        elif len(x) > 35:
            address=bech32_to_hash160(x)        
        outfile.write(address+'\n')
outfile.close()
    #print(address+'\n')