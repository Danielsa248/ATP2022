import csv

### função que lê a informação do ficheiro para um modelo, previamente pensado em memória ###

def readDataset(fnome):

    f = open(fnome, encoding='utf-8')
    f.readline()
    csv_reader = csv.reader(f, delimiter = ',')
    alunos = []

    for row in csv_reader:
        alunos.append(tuple(row))

    return alunos



### função que calcula a distribuição dos alunos por curso ###

def distribcurso(alunos):

    curso = {}

    for aluno in alunos:
        if aluno[2] in curso:
            curso[aluno[2]] = curso[aluno[2]] + 1
        
        else:
            curso[aluno[2]] = 1

    return curso


def ppcurso(alunos):
    
    curso = distribcurso(alunos)  
    for key in curso:
        print(f"{key:8} ------> {curso[key]}")



### função que calcula a média das notas de cada aluno e acrescenta essa nova coluna no dataset em memória ###

def calmedia(alunos):

    novalista = []

    for aluno in alunos:
        media = (float(aluno[3]) + float(aluno[4]) + float(aluno[5]) + float(aluno[6])) / 4
        listaaluno = list(aluno)
        listaaluno.append(media)
        aluno = tuple(listaaluno)
        novalista.append(aluno)
    
    return novalista


def addmedia(alunos):

    nf = open('alunos.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(nf, lineterminator='\n')
    csv_writer.writerow(['id_aluno','nome','curso','tpc1','tpc2','tpc3','tpc4', 'media'])
    csv_writer.writerows(calmedia(alunos))
    nf.close   



### acrescente uma coluna ao dataset com o escalão correspondente a cada aluno ###

import string

def escaloes():

    dicescalao = {}
    lescaloes = []
    n = 0
    b = 0

    for n in range(1, 21, 4):
        escalao = (n, n+3)
        lescaloes.append(escalao)
    
    for escalao in lescaloes:       
        if escalao not in dicescalao:
            dicescalao[escalao] = string.ascii_uppercase[len(lescaloes)-(1+b)]
            b += 1      

    return dicescalao


def lnota(alunos):

    alunos = calmedia(alunos)
    listanota = []
    dicescalao = escaloes()
    keys = list(dicescalao.keys())
    values = list(dicescalao.values())
    
    for aluno in alunos:
        n = 0

        while n <= (len(keys)-1): 
            a = keys[n][0]
            b = keys[n][1]
            
            if round(float(aluno[7]))>= float(a) and round(float(aluno[7]))<= float(b):
                listanota.append(values[n])
                
            n += 1

    novalista = []
    listaaluno = []
    i = 0

    while i < len(alunos):
        listaaluno = list(alunos[i])
        listaaluno.append(listanota[i])
        aluno = tuple(listaaluno)
        novalista.append(aluno)
        i += 1
        
    return novalista 


def addnota(alunos):

    nv = open('alunos.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(nv, lineterminator='\n')
    csv_writer.writerow(['id_aluno','nome','curso','tpc1','tpc2','tpc3','tpc4', 'media', 'nota'])
    csv_writer.writerows(lnota(alunos))
    nv.close



### distribuição dos alunos por escalão ###

def distribesc(alunos):
    esc = {}
    dicescalao = escaloes()
    alunos = lnota(alunos)

    for n in range(0, len(dicescalao)):

        esc[string.ascii_uppercase[n]] = 0
        n += 1
    
    for aluno in alunos:
        if aluno[8] in esc:
            esc[aluno[8]] = esc[aluno[8]] + 1
        
        else:
            esc[aluno[8]] = 1

    return esc



### qual distribuição queremos ###

def qualdistrib(alunos):
    print('Que distribuição pretende usar?')
    print('(1) Curso')
    print('(2) Escalões')
    print('')

    usar  = False

    while usar == False:

        usar = int(input('Digite o número da opção a usar: '))

        if usar == 1:
            res = distribcurso(alunos)
            usar = True
    
        elif usar == 2:
            res = distribesc(alunos)
            usar = True
    
        else:
            print('Digite um dos números acima indicados')
            usar = False

    return res



### função que apresenta na forma dum gráfico de linha uma distribuição ###
import matplotlib.pyplot as plt

def graf(alunos):

    distrib = qualdistrib(alunos)
    eixox = [x for x in range(0, len(distrib))]
    eixoy = []

    for key in distrib:
        y = distrib[key]
        eixoy.append(y)

    plt.plot(eixox, eixoy, marker = 'X', markersize = 11, markerfacecolor = 'red')
    plt.title('Gráfico de Distribuição')
    plt.xlabel('Distribuição')
    plt.ylabel('Número de alunos')
    plt.xticks(eixox, distrib.keys())
    plt.yticks(eixoy, distrib.values())
    plt.show()



### função que imprime na forma de uma tabela uma distribuição ###

def tabela(alunos):

    distrib = qualdistrib(alunos)
    print(f"| {'Distribuição' :=^50} |")

    for key in distrib:
        print(f"| {key:^20} | {distrib[key]:^27} |")
    
    print("| ================================================== |")



### limpar dataset ###

def readDatasetclear():

    f = open('alunosclear.csv', encoding='utf-8')
    f.readline()
    csv_reader = csv.reader(f, delimiter = ',')
    orig = []

    for row in csv_reader:
        orig.append(tuple(row))

    return orig

def clear():

    orig = readDatasetclear()
    nf = open('alunos.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(nf, lineterminator='\n')
    csv_writer.writerow(['id_aluno','nome','curso','tpc1','tpc2','tpc3','tpc4'])
    csv_writer.writerows(orig)
    nf.close

### MENU e APP ###

def menu():

    opcoes = ['Sair', 'Carregar Dataset', 'Calcular da distribuição por curso', 'Calcular média das notas e acrescentar ao dataset', 'Calcular escalões e acrescentá-los ao dataset', 'Mostrar o gráfico de uma distribuição', 'Mostrar tabela de uma distribuição', 'Restaurar ficheiro']
    print(f"| {'MENU':=^63} |")

    for opcao in opcoes:
        print(f'| -----> ({opcoes.index(opcao)}) : {opcao:50} |')

    print('| =============================================================== |')

def app(alunos):

    fnome = 'alunos.csv'
    modo = -1
    alunos = []
    flag1 = True
    flag2 = True
    marker = False
    marker2 = True
    clear()

    while modo != 0:
        menu()
        modo = int(input('Digite o modo que pretende utilizar'))
                    
        if modo == 1:
            if marker2 == True:
                print('')
                print('Modo carregar dataset')
                alunos = readDataset(fnome)
                print('.......')
                print('')
                print('')
                marker2 = False

            else:
                print('')
                print('Já carregou o dataset')
                print('')    

        elif modo == 2:
            if alunos ==[]:
                print('')
                print('Modo calcular da distribuição por curso')
                print('')
                print('Primeiro tem de carregar o dataset antes de realizar as proximas operações')
                print('')
                print('') 
                    
            else:
                print('')
                print('Modo calcular da distribuição por curso')
                print('')
                ppcurso(alunos)        
                print('')
                print('')
        
        elif modo == 3:
            if alunos ==[]:
                print('')
                print('Modo calcular média das notas e acrescentar ao dataset')
                print('')
                print('Primeiro tem de carregar o dataset antes de realizar as proximas operações')
                print('')
                print('')
                
            elif flag1 == True:
                print('')
                print('Modo calcular média das notas e acrescentar ao dataset')
                print('')
                calmedia(alunos)
                addmedia(alunos)
                print('Médias calculadas e acrescentadas a cada aluno')
                print('')
                print('')
                flag1 = False
                marker = True

            elif flag1 == False:
                print('')
                print('Modo calcular média das notas e acrescentar ao dataset')
                print('')
                print('As médias das notas já foram acrescentadas')
                print('')

        elif modo == 4:

            if alunos ==[]:
                print('')
                print('Modo calcular escalões e acrescentá-los ao dataset')
                print('')
                print('Primeiro tem de carregar o dataset antes de realizar as proximas operações')
                print('')
                print('')
                
            elif flag2 == True:
                if marker == False:
                    print('')
                    print('Modo calcular escalões e acrescentá-los ao dataset')
                    print('')
                    print('Primeiro use a opção 3 para usar a opção 4')
                    print('')
                    
                else:   
                    print('')
                    print('Modo calcular escalões e acrescentá-los ao dataset')
                    print('')
                    lnota(alunos)
                    addnota(alunos)
                    print('Escalões calculados e acrescentados a cada aluno')
                    print('')
                    print('')
                    flag2 = False
            
            elif flag2 == False:
                print('')
                print('Modo calcular média das notas e acrescentar ao dataset')
                print('')
                print('Os escalões já foram acrescentadas')
                print('')
        
        elif modo == 5:
            if alunos == []:
                print('')
                print('Modo mostrar o gráfico de uma distribuição ')
                print('')
                print('Primeiro tem de carregar o dataset antes de realizar as proximas operações')
                print('')
                print('')

            elif flag1 == False and flag2 == False:
                print('')
                print('Modo mostrar o gráfico de uma distribuição ')
                print('')
                graf(alunos)
                print('')
                print('')

            else:
                print('')
                print('Modo mostrar o gráfico de uma distribuição ')
                print('')
                print('Primeiro necessita de acrescentar as médias e os escalões aos dados para realizar esta operação ')
                print('')             
       
        elif modo == 6:
            if alunos ==[]:
                print('')
                print('Modo mostrar tabela de uma distribuição ')
                print('')
                print('Primeiro tem de carregar o dataset antes de realizar as proximas operações')
                print('')
                print('')

            elif flag1 == False and flag2 == False:
                print('')
                print('Modo mostrar tabela de uma distribuição ')
                print('')
                tabela(alunos)
                print('')
                print('')

            else:
                print('')
                print('Modo mostrar tabela de uma distribuição ')
                print('')
                print('Primeiro necessita de acrescentar as médias e os escalões aos dados para realizar esta operação ')
                print('')
                
        
        elif modo == 7:
            print('')
            print('Modo restaurar ficheiro ')
            clear()
            print('')
            print('Ficheiro restaurado')
            print('')
            print('')
            flag1 = True
            flag2 = True
            marker = False

        elif modo == 0:
            print('')
            print('Modo sair ')
            print('')
            print('.....')
        
        
