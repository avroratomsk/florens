INSTALLED_APPS = [
    # "django.contrib.admin",
    "admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # "debug_toolbar",
    # "corsheaders",
    'sorl.thumbnail',
    "home",
    "shop",
    "users",
    "reviews",
    "service",
    "cart",
    "order",
    "payment",
    'django_ckeditor_5',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    # "corsheaders.middleware.CorsMiddleware",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'avroraweb_floren',
        'USER': 'avroraweb_floren',
        'PASSWORD': 'b*29QFWu',
        'HOST': 'localhost',
    }
}
