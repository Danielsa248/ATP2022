import csv

def readDataset(fnome):
    f = open(fnome, encoding='utf-8')
    f.readline()
    csv_reader = csv.reader(f, delimiter=';')
    obras = []

    for row in csv_reader:
        obras.append(tuple(row))
    
    return obras



##### Pretty Print #####

def pp(obra):
    print(f'{obra[0][:25]:25} :: {obra[4][:30]:30} :: {obra[3][:15]:15} :: {obra[2][:6]:6} ')

    

#### Lista Título Ano ordenar Título #####

def ordtitulo(t):
    return t[0]

def listatituloano(obras):
    res = []

    for nome, _, ano, *_ in obras:
        res.append((nome, ano))
    
    res.sort(key=ordtitulo)

    return res



#### Lista Título Ano ordenar Ano #####

def ordano(t):
    return t[1]

def listatituloano2(obras):
    lista = []

    for nome, _, ano, *_ in obras:
        lista.append((nome, ano))
    
    lista.sort(key=ordano)

    return lista



#### Dicionário em que cada ano tem a ele associado a lista de títulos a ele associado #####

def titPorAno(obras):
    res = {}

    for nome, _, ano, *_, in obras:
        if ano in res.keys():
            res[ano].append(nome)

        else:
            res[ano] = [nome]
    
    return res



#### Lista de Compositores ordenada #####

def listacomp(obras):
    lista = []

    for _, _, _, _, compositor, *_ in obras:
        if compositor not in lista:
            lista.append(compositor)
            
    lista.sort()

    return lista



#### Calculo distribuição de obras por período #####

def distribperiodo(obras):
    periodo = {}

    for myObras in obras:
        if myObras[3] in periodo:
            periodo[myObras[3]] = periodo[myObras[3]] + 1
        
        else:
            periodo[myObras[3]] = 1
    
    return periodo



#### Calculo distribuição de obras por ano #####

def distribobras(obras):
    anos = {}

    for myObras in obras:
        
        if myObras[2] in anos:
            anos[myObras[2]] = anos[myObras[2]] + 1
        
        elif myObras[2] not in anos:
            anos[myObras[2]] = 1

    return anos



#### Calculo distribuição de obras por compositor #####

def ordcomp(t):
    return t(0)


def distribcomp(obras):
    comp = {}

    for myObras in obras:

        if myObras[4] in comp:
            comp[myObras[4]] = comp[myObras[4]] + 1
        
        else:
            comp[myObras[4]] = 1
        
    return comp
    

### Gráfico Período ###

import matplotlib.pyplot as plt

def graficperiodo(obras):

    periodo = distribperiodo(obras)
    numeros = [x for x in range(1, len(periodo)+1)]
    periodos = list(periodo.keys())
    height = []
    
    for p in periodos:
       height.append(periodo[p])

    plt.bar( numeros, height, tick_label = periodos)
    plt.xticks(rotation = 45)
    plt.xlabel('Períodos')
    plt.ylabel('Número de Obras')
    plt.title('Distribuição por Período')
    plt.show()



### Gráfico Ano ###

def graficano(obras):

    anos = distribobras(obras)
    numeros = [x for x in range(1, len(anos)+1)]
    ano = list(anos.keys())
    height = []

    for a in ano:
    
        height.append(anos[a])
    
    plt.bar(numeros, height, tick_label = ano, width=0.5)
    plt.xticks(rotation = 90)
    plt.xlabel('Ano')
    plt.ylabel('Número de Obras')
    plt.title('Distribuição por Ano')
    plt.show()



### Gráfico Compositor ###

def graficcomp(obras):

    comp = distribcomp(obras)
    numeros = [x for x in range(1, len(comp)+1)]
    compo = list(comp.keys())
    height=[]

    for c in compo:
        height.append(comp[c])
    
   
    plt.bar(numeros, height, tick_label = compo, width=0.5)
    plt.xticks(rotation = 90)
    plt.xlabel('Compositores')
    plt.ylabel('Número de Obras')
    plt.title('Distribuição por Compositor')
    plt.show()



