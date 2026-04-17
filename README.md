# Portfolio

Portfolio pessoal em Django, pronto para deploy no Railway com WhiteNoise, Gunicorn e healthcheck.

## Deploy no Railway

O projeto usa:

- `Django 5.2.13`
- `Gunicorn`
- `WhiteNoise`
- `railway.json` com `startCommand`, `preDeployCommand` e `healthcheckPath`

### Variaveis obrigatorias

Configure estas variaveis no Railway antes do redeploy:

- `SECRET_KEY`
- `DEBUG=False`
- `ALLOWED_HOSTS=.railway.app,seu-dominio.com,healthcheck.railway.app`
- `CSRF_TRUSTED_ORIGINS=https://*.railway.app,https://seu-dominio.com`
- `EMAIL_HOST`
- `EMAIL_PORT`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `EMAIL_USE_TLS=True`
- `DEFAULT_FROM_EMAIL`

### Variaveis recomendadas

- `SECURE_SSL_REDIRECT=True`
- `SECURE_HSTS_SECONDS=31536000`
- `SECURE_HSTS_INCLUDE_SUBDOMAINS=True`
- `SECURE_HSTS_PRELOAD=True`

### Comandos usados no deploy

- pre-deploy: `python manage.py migrate && python manage.py collectstatic --noinput`
- start: `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --log-file -`

### Healthcheck

O endpoint de healthcheck responde em:

- `/health/`
