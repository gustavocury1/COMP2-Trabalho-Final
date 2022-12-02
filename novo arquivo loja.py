import pandas as pd
import numpy as np

#Criacao Do Catalogo
Catalogo=pd.DataFrame({'Nome do jogo':['Hitman','The Medium','Into The Breach','The lion','Quest','Sea','Only Memories','Kraken Academy','Assasins Creed'],\
    'Preco do jogo':[300,250,390,300,200,150,430,123,213],\
      'genero':['Açao','Horror','Estrategia','RPG','RPG','RPG','Açao','Horror','Estrategia'],\
        'Estoque':[10,122,10,80,2,3,5,8,6]})


#Visualizacao e Filtagrem do Catalogo
def Visualizar_catalogo():
   #variaveis para a filtragem por genero
    indice_genero=0
    Catalogo_genero=  Catalogo[['Nome do jogo','Preco do jogo','genero']].copy(deep=True)
    
    #escolha do filtro
    filtro= input('Escolha o tipo de Filtro:\n[A]-Ordem Alfabetica\n[B]-Preco\n[C]-Genero\n')

    #filtragem por ordem alfabetica
    if filtro == 'A':
      print(Catalogo[['Nome do jogo','Preco do jogo','genero']].sort_values(by='Nome do jogo'))
    
    #filtagrem por preco
    elif filtro == 'B':
        print(Catalogo[['Nome do jogo','Preco do jogo','genero']].sort_values(by='Preco do jogo'))
    
    #filtagrem por genero
    elif filtro=='C':
        while True:
            filtro=input('Escolha o genero que deseja:\nAçao,Horror,Estrategia,RPG\n')
            if filtro== 'Açao' or filtro =='Horror' or filtro == 'Estrategia' or filtro =='RPG':
                for genero in Catalogo['genero']:
                    if genero != filtro:
                        Catalogo_genero.drop([indice_genero],inplace=True)
                    indice_genero+=1
                print(Catalogo_genero)
                break
            else:
                print('Escolha um genero existente!\n')
    else:
        print('Escolha entre A B ou C\n')
        Visualizar_catalogo()

#Criacao das Classes
class Cliente:
    def __init__(self,nome):
        self.nome=nome
        self.carrinho=pd.DataFrame({'Nome do jogo':[],\
    'Preco do jogo':[]})

    #metodo para acessar o catalogo
    def catalogo(self):
        Visualizar_catalogo()


    def adicionar_produto_carrinho(self):
        
        while True:
            try:
                produto=int(input('Digite o indice do produto que deseja colocar no carrinho\nCaso nao tenha escolhido ainda e deseja ver o catalago digite [-1]\nPara sair digite [-2]\n'))
                if produto < len(Catalogo.index) and produto>=0:
                    self.carrinho.loc[produto]=Catalogo.iloc[produto]
                    print('produto adicionado!\n')
                    print('Carrinho:\n')
                    print(self.carrinho)
                elif produto == -2:
                    break

                elif produto == -1:
                    self.catalogo()

                else:
                    print('indice do produto nao existe\n')
            except Exception:
                print('indice do produto nao existe\n')

                

    def remover_produto_carrinho(self):
      while True:
         try:
           produto=int(input('Digite o indice do produto que deseja remover do carrinho\nCaso nao tenha escolhido ainda e deseja ver o carrinho digite [-1]\nPara sair digite [-2]\n'))
           if produto < len(Catalogo.index) and produto>=0:
              self.carrinho.drop([produto],inplace=True)
              print('Produto retirado!\n')
              print(self.carrinho)
                      
           elif produto == -1:
              print(self.carrinho)

           elif produto==-2:
              break

           else:
              print('indice do produto nao existe\n')
         except Exception:
           print('indice do produto nao existe\n')










































           
