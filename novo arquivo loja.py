import pandas as pd
import numpy as np
listaUsuarios=[]
historico_compras_todos=[]

#Criacao Do Catalogo
Catalogo=pd.DataFrame({'Nome do jogo':['Hitman','The Medium','Into The Breach','The lion','Quest','Sea','Only Memories','Kraken Academy','Assasins Creed'],\
    'Preco do jogo':[300,250,390,300,200,150,430,123,213],\
      'genero':['Açao','Horror','Estrategia','RPG','RPG','RPG','Açao','Horror','Estrategia'],\
        'Estoque':[10,122,10,80,2,3,5,8,6]})


###Visualizacao e Filtagrem do Catalogo para cliente
def Visualizar_catalogoCliente():
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
        Visualizar_catalogoCliente()


    

    ###Visualizacao e Filtagrem do Catalogo para Vendedor
def Visualizar_catalogoVendedor():
   #variaveis para a filtragem por genero
    indice_genero=0
    Catalogo_genero=  Catalogo[['Nome do jogo','Preco do jogo','genero','Estoque']].copy(deep=True)
    
    #escolha do filtro
    filtro= input('Escolha o tipo de Filtro:\n[A]-Ordem Alfabetica\n[B]-Preco\n[C]-Genero\n')

    #filtragem por ordem alfabetica
    if filtro == 'A':
      print(Catalogo[['Nome do jogo','Preco do jogo','genero','Estoque']].sort_values(by='Nome do jogo'))
    
    #filtagrem por preco
    elif filtro == 'B':
        print(Catalogo[['Nome do jogo','Preco do jogo','genero','Estoque']].sort_values(by='Preco do jogo'))
    
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
        Visualizar_catalogoVendedor()



###Criacao das Classes
class Cliente:
    def __init__(self,nome):
        self.nome=nome
        self.carrinho=pd.DataFrame({'Nome do jogo':[],\
    'Preco do jogo':[]})
        self.historico_de_compras=[self.nome,self.carrinho.columns.values.tolist()]
        listaUsuarios.append(self.nome)

    #metodo para acessar o catalogo
    def catalogo(self):
        Visualizar_catalogoCliente()


    def adicionar_produto_carrinho(self):
        
        while True:
            try:
                produto=int(input('\nDigite o indice do produto que deseja colocar no carrinho\nCaso nao tenha escolhido ainda e deseja ver o catalago digite [-1]\nPara sair digite [-2]\n'))
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
           produto=int(input('\nDigite o indice do produto que deseja remover do carrinho\nCaso nao tenha escolhido ainda e deseja ver o carrinho digite [-1]\nPara sair digite [-2]\n'))
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


    def valor_carrinho(self):
        valor_carrinho=0

        for preco in self.carrinho['Preco do jogo']:
            valor_carrinho +=preco
        print(f'Valor Total do carrinho = {valor_carrinho}\n') 



    def finalizar_compra(self):

        self.valor_carrinho()

        for jogo in self.carrinho['Nome do jogo']:
            Catalogo.loc[Catalogo['Nome do jogo']==jogo,"Estoque"]-=1

        

        self.historico_de_compras.append(self.carrinho.values.tolist())

        self.carrinho=pd.DataFrame({'Nome do jogo':[],\
            'Preco do jogo':[]})
        print('Compra Finalizada!!!')

        historico_compras_todos.append(self.historico_de_compras)




        



class Vendedor(Cliente):
    def __init__(self, nome):
        super().__init__(nome)

    def catalogo(self):
        Visualizar_catalogoVendedor()

    def historico_compras_todos(self):
        print(historico_compras_todos)

        

