#!/usr/bin/python3
from ClientSever import Cliente
import sys

host = sys.argv[1]
porta = sys.argv[2]
arquivo = sys.argv[3]

cliente = Cliente(host,porta,arquivo)
cliente.Download()