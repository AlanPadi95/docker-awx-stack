DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "changeme",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "awx"
