#!/usr/bin/python3
from ClientSever import Servidor
import sys
import concurrent.futures


porta = sys.argv[1]
arquivo = 'logo.png'
Server = Servidor(porta,arquivo)
Server.Read()
i = 1
while True:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(Server.Upload,f'{i}')
    while not Server.flag:
        pass
    print(Server.mensagem)
    i = i+1
    Server.flag = False 
