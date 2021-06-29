# Eventex

___
[![Build Status](https://travis-ci.com/ZandorSabino/eventex.svg?branch=master)](https://travis-ci.com/ZandorSabino/eventex) [![Coverage Status](https://coveralls.io/repos/github/ZandorSabino/eventex/badge.svg?branch=master)](https://coveralls.io/github/ZandorSabino/eventex?branch=master)
___

Sistema desenvolvido no curso [Welcome To The Django](https://henriquebastos.net/produtos/welcome-to-the-django).

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com python 3.9
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes

```console

git clone https://github.com/ZandorSabino/eventex.git ~/<sua-pasta>/wttd
cd ~/<sua-pasta>/wttd
python -m venv .wttd
pip install --require-hashes -r requirements.txt
copy contrib/env-sample .env
pytest
```

## Como fazer o deploy?

1. Crie uma instancia no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5 .Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
set secret_key=python contrib/secret_gen.py
heroku config:set SECRET_KEY=%secret_key%
heroku config:set DEBUG=False
# configure o email
git push heroku master --force
```
