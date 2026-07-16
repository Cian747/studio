# San Wan Visuals — Django Website

## Folder Structure

```
your_django_project/
├── sanwan/                        ← your app (python manage.py startapp sanwan)
│   ├── views.py                   ← copy from this package
│   ├── urls.py                    ← copy from this package
│   ├── templates/
│   │   └── sanwan/
│   │       ├── base.html
│   │       ├── home.html
│   │       └── contact.html
│   └── static/
│       ├── css/
│       │   └── main.css
│       └── js/
│           └── main.js
└── your_project/
    ├── settings.py
    └── urls.py
```

## Setup Steps

### 1. Create & activate virtual environment
```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install django pillow
```

### 2. Start a project & app (if not already done)
```bash
django-admin startproject config .
python manage.py startapp sanwan
```

### 3. settings.py — add these lines
```python
INSTALLED_APPS = [
    ...
    'sanwan',
]

# Static files
STATICFILES_DIRS = [BASE_DIR / "sanwan" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media (for photo uploads later)
MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Templates — make sure APP_DIRS is True or add the path:
TEMPLATES = [{
    ...
    'APP_DIRS': True,
    ...
}]
```

### 4. Project urls.py
```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sanwan.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 5. Run
```bash
python manage.py migrate
python manage.py runserver
```

---

## Pages included
| URL           | View       | Template               |
|---------------|------------|------------------------|
| `/`           | home       | sanwan/home.html       |
| `/services/`  | services   | sanwan/services.html   |
| `/pricing/`   | pricing    | sanwan/pricing.html    |
| `/gallery/`   | gallery    | sanwan/gallery.html    |
| `/contact/`   | contact    | sanwan/contact.html    |

## Next Steps
- Add a `Photo` model and wire it to the gallery
- Connect `send_mail()` in the contact view to actually send booking emails
- Add `django-storages` + S3 for photo delivery to clients
- Add an `admin.py` so you can manage packages/photos from `/admin`
