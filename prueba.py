
from flask import Flask, Response
from flask import jsonify
from flask import request
from flask import session
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from flask_cors import CORS
import datetime
import json
from bson import json_util, ObjectId
from flask_mail import Mail,  Message

from openpyxl import Workbook, cell
from openpyxl.writer.excel import save_virtual_workbook
from openpyxl.styles import Alignment


app = Flask(__name__)
CORS(app)


app.secret_key = 'clavedelaaplicacion'
api = Api(app)

mongo = PyMongo(app, 'mongodb://localhost:27017/Aplicacion')
# print(dir(mongo.db.list_collection_names()))
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = 'adminsalas@udistrital.edu.co',
    MAIL_PASSWORD = 'ifucqwojzofscpzw'
)

mail = Mail(app)

class Usuario(Resource):
    status = 0
    datos = {}
    mensaje = ""
    token = '79548af95a6f0d909441d77c3814a3f36030dc317d05a9204dfd8172b7f51b6'

    def login(self):
        user = mongo.db.Usuarios
        usuario = request.json['usuario']
        contrasena = request.json['contrasena']
        tipo= ""
        pregunta = user.find_one(
            {"Código_usuario": usuario, "Contraseña": contrasena})  
        if pregunta:
            tipo = pregunta['Tipo']
            print(tipo)
            mensaje = "1"
            self.status = 1
            if tipo == "Laboratorista":
               self.datos = {'token': self.token, 'addr':"HomeLaboratorista", 'kind':"1"}       
            elif tipo == "Administrador":
                self.datos = {'token': self.token, 'addr':"HomeAdmin", 'kind':"2"}
            elif tipo == "Estudiante":
                self.datos = {'token': self.token, 'addr':"reservaestudiante", 'kind':"3"}
        else:  
            mensaje = "0"
            print(mensaje)
            self.status = 1    
        return mensaje

    def isLoggedIn(self):
        return self.token

    def cerrarSesion(self):
        session.pop('tipoUsuario', None)
        return "1"

    def registrar(self):
        mensaje = "0"
        user = mongo.db.Usuarios
        usuario = request.json['usuario']
        identificacion = request.json['identificacion']
        correo = request.json['correo']
        estado = request.json['estado']
        proyecto = request.json['proyecto']
        contraseña = request.json['contraseña']
        tipousuario = request.json['tipousuario']
        pregunta = user.find_one({"Código_usuario": identificacion})
        if pregunta:
            mensaje = "Este Laboratorista ya existe en el sistema"
            self.status = 1
        else:
            nuevoUsuario = user.insert({'Nombre_usuario': usuario, 'Código_usuario': identificacion, 'Correo_usuario': correo,
                                        'Código_Estado': estado, 'Proyecto_Curricular': proyecto, 'Contraseña': contraseña, 'Tipo': tipousuario})
            mensaje = "Usuario Registrado correctamente"
            self.status = 1
        return mensaje

    def desactivar(self):
        user = mongo.db.Usuarios
        codigo = request.json['codigo']
        print(codigo)
        estado = "NA"
        mensaje = "Desactivado"
        desactivar = user.update({"Código_usuario": codigo}, {
                                 "$set": {"Código_Estado": estado}})
        if desactivar:
            self.status = 1
            mensaje
        return mensaje

    def editaruser(self):
        user = mongo.db.Usuarios
        codigo = request.json['codigo']
        usuario = request.json['usuario']
        correo = request.json['correo']
        mensaje = "Laboratorista actualizado"
        actualizardatos = user.update({"Código_usuario": codigo}, {"$set": {
                                      "Nombre_usuario": usuario, "Correo_usuario": correo}})
        if actualizardatos:
            self.status = 1
            mensaje
        return mensaje

    def resetpass(self):
        user = mongo.db.Usuarios
        codigo = request.json['codigo']
        contraseña = request.json['codigo']
        mensaje = "Clave restaurada"
        actualizarpass = user.update({"Código_usuario": codigo}, {
                                     "$set": {"Contraseña": contraseña}})
        if actualizarpass:
            self.status = 1
            mensaje
        return mensaje

    def editaruserlab(self):
        user = mongo.db.Usuarios
        codigo = request.json['codigo']
        usuario = request.json['usuario']
        correo = request.json['correo']
        mensaje = "Datos actualizados"
        actualizardatos = user.update({"Código_usuario": codigo}, {
                                      "$set": {"Nombre_usuario": usuario, "Correo_usuario": correo}})
        if actualizardatos:
            self.status = 1
            mensaje
        return mensaje

    def editpass(self):
        user = mongo.db.Usuarios
        codigo = request.json['codigo']
        contraseña = request.json['contraseña']
        nuevacontraseña = request.json['nuevacontraseña']
        mensaje = "Contraseña actualizada"
        actualizarpass = user.update({"$and": [{'Código_usuario': codigo}, {
            'Contraseña': contraseña}]}, {"$set": {"Contraseña": nuevacontraseña}})
        if actualizarpass:
            self.status = 1
            mensaje
        return mensaje

    def editpassadmin(self):
        mensaje = "0"
        user = mongo.db.Usuarios
        codigo = request.json['codigo']
        contraseña = request.json['contraseña']
        nuevacontraseña = request.json['nuevacontraseña']
        pregunta = user.find_one(
            {"$and": [{'Código_usuario': codigo}, {'Contraseña': contraseña}]})
        if pregunta:
            user.update({"$and": [{'Código_usuario': codigo}, {'Contraseña': contraseña}]}, {
                "$set": {"Contraseña": nuevacontraseña}})
            self.status = 1
            mensaje = "Contraseña actualizada"
        else:
            mensaje = "Las contraseñas no corresponden"
            self.status = 2
        return mensaje

    def activar(self):
        user = mongo.db.Usuarios
        codigo = request.json['codigo']
        print(codigo)
        estado = "A"
        mensaje = "Activado"
        activar = user.update({"Código_usuario": codigo}, {
                              "$set": {"Código_Estado": estado}})
        if activar:
            self.status = 1
            mensaje
        return mensaje

    def reserva(self):
        mensaje = "0"
        user = mongo.db.Prestamo
        usuario = request.json['usuario']
        codigo = request.json['codigo']
        hora = request.json['hora']
        fecha_adicional = request.json['fecha_adicional']
        x = datetime.datetime.now()
        fecha_reserva = x.strftime("%d/%m/%Y")
        fecha_dt = datetime.datetime.strptime(fecha_adicional, '%d/%m/%Y')
        dia = fecha_dt.strftime("%A")
        sala = request.json['sala']
        banco = request.json['banco']
        practica = request.json['practica']
        elemento = request.json['elemento']
        estado = "PENDIENTE"
        reservas = user.find({'Codigo': codigo}).count()
        if (reservas == 3):
            self.status = 2
            mensaje = "Ya tiene tres laboratorios"
        else:
            nuevaReserva = user.insert({'Hora': hora, 'Dia': dia, 'Fecha_Adicional': fecha_adicional, 'Fecha_reserva': fecha_reserva,
                                        'Codigo': codigo, 'Usuario': usuario, 'Sala': practica
                                        , 'Banco': banco
                                        , 'Elemento': elemento, 'Estado': estado})
            mensaje = "Laboratorio Registrado correctamente"
            self.status = 1
        return mensaje

    def consultabanco(self):
        mensaje = "0"
        user = mongo.db.Prestamo
        hora = request.json['hora']
        fecha_adicional = request.json['fecha_adicional']
        sala = request.json['sala']
        banco = request.json['banco']
        pregunta = user.find_one({"$and": [{'Sala': sala}, {'Hora': hora}, {
                                 'Fecha_Adicional': fecha_adicional}, {'Banco': banco}]})
        if pregunta != None:
            self.status = 1
            mensaje = "banco ocupado"
        return mensaje

    def buscarreserva(self):
        user = mongo.db.Prestamo
        codigo = request.json['codigo']
        output = []
        self.status = 1
        mensaje = "Encontrado"
        for u in user.find({"Codigo": codigo}):
            output.append({'hora': u['Hora'], 'dia': u['Dia'], 'fecha_adicional': u['Fecha_Adicional'],
                           'fecha_reserva': u['Fecha_reserva'], 'sala': u['Sala'], 'banco': u['Banco'], 'elemento': u['Elemento']})
        return {'status': self.status, 'mensaje': mensaje, 'data': output}

    def buscarreservalabo(self):
        user = mongo.db.Prestamo
        output = []
        self.status = 1
        mensaje = "Encontrado"
        for u in user.find():
            output.append({'hora': u['Hora'], 'dia': u['Dia'], 'fecha_reserva': u['Fecha_reserva'],
                           'sala': u['Sala'], 'banco': u['Banco'], 'elemento': u['Elemento'], 'codigo': u['Codigo'], 'usuario': u['Usuario'], 'estado': u['Estado']})
        return {'status': self.status, 'mensaje': mensaje, 'data': output}

    def borrarreserva(self):
        user = mongo.db.Prestamo
        codigo = request.json['codigo']
        sala = request.json['sala']
        banco = request.json['banco']
        borrar = user.delete_one(
            {"$and": [{'Codigo': codigo}, {'Sala': sala}, {'Banco': banco}]})
        print(codigo)
        if borrar:
            self.status = 1
            mensaje = "usuarios eliminados"
        return mensaje

    def editarreserva(self):
        user = mongo.db.Prestamo
        codigo = request.json['codigo']
        hora = request.json['hora']
        fecha_adicional = request.json['fecha_adicional']
        fecha_reserva = request.json['fecha_reserva']
        dia = request.json['dia']
        sala = request.json['sala']
        banco = request.json['banco']
        elemento = request.json['elemento']
        mensaje = "Reserva actualizada"
        actualizardatos = user.update({"$and": [{'Sala': sala}, {'Hora': hora}, {'Dia': dia}, {'Fecha_Adicional': fecha_adicional}, {
                                      'Fecha_reserva': fecha_reserva}, {'Banco': banco}, {'Codigo': codigo}]}, {"$set": {"Elemento": elemento}})
        print(actualizardatos)
        if actualizardatos:
            self.status = 1
            mensaje
        return mensaje

    def buscarhorarios(self):
        user = mongo.db.Horario
        output = []
        self.status = 1
        mensaje = "Encontrado"
        for u in user.find():
            output.append({'asignatura': u['Asignatura'], 'docente': u['Docente'], 'proyecto': u['Proyecto'], 'grupo': u['Grupo'],
                           'dia': u['Dia'], 'horario': u['Horario'], 'sala': u['Sala'], 'fecha': u['Fecha ']})
        return {'status': self.status, 'mensaje': mensaje, 'data': output}

    def consultarLabo(self):
        usuario = mongo.db.Usuarios
        tipo = "Laboratorista"
        output = []
        self.status = 1
        mensaje = "Encontrado"
        for u in usuario.find({"Tipo": tipo}):
            output.append({'usuario': u['Nombre_usuario'], 'correo': u['Correo_usuario'],
                           'estado': u['Código_Estado'], 'identificacion': u['Código_usuario']})
        return {'status': self.status, 'mensaje': mensaje, 'data': output}

    def consultaeditlabo(self):
        print("HOLA AUXILIO")#BORRAR ESTO
        usuario = mongo.db.Usuarios
        codigo = request.json['codigo'] #NO ESTA LLEGANDO EL CÓDIGO DEL USUARIO        
        tipo = "Laboratorista"
        output = []
        self.status = 1
        mensaje = "Encontrado"
        print("HOLA AUXILIO 222")#BORRAR ESTO
        print([request.json['codigo'],codigo,tipo])#BORRAR ESTO


        for u in usuario.find({"$and": [{"Código_usuario": codigo}, {"Tipo": tipo}]}):
            print("11111POR")#BORRAR ESTO
            output.append(
                {'usuario': u['Nombre_usuario'], 'correo': u['Correo_usuario']})



        print("HOLA AUXILIO 333")#BORRAR ESTO
        return {'status': self.status, 'mensaje': mensaje, 'data': output}

    def consultaeditadmin(self):
        usuario = mongo.db.Usuarios
        codigo = request.json['codigo']
        tipo = "Administrador"
        output = []
        self.status = 1
        mensaje = "Encontrado"
        for u in usuario.find({"$and": [{"Código_usuario": codigo}, {"Tipo": tipo}]}):
            output.append(
                {'usuario': u['Nombre_usuario'], 'correo': u['Correo_usuario']})
        return {'status': self.status, 'mensaje': mensaje, 'data': output}

    def consultarEquipo(self):
        elemento = mongo.db.Elementos
        sede = "FICC01"
        output = []
        self.status = 1
        encontrar = elemento.find({"Id_Sede": sede})
        if encontrar:
            mensaje = "Equipo Encontrado"
            for u in elemento.find({"Id_Sede": sede}):
                output.append({'placa': u['Placa'], 'nombreEquipo': u['Nombre_Del_Equipo'], 'estado': u['Estado'],'serie':u['Serie'], 'modelo':u['Referencia/Modelo'],
                               'marca': u['Marca'],  'numeroInterno': u['Codigo_Interno'], 'sede':u['Sede'], 'idSede':u['Id_Sede'],'dependencia':u['Dependencia'],'idUbicacion':u['Id_Ubicacion'],
                               'espacioFisico': u['Espacio_Fisico'], 'proveedor':u['Proveedor'], 'valorElemento':u['Valor_Elemento'], 'nit':u['Nit'],'ivaAplicado':u['Iva_Aplicado'],
                               'tipoContrato':u['Tipo_De_Contrato'],'totalValorelemento':u['Total_Valor_Elemento'], 'cantidadAsignada':u['Cantidad_Asignada'],'vigencia':u['Vigencia'],
                               'fechaAdquisicion':u['Fecha_De_Adquisicion'], 'numeroContrato':u['Numero_De_Contrato'], 'numeroFactura':u['#_De_Factura_Compra'], 'tiempoGarantia':u['Tiempo_De_Garantia'],
                               'frecuenciaMantenimiento':u['Frecuencia_De_Mantenimiento'],'manual':u['Cuenta_Con_Manual'],'tiempoVidautil':u['Tiempo_De_Vida_Util'],'tipoUso':u['Tipo_De_Uso'],
                               'potenciaElectrica':u['Potencia_Electrica'], 'tipoUso_otro':u['Tipo_De_Uso_Otro'], 'paisOrigen':u['Pais_De_Origen'],'impactoEquipo':u['Impacto_Uso_Del_Equipo'],
                               'especificacionesTecnicas':u['Especificaciones_Tecnicas'], 'accesorios' :u['Accesorios'], 'documentoFuncionario':u['Documento_Funcionario'], 'nombreFuncionario':u['Nombre_Del_Funcionario']
                               })
        else:
            mensaje = "no se encontro"
        return {'status': self.status, 'mensaje': mensaje, 'data': output}

    def editarequipo(self):
        elemento = mongo.db.Elementos
        placa = request.json['placa']
        sala = request.json['sala']
        mensaje = "Ubicación del equipo actualizada"
        actualizardatos = elemento.update({"Placa": placa}, {"$set": {
            "Espacio_Fisico": sala}})
        if actualizardatos:
            self.status = 1
        else:
            self.status = 0
        return {'status': self.status, 'mensaje': mensaje}

    def desactivarEquipo(self):
        elemento = mongo.db.Elementos
        placa = request.json['placa']
        estado = "NO ACTIVO"
        mensaje = "Desactivado"
        desactivar = elemento.update({"Placa": placa}, {
            "$set": {"Estado": estado}})
        if desactivar:
            self.status = 1
            mensaje
        return mensaje

    def activarEquipo(self):
        elemento = mongo.db.Elementos
        placa = request.json['placa']
        estado = "ACTIVO"
        mensaje = "Activado"
        activar = elemento.update({"Placa": placa}, {
            "$set": {"Estado": estado}})
        if activar:
            self.status = 1
            mensaje
        return mensaje

    def registrarEquipo(self):
        mensaje = "0"
        elemento = mongo.db.Elementos
        placa = request.json['placa']
        serial = request.json['serial']
        nombreEquipo = request.json['nombreEquipo']
        serie = request.json['serie']
        estado = request.json['estado']
        modelo = request.json['modelo']
        marca = request.json['marca']
        numeroInterno = request.json['numeroInterno']
        sede = request.json['sede']
        idSede = request.json['idSede']
        dependencia = request.json['dependencia']
        idUbicacion = request.json['idUbicacion']
        espacioFisico = request.json['espacioFisico']
        proveedor = request.json['proveedor']
        valorElemento = request.json['valorElemento']
        nit = request.json['nit']
        ivaAplicado = request.json['ivaAplicado']
        tipoContrato = request.json['tipoContrato']
        totalValorelemento = request.json['totalValorelemento']
        cantidadAsignada = request.json['cantidadAsignada']
        vigencia = request.json['vigencia']
        fechaAdquisicion = request.json['fechaAdquisicion']
        numeroContrato = request.json['numeroContrato']
        numeroFactura = request.json['numeroFactura']
        tiempoGarantia = request.json['tiempoGarantia']
        frecuenciaMantenimiento = request.json['frecuenciaMantenimiento']
        manual = request.json['manual']
        tiempoVidautil = request.json['tiempoVidautil']
        tipoUso = request.json['tipoUso']
        potenciaElectrica = request.json['potenciaElectrica']
        tipoUso_otro = request.json['tipoUso_otro']
        paisOrigen = request.json['paisOrigen']
        impactoEquipo = request.json['impactoEquipo']
        especificacionesTecnicas = request.json['especificacionesTecnicas']
        accesorios = request.json['accesorios']
        documentoFuncionario = request.json['documentoFuncionario']
        nombreFuncionario = request.json['nombreFuncionario']
        laboratorista = request.json['laboratorista']
        pregunta = elemento.find_one({"Placa": placa})
        if pregunta:
            mensaje = "Este equipo ya existe en el sistema"
            self.status = 1
        else:
            nuevoElemento = elemento.insert({'Placa': placa, 'Serial': serial, 'Nombre_Del_Equipo': nombreEquipo,
                                             'Serie': serie, 'Estado': estado,
                                             'Referencia/Modelo': modelo, 'Marca': marca, 'Codigo_Interno': numeroInterno, 
                                             'Sede': sede, 'Id_Sede': idSede, 'Dependencia': dependencia, 'Id_Ubicacion': idUbicacion,
                                             'Espacio_Fisico': espacioFisico, 'Proveedor': proveedor, 'Valor_Elemento': valorElemento,
                                             'Nit': nit, 'Iva_Aplicado': ivaAplicado, 'Tipo_De_Contrato': tipoContrato, 'Total_Valor_Elemento': totalValorelemento,
                                             'Cantidad_Asignada': cantidadAsignada,
                                             'Vigencia': vigencia, 'Fecha_De_Adquisicion': fechaAdquisicion, 'Numero_De_Contrato': numeroContrato,
                                             '#_De_Factura_Compra': numeroFactura, 'Tiempo_De_Garantia': tiempoGarantia, 'Frecuencia_De_Mantenimiento': frecuenciaMantenimiento,
                                             'Cuenta_Con_Manual': manual, 'Tiempo_De_Vida_Util': tiempoVidautil, 'Tipo_De_Uso': tipoUso, 'Potencia_Electrica': potenciaElectrica,
                                             'Tipo_De_Uso_Otro': tipoUso_otro, 'Pais_De_Origen': paisOrigen, 'Impacto_Uso_Del_Equipo': impactoEquipo,
                                             'Especificaciones_Tecnicas': especificacionesTecnicas, 'Accesorios': accesorios,'Documento_Funcionario': documentoFuncionario,
                                             'Nombre_Del_Funcionario': nombreFuncionario, 'Laboratorista':laboratorista})
            mensaje = "Equipo Registrado correctamente"
            self.status = 1
        return mensaje

    def registrarMant(self):
        mensaje = "0"
        elemento = mongo.db.Mantenimientos
        fecha = request.json['fecha']
        fechaReal = request.json['fechaReal']
        placa = request.json['placa']
        codUsu = request.json['codUsu']
        numInterno = request.json['numInterno']
        nomUsu = request.json['nomUsu']
        nomEqu = request.json['nomEqu']
        sala = request.json['sala']
        numeroInterno = request.json['numeroInterno']
        descDano = request.json['descDano']
        nomEmpresa = request.json['nomEmpresa']
        nit = request.json['nit']
        tiempoGar = request.json['tiempoGar']
        costMant = request.json['costMan']
        numOrdServ = request.json['numOrdServ']
        vigencia = request.json['vigencia']
        supervisor = request.json['supervisor']
        repuestos = request.json['repuestos']
        proxMant = request.json['proxMant']
        espMantReal = request.json['espMantReal']
        observaciones = request.json['observaciones']
        nuevoElemento = elemento.insert({'Fecha':fecha,'fechaRealizacion':fechaReal,'Placa':placa,'codUsu':codUsu,'numInterno':numInterno,'nomUsu':nomUsu,'nomEqu':nomEqu,'sala':sala,'numeroInterno':numeroInterno,'nomUsu':nomUsu,'nomEqu':nomEqu,'sala':sala,'numeroInterno':numeroInterno,'descDano':descDano,'nomEmpresa':nomEmpresa,'nit':nit,'tiempoGar':tiempoGar,'costMant':costMant,'numOrdServ':numOrdServ,'vigencia':vigencia,'supervisor':supervisor,'repuestos':repuestos,'proxMant':proxMant,'espMantReal':espMantReal,'observaciones':observaciones})
        mensaje = "Mantenimiento Registrado correctamente"
        self.status = 1
        return mensaje


    def consultaMantenimiento(self):
        mantenimiento = mongo.db.Mantenimiento
        output = []
        self.status = 1
        encontrar = mantenimiento.find({})
        if encontrar:
            mensaje = "Mantenimientos Encontrados"
            for u in mantenimiento.find({}):
                output.append({'placa': u['Placa'], 'laboratorista': u['Nombre_Usuario'], 'fechaMantenimiento': u['Fecha'],'sala':u['Sala'], 'dano':u['Descripcion_Dano'],
                               'tipoMantenimiento': u['Tipo_De_Mantenimiento'],  'numeroInterno': u['Numero_Interno'], 'hora':u['Horario'], 'estado':u['Estado']
                               })
        else:
            mensaje = "no se encontro"
        return {'status': self.status, 'mensaje': mensaje, 'data': output}    


    def consultaTraslados(self):
        traslado = mongo.db.Traslados
        output = []
        self.status = 1
        codigoLab = request.json['codigoLab']
        estado = "PENDIENTE"
        encontrar = traslado.find({})
        if encontrar:

            mensaje = "Traslados encontrados"
            for u in traslado.find({"$and": [{"Codigo_Laboratorista": codigoLab}, {"Estado": estado}]}):
                output.append({'placa': u['Placa'], 'nombreEquipo': u['Nombre_Equipo'],'salaOrigen': u['Sala_Origen'], 'salaDestino': u['Sala_Destino'], 'codigoLaboratorista': u['Codigo_Laboratorista'],
                               'laboratorista': u['Nombre_Laboratorista'],'estado':u['Estado'], 'ubicacionExacta' :u['Ubicacion_Exacta']
                               })
        else:
            mensaje = "No hay traslados pendientes"
            
        return {'status': self.status, 'mensaje': mensaje, 'data': output} 
            

    def buscarUno(self):
        mensaje = "0"
        user = mongo.db.Usuarios
        identificacion = request.json['identificacion']
        pregunta = user.find_one({"identificacion": identificacion})
        if pregunta:
            mensaje = "Encontrado"
            self.status = 1
            self.datos = {
                "usuario": pregunta['usuario'], "correo": pregunta['correo'], "telefono": pregunta['telefono']}
        else:
            mensaje = "No fue encontrado"
            self.status = 2
        return mensaje

    def borrarPrueba(self):
        usuario = mongo.db.Usuarios
        usuarioBusc = request.json['usuario']
        print(usuarioBusc)
        borrar = usuario.delete_one({'usuario': usuarioBusc})
        if borrar:
            self.status = 1
            mensaje = " usuarios eliminados"
        return mensaje

    def post(self, accion):
        mensaje = "error"
        if accion == "registrar":
            mensaje = self.registrar()
        elif accion == "desactivar":
            mensaje = self.desactivar()
        elif accion == "desactivarEquipo":
            mensaje = self.desactivarEquipo()
        elif accion == "activarEquipo":
            mensaje = self.activarEquipo()
        elif accion == "editaruser":
            mensaje = self.editaruser()
        elif accion == "editarequipo":
            mensaje = self.editarequipo()
        elif accion == "registrarEquipo":
            mensaje = self.registrarEquipo()    
        elif accion == "editaruserlab":
            mensaje = self.editaruserlab()
        elif accion == "editpass":
            mensaje = self.editpass()
        elif accion == "editpassadmin":
            mensaje = self.editpassadmin()
        elif accion == "resetpass":
            mensaje = self.resetpass()
        elif accion == "activar":
            mensaje = self.activar()
        elif accion == "buscarUno":
            mensaje = self.buscarUno()
        elif accion == "login":
            mensaje = self.login()   
        elif accion == "borrar":
            mensaje = self.borrarPrueba()
        elif accion == "reserva":
            mensaje = self.reserva()
        elif accion == "buscarreserva":
            respuesta = self.buscarreserva()
            mensaje = respuesta['mensaje']
            self.datos = respuesta['data']
        elif accion == "borrarreserva":
            mensaje = self.borrarreserva()
        elif accion == "editarreserva":
            mensaje = self.editarreserva()
        elif accion == "consultaeditlabo":
            respuesta = self.consultaeditlabo()
            mensaje = respuesta['mensaje']
            self.datos = respuesta['data']
        elif accion == "consultaeditadmin":
            respuesta = self.consultaeditadmin()
            mensaje = respuesta['mensaje']
            self.datos = respuesta['data']
        elif accion == "consultaTraslados":
            respuesta = self.consultaTraslados()
            mensaje = respuesta['mensaje']
            self.datos = respuesta['data']
        elif accion == "consultabanco":
            mensaje = self.consultabanco()
        elif accion == "registrarMant":
            mensaje = self.registrarMant()
        else:
            self.status = 2
            mensaje = "Error en la peticion"
            print(mensaje)     
        return {'status': self.status, 'mensaje': mensaje, 'data': self.datos}

    def get(self, accion):
        mensaje = "error"
        if accion == "consultarTodos":
            respuesta = self.consultarTodos()
            mensaje = respuesta['mensaje']
            self.datos = respuesta['data']
        elif accion == "buscarreservalabo":
            respuesta = self.buscarreservalabo()
            mensaje = respuesta['mensaje']
            self.datos = respuesta['data']
        elif accion == "buscarhorarios":
            respuesta = self.buscarhorarios()
            mensaje = respuesta['mensaje']
            self.datos = respuesta['data']
        elif accion == "logueado":
            mensaje = self.isLoggedIn()
        elif accion == "cerrarSesion":
            mensaje = self.cerrarSesion()
        elif accion == "consultarLabo":
            respuesta = self.consultarLabo()
            mensaje = respuesta['mensaje']
            self.datos = respuesta['data']
        elif accion == "consultarEquipo":
            respuesta = self.consultarEquipo()
            mensaje = respuesta['mensaje']
            self.datos = respuesta['data']
        elif accion == "consultaMantenimiento":
            respuesta = self.consultaMantenimiento()
            mensaje = respuesta['mensaje']
            self.datos = respuesta['data']           
        elif accion == "getToken":
            mensaje = self.token


        ############### Pruebas Excel ###########################
        elif accion == "createExcel":
            libro = Workbook()
            docExcel = libro["Sheet"]

            docExcel.merge_cells('B2:I2')
            docExcel.merge_cells('B3:I3')
            docExcel.merge_cells('B4:I4')

            docExcel["B2"]="MANTENIMIENTOS LABORATORIOS DE INGENIERIA"
            docExcel["B3"]="SALAS DE INFORMATICA TRIMESTRE II"
            docExcel["B4"]="PERIODO COMPRENDIDO ENTRE EL 1 DE ABRIL HASTA EL 30 DE ABRIL DEL 2020"
            
            return Response(
                save_virtual_workbook(libro),
                headers={
                'Content-Disposition': 'attachment; filename=Prueba.xlsx',
                'Content-type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                }
            )          
        else:
            self.status = 2
            mensaje = "Error en la peticion"
        return {'status': self.status, 'mensaje': mensaje, 'data': self.datos}


@app.route('/ConsultaSelect2', methods=['POST'])
def consultarTodos():
    usuario = mongo.db.Usuarios
    output = []
    buscar = request.form['q']
    mensaje = "Encontrado"
    for u in usuario.find({"Nombre_usuario": {'$regex': '.*'+buscar+'.*','$options':"i"}}):
        output.append({'id': u['Nombre_usuario'], 'text': u['Correo_usuario'],
                       'estado': u['Código_Estado'], 'identificacion': u['Código_usuario']})
    resp = app.make_response(jsonify(output))
    resp.headers.add('Access-Control-Allow-Origin', '*')
    resp.headers.add('Access-Control-Allow-Credentials', 'true')
    resp.headers.add('Access-Control-Allow-Headers',
                     'Content-Type,Authorization')
    return resp

@app.route('/consAddMantLab', methods=['POST'])
def consultarLabora():
    usuario = mongo.db.Usuarios
    output = []
    buscar = request.form['q']
    mensaje = "Encontrado"
    for u in usuario.find({"$and":[{"Nombre_usuario": {'$regex': '.*'+buscar+'.*','$options':"i"}},{"Tipo":"Laboratorista"}]}):
        output.append({'id': u['Código_usuario'], 'text': u['Código_usuario']+' - '+u['Nombre_usuario'], 'nombre': u['Nombre_usuario']})
    resp = app.make_response(jsonify(output))
    resp.headers.add('Access-Control-Allow-Origin', '*')
    resp.headers.add('Access-Control-Allow-Credentials', 'true')
    resp.headers.add('Access-Control-Allow-Headers',
                     'Content-Type,Authorization')
    return resp

@app.route('/consAddMantPlaca', methods=['POST'])
def consultarPorPlaca():
    elemento = mongo.db.Elementos
    output = []
    buscar = request.form['q']
    mensaje = "Encontrado"
    for u in elemento.find({"$or":[{"Placa": {'$regex': '.*'+buscar+'.*','$options':"i"}},{"Espacio_Fisico": {'$regex': '.*'+buscar+'.*','$options':"i"}},{"Nombre_Del_Equipo": {'$regex': '.*'+buscar+'.*','$options':"i"}}]}):
        output.append({'id': u['Placa'], 'text': u['Placa']+'-'+u['Nombre_Del_Equipo'],'numInterno':u['Codigo_Interno'],'nomEqu':u['Nombre_Del_Equipo'],'sala':u['Espacio_Fisico']})
    resp = app.make_response(jsonify(output))
    resp.headers.add('Access-Control-Allow-Origin', '*')
    resp.headers.add('Access-Control-Allow-Credentials', 'true')
    resp.headers.add('Access-Control-Allow-Headers',
                     'Content-Type,Authorization')
    return resp


@app.route('/login', methods=['POST'])
def saludo():
    user = mongo.db.Usuarios
    usuario = request.json['usuario']
    contrasena = request.json['contrasena']
    pregunta = user.find_one(
        {"Código_usuario": usuario, "Contraseña": contrasena})
    token = ''
    if pregunta:
        session['tipoUsuario'] = "Admin"
        tokenGen = urandom(64)
        session['token'] = b64encode(tokenGen).decode('utf-8')
        token = session['token']
        mensaje = "1"
        status = 1
    else:
        mensaje = "0"
        status = 1
    resp = app.make_response(
        jsonify({'status': status, 'mensaje': mensaje, 'data': {'token': token}}))
    resp.set_cookie('Autorizacion', 'si')
    resp.headers.add('Access-Control-Allow-Origin', '*')
    resp.headers.add('Access-Control-Allow-Credentials', 'true')
    resp.headers.add('Access-Control-Allow-Methods',
                     'GET,PUT,POST,DELETE,OPTIONS')
    resp.headers.add('Access-Control-Allow-Headers',
                     'Content-Type,Authorization')
    return resp


api.add_resource(Usuario, '/Usuario/<string:accion>')  # Route_1

if __name__ == '__main__':
    app.secret_key = 'ssssshhhhh'
    app.run(port='7001', ssl_context='adhoc')


@app.route('/send-mail/')
def send_mail():
    msg = mail.send_message(
        'Send Mail tutorial!',
        sender='adminsalas@udistrital.edu.co',
        recipients=['adminsalas@udistrital.edu.co'],
        body="Prueba del correo."
    )
    return 'Mail sent'

