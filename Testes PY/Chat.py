import os

mensagens = []

nome = input("1° Nome: ")
nome2 = input("2° Nome: ")

while True:

    os.system('cls') 

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-" , m['texto'])
            print(m['nome2'], "-", m['texto2'])
    
    print("________________________")

    texto = input("mensagem: ")
    texto2 = input("mensagem: ")

    if texto == "fim":
        break

    mensagens.append({
        "nome": nome,
        "nome2": nome2,
        "texto": texto,
        "texto2":texto2
    })