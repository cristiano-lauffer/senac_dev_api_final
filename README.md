# senac_dev_api_final
Projeto final da cadeira Desenvolvimento de Serviços e APIs (ADS3N26-2)

# Instalação e execução em desenvolvimento

## Database (MySQL)
Executar scripts, em ordem, da pasta [_database](./_database).

## Criação do ambiente virtual (Windows)
Para execução em desenvolvimento, criar ambimente "venv enviroment" no Windows, conforme abaixo:

Abrir Powershel na pasta do projeto e rodar os comandos abaixo:

```powershell
python -m venv venv
 
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
 
.\venv\Scripts\Activate.ps1
 
# 4. Instale o Django e as dependências
pip install django djangorestframework mysqlclient django-cors-headers

```

## Executar a aplicação
Ainda na mesma janela aberta, para rodar a aplicação:

```powershell
python manage.py runserver
```

Se sair da janela, rodar novamente o comando abaixo, depois, o acima para subir a aplicação:

```powershell
.\venv\Scripts\Activate.ps1
```
## Consultando a api
Rodar utilizando o navegador:

[http://127.0.0.1:8000/api/despesas/](http://127.0.0.1:8000/api/despesas/)

