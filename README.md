# Sistema de Controle de Cadastros

Aplicação desktop em Python com interface gráfica e banco de dados MySQL para cadastrar, consultar e gerenciar informações.

## Funcionalidades
- Cadastro de registros com validação dos campos
- Consulta e listagem das informações salvas no banco
- Gerenciamento dos dados [edição / exclusão, se o seu sistema tiver]

## Tecnologias
Python · PySide6 · MySQL · SQL

## Como executar
1. Clone o repositório
   ```bash
   git clone https://github.com/SEU-USUARIO/sistema-controle-cadastros.git
   cd sistema-controle-cadastros
   ```
2. Instale as dependências
   ```bash
   pip install PySide6 [driver MySQL que você usa, ex.: mysql-connector-python]
   ```
3. Execute o script SQL em `/database` para criar o banco e as tabelas
4. Copie `config.example.py` para `config.py` e preencha com os dados de conexão do seu MySQL
5. Rode a aplicação
   ```bash
   python main.py
   ```

## Aprendizados
- Integração entre aplicação Python e banco de dados MySQL
- Construção de interface gráfica com PySide6
- Modelagem de tabelas e operações de cadastro e consulta (CRUD)
- Organização de um projeto e versionamento com Git/GitHub

## Autor
Eduardo Nunes dos S. Silva · [LinkedIn](https://www.linkedin.com/in/eduardo-nunes-dos-s-silva-18a321230) · [Portfólio](https://portfolio-eduardonunes.netlify.app)
