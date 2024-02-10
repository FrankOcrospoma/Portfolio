/*Carrito*/
 
recuperarDatos();

let sub_total=document.getElementById('sub_total');
let pagoTotal=document.getElementById('totalPag');


function recuperarDatos(){
    var registro ="";
    var subtotal=0;
    var total=0;
    var envio =10.00;
    if (localStorage.length == 0) {
        registro+= '<li>Vacío</li>';
        document.getElementById('carrito-contenido').innerHTML = registro;
        borrar();
        
    } else {
        for(var i = 0; i<=localStorage.length - 1; i++){
            var key = localStorage.key(i);
            var datosJson = JSON.parse(localStorage.getItem(key));
            
            registro += '<tr>'+'<td>'+`<img src="${datosJson.img}">`+'</td>'+'<td>'+key+'</td>'+'<td>'+datosJson.nombre+'</td>'
            +'<td>'+datosJson.cantidad+'</td>'+'<td>'+datosJson.precio+'</td>'+'<td>'+`<a  id="borrar-btn" onclick="eliminar_btn()" data-id="${key}"><i class="fa-solid fa-trash"></i></a>`+'</td>'+'</tr>'
            

            subtotal = parseFloat(datosJson.cantidad) * parseFloat(datosJson.precio);
            total = total + subtotal; 
           
           
        }
       
    }
    total = total.toFixed(2);
    envio = envio + parseFloat(total) ;
    envio = envio.toFixed(2);
    document.getElementById('carrito-contenido').innerHTML = registro;
    document.getElementById('sub_total').innerHTML = total;
    document.getElementById('totalPag').innerHTML = envio ;

}


function borrar(){
    sub_total.innerHTML = "0";
    pagoTotal.innerHTML = "0"; 
}
function eliminarTodo(){
    localStorage.clear();
    recuperarDatos();
}

function eliminar_btn(){
    var id = document.getElementById('borrar-btn').getAttribute('data-id');
   
    localStorage.removeItem(id);
    recuperarDatos();
}
