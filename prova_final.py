from datetime import date
from random import randint

nome_aluno = input("Digite seu nome: ").strip()
data_nascimento = int(input("Digite seu ano de nascimento: "))
idade = date.today().year - data_nascimento

if idade < 18:
    print("Menor de idade não pode seguir no cadastro!")

else:
    print("-=-" * 25)

    print(f"Seu nome todo maiusculo {nome_aluno.upper()}")
    print(f"Seu nome todo minusculo {nome_aluno.lower()}")
    print(f"Seu nome tem ao todo {len(nome_aluno.replace(' ', ''))} letras!")
    lista_nome = nome_aluno.split()
    print(f"Seu primeiro nome é {lista_nome[0]}, e seu ultimo nome é {lista_nome[-1]}.")
    if "silva" in nome_aluno.lower():
        print("Contém Silva no nome")
    else:
        print("Não contém Silva no seu nome")

    print("-=-" * 25)

    n1 = float(input("Sua primeira nota: "))
    n2 = float(input("Sua segunda nota: "))
    média = (n1 + n2) / 2
    print(f"Sua média é de {média}")
    if média >= 7:
        print("\033[1;32mAprovado\033[m! ")
    elif 5 <= média <= 6.9:
        print("Você está na \033[1;33mrecuperação\033[m!")
    elif média < 5:
        print("Você está \033[1;31mreprovado\033[m")

    print("-=-" * 25)

    mensalidade = 850.00
    print("A Mensalidade do curso custa R$850.00! escolha a forma de pagamento!")
    parcelas = int(input("Digite a quantidade de parcelas: "))

    if parcelas == 1:
        valor_final = mensalidade * 0.90
        print(
            f"Pagamento à vista com 10% de desconto! O valor total fica R$ {valor_final:.2f}."
        )
    elif parcelas == 2:
        valor_parcela = mensalidade / 2
        print(
            f"Pagamento em 2x sem juros. Valor total: R$ {mensalidade:.2f} (2x de R$ {valor_parcela:.2f})."
        )
    elif parcelas >= 3:
        valor_final = mensalidade * 1.20
        valor_parcela = valor_final / parcelas
        print(
            f"Pagamento em {parcelas}x com 20% de juros! O valor total fica R$ {valor_final:.2f} ({parcelas}x de R$ {valor_parcela:.2f})."
        )
    else:
        print("Quantidade de parcelas inválida.")

    print("-=-" * 25)

    sorteio = randint(1, 10)

    if média >= 8:
        print("Parabéns! Você pode participar do nosso sorteio!")
        if sorteio % 2 == 0:
            print("Parabéns!!! Que sorte você ganhou o sorteio!!")
        else:
            print("Deu a casa")
