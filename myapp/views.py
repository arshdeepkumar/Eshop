from django.shortcuts import render, redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from .models.product import Product
from.models.customer import Customer
from django.contrib import messages 
from .models.category import Category
#from .templatetags import cart 


def index(request):
    if request.method=="POST":
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect("/")

    
    #products=Product.get_all_products()
    #return render(request,"index.html",{'products':products})
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)

def Signup(request):

    if request.method=="GET":
        return render(request,'signup.html')
    elif request.method=="POST":
        #return HttpResponse(request.POST)
        #postData=request.POST
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        password=request.POST.get("password")
        

        x=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
        
        
    

        #validation
        error_message=None

        if(not first_name):
            error_message="first name required"
        elif len(first_name)<=3:
            error_message="First name more than 4 character"
        
        elif(not last_name):
            error_message="last name required"
        elif len(last_name)<=3:
            error_message="Last name more than 4 character"
        
        elif(not phone):
            error_message="phone no required"
        elif len(phone) < 10:
            error_message="Phone no must be 10 character"


        elif(not password):
            error_message="password required"
        elif len(password)<=6:
            error_message="Password more than 6 character"

        elif x.isExists():
            error_message = 'Email Address Already Registered..'

        #saving
        if not error_message:
            print(first_name,last_name,phone,email,password)
            x=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
            x.password = make_password(x.password)
            x.save()

        
        else:
            data = {
                'error': error_message,
                
            }
            return render(request,"signup.html",data)
        return HttpResponse("success")
def Login(request):
    return_url=None

    if request.method=="GET":
        return_url=request.GET.get("return_url")
        return render(request,"login.html")
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        x = Customer.get_customer_by_email(email)
        error_message = None
        if x:
            flag = check_password(password, x.password)
            if flag:
                request.session['customer'] = x.id

                    
                if return_url:
                    return HttpResponseRedirect(return_url)
                else:
                    return_url = None
                    return redirect('/')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

            
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('/login')


def Cart(request):
    
    ids = list(request.session.get('cart').keys())
    products = Product.get_products_by_id(ids)
    print(products)
    return render(request ,'cart.html',{'products':products})


