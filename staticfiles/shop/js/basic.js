   if (localStorage.getItem('cart') == null) {
    var cart = {};
    } else {
    cart = JSON.parse(localStorage.getItem('cart'));
    }
    
  
    var totalItem =  Object.keys(cart).length;
    document.getElementById('totalItem').innerHTML = totalItem;

    console.log('working')
    if(localStorage.getItem('cart')==null){
      var cart = {};
    }
    else
    {
      cart =JSON.parse(localStorage.getItem('cart'))
      updateCart(cart);
    }  
    
    $('.cart').click(function(){
      var idstr = this.id.toString();
      console.log(idstr)
      if (cart[idstr] != undefined) {
          qty = cart[idstr][0] + 1;
         
          
      } else {
          qty = 1;
          name = document.getElementById('name'+idstr).innerHTML;
          price = document.getElementById('price'+idstr).innerHTML;
          image = $('.imgdiv img').attr('src');
          catagory = document.getElementById('catagory'+idstr).innerHTML;
          cart[idstr] = [qty, name, parseInt(price), image, catagory ];
      }
      updateCart(cart);
       });
  
  
  
      function updateCart(cart) {
  
      localStorage.setItem('cart', JSON.stringify(cart));
    
      console.log(cart);
    
  }