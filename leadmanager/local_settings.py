# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y!gnk_3b)x40ey)7@s*1&c_5d&#fku(4k_60@sc-+!_8@pz_qp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'leadmanager',#database name, posihdun
        'USER': 'postgres',#posihdunuser or owner
        'PASSWORD': 'Mrlube11!',#owners password, #Onionturtle101!
        'HOST':'localhost',
        'PORT': '5432',
    }
}
