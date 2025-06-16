while True:

    numero1 = input("Digite um numero: ")
    numero2 = input("Digite outro numero: ")

    operador = input("Digite um operador: ")
    numeros_validos = None

    try:
        numerofloat = float(numero1)
        numerofloat2 = float(numero2)
        numeros_validos = True
    except:     
            numeros_validos = None
    
    if numeros_validos is None:
         print('O numero é invalido')

         continue
    
    operadores_permitidos = '+-*'

    if operador not in operadores_permitidos:
         print("Invalido")

         continue
    print("Realizando a sua conta, confira o resultado abaixo")

    if operador == '+':
         print(numerofloat + numerofloat2)

    elif operador == '-':
         print(numerofloat - numerofloat2)

    elif operador == '*':
         print(numerofloat * numerofloat2)

    else:
         print(numerofloat / numerofloat2)

    sair = input("Quer sair: ").lower().startswith("s")
