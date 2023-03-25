
# Projeto de API DataTarget
Este código é uma aplicação Flask que implementa algumas rotas que permitem a criação, listagem e autenticação de usuários, bem como a busca de previsões do tempo com base em um determinado CEP. O código também utiliza uma instância Elasticsearch para registrar logs de todas as solicitações recebidas.




## Tecnologias

- Docker
- MongoDB
- ElasticSeacrh
- Flask


## Iniciar aplicação

Clone o proejto

```bash
  git clone https://github.com/jloiola6/teste_datatarget.git
```

Acesse o diretório do proejto

```bash
  cd teste_datatarget
```

Construa o Container

```bash
  docker-compose build
```

Inicie o nosso container

```bash
  docker-compose up
```


**Nota**: Espere em torno de um minuto após iniciar a aplicação pois o elasticsearch ainda estará iniciando.

