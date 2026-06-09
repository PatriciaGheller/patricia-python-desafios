'''Crie um código em python que teste se o site Pudim 
está acessível pelo computador usado.'''

import urllib.request
import urllib.error

req = urllib.request.Request(
    'http://www.pudim.com.br',
    headers={'User-Agent': 'Mozilla/5.0'}
)

try:
    urllib.request.urlopen(req, timeout=5)    
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento!')    
else:    
    print('Consegui acessar o site Pudim com sucesso!')
    

