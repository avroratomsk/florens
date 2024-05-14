DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "florens",
        "USER": "florens",
        "PASSWORD": "1111",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

INSTALLED_APPS = [
    # "django.contrib.admin",
    "admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'ckeditor',
    'ckeditor_uploader',
    'allauth',
    'allauth.account',
    "debug_toolbar",
    "corsheaders",
    'sorl.thumbnail',
    "home",
    "shop",
    "coupons",
    "users",
    "reviews",
    "service",
    "cart",
    "order",
    "payment",
    'tinymce',
    # "blog",
    # "news",
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
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    'allauth.account.middleware.AccountMiddleware',
]