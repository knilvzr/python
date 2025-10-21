import os
continuar = 's'
cont= 's'
perfil = 0
option = 0 
cod = 0 
codigo_alterar= 0
codigo_excluir= 0
cod_alterar= 0
cod_excluir= 0
prod= 0 
lista_prod=[]
temp= []
temp_cod= []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input('\npressione ENTER para continuar\n')

def menu_logon():
    limpar_tela()
    print('\nmenu - logon\n')
    print ('\n1 - administrativo\n2 - Operador\n0 - Sair\n')
    op_logon= input ('\ndigite uma opçao valida\n')
    while op_logon == '' or op_logon !='0' and op_logon!='1' and op_logon!= '2':
        print ('\nopçao invalida\n')
        op_logon = input('\nescolha uma opçao valida\n')
    return op_logon 

def menu_adm():
    limpar_tela()
    print ('\nmenu - adm\n ')
    print ('\n1 - Cadastrar\n2 - Listar\n3 - Alterar\n4 - Apagar\n0 - Sair')
    op_adm= input ('\ndigite uma opçao valida\n')
    while op_adm == '' or op_adm != '1' and op_adm !='2' and op_adm!='3' and op_adm!= '4' and op_adm!='0':
        print ('\nopçao invalida\n')
        input ('\ndigite uma opçao valida\n')
    return op_adm 

def busca_cod():
    temp.clear()
    temp_cod.clear()
    codigo = '100'
    with open('produtos1.txt', 'r', encoding='utf-8') as arquivo:
        dados = arquivo.readlines()
    for linha in dados:
        if linha.strip() == '':
            continue
        partes = linha.strip().split(';')
        if len(partes) > 0 and partes[0].isdigit():
            temp.append(int(partes[0]))
    if temp:
        numeros = set(temp)
        esperado = set(range(min(numeros), max(numeros) + 1))
        faltantes = sorted(esperado - numeros)

        if faltantes:
            codigo = str(faltantes[0])
        else:
            codigo = str(max(temp) + 1)
    return codigo