### Lista dos compositores em que cada compositor tem a ele associado uma lista dos títulos das obras que compôs ###

def listacompobras(obras):
    res = {}

    for nome, _, _, _, compositor, *_, in obras:

        if compositor in res.keys():
            res[compositor].append(nome)
        
        else:
            res[compositor] = [nome]
    
    return res



### Função de visualização para estrutura de dados calculada na alínea anterior ###

def tabela(obras):

    dados = listacompobras(obras)
    print(f'COMPOSITORES                        | OBRAS ')
    print("-----------------------------------------------------------------------------------------------------------------------------------")

    for dado in dados:
        print(f'{dado:35} | {dados[dado]}')


### Função mostrar pp ###

def mostrarpp():
    myObras = readDataset('obras.csv')

    for i in range(0, len(myObras)):
        pp(myObras[i])
        


### Função mostrar listas/ dicionários ###

def mostrarlistatituloano(obras):
    mostrar = listatituloano(obras)
    print(mostrar)

def mostrarlistatituloano2(obras):
    mostrar = listatituloano2(obras)
    print(mostrar)

def mostrartitPorano(obras):
    mostrar = titPorAno(obras)
    print(mostrar) 

def mostartlistacomp(obras): 
    compo = listacomp(obras)
    print(compo)




### Menu ###

def menu():

    print('MENU')
    print('----------')
    print('(1) Carregar o dataset')
    print('(2) Imprimir no monitor uma tabela com o título da obra, o seu compositor, o período e o ano de criação')
    print('(3) Produzir uma lista de tuplos (título, ano) ordenada alfabeticamente por título')
    print('(4) Produzir uma lista de tuplos (título, ano) ordenada crescentemente por ano')
    print('(5) Produzir um dicionário em que cada ano tem a ele associado a lista de títulos a ele associado')
    print('(6) Produzir uma lista ordenada dos compositores')
    print('(7) Desenhar gráfico correspondente à distribuição por período ')
    print('(8) Desenhar gráfico correspondente à distribuição por ano')
    print('(9) Desenhar gráfico correspondente à distribuição por compositor')
    print('(10) Tabela em que a cada compositor corresponde os seus títulos ')
    print('(0) Sair')
    print('')



### Aplicação ###

def modo(obras):

    modo = -1
    
    
    while modo != 0:
        menu()
        modo = int(input('Digite o número do modo: '))
        
        if modo == 1:
            fnome = 'obras.csv'
            readDataset(fnome)
        
        elif modo == 2:
            print('')
            print('Modo Mostrar')
            print('')
            mostrarpp()
            print('')
            print('')
        
        elif modo == 3:
            print('')
            print('Modo Criar e Mostrar')
            print('')
            mostrarlistatituloano(obras)        
            print('')
            print('')
        
        elif modo == 4:
            print('')
            print('Modo Criar e Mostrar')
            print('')
            mostrarlistatituloano2(obras)
            print('')
            print('')
        
        elif modo == 5:
            print('')
            print('Modo Criar e Mostrar')
            print('')
            mostrartitPorano(obras)
            print('')
            print('')
        
        elif modo == 6:
            print('')
            print('Modo Criar e Mostrar')
            print('')
            mostartlistacomp(obras)
            print('')
            print('')
       
        elif modo == 7:
            print('')
            print('Modo Gráfico')
            print('')
            graficperiodo(obras)
            print('')
            print('')
        
        elif modo == 8:
            print('')
            print('Modo Gráfico')
            print('')
            graficano(obras)
            print('')
            print('')
        
        elif modo == 9:
            print('')
            print('Modo Gráfico')
            print('')
            graficcomp(obras)
            print('')
            print('')
        
        elif modo == 10:
            print('')
            print('Modo Tabela')
            print('')
            tabela(obras)
            print('')
            print('')

        elif modo == 0:
            print('')
            print('Modo Sair')
            print('')
            print('Sair . . . ')
            print('')
            print('')
