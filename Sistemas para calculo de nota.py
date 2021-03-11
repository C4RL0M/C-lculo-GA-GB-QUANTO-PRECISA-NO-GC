# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:45:48 2020

@author: Carlos Nowatzki, para o instituto UNISINOS
"""

alunos = {} # cria um dicionário para armazenar os dados dos alunos da turma

nome = input("Insira o nome do aluno: ")

while nome != '': # enquanto o nome não for vazio, cadastra o aluno
    aluno = {} # cria dicionário vazio para armazenar os dados do aluno
    A1 = float(input(f"Informe a nota A1 do aluno {nome}: "))
    A2 = float(input(f"Informe a nota A2 do aluno {nome}: "))
    B1 = float(input(f"Informe a nota B1 do aluno {nome}: "))
    B2 = float(input(f"Informe a nota B2 do aluno {nome}: "))
    GA = 0.4*A1+0.6*A2
    GB = 0.4*B1+0.6*B2
    media = (GA+2*GB)/3
    aluno['media'] = media # guarda a média no dicionário do aluno
    if media >= 6:
        aluno['status'] = 'aprovado'
    else:
        aluno['status'] = 'não aprovado'
        GCA = 18-2*GB
        GCB = (18-GA)/2
        if GCA < GCB:
            aluno['recupera'] = 'GA'
            aluno['GC'] = GCA
        else:
            aluno['recupera'] = 'GB'
            aluno['GC'] = GCB
    alunos[nome] = aluno # armazena dados do aluno no dicionário de alunos
    nome = input("Insira o nome do aluno: ")
    
continua = input("Deseja fazer uma consulta agora? [s]/n: ")

while continua != 'n': # repete enquanto for solicitada nova consulta
    nome = input("Insira o nome do aluno para consulta: ")
    if nome in alunos: # verifica se o nome escolhido está no dicionário de alunos (chave)
        aluno = alunos[nome] # busca os dados (dicionário) do aluno especificado
        print(f"Aluno: {nome}")
        print(f"Média: {aluno['media']:.1f}")
        print(f"Status: {aluno['status']}")
        if aluno['status'] == 'não aprovado':
            if aluno['recupera'] == 'GA': # verifica se o grau a recuperar é o GA
                print(f"O aluno {nome} precisa recuperar o GA e precisa tirar {aluno['GC']:.1f}")
            else:
                print(f"O aluno {nome} precisa recuperar o GB e precisa tirar {aluno['GC']:.1f}")
    else: # se nome não está cadastrado, informa ao usuário
        print(f"Aluno {nome} não encontrado.")
    continua = input("Deseja continuar? [s]/n: ")
