# Rastreador de localização

Projeto de estudo: um rastreador de localização em tempo real, com API em Python e um mapa que mostra a posição se movendo. A ideia é compartilhar a localização entre pessoas que concordam em se ver, usando apenas ferramentas gratuitas e rodando no meu próprio servidor.

> **Status:** em desenvolvimento. A Fase 1 (API, simulador e mapa) está pronta. Por enquanto o projeto usa apenas **dados simulados**, e a API ainda **não tem autenticação**. Não use com localização real nem exponha o servidor à internet.

## O que já funciona

- API com duas rotas: enviar a posição de um usuário e consultar a última posição.
- Validação dos dados (latitude entre -90 e 90, longitude entre -180 e 180).
- Banco SQLite que guarda apenas a última posição de cada usuário, sem histórico.
- Simulador que finge ser um celular andando e envia posições periodicamente.
- Página com mapa (Leaflet + OpenStreetMap) que consulta a API a cada 2 segundos e move o marcador.
- Documentação automática da API em `/docs`.

## Tecnologias

- Python 3 e [FastAPI](https://fastapi.tiangolo.com/)
- SQLite
- [Leaflet](https://leafletjs.com/) e [OpenStreetMap](https://www.openstreetmap.org/)
- HTML e JavaScript

## Como rodar

Pré-requisitos: Python 3 e Git, em Linux.

```bash
git clone https://github.com/jamsantoss/rastreador-localizacao.git
cd rastreador-localizacao
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Ligue o servidor:

```bash
uvicorn main:app --reload
```

Abra o mapa em `http://127.0.0.1:8000/` e a documentação da API em `http://127.0.0.1:8000/docs`.

Em outro terminal, com o ambiente virtual ativo, rode o simulador para o marcador andar:

```bash
python simulador.py
```

## Rotas da API

| Método | Rota | Descrição |
|---|---|---|
| POST | `/posicao` | Recebe `usuario`, `latitude` e `longitude` e grava a posição |
| GET | `/posicao/{usuario}` | Devolve a última posição do usuário |
| GET | `/` | Entrega a página com o mapa |

## Estrutura do projeto

```
rastreador-localizacao/
├── main.py            # API (FastAPI)
├── simulador.py       # Simula um celular enviando posições
├── index.html         # Página com o mapa
├── requirements.txt   # Dependências
└── .gitignore
```

## Próximos passos

- [ ] Usar o GPS real do celular, via navegador, com HTTPS
- [ ] Autenticação com token e dois usuários
- [ ] Botão para pausar o compartilhamento
- [ ] Atualização instantânea com WebSocket
- [ ] Aplicativo Android nativo, funcionando com a tela bloqueada

## Privacidade

O projeto foi pensado para uso entre pessoas que consentem em compartilhar a localização. O banco guarda só a última posição de cada usuário, e o arquivo `.db` fica fora do repositório.

## Autor

Jamilson Santos

[GitHub](https://github.com/jamsantoss) · 
[LinkedIn](https://www.linkedin.com/in/jamilson-santos-335a43155)
