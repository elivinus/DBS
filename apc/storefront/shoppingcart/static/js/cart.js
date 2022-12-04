console.log('testing')



var updateItem = document.getElementsByClassName('update-cart');
// loop through all the buttons
for (var i = 0; i < updateItem.length; i++) {
    updateItem[i].addEventListener('click', function(){
        var menuid = this.dataset.menuid;
        var action = this.dataset.action;
        console.log('menuID:', menuid, 'action:', action)
        console.log('USER:', user)

 
        if (user == 'AnonymousUser'){
            console.log('not authenticated')
        }else{
            updateUserOrder(menuid, action)
            
        }


    })

}

// function to update the order
function updateUserOrder(menuid, action){
    console.log('user is authenticated, sending data')

    var url = '/update_Item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'menuid':menuid, 'action':action})
    })
    
    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
    
}

// Path: apc\storefront\shoppingcart\static\js\cart.js