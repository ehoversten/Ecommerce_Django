from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..product.models.detailsModels import Color, Size, Category
from ..product.models.productModels import Product

pApp = "product"  # short for Product App


def landing(request):
    return render(request, pApp + '/landingPage.html')


def newProduct(request):
    logMessage = 'You need to be logged in to access this page.'
    if 'id' not in request.session:
        messages.add_message(request, messages.INFO, logMessage)
        return redirect('/')
    else:
        return render(request, pApp + '/new_product.html')


def productReview(request):  # This should be merged with the product details.
    return render(request, pApp + '/product_review.html')


def editProduct(request):
    return render(request, pApp + '/editProduct.html')


def producDetail(request):
    return render(request, pApp + '/producDetail.html')


# POST or PUT routes for Products
def addproduct(request):
    results = Product.objects.ProductManager(
        request.POST, request.session['id'])
    if results[0]:
        # Once product is created forward to products?
        return redirect('/dashboard/{}'.format(request.session['id']))
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error, extra_tags='adderror')
            return redirect('/add/{}'.format(request.session['id']))


# def updateProduct(request): # This will be the post for the update form
#     return render()

# def deleteProduct(request):
#     return render()
