from django.shortcuts import render
from django.http import Http404
from .fake_db.products import FAKE_DBPRODUCTS

def product_list_view(request) :
    context = dict(
        products = FAKE_DBPRODUCTS,
    )

    return render(request, 'product/products.html', context)


def product_detail_view(request,id):
    result = list(filter(lambda x: (x['id'] == id), FAKE_DBPRODUCTS))
    if result :
        context = dict(
            item=result[0],
            products = FAKE_DBPRODUCTS,
        )     
        return render(request, 'product/product_detail.html', context)
    else:
        raise Http404
    