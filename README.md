# Tasks API

Este é um projeto de API para gerenciar tarefas, desenvolvido em Python com FastAPI e SQLite. A API permite criar, ler, atualizar e deletar tarefas de forma simples e eficiente.

## Funcionalidades

- Listar todas as tarefas
- Obter uma tarefa específica pelo ID
- Adicionar uma nova tarefa
- Atualizar uma tarefa existente
- Deletar uma tarefa

## Tecnologias Utilizadas

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

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