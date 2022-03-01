from django.urls import path, include, re_path
from django.contrib import admin


admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('hello/', hello.views.say_hello),
    path('johnathan/', hello.views.johnathan),
    path('ricky/', hello.views.ricky),
    path('april/', hello.views.april),
    path('danica/', hello.views.danica),
    path('numpy/', hello.views.matrix)
]
