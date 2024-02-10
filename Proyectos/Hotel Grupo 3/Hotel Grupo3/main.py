import json
from flask import Flask, render_template, request, redirect, flash, jsonify
import controlador.controlador_habitaciones  as controlador_habitaciones
import clases.clase_habitacion as clase_habitacion
import controlador.controlador_categoria_habitacion as controlador_categoria_habitacion
import clases.clase_categoria_habitacion as clase_categoria_habitacion
import controlador.controlador_personas as controlador_personas
import clases.clase_persona as clase_persona
import controlador.controlador_transaccion as controlador_transaccion
import clases.clase_transaccion as clase_transaccion
import controlador.controlador_servicios as controlador_servicios
import clases.clase_servicios as clase_servicios
import controlador.controlador_detalle_servicios as controlador_detalle_servicios
import clases.clase_detalle_servicios as clase_detalle_servicios
import controlador.controlador_comprobante as controlador_comprobante
import clases.clase_comprobante as clase_comprobante
import controlador.controlador_detalle as controlador_detalle
import clases.clase_detalle as clase_detalle
import controlador.controlador_detalle_alojamiento as controlador_detalle_alojamiento
import clases.clase_detalle_alojamiento as clase_detalle_alojamiento
import controlador.controlador_usuario as controlador_usuario


from flask_jwt import JWT, jwt_required, current_identity



class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

usuarios = controlador_usuario.obtener_usuario()

users = []
for usuario in usuarios:
    id = usuario[0]
    username = usuario[1]
    password = usuario[2]
    user = User(id, username, password)
    users.append(user)


username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and user.password==password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Buscar el usuario en la lista de usuarios
        user = None
        for u in users:
            if u.username == username and u.password == password:
                user = u
                break

        if user:
            # Autenticación exitosa
            # Puedes realizar acciones adicionales aquí si es necesario
            return redirect("/index")
        else:
            error_message = "Usuario o contraseña incorrectos"
            return render_template("login.html", error_message=error_message)

    return render_template("login.html")



# APIs - Inicio
@app.route("/api_obtener_habitaciones")
@jwt_required()
def api_obtener_habitaciones():
        habitacion = controlador_habitaciones.obtener_habitacion()
        listaserializable = []
        for habitacion in habitacion:
             miobj = clase_habitacion.Habitacion(habitacion[0], habitacion[1], habitacion[2], habitacion[3])
             listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)

@app.route("/api_guardarhabitacion", methods=["POST"])
@jwt_required()
def api_guardarhabitacion():
    try:
        estado_habitacion = request.json["estado_habitacion"]
        descripcion = request.json["descripcion"]
        categoria_id = request.json["categoria"]
        categoria=controlador_categoria_habitacion.obtener_categoria_habitacion_por_id(categoria_id)
        if categoria is not None:
            controlador_habitaciones.insertar_habitacion(estado_habitacion, descripcion, categoria_id)
            return jsonify({"Mensaje":"Habitación registrada correctamente"})
        return jsonify({"Mensaje":"Habitación no registrada, la categoria id no existe"})

    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_actualizarhabitacion", methods=["POST"])
