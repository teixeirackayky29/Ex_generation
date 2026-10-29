#utilizando o while para a calculadora se repetir em loop
while True: 
    # 1. Pedindo os dois números e a opção da operação
    print("\n--- CALCULADORA ---")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o primeiro número: "))

    print("=-=-"*10)
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    print("=-=-"*10)

    operador = input("Escolha a operação: ")
    #if operador == "5":
        #print("Encerrando a calculadora. Até mais!")
        #break

    #Operação para o numero ficar inteiro
    n1_limpo = int(num1) if num1.is_integer() else num1
    n2_limpo = int(num2) if num2.is_integer() else num2

    #2-  Tomando as decisões baseadas na escolha númerica
    if operador == "1":
        resultado = num1 + num2
        if resultado.is_integer():
            resultado = int(resultado)
        print(f"A soma entre {n1_limpo} + {n2_limpo} é igual a {resultado}")
    elif operador == "2":
        resultado = num1 - num2
        if resultado.is_integer():
            resultado = int(resultado)
        print(f"A subtração entre {n1_limpo} - {n2_limpo} é igual a {resultado}")
    elif operador == "3":
        resultado = num1 * num2
        if resultado.is_integer():
            resultado = int(resultado)
        print(f"A Multiplicação entre {n1_limpo} * {n2_limpo} é igual a {resultado}")
    elif operador == "4":
        if num2 == 0:
            print("Não é possivel dividir por zero")
        else:
            resultado = num1 / num2
            if resultado.is_integer():
                resultado = int(resultado)
            print(f"A Divisão entre {n1_limpo} * {n2_limpo} é igual a {resultado}")
    elif operador == "5":
        print("Encerrando a calculadora. Até mais!")
        break
    else:
        print("Operador inválido")