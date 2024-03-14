
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.login.urls', namespace='login')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('accounts/', include('django.contrib.auth.urls')),

]
