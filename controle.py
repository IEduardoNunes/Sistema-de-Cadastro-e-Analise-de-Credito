#Importando recursos
from PySide6.QtWidgets import QApplication, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
import mysql.connector #importante instalar o driver de comunicação via cmd antes com o comando "pip install mysql-connector-python".

conexao = mysql.connector.connect( #Desse jeito nós realizamos a conexão do python com o mysql
    host = '127.0.0.1', #informando o número IP da máquina local
    user = 'dev', #Informando o usuário criado no mysql
    password = '123456', #Informando a senha cadastrada para o usuário
    database = 'credito' #Informando qual será o banco de dados utilizado para conexão
)

def inserir_dados(): #Função necessária para puxarmos os dados inseridos em cada campo de texto criado e adiciona-los em variaveis criadas.
    nome = cadastro.txtNome.text()
    cpf = cadastro.txtCpf.text()
    idade = cadastro.txtIdade.text()
    renda = cadastro.txtRenda.text()
    situacao = cadastro.txtSituacao.text()
    
    cursor = conexao.cursor() #Esse comando é necessário pois é ele que pega a conexão com o banco de dados e realiza a leitura dos itens criados.
    comando_SQL = 'insert into cadastros (nome, cpf, idade, renda, situacao) values (%s,%s,%s,%s,%s)' #Dessa forma nós iremos adicionar na tabela 'cadastros' os valores adicionados nas variaveis
    dados = (str(nome), str(cpf), str(idade), str(renda), str(situacao)) #Aqui nós estamos salvando todos os valores inseridos dentro da váriavel 'dados'
    cursor.execute(comando_SQL, dados) #Dessa forma, iremos executar o comando do insert into dentro do banco de dados junto com os dados inseridos dentro da váriavel 'dados.
    
    conexao.commit() #Necessário para estabelecermos a conexão passando os valores
    
    cadastro.txtNome.setText('')#Isso fará com que quando o botão salvar for clicado, todos os campos já digitados sejam apagados, impossibilitando de o usuário adicionar as mesmas informações por engano.
    cadastro.txtCpf.setText('')
    cadastro.txtIdade.setText('')
    cadastro.txtRenda.setText('')
    cadastro.txtSituacao.setText('')
    
    cadastro.lblAnalise.setText('Clique no botão "Analisar Crédito"') #Quando o botão 'salvar' for clicado, o 'lblAnalise' irá setar o texto definido, dando uma infomração para o usuário.

def analise():
    
    renda = cadastro.txtRenda.text()
    renda = float(renda)
    idade = cadastro.txtIdade.text()
    idade = int(idade) #Dessa forma, realizamos a conversão dos valores adicionados em string para seus respectivos tipos de variáveis.
    
    if renda >= 3500 and idade >= 21: #Dessa forma, estaremos verificando se o usuário tem o que é necessário para ser pré aaprovado no crédito
        cadastro.lblAnalise.setText('Cadastro pré-aprovado para crédito.') #Caso sim, ele ira setar o 'lblAnalise' com a informação descrita
    else: 
        cadastro.lblAnalise.setText('Cadastro não foi aprovado para crédito.') #Caso não, setara com a informação descrita
        
def relatorio():
    relatorio.show() #Abrindo a tela de relatório quando a função 'relatorio' for iniciada
    
    cursor = conexao.cursor() #Iniciando a conexão com o banco de dados
    comando_SQL = 'select * from cadastros' #Aplicando o comando SELECT do MySQL para realizar a leitura de todos os dados dentro da tabela cadastros
    cursor.execute(comando_SQL) #Executando o comando digitado acima
    leitura_cadastros = cursor.fetchall() #Aplicando os dados lidos dentro da variável 'leitura_cadastros'
    
    relatorio.tableCadastros.setRowCount(len(leitura_cadastros)) #Isso irá informar para a minha tabela na interface gráfica quantar linhas tem na tabela do banco de dados (Informação puxada pela variável "leitura_cadastros")
    relatorio.tableCadastros.setColumnCount(6) #Isso irá informar quantas colunas tem na minha tabela do banco de dados.
    
    for i in range(0, len(leitura_cadastros)): #Com essr for, nós iremos pegar o dado da i e da coluna j e armazená-lo dentro de 'tableCadastros'. Dessa forma, quando o usuário abrir a tela 'relatorios' ele irá verificar todos os dados salvos dentro do banco de dados 'cadastros'.
        for j in range(0, 6):
            relatorio.tableCadastros.setItem(i,j, QTableWidgetItem(str(leitura_cadastros[i][j])))
    
    
    cursor.commit()