def cadastrar():
  limpar_tela()
  print ('\ncadastro de produtos\n')
  arquivo = open('produtos1.txt', 'a', encoding='utf-8')
  cod= busca_cod()
  print('\ncodigo do produto a ser cadastrado: %s' %(cod))
  desc= input ('\ndigite uma descriçao para o produto\n').strip()
  while desc == '':
        print('\ndescriçao invalida\n')
        desc = input('\ndigite uma descriçao valida\n')
  valor = input('\ndigite o valor do produto %s \n' % (desc))
  while valor == '' or valor.isalpha():
        print('\nvalor invalido\n')
        valor = input('\ndigite um valor valido para o produto %s\n' % (desc))
  conf_cad = input('\ndeseja confirma o cadastro?\n1 - sim\n2 - nao \n')
  while conf_cad not in ['1', '2']:
        conf_cad = input('\nOpção inválida. \nDigite 1 para sim ou 2 para não.\n')
  if conf_cad == '1':
        with open('produtos1.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{cod};{desc};{valor}\n")
        print('\ncadastro confirmado com sucesso\n')
  elif conf_cad == '2':
        print('\ncadastro cancelado\n')
  pausar() 

def listar(): 
    with open('produtos1.txt', 'r', encoding='utf-8') as f:
        dados = f.readlines()
        if not dados:
            print('\nNenhum produto cadastrado.\n')
        else:
            dados = sorted(dados, key=lambda x: int(x.strip().split(';')[0]))
            print('\nLista de produtos:\n')
            for linha in dados:
                cod, desc, valor = linha.strip().split(';')
                print(f'Código: {cod} | Descrição: {desc} | Valor: R${valor}')
    pausar()

def listar2(): 
    with open('produtos1.txt', 'r', encoding='utf-8') as f:
        dados = f.readlines()
        if not dados:
            print('\nNenhum produto cadastrado.\n')
        else:
            dados = sorted(dados, key=lambda x: int(x.strip().split(';')[0]))
            print('\nLista de produtos:\n')
            for linha in dados:
                cod, desc, valor = linha.strip().split(';')
                print(f'Código: {cod} | Descrição: {desc} | Valor: R${valor}')

def alterar():
    limpar_tela()
    with open('produtos1.txt', 'r', encoding='utf-8') as f:
        dados = f.readlines()
    if not dados:
        print('\nNenhum produto cadastrado. \n')
        return
    listar()
    codigo = input('\nDigite o código do produto que deseja alterar:\n')
    encontrado = False
    for i in range(len(dados)):
        cod, desc, valor = dados[i].strip().split(';')
        if cod == codigo:
            print(f'Produto encontrado: {desc} - R${valor}')
            novo_desc = input('\nDigite a nova descrição (ou deixe em branco para manter):\n')
            novo_valor = input('\nDigite o novo valor (ou deixe em branco para manter):\n')
            if novo_desc == '':
                    novo_desc = desc
            if novo_valor == '':
                    novo_valor = valor
            dados[i] = f'{cod};{novo_desc};{novo_valor}\n'
            encontrado = True
            print('\nProduto alterado com sucesso.\n')
    if not encontrado:
         print('\nCódigo não encontrado. Voltando ao menu\n')
         pausar()
         return codigo
    with open('produtos1.txt', 'w', encoding='utf-8') as f:
        f.writelines(dados)
    pausar()

def excluir():
    with open('produtos1.txt', 'r', encoding='utf-8') as f:
        dados = f.readlines()
    if not dados:
        print('\nNenhum produto cadastrado. \n')
        pausar()
        return
    listar()
    encontrado = False
    while not encontrado:
        codigo = input('\nDigite o código do produto que deseja excluir (ou digite "0" para cancelar):\n')
        if codigo == '0':
            print('\nOperação cancelada pelo usuário.\n')
            pausar()
            return
        for i in range(len(dados)):
            cod, desc, valor = dados[i].strip().split(';')
            if cod == codigo:
                print(f'Produto encontrado: {desc} - R${valor}')
                conf = input('\nDeseja mesmo apagar esse produto?\n1 - Sim\n2 - Não\n')
                while conf not in ['1', '2']:
                    conf = input('\nResposta inválida. Digite 1 para sim ou 2 para não:\n')
                if conf == '1':
                    dados.pop(i)
                    print('\nProduto apagado com sucesso.\n')
                    encontrado = True
                else:
                    print('\nOperação cancelada.\n')
                    pausar()
                    return
                break
        if not encontrado:
            print('\nCódigo inválido. Tente novamente.\n')
    nova_lista = []
    for linha in dados:
        if linha.strip() == '':
            continue
        _, desc, valor = linha.strip().split(';')
        nova_lista.append((desc, valor))
    with open('produtos1.txt', 'w', encoding='utf-8') as f:
        for i, (desc, valor) in enumerate(nova_lista, start=100):
            f.write(f'{i};{desc};{valor}\n')

def menu_operador():
    limpar_tela()
    op= input('\nBem vindo, ao menu do cliente!\ndigite oque deseja fazer\n1 - fazer pedido\n2 - olhar carrinho\n3 - desfazer pedido\n4 - finalizar compra\n0 - sair\n')
    while op== '' or op!='0' and op!='1' and op!= '2' and op!='3' and op!='4':
        print('\nopçao invaida\n')
        op= input('\ndigite uma opçao valida\n')
    return op
    
def excluir2():
    limpar_tela()
    with open('carrinho.txt', 'r', encoding='utf-8') as f:
        dados = f.readlines()
    if dados=='':
        print('\nNenhum produto cadastrado.\n')
        return
    carrinho()
    codigo = input('\nDigite o código do produto que deseja excluir:\n')
    encontrado = False
    for i in range(len(dados)):
        cod, desc, valor = dados[i].strip().split(';')
        if cod == codigo:
            print(f'Produto encontrado: {desc} - R${valor}')
            conf= input('\ndeseja mesmo apagar esse produto?\n1 - sim\n2 - nao\n')
            while conf =='' or conf!='1' and conf!='2':
                input('\nresposta invalida, digite uma resposta valida\n')
                return conf
            if conf=='1':
                dados.pop(i)
                with open('carrinho.txt', 'w', encoding='utf-8') as f:
                    f.writelines(dados)
                print ('\nproduto apagado com sucesso\n')
                encontrado = True
            else:
                print('\noperaçao cancelada\n')
            break
    if not encontrado:
        print('\ncodigo invalido, voltando para o menu...\n')
        pausar()
        return

def pedido():
    limpar_tela()
    print('\nBem vindo!\n---porfavor digite suas informações conforme pedido a seguir---')
    listar()
    with open('produtos1.txt', 'r', encoding='utf-8') as f:
        dados = f.readlines()
    if not dados:
        print('\nNão há produtos ainda, volte mais tarde.\n')
        return
    pedido= input('\nqual sera o pedido de hoje?\ndigite o codigo do produto que deseja\n')
    encontrado= False
    #pedido=input('\ndigite um codigo valido\n')
    for linha in dados:
        cod, desc, valor=  linha.strip().split(';')
        if cod == pedido:
            encontrado= True
            print(f'produto selecionado:{desc} - R${valor}')
            conf= input('\ndeseja confirma adicionar o produto ao carrinho?\n 1 - sim\n 2 - nao \n')
            while conf not in ['1', '2']:
                conf = input('\nOpção inválida. \nDigite 1 para sim ou 2 para não.\n')
            if conf == '1':
                with open('carrinho.txt', 'a', encoding='utf-8') as carrinho:
                    carrinho.write(f"{cod};{desc};{valor}\n")
                print('\nseu produto foi colocado ao carrinho com sucesso\n')
            else:
                print('\ncadastro cancelado\n')
    if not encontrado:
        print('\ncodigo invalido, voltando para o menu...\n')
    pausar()
        
def carrinho():
    limpar_tela()
    with open('carrinho.txt', 'r', encoding='utf-8') as f:
        dados = f.readlines()
        if not dados:
            print('\nvoce nao adicionou nada ao carrinho ainda :(\n')
        else:
            print('\nLista de produtos:\n')
            for linha in dados:
                cod, desc, valor = linha.strip().split(';')
                print(f'Código: {cod} | Descrição: {desc} | Valor: R${valor}')
    pausar()

def finalizar():
    limpar_tela()
    nome = input('\nOlá! Falta pouco para finalizarmos seu pedido.\nPor favor, informe seu nome para te chamarmos quando estiver tudo pronto 😉\n')
    with open('carrinho.txt', 'r', encoding='utf-8') as f:
        dados = f.readlines()
    if not dados:
        print('\nParece que você não adicionou nada ao carrinho ainda :(\nNão é possível finalizar o pedido.\n')
        pausar()
        return
    print(f'\nResumo do pedido de {nome}:\n')
    total = 0
    for linha in dados:
        partes = linha.strip().split(';')
        if len(partes) == 3:
            cod, desc, valor = partes
            valor = valor.replace(',', '.')
            if valor.replace('.', '').isdigit():
                total += float(valor)
                print(f'Código: {cod} | Produto: {desc} | Valor: R${float(valor):.2f}')
            else:
                print(f'\nValor inválido no produto: {desc}')
    print(f'\nTotal da compra: R${total:.2f}')
    print(f'\nMuito obrigado, {nome}! Seu pedido está sendo preparado. 😊\n')
    with open('carrinho.txt', 'w', encoding='utf-8') as f:
        pass
    pausar()

os.system ('clear')
while continuar == "s":
    op_principal = menu_logon()
    if op_principal == "0":
        continuar = "n"
    elif op_principal == "1":
        cont = "s"
        while cont == "s":
            op_adm = menu_adm()
            if op_adm == "0":
                cont = "n"
            elif op_adm == "1":
                cadastrar()
            elif op_adm == "2":
                cont='s'
                listar()
            elif op_adm == "3":
                cont='s'
                alterar()
            elif op_adm =='4':
                cont= 's'
                excluir()
    elif op_principal == '2':
        cont= 's'
        while cont =='s':
            op_operador= menu_operador()
            if op_operador== '0':
                cont='n'
            elif op_operador== '1':
                cont='s'
                pedido()
            elif op_operador== '2':
                cont='s'
                carrinho()
            elif op_operador=='3':
                cont='s'
                excluir2()
            elif op_operador=='4':
                cont='s'
                finalizar()
    else:
        cont='n'
              