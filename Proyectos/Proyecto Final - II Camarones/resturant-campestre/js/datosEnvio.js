



recuperarDatos();

function recuperarDatos(){
    var registro ="";
    var subtotal=0;
    var total=0;
    var envio =10.00;
    if (localStorage.length == 0) {
        registro+= '<li>Vacío</li>';
        document.getElementById('carrito-contenido').innerHTML = registro;
        
        
    } else {
        for(var i = 0; i<=localStorage.length - 1; i++){
            var key = localStorage.key(i);
            var datosJson = JSON.parse(localStorage.getItem(key));
            
            registro += '<div class="producto-carrito" >'+
            `<img src="${datosJson.img}">`+
            '<div class="contenido-pro">'+
            '<div class="nombre-pro stilo">'+ datosJson.nombre+'</div>'+'<hr style="margin: 0;">'+
            '<hr style="margin: 0;">'+
            '<div class="cantidad-pro stilo text-center">'+datosJson.cantidad+'</div>'+ '<hr style="margin: 0;">'+
            '<div class="precio-pro stilo text-center ">'+ datosJson.precio+'</div>'+'</div>'+
             '</div> <br> <hr>'
            subtotal = parseFloat(datosJson.cantidad) * parseFloat(datosJson.precio);
            total = total + subtotal;
           
           
        }
       
    }
    total = total.toFixed(2);
    envio = envio + parseFloat(total) ;
    envio = envio.toFixed(2);
    document.getElementById('producto-cotenido').innerHTML = registro;
    document.getElementById('sub_total').innerHTML = total;
    document.getElementById('total').innerHTML = envio ;

}





function datosCliente(){
    const total= document.getElementById('total').textContent;
    localStorage.clear();
    const nombre= document.getElementById('nombre').value;
    const apellido=document.getElementById('apellido').value;
    const dni=document.getElementById('documento').value;
    const email=document.getElementById('email').value;
    const ciudad=document.getElementById('ciudad').value;
    const distrito=document.getElementById('distrito').value;
    const direccion=document.getElementById('domicilio').value;

    const referencia=document.getElementById('referencia').value;
  

    const datosC = {
        'nombre' : nombre,
        'apellido' : apellido,
        'email': email,
        'ciudad': ciudad,
        'distrito': distrito,
        'direccion':direccion,
        'referencia':referencia,
        'total':total,
    };


    localStorage.setItem(dni,JSON.stringify(datosC));
    console.log(datosC);


}