id_geral = 0 #Criando uma variável global para armazenar qual a ID de usuário sendo utilizada no momento e poder utilizá-la em qualquer outra função.
def editar_dados(): #Criando a função de edição dos dados da database
    global id_geral #Declarando a ID global para ser utilizada dentro de uma função.
    dados = relatorio.tableCadastros.currentRow() #Irá retornar para 'dados' a linha atualmente selecionada pelo usuário
    cursor = conexao.cursor() #Iniciando a conexão com o banco de dados
    cursor.execute("select id from cadastros") #Aqui eu estou buscando todos os 'ids' de 'cadastros'
    leitura_cadastros = cursor.fetchall() #Aqui eu estou pegando essas 'ids' selecionadas anteriormente e armazenando-as dentro de 'leitura_cadastros'
    id_ativo = leitura_cadastros[dados][0] #Esse comando irá pegar a linha que o usuário selecionou (que está armazenada em 'dados') e irá retornar o indíce '0' dela (que no caso da tabela 'cadastros', seria o 'ID' da linha selecionada pelo usuário)
    cursor.execute("select * from cadastros where id="+str(id_ativo)) #Irá buscar em todos os registros e selecionar o id que seja igual ao id selecionado no código anterior.
    leitura_cadastros = cursor.fetchall() #Irá armazenar esses dados desse ID específico e armazenando-os dentro de leitura_cadastros. (Agora eu selecionei todos os dados da linha selecionada pelo usuário desde o início)
    
    editar.show()
    
    id_geral = id_ativo
    
    editar.txtAlterarId.setText(str(leitura_cadastros[0][0]))
    editar.txtAlterarNome.setText(str(leitura_cadastros[0][1]))
    editar.txtAlterarCpf.setText(str(leitura_cadastros[0][2]))
    editar.txtAlterarIdade.setText(str(leitura_cadastros[0][3]))
    editar.txtAlterarRenda.setText(str(leitura_cadastros[0][4]))
    editar.txtAlterarSituacao.setText(str(leitura_cadastros[0][5])) #Essas linhas de código realizam a edição das caixas de texto dentro da tela 'Editar', fazendo com que elas recebam o dado da coluna específica clicada pelo usuário.

def alteracao_dados():
    global id_geral #Declarando uma  variável global para ser utilizada dentro de uma função
    
    id = editar.txtAlterarId.text()
    nome = editar.txtAlterarNome.text()
    cpf = editar.txtAlterarCpf.text()
    idade = editar.txtAlterarIdade.text()
    renda = editar.txtAlterarRenda.text()
    situacao = editar.txtAlterarSituacao.text() #Linhas utilizadas para armazenar os novos dados digitados para alteração
    
    cursor = conexao.cursor() #Realizando uma conexão com o banco de dados cadastrado no início do código.
    cursor.execute("update cadastros set id='{}',nome='{}',cpf='{}',idade='{}',renda='{}',situacao='{}' where id={}"
                   .format(id,nome,cpf,idade,renda,situacao,id_geral))#Comando SQL utilizado para receber os dados editados e alterá-los dentro do banco de dados.
    
    conexao.commit() #Realizando a inspeção e inserção dos dados dentro do banco de dados.
    
    editar.close()
    relatorio.close()
    cadastro.show() #Essas 3 linhas realizaram um 'refresh' após o uusuário salvar as edições. Fechando a tela de editar/relatorio e abrindo a tela de cadastro novamente.


def excluir_dados():
    excluir = relatorio.tableCadastros.currentRow() #Irá selecionar a linha clicada pelo usuário
    relatorio.tableCadastros.removeRow(excluir) #Irá remover a linha clicada pelo usuário dentro da interface gráfica
    
    cursor = conexao.cursor() #Iniciando a conexão com a database
    cursor.execute('select id from cadastros') #Selecionando os ids de cadastros
    leitura_cadastros = cursor.fetchall() #Recebendo todos os dados armazenados no cursor
    id_ativo = leitura_cadastros[excluir][0] #Irá armazenar a linha selecionada dentro de id_ativo e irá armazenar o ID da linha (índice 0) dentro de id_ativo
    cursor.execute('delete from cadastros where id='+str(id_ativo)) #Irá remolver do banco de dados onde o ID for igual ao id_ativo
    conexao.commit() #Realizando a inspeção e inserção dos dados.


app = QApplication([])

loader = QUiLoader()

arquivo = QFile("Cadastros.ui") #Aqui informamos qual arquivo será aberto pelo python.
arquivo.open(QIODevice.ReadOnly)

cadastro = loader.load(arquivo)
cadastro.btnSalvar.clicked.connect(inserir_dados) #Dessa forma, quando clicarmos no botao inserido na interface gráfica, ele irá acionar a função para adicionar os dados dentro do banco de dados.
cadastro.btnAnalise.clicked.connect(analise) #Adicionando uma ação no botão 'btnAnalise'
cadastro.btnRelatorio.clicked.connect(relatorio)

arquivo2 = QFile("Relatorio.ui")
arquivo2.open(QIODevice.ReadOnly)
relatorio = loader.load(arquivo2) #Essas 3 linhas definem qual arquivo será aberto quando o botão 'btnRelatorio' for clicado.
relatorio.btnSalvar.clicked.connect(editar_dados) #Botão 'Editar' dentro do relatório (Necessário ser criado após a linha "relatorio = loader.load(arquivo2)" ter sido escrita, senão o sistema dará erro).
relatorio.btnExcluir.clicked.connect(excluir_dados)

arquivo3 = QFile("Editar.ui")
arquivo3.open(QIODevice.ReadOnly)
editar = loader.load(arquivo3)#Essas 3 linhas definem qual arquivo será aberto quando o botão 'btnSalvar' for clicado.
editar.btnAlterar.clicked.connect(alteracao_dados) #Botão dentro da tela 'Editar' utilizado para atualizar os dados do banco de dados.



arquivo.close()
arquivo2.close()
arquivo3.close()

cadastro.show()

app.exec()
'''O código acima puxa os recursos de inicialização da 
Criada com o pyside6 e executa o arquivo, fazendo a
interface gráfica ser aberta na tela do usuário'''

