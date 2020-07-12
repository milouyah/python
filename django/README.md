
# Django


## [Django Rest framework](https://www.django-rest-framework.org/)

### [Quick Start](https://www.django-rest-framework.org/tutorial/quickstart/)

### [ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/)

**Routers**  
```python
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students',views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

### [Mixins](https://www.django-rest-framework.org/api-guide/generic-views/#mixins)

ListModelMxin  
CreateModelMixin  
RetrieveModelMixin  
UpdateModelMixin  
DestoryModelMixin  

### [Pagenamtion](https://www.django-rest-framework.org/api-guide/pagination/)

```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
```

**Request**
```
GET https://api.example.org/accounts/?page=4
```

### [Authentication](https://www.django-rest-framework.org/api-guide/authentication/)

## [Django Rest Framework(Video)](https://subscription.packtpub.com/video/web_development/9781800207585)

```bash
python -m django --version
pip install django

# Djaong Rest Framework
pip install djangorestframework

# MySQL Clinet
pip insall mysqlclinet
```

## Create Project

```bash
django-admin start project fbvSerializer
python .\manage.py startapp fbvApp
```

## Check DB

```
create database studentdb;
use studentdb;
show tables;
select * from cbvApp_student;
insert into cbvApp_student values(1,'John',100);
insert into cbvApp_student values(2,'Bob',100);
```


## [Django 3 By Example - Third Edition](https://subscription.packtpub.com/book/web_development/9781838981952) 


## [Postman](https://www.postman.com/)