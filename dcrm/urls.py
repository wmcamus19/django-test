"""
URL configuration for dcrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf import global_settings
from django.conf.urls import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from leads.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('leads.urls', namespace='leads'), name='main'),
    # path('login/', LoginView.as_view(), name='login'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if global_settings.DEBUG:
    urlpatterns += (static(global_settings.STATIC_URL,
                    document_root=global_settings.STATIC_ROOT))
