print("Bem vindo(a), Usuário(a) !!")

op = int(input("\nDigite 1 para Calcular seu IMC ou digite 0 para Encerrar Sessão.\n"))

if (op != 1 and op != 0):
    print("Ação inválida !!")

if(op == 1):
    peso = float(input("\nDigite seu peso: "))
    altura = float(input("\nDigite sua altura: "))

    imc = peso/(altura*altura)

    if(imc < 18.5):
        print("Abaixo do peso")
    
    if(imc >= 18.5 and imc <=24.9):
        print("Peso ideal")

    if(imc >=25 and imc <= 29.9):
        print("Sobrepeso")
    
    if(imc >=30 and imc <= 34.9):
        print("Obesidade 1")
    
    if(imc >=35 and imc <= 39.9):
        print("Obesidade 2")

    if(imc >=40):
        print("Obesidade 3")

if(op == 0):
    print("Sessão Encerrada !")
