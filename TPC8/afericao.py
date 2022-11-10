### tpc1.a) Recebe duas strings, _s1_ e _s2_, e retorna o comprimento da substring inicial de _s1_ que não contem nenhum caráter de _s2_:

def inicDiferente(s1, s2):
    res = 0
    
    for letter in s1:
        if letter not in s2:
            res += 1
        
        else:
            return(res)    
    
    print(res)


inicDiferente("Está um bom dia...", "Hoje é um dia alegre.")


### tpc1.b) Recebe um parâmetro _n_ e lê _n_ números inteiros; no fim retorna quantos dos números lidos são superiores à média dos números lidos:

def acimaMedia(n):
    res = 0
    lista = []
    listasup = []
    i = 0
    media = 0

    while i < n:
        num = int(input('Digite um número a ser lido'))
        lista.append(num)
        i += 1
        res = res + num
    
    media = res/len(lista)

    for elem in lista:
        if elem > media:
            listasup.append(elem)

    print(media)
    return len(listasup)
   

acimaMedia(5)


### tpc1.c) Faz o merge de duas listas ordenadas, retornando uma lista ordenada com os elementos das duas listas (__não podes usar nenhuma função de ordenação do Python__):

def merge(l1, l2):

        l = l1 + l2
        trocar = True

        while trocar:
                i = 1
                trocar = False
                while i < len(l):
                        if l[i] < l[i-1]:
                                l[i], l[i-1] = l[i-1], l[i]
                                trocar = True
                
                        i += 1
        
        return l
  
  
merge([1,2,6,9], [3,4,7,12])


### tpc1.d) Recebe o nome de dois ficheiros de texto, _f1_ e _f2_, e indica se são iguais (__True__) no seu conteúdo ou se são diferentes (__False__):

def figuais(f1, f2):
    listaf1 = []
    listaf2 = []

    file1 = open(f1, 'r')
    
    for l in file1:
        listaf1.append(l.strip('\n'))
    
    file1.close()
    
    file2 = open(f2, 'r')

    for l in file2:
        listaf2.append(l.strip('\n'))
    
    file2.close()
    
    listaf1.sort()
    print(listaf1)
    listaf2.sort()
    print(listaf2)

    return listaf1 == listaf2 
  
  
print(figuais('texto1.txt', 'texto2.txt'))


### tpc2.a)  Devolve uma lista dos atores participantes nos filmes armazenados, ordenada alfabeticamente e sem repetições:

def atores(cinemateca):
    lista = []
    
    for filme in cinemateca:
        for ator in filme[2]:
            if ator not in lista:
                lista.append(ator)
            
    lista.sort()
    return lista


print(atores(CineUM))


### tpc2.b)  Devolve uma lista de todos os títulos dos filmes, em ordem alfabética, e de um determinado género passado como argumento:

def listarPorGenero(cinemateca, genero):
    
    filmes = []

    for filme in cinemateca:
        if genero in filme[3]:
            filmes.append(filme[0])
    
    filmes.sort()
    return filmes

  
print(listarPorGenero(CineUM, "Comedy"))


### tpc2.c)  Devolve o título do filme com o maior elenco:

def maiorElenco( cinemateca ):

    natc = []

    for filme in cinemateca:
        natc.append(len(filme[2]))
        
    natc.sort()

    for filme in cinemateca:
        if len(filme[2]) == natc[-1]:
            movie = filme[0]

    return movie

  
print(maiorElenco(CineUM))


### tpc2.d)  Calcula a distribuição de filmes por Género:

def filmePorGenero( cinemateca ):
    
    dicgen = {}

    for filme in cinemateca:
        for genero in filme[3]:
            if genero not in dicgen:
                dicgen[genero] = 1
            
            else:
                dicgen[genero] = dicgen[genero] +1

    return dicgen

  
filmePorGenero(CineUM)


### tpc2.e)  Represente num gráfico de barras a distribuição calculada na alínea anterior (pode usar o material que entender das aulas):

import matplotlib.pyplot as plt

def graf(cinemateca):

    dicgen = filmePorGenero(cinemateca)
    eixox = [x for x in range(0, len(dicgen))]
    eixoy = []

    for key in dicgen:
        eixoy.append(dicgen[key])
    
    plt.bar(eixox, eixoy, width=0.5, color = ('r', 'b', 'y', 'black'))
    plt.xticks(eixox, dicgen.keys())
    plt.yticks(eixoy, dicgen.values())
    plt.xlabel('Géneros')
    plt.ylabel('Número de filmes')
    plt.title('Gráfico de distribuição')
    plt.show()

    
graf(CineUM)