@jwt_required()
def api_actualizarhabitacion():
    try:
        id = request.json["id"]
        estado_habitacion = request.json["estado_habitacion"]
        descripcion = request.json["descripcion"]
        categoria_id = request.json["categoria"]
        categoria=controlador_categoria_habitacion.obtener_categoria_habitacion_por_id(categoria_id)
        if categoria is not None:
            controlador_habitaciones.actualizar_habitacion(estado_habitacion, descripcion, categoria_id, id)
            return jsonify({"Mensaje":"Habitación actualizada correctamente"})
        return jsonify({"Mensaje":"Habitación no actualizada, la categoria id no existe"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_eliminarhabitacion", methods=["POST"])
@jwt_required()
def api_eliminarhabitacion():
    try:
        controlador_habitaciones.eliminar_habitacion(request.json["id"])
        return jsonify({"Mensaje":"Habitación eliminada correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_obtenerhabitacion/<int:id>")
@jwt_required()
def api_obtenerhabitacion(id):
    try:
        habitacion = controlador_habitaciones.obtener_habitacion_por_id(id)
        listaserializable = []
        miobj = clase_habitacion.Habitacion(habitacion[0], habitacion[1], habitacion[2], habitacion[3])
        listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

# APIs - Fin

@app.route("/agregar_habitacion")

def formulario_agregar_habitacion():
    categorias = controlador_categoria_habitacion.obtener_categoria_habitacion()
    return render_template("agregar_habitacion.html", categorias=categorias)

@app.route("/guardar_habitacion", methods=["POST"])
def guardar_habitacion():
    estado = request.form["estado"]
    descripcion = request.form["descripcion"]
    categoria_id = request.form["categoria_id"]
    categoria=controlador_categoria_habitacion.obtener_categoria_habitacion_por_id(categoria_id)
    if categoria is not None:
            controlador_habitaciones.insertar_habitacion(estado, descripcion, categoria_id)
            return redirect("/habitacion")
    return redirect("/habitacion")



@app.route("/")
@app.route("/habitacion")
def habitacion():
    habi = controlador_habitaciones.obtener_habitacion()
    return render_template("habitacion.html", habitacion=habi)


@app.route("/eliminar_habitacion", methods=["POST"])
def eliminar_habitacion():
    controlador_habitaciones.eliminar_habitacion(request.form["id"])
    return redirect("/habitacion")

@app.route("/formulario_editar_habitacion/<int:id>")
def editar_habitacion(id):
    # Obtener la habitacion por ID
    habitacion = controlador_habitaciones.obtener_habitacion_por_id(id)
    categorias = controlador_categoria_habitacion.obtener_categoria_habitacion()
    return render_template("editar_habitacion.html", categorias=categorias, habitacion=habitacion)


@app.route("/actualizar_habitacion", methods=["POST"])
def actualizar_habitacion():
    id = request.form["id"]
    estado = request.form["estado"]
    descripcion = request.form["descripcion"]
    categoria_id = request.form["categoria_id"]
    categoria=controlador_categoria_habitacion.obtener_categoria_habitacion_por_id(categoria_id)

    if categoria is not None:
            controlador_habitaciones.actualizar_habitacion(estado, descripcion, categoria_id, id)
            return redirect("/habitacion")
    return redirect("/habitacion")





@app.route("/api_obtenercategoria_habitacion")
@jwt_required()
def api_obtenercategoria_habitacion():
    try:
        categoria_habitacion = controlador_categoria_habitacion.obtener_categoria_habitacion()
        listaserializable = []
        for categoria_habitacion in categoria_habitacion:
            miobj = clase_categoria_habitacion.Categoria_habitacion(categoria_habitacion[0], categoria_habitacion[1], categoria_habitacion[2])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_guardarcategoria_habitacion", methods=["POST"])
@jwt_required()
def api_guardarcategoria_habitacion():
    try:
        nombre = request.json["nombre"]
        precio = request.json["precio"]
        controlador_categoria_habitacion.insertar_categoria_habitacion(nombre, precio)
        # De cualquier modo, y si todo fue bien, redireccionar
        return jsonify({"Mensaje":"Categoría de habitación registrada correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_actualizarcategoria_habitacion", methods=["POST"])
@jwt_required()
def api_actualizarcategoria_habitacion():
    try:
        id = request.json["id"]
        nombre = request.json["nombre"]
        precio = request.json["precio"]
        controlador_categoria_habitacion.actualizar_categoria_habitacion(nombre, precio, id)
        return jsonify({"Mensaje":"Categoría de habitación actualizada correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_eliminarcategoria_habitacion", methods=["POST"])
@jwt_required()
def api_eliminarcategoria_habitacion():
    try:
        controlador_categoria_habitacion.eliminar_categoria_habitacion(request.json["id"])
        return jsonify({"Mensaje":"Categoría de habitación eliminada correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_obtener_categoria_habitacion/<int:id>")
@jwt_required()
def api_obtener_categoria_habitacion(id):
    try:
        categoria_habitacion = controlador_categoria_habitacion.obtener_categoria_habitacion_por_id(id)
        listaserializable = []
        miobj = clase_categoria_habitacion.Categoria_habitacion(categoria_habitacion[0], categoria_habitacion[1], categoria_habitacion[2])
        listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})


# APIs - Fin

@app.route("/agregar_categoria_habitacion")
def formulario_agregar_categoria_habitacion():
    return render_template("agregar_categoria_habitacion.html")


@app.route("/guardar_categoria_habitacion", methods=["POST"])
def guardar_categoria_habitacion():
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    controlador_categoria_habitacion.insertar_categoria_habitacion(nombre, precio)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/categoria_habitacion")


@app.route("/")
@app.route("/categoria_habitacion")
def categoria_habitacion():
    categoria_habitacion = controlador_categoria_habitacion.obtener_categoria_habitacion()
    return render_template("categoria_habitacion.html", categoria_habitacion=categoria_habitacion)


@app.route("/eliminar_categoria_habitacion", methods=["POST"])
def eliminar_categoria_habitacion():
    controlador_categoria_habitacion.eliminar_categoria_habitacion(request.form["id"])
    return redirect("/categoria_habitacion")


@app.route("/formulario_editar_categoria_habitacion/<int:id>")
def editar_categoria_habitacion(id):
    # Obtener la categorìa habitaciòn por ID
    categoria_habitacion = controlador_categoria_habitacion.obtener_categoria_habitacion_por_id(id)
    return render_template("editar_categoria_habitacion.html", categoria_habitacion=categoria_habitacion)


@app.route("/actualizar_categoria_habitacion", methods=["POST"])
def actualizar_categoria_habitacion():
    id = request.form["id"]
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    controlador_categoria_habitacion.actualizar_categoria_habitacion(nombre, precio, id)
    return redirect("/categoria_habitacion")


@app.route("/api_guardar_persona", methods=["POST"])
@jwt_required()
def api_guardar_persona():
    try:
        dni = request.json["dni"]
        numero_telefono = request.json["numero_telefono"]
        nombres = request.json["nombres"]
        apellidos = request.json["apellidos"]
        sexo = request.json["sexo"]
        fecha_ingreso = request.json["fecha_ingreso"]
        fecha_salida = request.json["fecha_salida"]
        controlador_personas.insertar_persona(dni, numero_telefono, nombres, apellidos, sexo, fecha_ingreso, fecha_salida)
        # De cualquier modo, y si todo fue bien, redireccionar
        return jsonify({"Mensaje":"Persona registrada correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_obtener_personas")
@jwt_required()
def api_obtenerpersonas():
    try:
        personas = controlador_personas.obtener_personas()
        listaserializable = []
        for persona in personas:
            miobj = clase_persona.persona(persona[0], persona[1], persona[2], persona[3],persona[4], persona[5], persona[6], persona[7])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_actualizar_persona", methods=["POST"])
@jwt_required()
def api_actualizar_persona():
    try:
        persona_id = request.json["persona_id"]
        dni = request.json["dni"]
        numero_telefono = request.json["numero_telefono"]
        nombres = request.json["nombres"]
        apellidos = request.json["apellidos"]
        sexo = request.json["sexo"]
        fecha_ingreso = request.json["fecha_ingreso"]
        fecha_salida = request.json["fecha_salida"]
        controlador_personas.actualizar_persona(dni, numero_telefono, nombres, apellidos, sexo, fecha_ingreso, fecha_salida,persona_id)
        return jsonify({"Mensaje":"Persona acualizada correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})
@app.route("/api_eliminarpersona", methods=["POST"])
@jwt_required()
def api_eliminarpersona():
    try:
        controlador_personas.eliminar_persona(request.json["persona_id"])
        return jsonify({"Mensaje":"Persona eliminada correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_obtenerpersona/<int:persona_id>")
@jwt_required()
def api_obtenerpersona(persona_id):
    try:
        persona = controlador_personas.obtener_persona_por_id(persona_id)
        listaserializable = []
        miobj = clase_persona.persona(persona[0], persona[1], persona[2], persona[3],persona[4], persona[5], persona[6], persona[7])
        listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})


@app.route("/agregar_persona")
def formulario_agregar_persona():
    return render_template("agregar_persona.html")


@app.route("/guardar_persona", methods=["POST"])
def guardar_persona():
    dni = request.form["dni"]
    numero_telefono = request.form["numero_telefono"]
    nombres = request.form["nombres"]
    apellidos = request.form["apellidos"]
    sexo = request.form["sexo"]
    fecha_ingreso = request.form["fecha_ingreso"]
    fecha_salida = request.form["fecha_salida"]
    controlador_personas.insertar_persona(dni, numero_telefono, nombres, apellidos, sexo, fecha_ingreso, fecha_salida)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/personas")


@app.route("/")
@app.route("/personas")
def personas():
    personas = controlador_personas.obtener_personas()
    return render_template("personas.html", personas=personas)


@app.route("/eliminar_persona", methods=["POST"])
def eliminar_persona():
    controlador_personas.eliminar_persona(request.form["persona_id"])
    return redirect("/personas")


@app.route("/formulario_editar_persona/<int:persona_id>")
def editar_persona(persona_id):
    # Obtener el persona por ID
    persona = controlador_personas.obtener_persona_por_id(persona_id)
    return render_template("editar_persona.html", persona=persona)


@app.route("/actualizar_persona", methods=["POST"])
def actualizar_persona():
    persona_id = request.form["persona_id"]
    dni = request.form["dni"]
    numero_telefono = request.form["numero_telefono"]
    nombres = request.form["nombres"]
    apellidos = request.form["apellidos"]
    sexo = request.form["sexo"]
    fecha_ingreso = request.form["fecha_ingreso"]
    fecha_salida = request.form["fecha_salida"]
    controlador_personas.actualizar_persona(dni, numero_telefono, nombres, apellidos, sexo, fecha_ingreso, fecha_salida, persona_id)
    return redirect("/personas")




@app.route("/api_obtenertransacciones")
@jwt_required()
def api_obtenertransacciones():
    try:
        transacciones = controlador_transaccion.obtener_transaccion()
        listaserializable = []
        for transaccion in transacciones:
          miobj = clase_transaccion.Transaccion(transaccion[0], transaccion[1], transaccion[2], transaccion[3], transaccion[4], transaccion[5], transaccion[6], transaccion[7], transaccion[8], transaccion[9])
          transaccion_serializable = miobj.midic.copy()
          # Convertir objetos timedelta a cadenas de texto
          transaccion_serializable['fecha_registro'] = str(transaccion_serializable['fecha_registro'])
          transaccion_serializable['hora_registro'] = str(transaccion_serializable['hora_registro'])
          transaccion_serializable['fecha_entrada'] = str(transaccion_serializable['fecha_entrada'])
          transaccion_serializable['hora_entrada'] = str(transaccion_serializable['hora_entrada'])
          transaccion_serializable['fecha_salida'] = str(transaccion_serializable['fecha_salida'])
          transaccion_serializable['hora_salida'] = str(transaccion_serializable['hora_salida'])

          listaserializable.append(transaccion_serializable)

        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})



import traceback

@app.route("/api_guardartransaccion", methods=["POST"])
@jwt_required()
def api_guardartransaccion():
    try:
        fecha_registro = request.json["fecha_registro"]
        hora_registro = request.json["hora_registro"]
        tipo_transaccion = request.json["tipo_transaccion"]
        fecha_entrada = request.json["fecha_entrada"]
        hora_entrada = request.json["hora_entrada"]
        fecha_salida = request.json["fecha_salida"]
        hora_salida = request.json["hora_salida"]
        habitacion_id = request.json["habitacion_id"]
        persona_id = request.json["persona_id"]
        habitacion = controlador_habitaciones.obtener_habitacion_por_id(habitacion_id)
        personas = controlador_personas.obtener_persona_por_id(persona_id)
        if habitacion is not None:
            if personas is not None:
                controlador_transaccion.insertar_transaccion(
                    fecha_registro, hora_registro, tipo_transaccion,
                    fecha_entrada, hora_entrada, fecha_salida, hora_salida,
                    habitacion_id, persona_id)
                return jsonify({"Mensaje": "Transacción guardada correctamente"})
            else:
                return jsonify({"Mensaje": "Persona no encontrada"})
        else:
            return jsonify({"Mensaje": "Habitación no encontrada"})
    except:
        return jsonify({"Mensaje": "Error en la transacción. Consulta el registro para más detalles."})



@app.route("/api_actualizartransaccion", methods=["POST"])
@jwt_required()
def api_actualizartransaccion():
    try:
        id = request.json["id"]
        fecha_registro = request.json["fecha_registro"]
        hora_registro = request.json["hora_registro"]
        tipo_transaccion = request.json["tipo_transaccion"]
        fecha_entrada = request.json["fecha_entrada"]
        hora_entrada = request.json["hora_entrada"]
        fecha_salida = request.json["fecha_salida"]
        hora_salida = request.json["hora_salida"]
        habitacion_id = request.json["habitacion_id"]
        persona_id = request.json["persona_id"]
        habitacion= controlador_habitaciones.obtener_habitacion_por_id(habitacion_id)
        personas=controlador_personas.obtener_persona_por_id(persona_id)
        if habitacion is not None:
            if personas is not None:
               controlador_transaccion.actualizar_transaccion(fecha_registro,hora_registro, tipo_transaccion,fecha_entrada,hora_entrada, fecha_salida,hora_salida, habitacion_id,persona_id,id)
            return jsonify({"Mensaje":"Transacción  actualizada"})
        # De cualquier modo, y si todo fue bien, redireccionar
        return jsonify({"Mensaje":"Transacción no actualizada"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_eliminartransaccion", methods=["POST"])
@jwt_required()
def api_eliminartransaccion():
    try:
        controlador_transaccion.eliminar_transaccion(request.json["id"])
        return jsonify({"Mensaje":"Transacción eliminada correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_obtenertransaccion/<int:id>")
@jwt_required()
def api_obtenertransaccion(id):
    try:
        transaccion = controlador_transaccion.obtener_transaccion_por_id(id)
        listaserializable = []
        miobj = clase_transaccion.Transaccion(transaccion[0], transaccion[1], transaccion[2], transaccion[3],transaccion[4], transaccion[5], transaccion[6],transaccion[7], transaccion[8], transaccion[9])
        transaccion_serializable = miobj.midic.copy()
         # Convertir objetos timedelta a cadenas de texto
        transaccion_serializable['fecha_registro'] = str(transaccion_serializable['fecha_registro'])
        transaccion_serializable['hora_registro'] = str(transaccion_serializable['hora_registro'])
        transaccion_serializable['fecha_entrada'] = str(transaccion_serializable['fecha_entrada'])
        transaccion_serializable['hora_entrada'] = str(transaccion_serializable['hora_entrada'])
        transaccion_serializable['fecha_salida'] = str(transaccion_serializable['fecha_salida'])
        transaccion_serializable['hora_salida'] = str(transaccion_serializable['hora_salida'])
        listaserializable.append(transaccion_serializable)
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

# APIs - Fin

@app.route("/agregar_transaccion")
def formulario_agregar_transaccion():
    personas= controlador_personas.obtener_personas()
    habitacion= controlador_habitaciones.obtener_habitacion()
    return render_template("agregar_transaccion.html",personas=personas,habitacion=habitacion)


@app.route("/guardar_transaccion", methods=["POST"])
def guardar_transaccion():
    fecha_registro = request.form["fecha_registro"]
    hora_registro = request.form["hora_registro"]
    tipo_transaccion = request.form["tipo_transaccion"]
    fecha_entrada = request.form["fecha_entrada"]
    hora_entrada = request.form["hora_entrada"]
    fecha_salida = request.form["fecha_salida"]
    hora_salida = request.form["hora_salida"]
    habitacion_id = request.form["habitacion_id"]
    persona_id = request.form["persona_id"]
    personas=controlador_personas.obtener_persona_por_id(persona_id)
    habitacion=controlador_habitaciones.obtener_habitacion_por_id(habitacion_id)
    if  personas is not None and habitacion is not None:
               controlador_transaccion.insertar_transaccion(fecha_registro, hora_registro, tipo_transaccion, fecha_entrada, hora_entrada, fecha_salida, hora_salida, habitacion_id, persona_id)
               return redirect("/transaccion")

    return redirect("/transaccion")
    # De cualquier modo, y si todo fue bien, redireccionar



@app.route("/")
@app.route("/transaccion")
def transaccion():
    transaccion = controlador_transaccion.obtener_transaccion()
    return render_template("transaccion.html", transaccion=transaccion)


@app.route("/eliminar_transaccion", methods=["POST"])
def eliminar_transaccion():
    controlador_transaccion.eliminar_transaccion(request.form["id"])
    return redirect("/transaccion")


@app.route("/formulario_editar_transaccion/<int:id>")
def editar_transaccion(id):
    # Obtener el transaccion por ID
    transaccion = controlador_transaccion.obtener_transaccion_por_id(id)
    personas=controlador_personas.obtener_personas()
    habitacion=controlador_habitaciones.obtener_habitacion()
    return render_template("editar_transaccion.html", transaccion=transaccion,personas=personas,habitacion=habitacion)


@app.route("/actualizar_transaccion", methods=["POST"])
def actualizar_transaccion():
    id = request.form["id"]
    fecha_registro = request.form["fecha_registro"]
    hora_registro = request.form["hora_registro"]
    tipo_transaccion = request.form["tipo_transaccion"]
    fecha_entrada = request.form["fecha_entrada"]
    hora_entrada = request.form["hora_entrada"]
    fecha_salida = request.form["fecha_salida"]
    hora_salida = request.form["hora_salida"]
    habitacion_id = request.form["habitacion_id"]
    persona_id = request.form["persona_id"]

    personas = controlador_personas.obtener_persona_por_id(persona_id)
    habitacion = controlador_habitaciones.obtener_habitacion_por_id(habitacion_id)

    if personas is not None and habitacion is not None:
        controlador_transaccion.actualizar_transaccion(fecha_registro, hora_registro, tipo_transaccion, fecha_entrada, hora_entrada, fecha_salida, hora_salida, habitacion_id, persona_id, id)

    return redirect("/transaccion")



@app.route("/api_obtenerservicios")
@jwt_required()
def api_obtenerservicios():
    try:
        servicios = controlador_servicios.obtener_servicios()
        listaserializable = []
        for servicio in servicios:
            miobj = clase_servicios.Servicios(servicio[0], servicio[1])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_guardarservicio", methods=["POST"])
@jwt_required()
def api_guardarservicio():
    try:
        descripcion = request.json["descripcion"]
        controlador_servicios.insertar_servicios( descripcion)
        # De cualquier modo, y si todo fue bien, redireccionar
        return jsonify({"Mensaje":"Servicio registrado correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_actualizarservicio", methods=["POST"])
@jwt_required()
def api_actualizarservicio():
    try:
        id = request.json["id"]
        descripcion = request.json["descripcion"]
        controlador_servicios.actualizar_servicios(descripcion, id)
        return jsonify({"Mensaje":"Servicio actualizado correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_eliminarservicio", methods=["POST"])
@jwt_required()
def api_eliminarservicio():
    try:
        controlador_servicios.eliminar_servicios(request.json["id"])
        return jsonify({"Mensaje":"Servicio eliminado correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_obtenerservicio/<int:id>")
@jwt_required()
def api_obtenerservicio(id):
    try:
        servicio = controlador_servicios.obtener_servicios_por_id(id)
        listaserializable = []
        miobj = clase_servicios.Servicios(servicio[0], servicio[1])
        listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

# APIs - Fin

@app.route("/agregar_servicios")
def formulario_agregar_servicios():
    return render_template("agregar_servicios.html")


@app.route("/guardar_servicios", methods=["POST"])
def guardar_servicios():
    descripcion = request.form["descripcion"]
    controlador_servicios.insertar_servicios(descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/servicios")


@app.route("/")
@app.route("/servicios")
def servicios():
    servicios = controlador_servicios.obtener_servicios()
    return render_template("servicios.html", servicios=servicios)


@app.route("/eliminar_servicios", methods=["POST"])
def eliminar_servicios():
    controlador_servicios.eliminar_servicios(request.form["id"])
    return redirect("/servicios")


@app.route("/formulario_editar_servicios/<int:id>")
def editar_servicios(id):
    # Obtener el servicios por ID
    servicios = controlador_servicios.obtener_servicios_por_id(id)
    return render_template("editar_servicios.html", servicios=servicios)


@app.route("/actualizar_servicios", methods=["POST"])
def actualizar_servicios():
    id = request.form["id"]
    descripcion = request.form["descripcion"]
    controlador_servicios.actualizar_servicios(descripcion, id)
    return redirect("/servicios") @jwt_required()

@app.route("/api_obtenerdetalleservicios")
@jwt_required()
def api_obtenerdetalleservicios():
  try:
        detalle_servicios = controlador_detalle_servicios.obtener_detalle_servicios()
        listaserializable = []
        for detalle_servicio in detalle_servicios:
            miobj = clase_detalle_servicios.Detalle_S(detalle_servicio[0], detalle_servicio[1], detalle_servicio[2], detalle_servicio[3],detalle_servicio[4],detalle_servicio[5],detalle_servicio[6])
            detalle_servicios_serializable = miobj.midic.copy()
            # Convertir objetos timedelta a cadenas de texto
            detalle_servicios_serializable['fecha_solicitud'] = str(detalle_servicios_serializable['fecha_solicitud'])
            detalle_servicios_serializable['hora_solicitud'] = str(detalle_servicios_serializable['hora_solicitud'])
            listaserializable.append(detalle_servicios_serializable)
        return jsonify(listaserializable)
  except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_guardardetalleservicios", methods=["POST"])
@jwt_required()
def api_guardardetalleservicios():
    try:
        fecha_solicitud =request.json["fecha_solicitud"]
        hora_solicitud =request.json["hora_solicitud"]
        descripcion_solicitud =request.json["descripcion_solicitud"]
        monto_servicio =request.json["monto_servicio"]
        transaccion_id = request.json["transaccion_id"]
        servicio_id = request.json["servicio_id"]
        transaccion= controlador_transaccion.obtener_transaccion_por_id(transaccion_id)
        servicio=controlador_servicios.obtener_servicios_por_id(servicio_id)
        if transaccion is not None:
            if servicio is not None:
                controlador_detalle_servicios.insertar_detalle_servicios(fecha_solicitud, hora_solicitud, descripcion_solicitud, monto_servicio, transaccion_id, servicio_id)
            return jsonify({"Mensaje":"Detalles de servicio registrado correctamente"})
        # De cualquier modo, y si todo fue bien, redireccionar
        return jsonify({"Mensaje":"Detalles de servicio registrado correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_actualizardetalleservicios", methods=["POST"])
@jwt_required()
def api_actualizardetalleservicios():
    try:
        id = request.json["id"]
        fecha_solicitud = request.json["fecha_solicitud"]
        hora_solicitud = request.json["hora_solicitud"]
        descripcion_solicitud = request.json["descripcion_solicitud"]
        monto_servicio = request.json["monto_servicio"]
        transaccion_id = request.json["transaccion_id"]
        servicio_id = request.json["servicio_id"]
        transaccion= controlador_transaccion.obtener_transaccion_por_id(transaccion_id)
        servicio=controlador_servicios.obtener_servicios_por_id(servicio_id)
        if transaccion is not None:
            if servicio is not None:
             controlador_detalle_servicios.actualizar_detalle_servicios(fecha_solicitud, hora_solicitud, descripcion_solicitud, monto_servicio,transaccion_id,servicio_id, id)
            return jsonify({"Mensaje":"Detalles de servicio actualizado correctamente"})
        return jsonify({"Mensaje":"Detalles de servicio actualizado correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_eliminardetalleservicios", methods=["POST"])
@jwt_required()
def api_eliminardetalleservicios():
    try:
        controlador_detalle_servicios.eliminar_detalle_servicios(request.json["id"])
        return jsonify({"Mensaje":"Detalles de servicio eliminado correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_obtener_detalle_servicio_id/<int:id>")
@jwt_required()
def api_obtener_detalle_servicio_id(id):
    try:

        detalle_servicios = controlador_detalle_servicios.obtener_detalle_servicios_por_id(id)
        listaserializable = []
        miobj = clase_detalle_servicios.Detalle_S(detalle_servicios[0], detalle_servicios[1], detalle_servicios[2], detalle_servicios[3], detalle_servicios[4], detalle_servicios[5], detalle_servicios[6])
        detalle_servicios_serializable = miobj.midic.copy()
            # Convertir objetos timedelta a cadenas de texto
        detalle_servicios_serializable['fecha_solicitud'] = str(detalle_servicios_serializable['fecha_solicitud'])
        detalle_servicios_serializable['hora_solicitud'] = str(detalle_servicios_serializable['hora_solicitud'])
        listaserializable.append(detalle_servicios_serializable)
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/agregar_detalle_servicios")
def formulario_agregar_detalle_servicios():
    servicios = controlador_servicios.obtener_servicios()
    return render_template("agregar_detalle_servicios.html", servicios=servicios)

@app.route("/guardar_detalle_servicios", methods=["POST"])
def guardar_detalle_servicios():
    fecha_solicitud = request.form["fecha_solicitud"]
    hora_solicitud = request.form["hora_solicitud"]
    descripcion_solicitud = request.form["descripcion_solicitud"]
    monto_servicio = request.form["monto_servicio"]
    transaccion_id = request.form["transaccion_id"]
    servicio_id = request.form["servicio_id"]
    servicios=controlador_servicios.obtener_servicios_por_id(servicio_id)
    if servicios is not None:
        controlador_detalle_servicios.insertar_detalle_servicios(fecha_solicitud, hora_solicitud, descripcion_solicitud, monto_servicio,transaccion_id,servicio_id)
        return redirect("/detalle_servicios")
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/detalle_servicios")


@app.route("/")
@app.route("/detalle_servicios")
def detalle_servicios():
    detalle_servicios = controlador_detalle_servicios.obtener_detalle_servicios()
    return render_template("detalle_servicios.html", detalle_servicios=detalle_servicios)


@app.route("/eliminar_detalle_servicios", methods=["POST"])
def eliminar_detalle_servicios():
    controlador_detalle_servicios.eliminar_detalle_servicios(request.form["id"])
    return redirect("/detalle_servicios")


@app.route("/formulario_editar_detalle_servicios/<int:id>")
def editar_detalle_servicios(id):
    # Obtener el detalle servicios  por ID
    detalle_servicios = controlador_detalle_servicios.obtener_detalle_servicios_por_id(id)
    servicios=controlador_servicios.obtener_servicios()
    return render_template("editar_detalle_servicios.html", detalle_servicios=detalle_servicios, servicios=servicios)


@app.route("/actualizar_detalle_servicios", methods=["POST"])
def actualizar_detalle_servicios():
    id = request.form["id"]
    fecha_solicitud = request.form["fecha_solicitud"]
    hora_solicitud = request.form["hora_solicitud"]
    descripcion_solicitud = request.form["descripcion_solicitud"]
    monto_servicio = request.form["monto_servicio"]
    transaccion_id = request.form["transaccion_id"]
    servicio_id = request.form["servicio_id"]
    servicios=controlador_servicios.obtener_servicios_por_id(id)
    if servicios is not None:
        controlador_detalle_servicios.actualizar_detalle_servicios(fecha_solicitud, hora_solicitud, descripcion_solicitud, monto_servicio,transaccion_id,servicio_id, id)
        return redirect("/detalle_servicios")
    return redirect("/detalle_servicios")

# Inicio comprobante
@app.route("/api_obtenercomprobantes")
@jwt_required()
def api_obtenercomprobantes():
    try:
        comprobante = controlador_comprobante.obtener_comprobante()
        listaserializable = []
        for comprobante in comprobante:
            miobj = clase_comprobante.Comprobante(comprobante[0], comprobante[1], comprobante[2], comprobante[3],comprobante[4],comprobante[5],comprobante[6])
            comprobante_serializable = miobj.midic.copy()
             # Convertir objetos timedelta a cadenas de texto

            comprobante_serializable['fecha_comprobante'] = str(comprobante_serializable['fecha_comprobante'])

            listaserializable.append(comprobante_serializable)

        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 946 951 631"})

@app.route("/api_guardarcomprobante", methods=["POST"])
@jwt_required()
def api_guardarcomprobante():

        tipo_comprobante = request.json["tipo_comprobante"]
        numero_comprobante = request.json["numero_comprobante"]
        fecha_comprobante = request.json["fecha_comprobante"]
        monto_total = request.json["monto_total"]
        transaccion_id = request.json["transaccion_id"]
        persona_id = request.json["persona_id"]

        transaccion= controlador_transaccion.obtener_transaccion_por_id(transaccion_id)
        personas=controlador_personas.obtener_persona_por_id(persona_id)
        if transaccion is not None:
            if personas is not None:
               controlador_comprobante.insertar_comprobante(tipo_comprobante,numero_comprobante,fecha_comprobante,monto_total,transaccion_id,persona_id)
            return jsonify({"Mensaje":"Comprobante guardado correctamente"})
        # De cualquier modo, y si todo fue bien, redireccionar
        return jsonify({"Mensaje":"Comprobante guardado correctamente"})


@app.route("/api_actualizar_comprobante", methods=["POST"])
@jwt_required()
def api_actualizar_comprobante():
    try:
        id = request.json["id"]
        tipo_comprobante = request.json["tipo_comprobante"]
        numero_comprobante = request.json["numero_comprobante"]
        fecha_comprobante = request.json["fecha_comprobante"]
        monto_total = request.json["monto_total"]

        transaccion_id = request.json["transaccion_id"]
        persona_id = request.json["persona_id"]

        transaccion= controlador_transaccion.obtener_transaccion_por_id(transaccion_id)
        persona=controlador_personas.obtener_persona_por_id(persona_id)
        if transaccion is not None:
            if persona is not None:
                controlador_comprobante.actualizar_comprobante(tipo_comprobante,numero_comprobante,fecha_comprobante,monto_total,transaccion_id,persona_id,id)
                return jsonify({"Mensaje":"Comprobante actualizado"})
        # De cualquier modo, y si todo fue bien, redireccionar
        return jsonify({"Mensaje":"Comprobante no actualizado"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_eliminar_comprobante", methods=["POST"])
@jwt_required()
def api_eliminar_comprobante():
    try:
        controlador_comprobante.eliminar_comprobante(request.json["id"])
        return jsonify({"Mensaje":"Comprobante eliminado correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 946 951 631"})

@app.route("/api_obtenercomprobante/<int:id>")
@jwt_required()
def api_obtenercomprobante(id):
    try:
        comprobante = controlador_comprobante.obtener_comprobante_por_id(id)
        listaserializable = []
        miobj = clase_comprobante.Comprobante(comprobante[0], comprobante[1], comprobante[2], comprobante[3],comprobante[4],comprobante[5],comprobante[6])
        listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 946 951 631"})


#Apis - Fin

@app.route("/agregar_comprobante")
def formulario_agregar_comprobante():
    return render_template("agregar_comprobante.html")


@app.route("/guardar_comprobante", methods=["POST"])
def guardar_comprobante():
    tipo_comprobante = request.form["tipo_comprobante"]
    numero_comprobante = request.form["numero_comprobante"]
    fecha_comprobante = request.form["fecha_comprobante"]
    monto_total = request.form["monto_total"]

    transaccion_id = request.form["transaccion_id"]
    persona_id = request.form["persona_id"]
    transaccion = controlador_transaccion.obtener_transaccion_por_id(transaccion_id)
    persona = controlador_personas.obtener_persona_por_id(persona_id)
    if transaccion is not None:
        if persona is not None:
            controlador_comprobante.insertar_comprobante(tipo_comprobante, numero_comprobante,fecha_comprobante,monto_total,transaccion_id,persona_id)
            return redirect("/comprobante")
        return redirect("/comprobante")
    return redirect("/comprobante")

@app.route("/")
@app.route("/comprobante")
def comprobante():
    comprobante = controlador_comprobante.obtener_comprobante()
    return render_template("comprobante.html", comprobante=comprobante)


@app.route("/eliminar_comprobante", methods=["POST"])
def eliminar_comprobante():
    controlador_comprobante.eliminar_comprobante(request.form["id"])
    return redirect("/comprobante")


@app.route("/formulario_editar_comprobante/<int:id>")
def editar_comprobante(id):
    # Obtener el comprobante por ID
    comprobante = controlador_comprobante.obtener_comprobante_por_id(id)
    return render_template("editar_comprobante.html", comprobante=comprobante)


@app.route("/actualizar_comprobante", methods=["POST"])
def actualizar_comprobante():
    id = request.form["id"]
    tipo_comprobante = request.form["tipo_comprobante"]
    numero_comprobante = request.form["numero_comprobante"]
    fecha_comprobante = request.form["fecha_comprobante"]
    monto_total = request.form["monto_total"]
    transaccion_id = request.form["transaccion_id"]
    persona_id = request.form["persona_id"]
    transaccion = controlador_transaccion.obtener_transaccion_por_id(transaccion_id)
    persona = controlador_personas.obtener_persona_por_id(persona_id)
    if transaccion is not None:
        if persona is not None:
            controlador_comprobante.actualizar_comprobante(tipo_comprobante, numero_comprobante,fecha_comprobante,monto_total,transaccion_id,persona_id, id)
        return redirect("/comprobante")
    return redirect("/comprobante")
#Fin comprobante

#Inicio Detalle

@app.route("/api_obtenerdetalles")
@jwt_required()
def api_obtenerdetalles():
    try:
        detalle = controlador_detalle.obtener_detalle()
        listaserializable = []
        for detalle in detalle:
            miobj = clase_detalle.Detalle(detalle[0], detalle[1], detalle[2])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_guardardetalle", methods=["POST"])
@jwt_required()
def api_guardardetalle():
    try:
        comprobante_id = request.json["comprobante_id"]
        servicios_id = request.json["servicios_id"]
        monto = request.json["monto"]

        comprobante=controlador_comprobante.obtener_comprobante_por_id(comprobante_id)
        servicio=controlador_servicios.obtener_servicios_por_id(servicios_id)
        if comprobante is not None:
            if servicio is not None:
             controlador_detalle.insertar_detalle(servicios_id,comprobante_id, monto)
            return jsonify({"Mensaje":"Detalles de comprobante registrado"})
        # De cualquier modo, y si todo fue bien, redireccionar
        return jsonify({"Mensaje":"Detalles de comprobante no registrado"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_actualizardetalle", methods=["POST"])
@jwt_required()
def api_actualizardetalle():
    try:
        servicios_id = request.json["servicios_id"]
        comprobante_id = request.json["comprobante_id"]
        monto = request.json["monto"]

        comprobante=controlador_comprobante.obtener_comprobante_por_id(comprobante_id)
        servicio=controlador_servicios.obtener_servicios_por_id(servicios_id)
        if comprobante is not None:
            if servicio is not None:
             controlador_detalle.actualizar_detalle(comprobante_id, monto, servicios_id)
             return jsonify({"Mensaje":"Detalle Comprobante actualizado"})

        return jsonify({"Mensaje":"Detalles de comprobante no actualizado"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_eliminardetalle", methods=["POST"])
@jwt_required()
def api_eliminardetalle():
    try:
        controlador_detalle.eliminar_detalle(request.json["servicios_id"])
        return jsonify({"Mensaje":"Detalle eliminado correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})

@app.route("/api_obtenerdetalle/<int:id>")
@jwt_required()
def api_obtenerdetalle(id):
    try:
        detalle = controlador_detalle.obtener_detalle_por_id(id)
        listaserializable = []
        miobj = clase_detalle.Detalle(detalle[0], detalle[1], detalle[2])
        listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 920 532 729"})


#Apis - Fin
@app.route("/agregar_detalle")
def formulario_agregar_detalle():
    return render_template("agregar_detalle.html")


@app.route("/guardar_detalle", methods=["POST"])
def guardar_detalle():
    servicios_id = request.form["servicios_id"]
    comprobante_id = request.form["comprobante_id"]
    monto = request.form["monto"]
    servicios = controlador_servicios.obtener_servicios_por_id(servicios_id)
    coprobante = controlador_comprobante.obtener_comprobante_por_id(comprobante_id)
    if servicios is not None:
        if coprobante is not None:
            controlador_detalle.insertar_detalle(servicios_id,comprobante_id,monto)
            return redirect("/detalle_comprobante")
        return redirect("/detalle_comprobante")
    return redirect("/detalle_comprobante")

@app.route("/")
@app.route("/detalle_comprobante")
def detalle():
    detalle = controlador_detalle.obtener_detalle()
    return render_template("detalle.html", detalle=detalle)


@app.route("/eliminar_detalle", methods=["POST"])
def eliminar_detalle():
    controlador_detalle.eliminar_detalle(request.form["servicios_id"])
    return redirect("/detalle_comprobante")


@app.route("/formulario_editar_detalle/<int:id>")
def editar_detalle(id):
    # Obtener el comprobante por ID
    detalle = controlador_detalle.obtener_detalle_por_id(id)
    return render_template("editar_detalle.html", detalle=detalle)


@app.route("/actualizar_detalle", methods=["POST"])
def actualizar_detalle():

    servicios_id = request.form["servicios_id"]
    comprobante_id = request.form["comprobante_id"]
    monto = request.form["monto"]

    comprobante=controlador_comprobante.obtener_comprobante_por_id(comprobante_id)
    servicio=controlador_servicios.obtener_servicios_por_id(servicios_id)
    if comprobante is not None:
        if servicio is not None:
            controlador_detalle.actualizar_detalle(comprobante_id, monto, servicios_id)
            return redirect("/detalle_comprobante")

    return redirect("/detalle_comprobante")


#Detalle_alojamiento

@app.route("/api_obtenerdetalle_alojamientos")
@jwt_required()
def api_obtenerdetalle_alojamientos():
    try:
        detalle_alojamientos = controlador_detalle_alojamiento.obtener_detalle_alojamiento()
        listaserializable = []
        for detalle_alojamiento in detalle_alojamientos:
          miobj = clase_detalle_alojamiento.detalle_alojamiento(detalle_alojamiento[0], detalle_alojamiento[1], detalle_alojamiento[2])
          detalle_alojamiento_serializable = miobj.midic.copy()
          listaserializable.append(detalle_alojamiento_serializable)

        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})



@app.route("/api_guardardetalle_alojamiento", methods=["POST"])
@jwt_required()
def api_guardardetalle_alojamiento():
    try:
        transaccion_id = request.json["transaccion_id"]
        persona_id = request.json["persona_id"]
        transaccion= controlador_transaccion.obtener_transaccion_por_id(transaccion_id)
        persona=controlador_personas.obtener_persona_por_id(persona_id)
        if transaccion is not None:
            if persona is not None:
                controlador_detalle_alojamiento.insertar_detalle_alojamiento(transaccion_id,persona_id)
                return jsonify({"Mensaje":"Detalle alojamiento guardada correctamente"})
            return jsonify({"Mensaje":"Detalle alojamiento no guardado"})
        # De cualquier modo, y si todo fue bien, redireccionar
        return jsonify({"Mensaje":"Detalles de alojamiento no guardado"})
    except Exception as e:
        return jsonify({"Mensaje": str(e)})


@app.route("/api_actualizardetalle_alojamiento", methods=["POST"])
@jwt_required()
def api_actualizardetalle_alojamiento():
    try:
        id = request.json["id"]
        transaccion_id = request.json["transaccion_id"]
        persona_id = request.json["persona_id"]
        transaccion= controlador_transaccion.obtener_transaccion_por_id(transaccion_id)
        persona=controlador_personas.obtener_persona_por_id(persona_id)
        if transaccion is not None:
            if persona is not None:
                controlador_detalle_alojamiento.actualizar_detalle_alojamiento(transaccion_id,persona_id, id)
                return jsonify({"Mensaje":"Detalle alojamiento  actualizada"})
            return jsonify({"Mensaje":"Detalle alojamiento no actualizada"})
        # De cualquier modo, y si todo fue bien, redireccionar
        return jsonify({"Mensaje":"Detalles de alojamiento no actualizada"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_eliminardetalle_alojamiento", methods=["POST"])
@jwt_required()
def api_eliminardetalle_alojamiento():
    try:
        controlador_detalle_alojamiento.eliminar_detalle_alojamiento(request.json["id"])
        return jsonify({"Mensaje":"Detalles de alojamiento eliminada correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_obtenerdetalle_alojamiento/<int:id>")
@jwt_required()
def api_obtenerdetalle_alojamiento(id):
    try:
        detalle_alojamiento = controlador_detalle_alojamiento.obtener_detalle_alojamiento_por_id(id)
        listaserializable = []
        miobj = clase_detalle_alojamiento.detalle_alojamiento(detalle_alojamiento[0], detalle_alojamiento[1],detalle_alojamiento[2])
        detalle_alojamiento_serializable = miobj.midic.copy()
        listaserializable.append(detalle_alojamiento_serializable)
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

# APIs - Fin

@app.route("/agregar_detalle_alojamiento")
def formulario_agregar_detalle_alojamiento():
    personas=controlador_personas.obtener_personas()
    transaccion=controlador_transaccion.obtener_transaccion()
    return render_template("agregar_detalle_alojamiento.html", transaccion=transaccion, personas=personas)


@app.route("/guardar_detalle_alojamiento", methods=["POST"])
def guardar_detalle_alojamiento():
    transaccion_id = request.form["transaccion_id"]
    persona_id = request.form["persona_id"]
    transaccion= controlador_transaccion.obtener_transaccion_por_id(transaccion_id)
    persona=controlador_personas.obtener_persona_por_id(persona_id)
    if transaccion is not None:
        if persona is not None:
            controlador_detalle_alojamiento.insertar_detalle_alojamiento(transaccion_id,persona_id)
            return redirect("/detalle_alojamiento")
        # De cualquier modo, y si todo fue bien, redireccionar
        return redirect("/detalle_alojamiento")
    return redirect("/detalle_alojamiento")



@app.route("/")
@app.route("/detalle_alojamiento")
def detalle_alojamiento():
    detalle_alojamiento = controlador_detalle_alojamiento.obtener_detalle_alojamiento()
    return render_template("detalle_alojamiento.html", detalle_alojamiento=detalle_alojamiento)


@app.route("/eliminar_detalle_alojamiento", methods=["POST"])
def eliminar_detalle_alojamiento():
    controlador_detalle_alojamiento.eliminar_detalle_alojamiento(request.form["id"])
    return redirect("/detalle_alojamiento")


@app.route("/formulario_editar_detalle_alojamiento/<int:id>")
def editar_detalle_alojamiento(id):
    # Obtener el detalle_alojamiento por ID
    transaccion=controlador_transaccion.obtener_transaccion()
    personas=controlador_personas.obtener_personas()
    detalle_alojamiento = controlador_detalle_alojamiento.obtener_detalle_alojamiento_por_id(id)
    return render_template("editar_detalle_alojamiento.html", detalle_alojamiento=detalle_alojamiento,  transaccion=transaccion, personas=personas)


@app.route("/actualizar_detalle_alojamiento", methods=["POST"])
def actualizar_detalle_alojamiento():
    id = request.form["id"]
    transaccion_id = request.form["transaccion_id"]
    persona_id = request.form["persona_id"]
    transaccion= controlador_transaccion.obtener_transaccion_por_id(transaccion_id)
    persona=controlador_personas.obtener_persona_por_id(persona_id)
    if transaccion is not None:
        if persona is not None:
            controlador_detalle_alojamiento.actualizar_detalle_alojamiento(transaccion_id, persona_id, id)
            return redirect("/detalle_alojamiento")
        # De cualquier modo, y si todo fue bien, redireccionar
        return redirect("/detalle_alojamiento")
    return redirect("/detalle_alojamiento")

@app.route("/documentacion_habitacion")
def documentacion_habitacion():
    return render_template("documentacion_habitacion.html")


@app.route("/docu_detalle_servicios")
def docu_detalle_servicios():
    return render_template("docu_detalle_servicios.html")

@app.route("/documentacion_servicio")
def documentacion_servicio():
    return render_template("documentacion_servicio.html")

@app.route("/documentacion_transaccion")
def documentacion_transaccion():
    return render_template("documentacion_transaccion.html")

@app.route("/documentacion_personas")
def documentacion_personas():
    return render_template("documentacion_personas.html")

@app.route("/documentacion_categoria_habitacion")
def documentacion_categoria_habitacion():
    return render_template("documentacion_categoria_habitacion.html")

@app.route("/documentacion_detalle_alojamiento")
def documentacion_detalle_alojamiento():
    return render_template("documentacion_detalle_alojamiento.html")

@app.route("/documentacion_detalle_comprobante")
def documentacion_detalle():
    return render_template("documentacion_detalleComprobante.html")

@app.route("/documentacion_comprobante")
def documentacion_comprobante():
    return render_template("documentacion_comprobante.html")

@app.route("/index")
def index():
    return render_template("index.html")



@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity





# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
