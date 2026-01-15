# Dashboard de Gestão de Tarefas com Flask

## Descrição do Projeto
Este projeto consiste em uma aplicação web para gerenciamento de tarefas (To-Do List), desenvolvida com foco em organização e produtividade. A aplicação permite a criação, edição, conclusão e exclusão de tarefas, além da gestão dinâmica de categorias.

O objetivo principal deste projeto é demonstrar competências em desenvolvimento web utilizando Python, manipulação de bancos de dados relacionais e implementação de interfaces responsivas com frameworks front-end.

## Funcionalidades Principais
* Gerenciamento de Tarefas (CRUD): Criação, leitura, atualização e deleção de itens.
* Gestão de Categorias: Possibilidade de criar novas categorias personalizadas para organizar as atividades.
* Filtros Dinâmicos: Filtragem de tarefas por categoria e ordenação por data de criação ou ordem alfabética através de parâmetros na URL.
* Persistência de Dados: Uso de banco de dados para armazenamento permanente das informações através de relacionamentos entre tabelas.
* Interface Responsiva: Design adaptável para diferentes tamanhos de tela utilizando componentes modernos.

## Tecnologias Utilizadas

### Back-end
* Python: Linguagem de programação principal.
* Flask: Micro-framework para desenvolvimento das rotas e lógica do servidor.
* Flask-SQLAlchemy: ORM (Object Relational Mapper) para interação com o banco de dados via classes Python.
* SQLite: Banco de dados relacional leve utilizado para persistência local.

### Front-end
* Jinja2: Motor de templates para renderização dinâmica de conteúdo HTML.
* Bootstrap 5: Framework CSS para estilização, sistema de grid e componentes visuais (Modais).
* FontAwesome: Biblioteca de ícones para auxílio na navegação visual.

[Image of MVC architectural pattern diagram for web applications]

## Estrutura de Arquivos
* app.py: Arquivo principal contendo as rotas, modelos do banco de dados e lógica da aplicação.
* templates/: Diretório que armazena os arquivos HTML.
    * index.html: Página principal da aplicação com a lógica de interface.
* instance/: Diretório gerado automaticamente pelo Flask para armazenar o arquivo do banco de dados SQLite (tasks.db).

## Como Executar o Projeto

1. Pré-requisitos: Certifique-se de ter o Python instalado em sua máquina.
2. Instalação de Dependências:
   Execute o seguinte comando no terminal para instalar as bibliotecas necessárias:
   ```bash
   pip install flask flask-sqlalchemy
