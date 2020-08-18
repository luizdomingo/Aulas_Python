"""
Para trabalharmos com manipulação de arquivos usamos os seguintes comandos:
R -> para abrir o arquivo somente para leitura - comando read
A -> Para adcionar uma modificação no arquivo, colocando no final - comando append

W -> Para escrever dentro do arquivo, se o arquivo não existir ele cria um arquivo 
mesmo que você tente escrever em um arquivo que nao existe - comando white 

X -> Para criação de um novo arquivo - comando - create
-> lembrando que toda vez que você abrir um arquivo não esqueça de fechar o mesmo
comando close(nome) do arquivo, para abrir - usamos o comando open(nome do arquivo)
"""
arquvio_file = "produtos.txt"
arquivo_open = open("F:/Luiz/Python/Aulas_Python/" + arquvio_file, "x")





arquivo_open.close()