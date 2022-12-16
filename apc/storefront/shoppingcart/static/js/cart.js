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
            addCookieItem(menuid, action)
            
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

function addCookieItem(menuid, action){
	console.log('User is not authenticated test')

	if (action == 'add'){
		if (cart[menuid] == undefined){
		cart[menuid] = {'quantity':1}

		}else{
			cart[menuid]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[menuid]['quantity'] -= 1

		if (cart[menuid]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[menuid];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}