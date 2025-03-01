from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('user.urls')),
    path('', include('shop.urls')),
    path('', include('cart.urls')),
    path('', include('contact.urls')),
    path('', include('chackout.urls')),
    path('', include('testimonial.urls')),
    path('', include('shopdetail.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
