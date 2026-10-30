# ==========================================
# 1. AS NOVAS FUNÇÕES (PEDIDAS PELO PROFESSOR)
def ehinteiro(numero):
    return numero.is_integer()

def ehpar(numero):
    if ehinteiro(numero) and (numero % 2 ==0):
        return True
    return False

def somarmultiplosnumeros(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma

def multiplicarmultiplosnumeros(lista):
    produto = 1
    for num in lista:
        produto *= num
    return produto

# 2. A SUA CALCULADORA INTERATIVA EM LOOP
while True: 
    # 1. Pedindo os dois números e a opção da operação
    print("\n--- CALCULADORA MELHORADA ---")
    print("=-=-" * 10)
    print("1 - Adição (dois números)")
    print("2 - Subtração (dois números)")
    print("3 - Multiplicação (dois números)")
    print("4 - Divisão (dois números)")
    print("5 - Somar uma lista inteira de números")
    print("6 - Multiplicar uma lista inteira de números")
    print("7 - Verificar se um número é par")
    print("8 - Verificar se um número é inteiro")
    print("9 - Sair")
    print("=-=-" * 10)

    operador = input("Escolha a operação: ")

    # Opção para sair do programa
    if operador == "9":
        print("Encerrando a calculadora. Até mais!")
        break

    # Opções 1 a 4: Contas tradicionais com dois números
    elif operador in ["1","2","3","4"]:      
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        n1_limpo = int(num1) if num1.is_integer() else num1
        n2_limpo = int(num2) if num2.is_integer() else num2

        if operador == "1":
            resultado = num1 + num2
            if resultado.is_integer():
                resultado = int(resultado)
                print("=-=-" * 10)
            print(f"A soma entre {n1_limpo} + {n2_limpo} é igual a {resultado}")
            print("=-=-" * 10)

        elif operador == "2":
            resultado = num1 - num2
            if resultado.is_integer():
                resultado = int(resultado)
                print("=-=-" * 10)
            print(f"A subtração entre {n1_limpo} - {n2_limpo} é igual a {resultado}")
            print("=-=-" * 10)

        elif operador == "3":
            resultado = num1 * num2
            if resultado.is_integer():
                resultado = int(resultado)
                print("=-=-" * 10)
            print(f"A Multiplicação entre {n1_limpo} * {n2_limpo} é igual a {resultado}")
            print("=-=-" * 10)

        elif operador == "4":
            if num2 == 0:
                print("Não é possivel dividir por zero")
            else:
                resultado = num1 / num2
                if resultado.is_integer():
                    resultado = int(resultado)
                    print("=-=-" * 10)
                print(f"A Divisão entre {n1_limpo} * {n2_limpo} é igual a {resultado}")
                print("=-=-" * 10)

    elif operador == "5":
        entrada = input("Digite os números separados por espaço (ex: 5 10 15): ")

        lista_num = [float(x) for x in entrada.split()]
        resultado_soma = somarmultiplosnumeros(lista_num)

        if resultado_soma.is_integer():
            resultado_soma = int(resultado_soma)
            print("=-=-" * 10)
        print(f"A soma da lista é igual a: {resultado_soma}")
        print("=-=-" * 10)

    elif operador == "6":
        entrada = input("Digite os números separados por espaço (ex: 2 5 3): ")

        lista_num = [float(x) for x in entrada.split()]
        resultado_mult = multiplicarmultiplosnumeros(lista_num)

        if resultado_mult.is_integer():
            resultado_mult = int(resultado_mult)
            print("=-=-" * 10)
        print(f"O produto da multiplicação da lista é igual a: {resultado_mult}")
        print("=-=-" * 10)

    elif operador == "7":
        num = float(input("Digite um número para verificar se é par: "))

        if ehpar(num):
            print(f"O número {int(num) if num.is_integer() else num} é PAR: True")
        else:
            print(f"O número {num} é PAR: False")

    elif operador == "8":
        num = float(input("Digite um número para verificar se é inteiro:"))
        if ehinteiro(num):
            print(f"O número {num} é inteiro: True")
        else:
            print(f"O número {num} é inteiro: False")

    else:
        print("Operador inválido")