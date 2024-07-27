from django.urls import path
from .views import HomeView, chackout_view, ShopView, testimonial_view, cart_view, ContactView, shop_detail_view, ProductCreateView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('chackout/', chackout_view, name='chackout'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('testimonial/', testimonial_view, name='testimonial'),
    path('cart/', cart_view, name='cart'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('shop_detail/', shop_detail_view, name='shop_detail'),
    path('product/', ProductCreateView.as_view(), name='product'),
]
