var updateBtns = document.getElementsByClassName("update-cart")

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId: ', productId, 'action: ', action)

        if (user === 'AnonymousUser') {
            console.log("Need to Login")
        } else {
            updateUserOrder(productId, action)
            console.log("Successfull")
        }
    })
}

function updateUserOrder(productId, action) {
    console.log('User is logged in, sending data...')

    var url = 'updateItem'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
    .then((respone) => {
        return respone.json()
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}
document.addEventListener('DOMContentLoaded', function () {
    const main = document.querySelector('.themechange')
    const toggleSwitch = document.querySelector('.switch')

    toggleSwitch.addEventListener('click', () => {
        console.log("clicked");
        main.classList.toggle('dark-theme')
    })
}) 


// click to scroll top
    $('.move-up span').click(function () {
        $('html, body').animate({
            scrollTop: 0
        }, 1000);
    })
