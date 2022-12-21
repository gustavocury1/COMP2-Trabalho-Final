from tkinter import *
from tkinter import Tk, mainloop, LEFT, TOP, NW,END,CENTER
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot
from datetime import datetime


#INICIO DO PROGRAMA

listaUsuarios=[]
historico_compras_todos=[]


#Criacao Do Catalogo

Catalogo=pd.DataFrame({'Nome do jogo':['Hitman','The Medium','Into The Breach','The lion','Quest','Sea','Only Memories','Kraken Academy','Assasins Creed'],\
'Preco do jogo':[300,250,390,300,200,150,430,123,213],\
      'Genero':['Açao','Horror','Estrategia','RPG','RPG','RPG','Açao','Horror','Estrategia'],\
        'Estoque':[10,122,10,80,2,3,5,8,6]})


###Visualizacao e Filtagrem do Catalogo para cliente

def Visualizar_catalogoCliente():
   #variaveis para a filtragem por genero
    indice_Genero=0
    Catalogo_Genero=  Catalogo[['Nome do jogo','Preco do jogo','Genero']].copy(deep=True)
    
    #escolha do filtro
    filtro= input('Escolha o tipo de Filtro:\n[A]-Ordem Alfabetica\n[B]-Preco\n[C]-Genero\n')

    #filtragem por ordem alfabetica
    if filtro == 'A':
      print(Catalogo[['Nome do jogo','Preco do jogo','Genero']].sort_values(by='Nome do jogo'))
    
    #filtagrem por preco
    elif filtro == 'B':
        print(Catalogo[['Nome do jogo','Preco do jogo','Genero']].sort_values(by='Preco do jogo'))
    
    #filtagrem por genero
    elif filtro=='C':
        while True:
            filtro=input('Escolha o genero que deseja:\nAçao,Horror,Estrategia,RPG\n')
            if filtro== 'Açao' or filtro =='Horror' or filtro == 'Estrategia' or filtro =='RPG':
                for Genero in Catalogo['Genero']:
                    if Genero != filtro:
                        Catalogo_Genero.drop([indice_Genero],inplace=True)
                    indice_Genero+=1
                print(Catalogo_Genero)
                break
            else:
                print('Escolha um genero existente!\n')
    else:
        print('Escolha entre A B ou C\n')
        Visualizar_catalogoCliente()


    

###Visualizacao e Filtagrem do Catalogo para Vendedor
        
def Visualizar_catalogoVendedor():
   #variaveis para a filtragem por genero
    indice_Genero=0
    Catalogo_Genero=  Catalogo[['Nome do jogo','Preco do jogo','Genero','Estoque']].copy(deep=True)
    
    #escolha do filtro
    filtro= input('Escolha o tipo de Filtro:\n[A]-Ordem Alfabetica\n[B]-Preco\n[C]-Genero\n')

    #filtragem por ordem alfabetica
    if filtro == 'A':
      print(Catalogo[['Nome do jogo','Preco do jogo','Genero','Estoque']].sort_values(by='Nome do jogo'))
    
    #filtagrem por preco
    elif filtro == 'B':
        print(Catalogo[['Nome do jogo','Preco do jogo','Genero','Estoque']].sort_values(by='Preco do jogo'))
    
    #filtagrem por genero
    elif filtro=='C':
        while True:
            filtro=input('Escolha o genero que deseja:\nAçao,Horror,Estrategia,RPG\n')
            if filtro== 'Açao' or filtro =='Horror' or filtro == 'Estrategia' or filtro =='RPG':
                for Genero in Catalogo['Genero']:
                    if Genero != filtro:
                        Catalogo_Genero.drop([indice_Genero],inplace=True)
                    indice_Genero+=1
                print(Catalogo_Genero)
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




