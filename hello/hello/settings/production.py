from .base import *

DEBUG = False

INSTALLED_APPS += (
                   # other apps for production
                   )
SECURE_SSL_REDIRECT = True

# We set the CORS to True at the beginning because we used Ionic Framework for mobile app, which is browser
# simulation and needs to redirect between origins.
'''
10-13 19:42:27.898 11311 11311 D SystemWebChromeClient: http://localhost/dashboard/tabs/tab1: Line 0 : Access to XMLHttpRequest at 'https://hg-ingress.mybluemix.net/api/v1/response' from origin 'http://localhost' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
'''
CORS_ALLOW_ALL_ORIGINS = False

# IBM app scan requirements:
SESSION_COOKIE_SAMESITE = 'Strict'

SESSION_COOKIE_SECURE = True

# python manage.py check --deploy warnings:
'''
WARNINGS:
?: (security.W004) You have not set a value for the SECURE_HSTS_SECONDS setting. If your entire site is served only over SSL, you may want to consider setting a value and enabling HTTP Strict Transport Security. Be sure to read the documentation first; enabling HSTS carelessly can cause serious, irreversible problems.
?: (security.W008) Your SECURE_SSL_REDIRECT setting is not set to True. Unless your site should be available over both SSL and non-SSL connections, you may want to either set this setting True or configure a load balancer or reverse-proxy server to redirect all connections to HTTPS.
?: (security.W016) You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE, but you have not set CSRF_COOKIE_SECURE to True. Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.
?: (security.W018) You should not have DEBUG set to True in deployment.
app.Handler: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the ApiConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
'''

CSRF_COOKIE_SECURE = True
