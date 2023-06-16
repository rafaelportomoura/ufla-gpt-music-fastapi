# Projeto de Sistemas Distribuídos - Sugeridor de Músicas

Este projeto foi desenvolvido como parte da disciplina de Sistemas Distribuídos da Universidade Federal de Lavras. O objetivo projeto é criar um site que sugere 5 músicas com links para o YouTube a partir do texto inserido pelo usuário. O site também terá integração com o chatbot GPT para fornecer sugestões personalizadas com base nas conversas com o usuário.

## Tecnologias Utilizadas

- Python 3.11
- FastAPI
- Docker
- Docker Compose
- ChatGPT
- HTML
- CSS
- JavaScript

## Como Executar o Projeto

Para executar o projeto, siga os passos abaixo:

1. Clone o repositório o seu computador:

```bash
git clone https://github.com/rafaelportomoura/ufla-gpt-music-fastapi.git
```

2. Navegue até o diretório do projeto:

```bash
cd ufla-gpt-music-fastapi
```

3. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

```bash
CHATGPT_API_KEY=<sua-chave-api-do-chatgpt>
```

4. Execute o seguinte comando para construir e iniciar o contêiner Docker:

```bash
docker-compose up --build
```

5. Acesse o site em `http://localhost:8000`.

## Referências

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [ChatGPT Documentation](https://platform.openai.com/docs/guides/gpt)