class Administrador(Vendedor):
    def __init__(self, nome):
        super().__init__(nome)


    def adicionar_produto_estoque(self):
         while True:
            try:
                produto=int(input('\nDigite o indice do produto que deseja adionar ao estoque\nCaso nao tenha escolhido ainda e deseja ver o catalago digite [-1]\nPara sair digite [-2]\n'))
                if produto < len(Catalogo.index) and produto>=0:
                    while True:
                        try:
                            qntd=int(input('\nDigite a quantidade desse produto que deseja adicionar ao estoque\n'))
                            Catalogo['Estoque'][produto]+=qntd
                            print('\nEstoque atualizado!!!\n')
                            break

                        except Exception:
                            print('A quantidade tem que ser um numero inteiro!')


                elif produto == -2:
                    break

                elif produto == -1:
                    self.catalogo()

                else:
                    print('indice do produto nao existe\n')
            except Exception:
                print('indice do produto nao existe\n')



    def alterar_preco(self):
         while True:
            try:
                produto=int(input('\nDigite o indice do produto que deseja alterar o preco\nCaso nao tenha escolhido ainda e deseja ver o catalago digite [-1]\nPara sair digite [-2]\n'))
                if produto < len(Catalogo.index) and produto>=0:
                    while True:
                        try:
                            preco=float(input('\nDigite o novo preco do produto\n'))
                            Catalogo['Preco do jogo'][produto]=preco
                            print('\nPreco atualizado!!!\n')
                            break

                        except Exception:
                            print('o preco tem que ser um numero!!!')


                elif produto == -2:
                    break

                elif produto == -1:
                    self.catalogo()

                else:
                    print('indice do produto nao existe\n')
            except Exception:
                print('indice do produto nao existe\n')
        


#Criando a interface grafica da loja de jogos.
                
loja = Tk() #criando a tela principal da loja
loja.title('LOJA EPIC GAMES') #nome da loja
loja.geometry('800x800') #tamanho da tela
loja.configure(background = 'black') #cor de fundo
titulo_loja = Label(loja,text='LOJA EPIC GAMES',font='OpenSans 30',fg = 'blue').pack(padx=10,pady=10) #colocando o nome da loja.
caixa_texto1 =LabelFrame(loja,text='Usuários cadastrados',font='OpenSans 25',fg= 'blue',bg='black',bd=12) #Indicando os usuários cadastrados na loja.
caixa_texto1.pack(expand = 'yes', fill = 'both')
bt1= Button(caixa_texto1,text='Cliente',command=lambda:AbrirTelaCliente()).pack(padx=20,pady=20) #criando botao cliente centralizado e abrindo tela cliente
bt2= Button(caixa_texto1,text='Vendedor',command=lambda:AbrirTelaVendedor()).pack(padx=20,pady=20) #criando botao vendedor centralizado e abrindo tela vendedor
bt3= Button(caixa_texto1,text='Administrador',command=lambda:AbrirTelaAdm()).pack(padx=20,pady=20) #criando botao Administrador centralizado e abrindo tela adm


#Configuracao da tela cliente


def AbrirTelaCliente():
    tela_cliente = Toplevel(loja)
    tela_cliente.title('Acesso Cliente - LOJA EPIC GAMES')
    tela_cliente.geometry('800x800') #tamanho da tela
    Label(tela_cliente,text='Seja bem-vindo Cliente').pack()
    caixa_texto2 =LabelFrame(tela_cliente,text='Catálogo de Jogos',font='OpenSans 25',fg= 'blue',bg='black',bd=12)
    caixa_texto2.pack(expand = 'yes', fill = 'both')
    bt4= Button(caixa_texto2,text='Filtrar Jogos - Ordem Alfabética ou Gênero ou Preço',command=lambda:Visualizar_catalogoCliente()).pack(padx=20,pady=20)
    data_atual = datetime.now() #Verificando a data atual da compra
    data_atual = data_atual.strftime('%d/%m/%Y')
    print('Iniciando sua compra no dia',data_atual)




    
    
#Configuracao da tela vendedor

                         
def AbrirTelaVendedor():
    tela_vendedor = Toplevel(loja)
    tela_vendedor.title('Acesso Vendedor - LOJA EPIC GAMES')
    tela_vendedor.geometry('800x800') #tamanho da tela
    Label(tela_vendedor,text='Seja bem-vindo Vendedor').pack()
    caixa_texto6 =LabelFrame(tela_vendedor,text='Catálogo de Jogos',font='OpenSans 25',fg= 'blue',bg='black',bd=12)
    caixa_texto6.pack(expand = 'yes', fill = 'both')
    bt5= Button(caixa_texto6,text='Filtrar Jogos - Ordem Alfabética ou Gênero ou Preço',command=lambda:Visualizar_catalogoVendedor()).pack(padx=20,pady=20)
    data_atual = datetime.now() #Verificando a data atual da compra
    data_atual = data_atual.strftime('%d/%m/%Y')
    print('Iniciando sua compra no dia',data_atual)

    

