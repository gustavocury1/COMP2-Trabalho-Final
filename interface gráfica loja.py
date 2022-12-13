from tkinter import *
from tkinter import Tk, mainloop, LEFT, TOP, NW,END,CENTER
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  


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


#configuracao da tela cliente

def AbrirTelaCliente():
    tela_cliente = Toplevel(loja)
    tela_cliente.title('Acesso Cliente - LOJA EPIC GAMES')
    tela_cliente.geometry('800x800') #tamanho da tela
    Label(tela_cliente,text='Seja bem-vindo Cliente').pack()
    caixa_texto2 =LabelFrame(tela_cliente,text='Catálogo de Jogos',font='OpenSans 25',fg= 'blue',bg='black',bd=12)
    caixa_texto2.pack(expand = 'yes', fill = 'both')
    bt4= Button(caixa_texto2,text='Filtrar Jogos - Ordem Alfabética',command=lambda:Visualizar_catalogoCliente()).pack(padx=20,pady=20)
    bt5= Button(caixa_texto2,text='Filtrar Jogos - Gênero',command=lambda:Visualizar_catalogoCliente()).pack(padx=20,pady=20)
    bt6= Button(caixa_texto2,text='Filtrar Jogos - Preço',command=lambda:Visualizar_catalogoCliente()).pack(padx=20,pady=20)
    #scrollbar=Scrollbar(caixa_texto2)  #criando barra de rolagem no catalogo de jogos.
    #scrollbar.pack(side = RIGHT, fill = Y)
    #lb1 = Listbox(caixa_texto2, yscrollcommand = scrollbar.set) #adicionando a barra de rolagem no catalogo de jogos.
    #lb1.pack(fill=BOTH, expand=1)
    #scrollbar.config(command=lb1.yview)
    tree=ttk.Treeview(caixa_texto2,selectmode='browse',column=('col1','col2','col3'),show='headings').pack() #criando uma treeview
    tree.column('col1',width=300,minwidth=50)
    tree.heading(text='Nome do Jogo')
    tree.column('col2',width=200,minwidth=50)
    tree.heading(text='Genero')
    tree.column('col3',width=100,minwidth=50)
    tree.heading(text='Preço')
    
    


    #for i in range(catalogo_jogos):
        #lista_jogos.insert("",END,values=(catalogo_jogos.iloc[i][0],catalogo_jogos.iloc[i][1],catalogo_jogos.iloc[i][2]))
                             
      # Adicionando um elemento à listbox
    #def Catalogo_to_list(self,Catalogo):
        #self.tree["columns"] = Catalogo.columns.values.tolist()
        #for x in range(len(Catalogo.columns.values)):
            #self.tree.column(Catalogo.columns.values[x], width=100)
            #self.tree.heading(Catalogo.columns.values[x], text=Catalogo.columns.values[x], command=self.populate_selection)
        #for index, row in Catalogo.iterrows():
            #self.tree.insert("",0,text=index,values=list(row))
        #self.tree.grid(row=50,column=0,rowspan=1,columnspan=12,sticky=N+E+W+S)
        #self.tree.bind("<<TreeviewSelect>>", self.populate_selection)
    

    
    
#tela vendedor
                         
