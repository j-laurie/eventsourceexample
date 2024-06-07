"""
URL configuration for eventsourcing project.

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
from django.contrib import admin
from django.urls import path
from features.views import add_block, remove_block, view_feature, change_status, read_feature

urlpatterns = [
    path("admin/", admin.site.urls),
    path("remove/<int:block_id>", remove_block),
    path("add/<int:block_id>", add_block),
    path("feature", view_feature),
    path("changestatus/<str:new_status>", change_status),
    path("readfeature", read_feature)
] 
