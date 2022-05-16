
from platform import python_build
from django.contrib import admin
from django.urls import path
from blog.views import frontpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",frontpage) #veiws.pyにいく
]




