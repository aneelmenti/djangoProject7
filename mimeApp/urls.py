from django.contrib import admin
from django.urls import path
from .views import Htmlview,xmlview,excelview


urlpatterns = [
    path('admin/', admin.site.urls),
    path('html', Htmlview.as_view()),
    path('xml',xmlview.as_view()),
    path('excel', excelview.as_view())
]
