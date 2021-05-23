import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu erro.')
    print('O site Pudim não está acessivel no momento.')
else:
    print('Tudo ok.')
    print('O site Pudim está acessivel.')
