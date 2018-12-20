"""wishlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from items import views
from django.conf import settings
from django.conf.urls.static import static
from api.views import ItemListView, ItemDetailView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('items/list/', views.item_list, name='item-list'),
    path('items/detail/<int:item_id>/', views.item_detail, name='item-detail'),
    path('items/wishlist/', views.wishlist, name='wishlist' ),

    path('user/register/', views.user_register, name='user-register'),
    path('user/login/', views.user_login, name='user-login'),
    path('user/logout/', views.user_logout, name='user-logout'),

    path('items/<int:item_id>/favorite/', views.item_favorite, name='item-favorite'),

    path('list-api/', ItemListView.as_view(), name='list-api'),
    path('detail-api/<int:item_id>/', ItemDetailView.as_view(), name='detail-api'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)