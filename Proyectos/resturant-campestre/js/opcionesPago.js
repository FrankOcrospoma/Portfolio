//Ocultar cuadro de la tarjeta


recuperardatos();
function toggle(elemento) {
    if(elemento.value=="tarjeta") {
        document.getElementById("div").style.display = "block";
     }else{
         if(elemento.value=="yape"){
             document.getElementById("div").style.display = "block";
             document.getElementById("div").style.display = "none";
         }else{
             if(elemento.value=="pagEfectivo"){
                  document.getElementById("div").style.display = "block";
                  document.getElementById("div").style.display = "none";
              }  
          }
      }
}

function toggle2(elemento) {
    if(elemento.value=="yape") {
        document.getElementById("yape").style.display = "block";
     }else{
         if(elemento.value=="tarjeta"){
             document.getElementById("yape").style.display = "block";
             document.getElementById("yape").style.display = "none";
         }else{
             if(elemento.value=="pagEfectivo"){
                  document.getElementById("yape").style.display = "block";
                  document.getElementById("yape").style.display = "none";
              }  
          }
      }
}
function recuperardatos(){
    var registro ="";
    if (localStorage.length == 0) {
        registro+= '<li>Vacío</li>';
        
    } else {
        for(var i = 0; i<=localStorage.length - 1; i++){
            var key = localStorage.key(i);
            var datosC = JSON.parse(localStorage.getItem(key));
            registro += '<p> Nombre:'+ datosC.nombre+'</p>'+
            '<p> Apellido:'+ datosC.apellido+'</p>'+
            '<p> Documento:'+ key+'</p>'+        
            '<p> Ciudad:'+ datosC.ciudad+'</p>'+
            '<p> Distrito:'+ datosC.distrito+'</p>'+
            '<p> Dirección:'+ datosC.direccion+'</p>'+
            '<p> Referencia:' +datosC.referencia+'</p>'
        }
        
    }
    document.getElementById('resumenCliente').innerHTML = registro;
}
function eliminar(){
    localStorage.clear();
}