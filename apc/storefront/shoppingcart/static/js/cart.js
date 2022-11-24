console.log('testing')



var updateBtn = document.getElementsByClassName('update-cart');

for (var i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function(){
        var menu = this.dataset.menu;
        var action = this.dataset.action;
        console.log('menu:', menu, 'action:', action)


    })

}

// Path: apc\storefront\shoppingcart\static\js\cart.js