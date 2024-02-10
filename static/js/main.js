
let allcontainerCart = document.querySelector('.carousel-products');
let buythings = [];
let priceTotal = document.querySelector('.price-total');
let containerBuyCart= document.querySelector('.card-items');
let amountProduct = document.querySelector('.count-product')
let totalCard = 0;
let countProduct=0;

let allcontainerCart2 = document.querySelector('.carousel-products2');
let allcontainerCart3 = document.querySelector('.carousel-products3');
let allcontainerCart4 = document.querySelector('.carousel-products4');



function pPagina(){
   location.href="Producto/producto.html";
}
loadEventListenrs();
function loadEventListenrs(){
    allcontainerCart.addEventListener('click',addProduct);
    containerBuyCart.addEventListener('click',deleteProduct);
    allcontainerCart2.addEventListener('click',addProduct);
    allcontainerCart3.addEventListener('click',addProduct);
    allcontainerCart4.addEventListener('click',addProduct);
}


function addProduct(e){
    e.preventDefault();
    if(e.target.classList.contains('btn-add-cart')){
        const selectProduct = e.target.parentElement;
        
        readTheContent(selectProduct);
        
    }
   
}
function deleteProduct(e){
    if(e.target.classList.contains('delete-product')){
        const deleteId= e.target.getAttribute('data-id');
        buythings.forEach(value=>{
            if(value.id == deleteId){
                let priceReduce= parseFloat(value.price) * parseFloat(value.amount);
                totalCard = totalCard- priceReduce;
                totalCard = totalCard.toFixed(2);
                countProduct--;
            }
        })
        
        buythings = buythings.filter(product => product.id !== deleteId);
      
          
        localStorage.removeItem(deleteId);
           
      
    }
    loadHtml();
}


function readTheContent(product){
    const infoProduct = {
        image: product.querySelector('.item-image').src,
        title: product.querySelector('.title').textContent,
        price: product.querySelector('.precio').textContent,
        id: product.querySelector('.btn-add-cart').getAttribute('data-id'),
        amount:1
    }
    totalCard =  parseFloat(totalCard) + parseFloat(infoProduct.price);
    totalCard = totalCard.toFixed(2);

    const exist = buythings.some(product => product.id === infoProduct.id)
    if(exist){
        const pro = buythings.map(product =>{
            if(product.id === infoProduct.id){
                product.amount++;
                return product;
            }else{
                return product
            }
        });
        buythings = [...pro];
    }else{
        buythings=[...buythings,infoProduct]
        countProduct++;
    }
    
    loadHtml();
    console.log(infoProduct);
}

function loadHtml(){
    clearHtml();
    buythings.forEach(product =>{
        const{image,title,price,code,amount, id}=product;
        const row = document.createElement('div');
        row.classList.add('item'),
        row.innerHTML=`
        <img src="${image}">
        <div class="item-content"> 
        <h5 >${title}</h5>
        <hr style="margin: 0;">
        <h4 class="cart-price">Precio:${price}</h4>
        <hr style="margin: 0;">
        <h6> Cantidad:${amount}</h6>
       </div>
       <span class="delete-product" data-id="${id}">X</span>       
       `;
       containerBuyCart.appendChild(row); 
       const datos = {
        'nombre' : title,
        'img' : image,
        'precio': price,
        'cantidad':amount,
        'codigo': code,
        };

       localStorage.setItem(id,JSON.stringify(datos));
       priceTotal.innerHTML = totalCard;
       amountProduct.innerHTML = countProduct;

       document.getElementById('dato').innerHTML = `
       <img class="modal-imagen" src="${image}">
       <h5 class="modal-carrito" >${title}</h5>
       <h4 class="">Precio:${price}</h4>    
       `;

    });
   
}
function clearHtml(){
    containerBuyCart.innerHTML='';
    amountProduct.innerHTML="0";
    priceTotal.innerHTML="0";
}










function toggle(elemento) {
    (elemento.value == "Cerrar")
    document.getElementById("myModal").style.display = "none";
}