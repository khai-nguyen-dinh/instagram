import time
from random import choice, random,sample
from string import letters,digits
from proxylist import ProxyList

from signup import auto_signup


proxy = ProxyList()
proxy.load_file('source/proxy.txt')

with open('source/data_user.csv') as f:
    count = 0
    for name in f:
        digits = ''.join(sample(digits, 2))
        chars = ''.join(sample(letters, 2))
        email = 'khainguyenptiter+' + digits + chars.lower() + '@gmail.com'
        auto_signup(name,email,'vPbhHYMr75BYFZ8W',proxy[count])
        if count >=50:
            count =0
        else:
            count +=1
        print ('wait!')
        time.sleep(3000)



