#exercicio 3
import funçoes as f
ano = int(input("forneça um ano(1997 a 2019):"))

if (ano >=1997 and ano<2019):
    filem = f.codfilom(ano)
    print('O ano {}\nem film = \'{}\''.format(valor, por))

else:
    print('ano invalido!!')


def codfilm(ano):
    dicfilm = {
         2013:"Frozen ",
         2012:"titanic",
         2018:"Black Panther", 
         2015:"Avengers: Age of Ultron", 
         2009:"Avatar", 
         2015:"Star Wars: The Force Awakens",
         2017:"Star Wars: The Last Jedi", 
         2015:"Furious 7", 
         2011:"Harry Potter and the Deathly Hallows – Part 2", 
         2019:"Avengers: Endgame",
         2015:"Jurassic World",
         2018:"Avengers: Infinity War",
         2017:"Beauty and the Beast", 
         2018:"Jurassic World: Fallen Kingdom ",
         {
     return(dicfilm[ano])]

def gerafilm(ano):
    dsecr = []

    s = str(ano)

    for c in s:
         descr.append(codfilm(int(c)))

     return descr