def AbrirTelaVendedor():
    tela_vendedor = Toplevel(loja)
    tela_vendedor.title('Acesso Vendedor - LOJA EPIC GAMES')
    tela_vendedor.geometry('800x800') #tamanho da tela
    Label(tela_vendedor,text='Seja bem-vindo Vendedor').pack()
    caixa_texto6 =LabelFrame(tela_vendedor,text='Catálogo de Jogos',font='OpenSans 25',fg= 'blue',bg='black',bd=12)
    caixa_texto6.pack(expand = 'yes', fill = 'both')
    bt7= Button(caixa_texto6,text='Filtrar Jogos - Ordem Alfabética',command=lambda:Visualizar_catalogoVendedor()).pack(padx=20,pady=20)
    bt8= Button(caixa_texto6,text='Filtrar Jogos - Gênero',command=lambda:Visualizar_catalogoVendedor()).pack(padx=20,pady=20)
    bt9= Button(caixa_texto6,text='Filtrar Jogos - Preço',command=lambda:Visualizar_catalogoVendedor()).pack(padx=20,pady=20)
    
    
    #self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
    #self.titulo["font"] = ("Arial", "10", "bold")
    #self.titulo.pack()
    #self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
    #self.nomeLabel.pack(side=LEFT)
    #self.nome = Entry(self.segundoContainer)
    #self.nome["width"] = 30
    #self.nome["font"] = self.fontePadrao
    #self.nome.pack(side=LEFT)
    #self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
    #self.senhaLabel.pack(side=LEFT)
    #self.senha = Entry(self.terceiroContainer)
    #self.senha["width"] = 30
    #self.senha["font"] = self.fontePadrao
    #self.senha["show"] = "*"
    #self.senha.pack(side=LEFT)
    #self.autenticar = Button(self.quartoContainer)
        #self.autenticar["text"] = "Autenticar"
        #self.autenticar["font"] = ("Calibri", "8")
        #self.autenticar["width"] = 12
        #self.autenticar["command"] = self.verificaSenha
        #self.autenticar.pack()

        #self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        #self.mensagem.pack()

#Método verificar senha
#def verificaSenha(self):
        #usuario = self.nome.get()
        #senha = self.senha.get()
        #if usuario == "usuariodevmedia" and senha == "dev":
            #self.mensagem["text"] = "Autenticado"
        #else:


            #self.mensagem["text"] = "Erro na autenticação"

#tela adm

def AbrirTelaAdm():
    tela_adm = Toplevel(loja)
    tela_adm.title('Acesso Administrador - LOJA EPIC GAMES')
    tela_adm.geometry('800x800') #tamanho da tela
    Label(tela_adm,text='Seja bem-vindo Administrador').pack()
    caixa_texto7 =LabelFrame(tela_adm,text='Catálogo de Jogos',font='OpenSans 25',fg= 'blue',bg='black',bd=12)
    caixa_texto7.pack(expand = 'yes', fill = 'both')
    bt10= Button(caixa_texto7,text='Filtrar Jogos - Ordem Alfabética',command=lambda:Visualizar_catalogoVendedor()).pack(padx=20,pady=20)
    bt11= Button(caixa_texto7,text='Filtrar Jogos - Gênero',command=lambda:Visualizar_catalogoVendedor()).pack(padx=20,pady=20)
    bt12= Button(caixa_texto7,text='Filtrar Jogos - Preço',command=lambda:Visualizar_catalogoVendedor()).pack(padx=20,pady=20)
    
    


 #self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
    #self.titulo["font"] = ("Arial", "10", "bold")
    #self.titulo.pack()
    #self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
    #self.nomeLabel.pack(side=LEFT)
    #self.nome = Entry(self.segundoContainer)
    #self.nome["width"] = 30
    #self.nome["font"] = self.fontePadrao
    #self.nome.pack(side=LEFT)
    #self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
    #self.senhaLabel.pack(side=LEFT)
    #self.senha = Entry(self.terceiroContainer)
    #self.senha["width"] = 30
    #self.senha["font"] = self.fontePadrao
    #self.senha["show"] = "*"
    #self.senha.pack(side=LEFT)
    #self.autenticar = Button(self.quartoContainer)
        #self.autenticar["text"] = "Autenticar"
        #self.autenticar["font"] = ("Calibri", "8")
        #self.autenticar["width"] = 12
        #self.autenticar["command"] = self.verificaSenha
        #self.autenticar.pack()

        #self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        #self.mensagem.pack()

#Método verificar senha
#def verificaSenha(self):
        #usuario = self.nome.get()
        #senha = self.senha.get()
        #if usuario == "usuariodevmedia" and senha == "dev":
            #self.mensagem["text"] = "Autenticado"
        #else:
            #self.mensagem["text"] = "Erro na autenticação"














loja.mainloop()
