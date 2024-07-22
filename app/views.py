from django.shortcuts import render
from shop.models import Shop, Category, Nav_Category, Meat, Bread, Fruits, Vegetables, All_products
from django.contrib.auth.decorators import login_required


def home_view(request):
    mans_product = All_products.objects.all()
    vegetable = Vegetables.objects.all()
    fruit = Fruits.objects.all()
    bread = Bread.objects.all()
    nav_category = Nav_Category.objects.all()
    meat = Meat.objects.all()
    all_product = Shop.objects.all()
    context = {'all_product': all_product,
               'nav_category': nav_category,
               'meat': meat,
               'bread': bread,
               'fruit': fruit,
               'vegetable': vegetable,
               'mans_product': mans_product

               }
    return render(request, 'index.html', context)


def contact_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Shop.objects.filter(title__icontains=search)
        return render(request, 'index.html', {'products': products})
    product = Shop.objects.all()
    category = Category.objects.all()
    cantext = {
        'products': product,
        'category': category
    }
    return render(request, 'contact.html', cantext)


def shop_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Shop.objects.filter(title__icontains=search)
        return render(request, 'shop.html', {'products': products})
    meat = Meat.objects.all
    all_shop = Shop.objects.all()
    categories = Category.objects.all()
    context = {'all_shop': all_shop, 'categories': categories, 'meat': meat}
    return render(request, 'shop.html', context)

    # meat = Meat.objects.all()
    # all_shop = Shop.objects.all()
    # categories = Category.objects.all()
    # context = {'all_shop': all_shop, 'categories': categories, 'meat': meat}
    # return render(request, 'shop.html', context)


def testimonial_view(request):
    return render(request, 'testimonial.html')


def chackout_view(request):
    return render(request, 'chackout.html')


def cart_view(request):
    return render(request, 'cart.html')

@login_required()
def shop_detail_view(request):
    return render(request, 'shop-detail.html')