#Configuracao da tela adm

def vendas_faturamento_dia():
    valores=[100,200,300,500,600,1000,400]
    dias=['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']
    matplotlib.pyplot.plot(dias,valores)
    matplotlib.pyplot.title("Vendas por dia")  
    matplotlib.pyplot.xlabel("Dias")  
    matplotlib.pyplot.ylabel("Valores em R$")
    matplotlib.pyplot.plot(dias, valores, color ="green")  
    matplotlib.pyplot.show()

def vendas_genero():
    genero = ['Açao','Horror','Estrategia','RPG']
    vendas = [100, 60, 150, 100]
    matplotlib.pyplot.plot(genero, vendas)
    matplotlib.pyplot.ylim(50, 200)
    matplotlib.pyplot.title('Vendas por Categoria de Produtos')
    matplotlib.pyplot.xlabel('Gênero dos Jogos')
    matplotlib.pyplot.ylabel('Número de Vendas')
    matplotlib.pyplot.plot(genero, vendas, color ="red")  
    matplotlib.pyplot.show()


def media_vendas_semana():
    valores_segunda=[100,200,300,500]
    valores_terca=[200,250,500,100]
    valores_quarta=[500,300,200,150]
    valores_quinta=[250,350,400,100]
    valores_sexta=[600,400,100,50]
    valores_sabado=[350,100,200,150]
    valores_domingo=[200,500,350,100]
    media_segunda=np.average(valores_segunda)
    media_terca=np.average(valores_terca)
    media_quarta=np.average(valores_quarta)
    media_quinta=np.average(valores_quinta)
    media_sexta=np.average(valores_sexta)
    media_sabado=np.average(valores_sabado)
    media_domingo=np.average(valores_domingo)
    dias=['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']
    valores=[media_segunda,media_terca,media_quarta,media_quinta,media_sexta,media_sabado,media_domingo]
    desvio_padrao_segunda=np.std(valores_segunda)
    desvio_padrao_terca=np.std(valores_terca)
    desvio_padrao_quarta=np.std(valores_quarta)
    desvio_padrao_quinta=np.std(valores_quinta)
    desvio_padrao_sexta=np.std(valores_sexta)
    desvio_padrao_sabado=np.std(valores_sabado)
    desvio_padrao_domingo=np.std(valores_domingo)
    desvio_padrao=[desvio_padrao_segunda,desvio_padrao_terca,desvio_padrao_quarta,desvio_padrao_quinta,desvio_padrao_sexta,desvio_padrao_sabado,desvio_padrao_domingo]
    matplotlib.pyplot.title("Média e desvio padrão de vendas")
    matplotlib.pyplot.bar(dias,valores,color='pink')
    matplotlib.pyplot.plot(desvio_padrao,color='black')
    matplotlib.pyplot.xlabel("Dia da semana")  
    matplotlib.pyplot.ylabel("Valores em R$")
    matplotlib.pyplot.show()
    
 
    

def AbrirTelaAdm():
    tela_adm = Toplevel(loja)
    tela_adm.title('Acesso Administrador - LOJA EPIC GAMES')
    tela_adm.geometry('800x800') #tamanho da tela
    Label(tela_adm,text='Seja bem-vindo Administrador').pack()
    caixa_texto7 =LabelFrame(tela_adm,text='Catálogo de Jogos',font='OpenSans 25',fg= 'blue',bg='black',bd=12)
    caixa_texto7.pack(expand = 'yes', fill = 'both')
    bt6= Button(caixa_texto7,text='Filtrar Jogos - Ordem Alfabética ou Gênero ou Preço',command=lambda:Visualizar_catalogoVendedor()).pack(padx=20,pady=20)
    bt7= Button(caixa_texto7,text='Gráfico de Vendas e Faturamento',command=lambda:vendas_faturamento_dia()).pack(padx=20,pady=20)
    bt8= Button(caixa_texto7,text='Gráfico de Vendas por Categoria',command=lambda:vendas_genero()).pack(padx=20,pady=20)
    bt9= Button(caixa_texto7,text='Média e desvio padrão de vendas por dia da semana',command=lambda:media_vendas_semana()).pack(padx=20,pady=20)
    

    
#loja.mainloop() 


# FIM DO PROGRAMA


