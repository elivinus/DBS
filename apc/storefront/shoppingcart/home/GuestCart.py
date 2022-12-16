import json
from ..authentication.models import *

def guestCart(request):
    #guest cart
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    print('Cart:', cart)
    items = []
    order = {'get_cart_total':0, 'get_cart_items':0}
    cartItems = order['get_cart_items']

    for i in cart:
        try:

            cartItems += cart[i]['quantity']

            menuItem = MenuItem.objects.get(id=i)
            total = (menuItem.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                    'menuItem':{
                        'id':menuItem.id,
                        'name':menuItem.name, 
                        'price':menuItem.price, 
                        'imageURL':menuItem.imageURL
                        }, 
                    'quantity':cart[i]['quantity'],
                    'get_total':total,
                        }
            items.append(item)	
        except:
            pass
    return {'cartItems':cartItems ,'order':order, 'items':items}
