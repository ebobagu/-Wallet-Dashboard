INSTALLED_APPS = [
    "rest_framework",
    "corsheaders",
    "api",  # Your API app
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True  # Allow frontend requests
