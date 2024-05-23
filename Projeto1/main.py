manifestacoes = []
codigos = 1
opcao = 0

print("---BEM VINDO A OUVIDORIA---")

while opcao != 7:
    print('1. Listar manifestações (Geral)')
    print('2. Listar manifestações (Por tipo)')
    print('3. Criar nova manifestação')
    print('4. Exibir quantidade de manifestações')
    print('5. Pesquisar manifestação (Por código)')
    print('6. Excluir manifestação (Por código)')
    print('7. Sair do sistema')

    opcao = int(input("Digite a opção desejada: "))    

    if opcao == 1:
        
        if len(manifestacoes) == 0:
            print("Não foi criada nenhuma manifestação!")
        
        elif len(manifestacoes) != 0:
            for i in manifestacoes:
                print(i)

    elif opcao == 2:
        tipo = input("Digite o tipo de manifestação desejada (Reclamação, Elogio ou Sugestão)? ").lower()
        filtro = []
        for i in manifestacoes:
            if i['tipo'] == tipo:
                filtro.append(i)
        if len(filtro) == 0:
            print(f"Não existem manifestações do tipo '{tipo}' cadastradas!")
        else:
            for i in filtro:
                print(i)

    elif opcao == 3:
        tipo = input("Digite o tipo de manifestação (Reclamação, Elogio, Sugestão): ").lower()
        descricao = input("Digite a manifestação: ")
        novaManifestacao = {
            'codigo':  codigos,
            'tipo': tipo,
            'descrição': descricao
        }
        manifestacoes.append(novaManifestacao)
        codigos += 1
        print("Nova manifestação criada com sucesso!")

    elif opcao == 4:
        if len(manifestacoes) == 0:
            print("Não existem manifestações cadastradas")
        else:
            print(f"Quantidade de manifestações: '{len(manifestacoes)}'")

    elif opcao == 5:
        codigo = int(input("Digite o código da manifestação: "))
        for i in manifestacoes:
            if i['codigo'] == codigo:
                print(i)
            else:
                print('Manifestação não encontrada!')

    elif opcao == 6:
        codigo = int(input("Digite o código da manifestação desejada: "))
        for i in manifestacoes:
            if i['codigo'] == codigo:
                manifestacoes.remove(i)
                print("Manifestação excluida com sucesso!")
            else:
                print("Manifestação não encontrada!")

    elif opcao == 7:
        print("Obrigado pela sua opinião!")

    else:
        print("Opção inválida, por favor escolha um opção válida")

