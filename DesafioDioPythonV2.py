import datetime
import os
import platform
import textwrap


data=datetime.datetime.now()
dataHoje=data.strftime("%d/%m/%Y")
data_deposito=data.strftime("%A %d/%m/%Y")   
plataforma=platform.system()
LIMITE_SAQUES=3
numero_saques=0


cabecalho="""
Aluno=Tiberio Coelho
Sistema Bancário: versão 2.0
"""
print(cabecalho)
def menu():
    menu=f"""
    Menu
    Data : {dataHoje}
    -------------------------------------------
    (d)\tDepósito
    (s)\tSaque
    (e)\tExtrato
    (nu)\tNovo Usuário
    (nc)\tNova Conta
    (lc)\tLista Contas   
    (h)\tAjuda
    (q)\tSair
    -------------------------------------------
    :"""
    return input(textwrap.dedent(menu))

def depositar(saldo,valor_deposito,extrato,/):  
    
    if valor_deposito>0:
        saldo+=valor_deposito        
        extrato+=f"Depósito: R$ {valor_deposito:.2f}\t | data = {data_deposito}\n"
        print("Deposito realizado com sucesso!")        
        if plataforma=="Windows":
            os.system('cls')
        else:
            os.system('clear')
        print("Depósito realizado com sucesso!")        
    else:
        print("Valor do depósito inválido")
        
    return saldo,extrato

def saque(*,saldo,valor_saque,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo=valor_saque>saldo
    excedeu_limite=valor_saque>limite
    excedeu_saques=numero_saques==limite_saques
   
    
    if excedeu_saldo:
        if plataforma=="Windows":
            os.system('cls')                
        else:
            os.system('clear')
        print("Falha na operação, Saldo insuficiente.")
    elif excedeu_limite:
        if plataforma=="Windows":
            os.system('cls')                
        else:
            os.system('clear')
        print("Falha na operação, Limite de saque excedeu limite. ")
    elif excedeu_saques:
        if plataforma=="Windows":
            os.system('cls')                
        else:
            os.system('clear')
        print("Falha na operação, Número maximos de saques excedido.")    
    elif valor_saque>0:          
        saldo-=valor_saque        
        numero_saques+=1
        extrato+=f"Saque:\t  R$ {valor_saque:.2F}\t | data = {data_deposito}\n"        
        if plataforma=="Windows":
            os.system('cls')                
        else:
            os.system('clear')
        print("Saque realizado com sucesso!")            
        
    return saldo,extrato,numero_saques
                    
def exibir_extrato(saldo,/,*,extrato):
    if plataforma=="Windows":
        os.system('cls')
    else:
        os.system('clear')
                                
    print("---------Extrato bancário---------")
    print("Não foram realizadas movimentações." if not extrato else extrato )
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("----------------------------------")
    print("Número de saques permitidos para o dia: ",LIMITE_SAQUES-numero_saques)
    
def criar_usuario(usuarios):
    if plataforma=="Windows":
        os.system('cls')                
    else:
        os.system('clear')
    cpf=input("Informe o CPF (somente números): ")  
    usuario=filtrar_usuario(cpf,usuarios)
    if usuario:
        print("Não exite usuario com esse CPF")
        return
    nome=input("Informe o nome completo: ")
    data_nascimento=input("Informe a data de nascemento (dd-mm-aaaa): ")
    endereco= input("Informe o endereco (lograddouro, nro- bairro , cidade/sigla estado): ")
    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuario Criado com sucesso!")
    
def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados=[usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios):
    if plataforma=="Windows":
        os.system('cls')                
    else:
        os.system('clear')
    cpf=input("Informe o CPF do usuário: ")       
    usuario=filtrar_usuario(cpf,usuarios)
    if usuario:
        print("Conta criada com sucesso! ")
        return {"agencia":agencia,"numero_conta": numero_conta,"usuario":usuario}
    print("Usuario não encontrado, fluxo de criação de conta encerrado! ")
    
def listar_contas(contas):
    if plataforma=="Windows":
        os.system('cls')                
    else:
        os.system('clear')
    for conta in contas:
        linha=f"""
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
 
           
def ajuda():
    if plataforma=="Windows":
        os.system('cls')                
    else:
        os.system('clear')
    ajuda="""
    ---------------------------------------------------
    1- Limite de saques diário é de três vezes
    2- Limite máximo de valor para saque é de R$ 500.00
    3- SAC: 0800 000 000
    ---------------------------------------------------     
    """
    print(ajuda)        
def principal():
    AGENCIA="0001" 
    global LIMITE_SAQUES
       

    global numero_saques
    global data
    global data_deposito
    
    saldo=0
    limite=500
    extrato=""
    usuarios=[]
    contas=[]
    #numero_conta=1  
    
    
    while True:
        opcao=menu()
        if(opcao=="d"):
            try:
                valor_deposito=float(input("Informe o valor do depósito: "))
                saldo,extrato=depositar(saldo,valor_deposito,extrato)                                   
            except:
                if plataforma=="Windows":
                    os.system('cls')                
                else:
                    os.system('clear')
                print("Digite um valor numérico")
        elif(opcao=="s"):
            try:
                valor_saque=float(input("Informe o valor do saque: "))
                #os.system('cls') 
                saldo,extrato,numero_saques=saque(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,                              
                )
            except:
                if plataforma=="Windows":
                    os.system('cls')                
                else:
                    os.system('clear')
                print("Digite um valor numérico")
                    
            
            
        elif(opcao=="e"):
            exibir_extrato(saldo,extrato=extrato)
            
        elif(opcao=="nu"):
            criar_usuario(usuarios)
        elif(opcao=="nc"):
            numero_conta=len(contas)+1
            conta=criar_conta(AGENCIA,numero_conta,usuarios)
            if conta:
                contas.append(conta)
                #numero_conta +=1
        elif(opcao=="lc"):
            listar_contas(contas)                    
        elif(opcao=="h"):
            ajuda()            
                    
        elif(opcao=="q"):
            break
        else:
            print("Opção inválida, selecione uma opção valida")
            
       
            
            
     
        
    
principal()    
              
                       
    
           
            
    
            
    



