# API Rest de Transações
Este projeto é uma API Rest que gerência transações e efetua o cálculo estatístico de todas as transações realizadas no últimos 60 segundo por padrão, sendo possível usuário definir um valor diferente. Está API foi desenvolvida com Python e Flask

# Requisitos para executar esse projeto
Git: Para clonar o repositório.

Docker: Para executar o projeto em um container.

## Documentação da API

#### Inserir Transações

```http
    POST /transacao
    HEADERS
        Content-Type: application/json
    BODY
        {
            "valor" : float,
            "dataHora" : string, // ISO 8601 Exemplo: "2025-03-29T12:00:00.000-00:00"
        }
```

#### Deletar todas as Transações

```http
    DELETE /transacao
```

#### Calcular Estatísticas

```http
    GET /estatistica

    GET /estatistica?intervaloSegundos=120
        //Parâmetro intervaloSegundo é opcional o valor padrão é de 60 segundos
```