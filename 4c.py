import sys
import hashlib
import binascii

password = sys.argv[1]
print "Password: " + password

sha1 = hashlib.sha1()
sha1.update(password)
hash = sha1.hexdigest()
print "SHA1: " + hash

print "Writing new exe..."

filename = '44688091.program2.exe'
with open(filename, 'rb') as f:
    content = f.read()
hex = binascii.hexlify(content)

hex = hex.replace("55e194f88ade9f1eb71b9b241ed5f1b88181f19f", hash)
out = binascii.unhexlify(hex)

f = open('44688091.program2.exe', 'wb')
f.write(out)
f.close()

print "Done."