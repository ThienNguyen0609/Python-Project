const AddBtns = document.getElementsByClassName('add-to-card')
const IncBtn = document.getElementsByClassName('inc-btn')
const DecBtn = document.getElementsByClassName('dec-btn')
const Count = document.getElementsByClassName('count')  
const Item = document.getElementsByClassName('item')
const Price = document.getElementsByClassName('prod-price')
const Total = document.getElementsByClassName('total')
const Get_items = document.getElementById('get-items')
const Get_total = document.getElementById('get-total')
const Check = document.getElementById('check')
const UpdCart = document.getElementById('upd-quantity-cart')

function AddToCart() {
    for(i=0; i<AddBtns.length; i++){
        AddBtns[i].addEventListener('click', function(){
            let productId = this.dataset.product
            let action = this.dataset.action
            let url = '/update_item/'
            UpdCart.innerHTML++
            // console.log("productId", productId, 'action', action)
            verifyUsertoUpdate(productId, action, url)
        })
    }
}

function UpdatingCart(){
    Check.addEventListener('click', function(){
        let total_item = 0, total_price = 0
        for(i=0; i<Item.length; i++){
            total_item+=parseInt(Count[i].innerHTML)
            total_price+=parseInt(Total[i].innerHTML)
        }
        Get_items.innerHTML=total_item
        Get_total.innerHTML=total_price
    })
    for(let i=0; i<Item.length; i++){
        IncBtn[i].addEventListener('click', function(e) { 
            let productId = this.dataset.product
            let action = this.dataset.action
            let url = '/inc_dec_item/'
            // console.log("productId:", productId, "action:", action)
            updateValueHTML(i, action)
            verifyUsertoUpdate(productId, action, url)
        })
        DecBtn[i].addEventListener('click', function(e) {
            let productId = this.dataset.product
            let action = this.dataset.action
            let url = '/inc_dec_item/'
            // console.log("productId:", productId, "action:", action)
            updateValueHTML(i, action)
            verifyUsertoUpdate(productId, action, url)
        })
    }
}

function updateValueHTML(i, action) {
    if(action == 'increase'){
        Count[i].innerHTML++
        UpdCart.innerHTML++
    }
    else{
        Count[i].innerHTML--
        UpdCart.innerHTML--
    }
    Total[i].innerHTML=Count[i].innerHTML*Price[i].innerHTML
    if(Count[i].innerHTML==0){
        Item[i].style.display = 'none'
    }
}

function verifyUsertoUpdate(productId, action, url) {
    if(user === "AnonymousUser"){
        console.log("user not logged in")
    }
    else {
        updateUserOrder(productId, action, url)
    }
}

function updateUserOrder(productId, action, url) {
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({"productId": productId, 'action': action})
    })
    .then((response)=>
        response.json()
    )
    .then((data)=>{
        console.log('data', data)
    })
}


AddToCart()
UpdatingCart()