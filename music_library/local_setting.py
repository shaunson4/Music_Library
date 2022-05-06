# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e!3av#0v(bh^+ar=m-1n7b&bl51t5%gi!ju@mdu!5yx$y(9xn8'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_library_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}

