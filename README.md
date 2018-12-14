# Famae-Gr-10-Django-Api

## Lancer le projet
Prérequis: 
- avoir installé Django >= 2.1.4
- avoir installé Python 3

Lancer serveur de développement: 
` python manage.py runserver `

## Ajout d'une nouvelle route

Créer une nouvelle view (prendre le modèle views.py) dans le sous-dossier famaeGr10.
Spécifier la route dans urls.py

```
from famaeGr10.views import TestPage

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^zipcode/(?P<zip_code>\d+)/', TestPage.as_view()),
    url(r'^zipcode/', TestPage.as_view()),
]
```
