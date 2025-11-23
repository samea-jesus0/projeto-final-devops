# Projeto Final - DEVOPS

Este repositório contém uma API Flask simples criada como projeto final da disciplina de DevOps. A aplicação expõe alguns endpoints REST, um endpoint de login que retorna um token JWT, e uma interface Swagger para documentação da API.

**Stack:** Python 3.9, Flask, flask-jwt-extended, flask-swagger-ui

## Estrutura

- `app.py` - aplicação Flask principal
- `requirements.txt` - dependências Python
- `Dockerfile` - instruções para construir imagem Docker
- `test_app.py` - testes unitários
- `static/swagger.json` - especificações com o Swagger

## Endpoints principais

- `GET /` - retorna mensagem indicando que a API está rodando
- `GET /items` - retorna uma lista de itens (ex.: `item1`, `item2`, `item3`)
- `POST /login` - gera e retorna um `access_token` JWT 
- `GET /protected` - rota protegida por JWT; requer cabeçalho `Authorization: Bearer <token>`
- Swagger UI disponível em `/swagger` 

## Requisitos

- Python 3.9+
- Docker (opcional, para execução em container)

## Instalação e execução local

1. Instale as dependências:

	 ```powershell
	 pip install --upgrade pip
	 pip install -r requirements.txt
	 ```

2. Execute a aplicação:

	 ```powershell
	 python app.py
	 ```

	 A aplicação vai escutar em `http://0.0.0.0:1313` (acessível localmente via `http://localhost:1313`). O Swagger UI ficará em `http://localhost:1313/swagger`.

## Exemplos de uso (curl)

- Listar itens:

	```bash
	curl http://localhost:1313/items
	```

- Obter token (login):

	```bash
	curl -X POST http://localhost:1313/login
	```

- Acessar rota protegida (substitua `<TOKEN>` pelo token retornado):

	```bash
	curl -H "Authorization: Bearer <TOKEN>" http://localhost:1313/protected
	```

## Rodando com Docker

1. Build da imagem:

	 ```powershell
	 docker build -t projeto-devops:latest .
	 ```

2. Rodar o container:

	 ```powershell
	 docker run -p 1313:1313 projeto-devops:latest
	 ```

## Testes

O repositório inclui testes com `unittest` em `test_app.py`. Execute-os com:

```powershell
python -m unittest
pytest
```

## Integração contínua

O workflow de GitHub Actions está em `.github/workflows/validacao.yaml`. Ele realiza as etapas de build da imagem Docker, execução dos testes e, se tudo passar, aciona um hook de deploy, pois o Render está sendo usado, usando a variável de ambiente/segredo `RENDER_DEPLOY_HOOK`.

