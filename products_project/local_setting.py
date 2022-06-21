# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vv3zkg%vo$qn8xtsh@e#j2s#n56!g@+#!pf@v)xq&e5w*6cq9c'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD' : 'password'
    }
}