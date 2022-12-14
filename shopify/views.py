from turtle import home
from django.shortcuts import render
from .models import *
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import routers, serializers, viewsets
from .serailizers import UserSerializer

# Create your views here.


def index(request):

    if request.method == 'POST':
        product_id = request.POST.get('cartid')
        remove = request.POST.get('minus')
        cart_id = request.session.get('cart')

        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity - 1
                else:
                    cart_id[product_id] = quantity + 1
            else:
                cart_id[product_id] = 1
        else:
            cart_id = {}
            cart_id[product_id] = 1

        request.session['cart'] = cart_id
        print(request.session['cart'])

    cate = Category.objects.all()
    cat_id = request.GET.get('category_id')

    if cat_id:
        pro = Product.objects.filter(category=cat_id)
    else:
        pro = Product.objects.all()
    return render(request, 'home.html', {'cat': cate, 'pro': pro, })


def contact(request):
    return render(request, 'contact.html')


def price(request):
    return render(request, 'price.html')


def user_registration(request):
    if request.method == 'POST':
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        email = request.POST.get('emailid')
        password = request.POST.get('pwd')
        mobile = request.POST.get('mbl')
        gender = request.POST.get('gender')
        #qq = request.POST.get('q')

        info = Signup(
            first_name=f_name,
            last_name=l_name,
            email=email,
            password=make_password(password),
            mobile_no=mobile,
            gender=gender,
            # a=qq

        )
        info.save()

        return redirect('home')


def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pwd')

        try:
            fetch_info = Signup.objects.get(email=email)
            if check_password(password, fetch_info.password):
                request.session['name'] = fetch_info.first_name
                request.session['customer'] = fetch_info.id
                return redirect('home')
            else:
                return HttpResponse('enter a valid password')
        except:
            return HttpResponse('enter a valid email')


def Logout(request):
    request.session.clear()
    return redirect('home')


def Cart(request):
    cart_info = request.session['cart'].keys()
    cart_dtls = Product.objects.filter(id__in=cart_info)
    return render(request, 'cart.html', {'cart_dtls': cart_dtls})


def Checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        customer_id = request.session.get('customer')
        cart = request.session.get('cart')
        product = Product.objects.filter(id__in=list(cart.keys()))

        if not customer_id:
            return HttpResponse('please login')

        for pro in product:
            save_ord_dtls = Order(
                address=address,
                mobile_no=mobile,
                customer=Signup(id=customer_id),
                product=pro,
                quantity=cart.get(str(pro.id)),
                price=pro.price

            )
            save_ord_dtls.save()
        request.session['cart'] = {}
        return redirect('Order_dtls')


def Order_dtls(request):

    customer_id = request.session.get('customer')
    fetch_order = Order.objects.filter(customer=customer_id)
    tp = 0
    for i in fetch_order:
        tp = tp + (i.price*i.quantity)
    return render(request, 'order.html', {'fetch_order': fetch_order, 'tppp': tp})


# def myorder(request):
#     fetch_order = Order.objects.filter()
#     return render(request, 'myorder.html', {'fetch_order': fetch_order})


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = UserSerializer


def table(request):
    if request.method == 'POST':
        ff = request.POST.get('p')
        ll = request.POST.get('q')
        fv = request.POST.get('r')
        ag = request.POST.get('s')

        zz = Table(
            first=ff,
            last=ll,
            fav=fv,
            age=ag
        )
        zz.save()

        return redirect('home')


def tt(request):
    if request.method == 'POST':
        fstt = request.POST.get('fst')
        tbl = Table.objects.filter(first=fstt)
        if Table.objects.get(first=fstt):
            print(tbl.first)
        return render(request, 'contact.html', {'tbl': tbl})
        # try:
        #     fetch = Table.objects.get(first=fstt)
        #     if fetch:
        #         print(fetch.first)
        #     return render(request, 'contact.html')

        # except:
        #     return HttpResponse('enter a valid data')


# def buynow(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('cartid')

#         cart_id = request.session.get('cart')

#         if cart_id:
#             pass
#         else:
#             cart_id = {}
#             cart_id[product_id] = 1

#         request.session['cart'] = cart_id
#         print(request.session['cart'])

#     return render(request, 'cart.html')


def find(request):
    if request.method == 'POST':
        name = request.POST.get('search')
        # if name in
        fnd = Product.objects.filter(pro_name=name)
        if fnd:
            return render(request, 'search.html', {'fnd': fnd})
    return HttpResponse('result not found')
