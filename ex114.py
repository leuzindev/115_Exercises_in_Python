import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site Pudim não está acessivel no momento')
else:
    print('O site Pudim está acessivel no momento')
