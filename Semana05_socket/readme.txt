prog 01
    Criaço de um servidor que envia o arquivo desejado para um unico criente
execução
    Em um terminal execute o comando parcido com a linha a seguir para a criação do servidor
    python3 ./prog01_server.py 8401 logo.png 
    Em outro terminal  execeute o comando analogo ao a seguir
    python3 ./Cliente.py 127.0.1.8 8401 newnome.png
prog 02
    Criaço de um servidor que envia o arquivo desejado para multiplos crientes
    execução
    Em um terminal execute o comando parcido com a linha a seguir para a criação do servidor
    python3 ./prog02_server.py 8401
    Em outro terminal  execeute o comando analogo ao a seguir pode repertir o && ... a quantidade de clirntes que desejar
    python3 ./Cliente.py 127.0.1.8 8401 nome1.png && python3 ./Cliente.py 127.0.1.8 8401 nome2.png