# Tasks API

Este é um projeto de API RESTful para gerenciamento tarefas, desenvolvido em Python com FastAPI e SQLite. A API permite criar, ler, atualizar e deletar tarefas de forma simples e eficiente.

## Funcionalidades

- Listar todas as tarefas
- Obter uma tarefa específica pelo ID
- Adicionar uma nova tarefa
- Atualizar uma tarefa existente
- Deletar uma tarefa

## Tecnologias Utilizadas

- **Python:** Linguagem de programação.
- **FastAPI:** Framework para construir APIs de forma rápida e eficiente.
- **SQLite:** Banco de dados relacional leve utilizado para armazenar as tarefas.
- **Pydantic:** Biblioteca para validação de dados e criação de modelos.
- **Uvicorn:** Servidor ASGI para executar a aplicação FastAPI.

## Endpoints

### 1. Home

- **GET** `/`
  
  Retorna uma mensagem de boas-vindas.

### 2. Listar todas as tarefas

- **GET** `/tasks`
  
  Retorna uma lista de todas as tarefas.

### 3. Obter uma tarefa específica

- **GET** `/tasks/{id}`
  
  Retorna os detalhes de uma tarefa específica pelo ID.

### 4. Adicionar uma nova tarefa

- **POST** `/tasks`
  
  Adiciona uma nova tarefa. O corpo da requisição deve ser um JSON com o seguinte formato:

  ```json
  {
      "title": "Título da tarefa",
      "description": "Descrição da tarefa",
      "category": "Categoria da tarefa",
      "status": false
  }
  ```

### 5. Atualizar uma tarefa existente

- **PUT** `/tasks/{id}`
  
  Atualiza uma tarefa existente. O corpo da requisição deve ser um JSON com o mesmo formato do endpoint de adição.

### 6. Deletar uma tarefa

- **DELETE** `/tasks/{id}`
  
  Deleta uma tarefa específica pelo ID.

### Estrutura do Repositório

1. **`.json`**: 
   - Contém um modelo de tarefa em formato JSON, definindo a estrutura básica com campos como `title`, `description`, `category` e `status`.

2. **`actions.py`**: 
   - Contém funções para interagir com o banco de dados SQLite, incluindo inicialização do banco, leitura, adição, atualização e exclusão de tarefas. Utiliza logging para registrar operações.

3. **`app.py`**: 
   - Arquivo principal da aplicação FastAPI. Define as rotas da API, inicializa o banco de dados na inicialização da aplicação e implementa as operações CRUD (Create, Read, Update, Delete) para as tarefas.

4. **`local.db`**: 
   - Arquivo do banco de dados SQLite que armazena as tarefas. É criado automaticamente quando a aplicação é executada pela primeira vez.

5. **`models.py`**: 
   - Define os modelos de dados utilizando Pydantic. Inclui um modelo de tarefa (`Task`) e um modelo de consulta (`query_model`) para validação de dados.

6. **`requirements.txt`**: 
   - Lista as dependências do projeto, especificando as versões das bibliotecas necessárias para executar a aplicação, como FastAPI, Pydantic e Uvicorn.

## Instalação

Certifique-se de ter o Python 3.7 ou superior instalado em sua máquina.

1. Clone o repositório:

   ```bash
   git clone https://github.com/ianfelps/tasks_api.git
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Execução

Para executar a API, use o seguinte comando:

```bash
uvicorn app:app --reload
```

A API estará disponível localmente em `http://localhost:8000`.

### Conclusão

O repositório `tasks_api` fornece uma implementação básica de uma API RESTful para gerenciamento de tarefas, utilizando tecnologias modernas e práticas recomendadas para desenvolvimento de APIs. Cada arquivo tem um papel específico, contribuindo para a funcionalidade e a organização do projeto.
