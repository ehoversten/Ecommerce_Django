from django.shortcuts import render, HttpResponse, redirect

pApp = "product"


def landing(request):
    return render(request, pApp + '/landingPage.html')

def newProduct(request):
    return render(request, pApp + '/new_product.html')

def productReview(request):
    return render(request, pApp + '/product_review.html')

def editProduct(request):
    return render(request, pApp + '/editProduct.html')

def producDetail(request):
    return render(request, pApp + '/producDetail.html')


# def updateProduct(request): # This will be the post for the update form
#     return render()


# def deleteProduct(request):
#     return render()
