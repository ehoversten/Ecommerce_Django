from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from  .forms import createProduct, createColor

Pro = "product"  # short for Product App

User = get_user_model()


def product_landing(request):
    return render(request, Pro + '/product_landing.html')


def product_new(request):
    if request.method == 'POST':
        form = createProduct(request.POST, request.FILES)
        if form.is_valid():
            print(form)
    else:
        form = createProduct(prefix="product", label_suffix='')
        pForm = createProduct(prefix="color", label_suffix='')
        return render(request, Pro + '/product_new.html', {'form': form}, {'pForm': pForm})


def product_review(request):  # This should be merged with the product details.
    return render(request, Pro + '/product_review.html')


def editProduct(request):
    return render(request, Pro + '/editProduct.html')


def producDetail(request):
    return render(request, Pro + '/producDetail.html')


# POST or PUT routes for Products

# def updateProduct(request): # This will be the post for the update form
#     return render()

# def deleteProduct(request):
#     return render()
