console.log('testing')



var updateBtn = document.getElementsByClassName('update-cart');
// loop through all the buttons
for (var i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function(){
        var menuname = this.dataset.menu;
        var action = this.dataset.action;
        console.log('menuname:', menuname, 'action:', action)
        console.log('USER:', user)

 
        if (user == 'AnonymousUser'){
            console.log('not authenticated')
        }else{
            updateUserOrder(menuname, action)
        }


    })

}

// function to update the order
function updateUserOrder(menuname, action){
    console.log('user is authenticated, sending data...')

    var url = '/update_Item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'menuname':menuname, 'action':action})
    })
    
    .then((response) => {
        return response.json()
    })

    .then((data) => {
        location.reload()
    })
    
}

// Path: apc\storefront\shoppingcart\static\js\cart.js