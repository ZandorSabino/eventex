# Eventex

Sistema de eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com python 3.9
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute od testes

```console
git clone git@github.com/ZandorSabino/eventex.git wttd
cd wttd
python -m venv .wttd
.wttd/bin/activate.bat
pip install -r requirements-dev.txt
copy contrib/env-sample .env
python manage.py test
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
heroku config:push
set secret_key=python contrib/secret_gen.py
heroku config:set SECRET_KEY=%secret_key%
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```
