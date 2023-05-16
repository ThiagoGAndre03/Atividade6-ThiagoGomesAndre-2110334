# Atividade6-ThiagoGomesAndre-2110334
Repositório criado para realização da Atividade 6 da matéria Projeto de Software - ENG4021
1) Configurar SECRET_KEY:
>python3
>import_secrets
>secrets.token_urlsafe(32)

2)Criar o app:
> python3 manage.py startapp appdoTG

3)Migrar módulos para página admin
>python3 manage.py makemigrations
>pithon3 manage.py migrate

4)Criar superuser
>python3 manage.py create superuser
Colocar usuário e senha de preferência
