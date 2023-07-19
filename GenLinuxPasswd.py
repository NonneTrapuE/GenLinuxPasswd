import random,string,crypt,os

randomsalt = "".join(random.sample(string.ascii_letters,8))
passwd_salted = crypt.crypt(passwd, '$5$%s$' % randomsalt)
print (passwd_salted)