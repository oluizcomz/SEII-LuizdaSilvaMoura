#!/usr/bin/python3
from ClientSever import Servidor
import sys


porta = sys.argv[1]
arquivo = sys.argv[2]
#'127.0.1.7' 5005
Server = Servidor(porta,arquivo)
Server.Read()
Server.Upload()