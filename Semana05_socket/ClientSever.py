import socket 
class Servidor:
   
    def __init__(self, porta, file):
        self.flag= False
        self.host = '127.0.1.8'
        print('IP: ',self.host)
        self.port = int(porta)         
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#criando socket do tipo tcp
        self.address = (self.host, self.port)#passando o ip e a porta
        self.tcp.bind(self.address)#passnando para aa conceçáo tcp o indereço
        self.tcp.listen(999999)# quantas conecçoes podem ser feitas nesse servidor no aso 1
        self.nameFile = file #nome arquivo a ser enviado
    
    
    def Read(self):#lendo o arquivo
        try:
            fileOpen = open(self.nameFile, "rb")#abre o qrquivo
            self.send = fileOpen.read()#le o arquivo
        except IOError as e:
            print ('ERROR: ARQUIVO NAO ENCONTRADO')
        finally:
            fileOpen.close()#fecha o fluxo de arquivo
        
    def Upload(self, contador = '1'):#envio servidor
        self.mensagem = f'cliente {contador} peguei'
        print ('Esperando cliente...')
        self._connection, self._client = self.tcp.accept()
        self.flag = True
        print ('Cliente {} conectado'.format(self._client[0]))      
        self._connection.sendall(self.send)#envia variavel envio
        self._connection.close()

    
class Cliente:
    def __init__(self, IP , porta , file ):
        self.host = IP
        self.port = int(porta)            # mudar como parametro
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#criando socket do tipo tcp
        self.address = (self.host, self.port)#passando o ip e a porta
        print ('Conectando...')
        self.tcp.connect(self.address)
        self.nameFile = file #mudar comoparametro
    
    def Download(self):#baixar cliente
        with open(self.nameFile,'wb') as wf:
            print ('Baixando...')
            while True:
                Received = self.tcp.recv(4096)
                if not Received: break
                wf.write(Received)
            print ('Concluido!')
            self.tcp.close()
