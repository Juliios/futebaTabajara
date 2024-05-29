jogadores= []
nota =[]
i= 0

while True: 
    resposta= input('Quer Adicionar um novo jogador?(y/n)')
    if "n" == resposta:
        break
    novo_jogador= input('Adicione um novo jogador:')
    jogadores.append(novo_jogador)
    print(novo_jogador)
    notai = float(input("Digite sua nota para o jogador acima: "))
    nota.append(notai)
    print ("A nota do: ", jogadores[i],' é:', nota[i] )
    i = i+1
#else 
print(jogadores)
print(nota)

nota_soma= sum(nota)
print("A soma das notas do time é: ", nota_soma)
media_time= nota_soma/i

print("A media do time é:", media_time)
i = 0
for jogador in jogadores:
    print ("A nota do: ", jogadores[i],' é:', nota[i])
    i = i+1