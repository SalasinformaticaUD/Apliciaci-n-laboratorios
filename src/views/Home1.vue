<template>
  <v-container fluid>
    <Headerhome />

    <v-row no-gutters>
      <!--INGRESO ESTUDIANTES-->
      <v-col align="center" class="mt-4"> 
        <v-card color="#424242" style="padding-left:30px">
          <v-card-title
            class="justify-center"
            style="color:white;font-weigth:bolder;"
          >Consulta y Cancelacion de Laboratorios Adicionales</v-card-title>
          <v-card-subtitle class="text-center" style="color:white">
            Por favor ingrese sus datos, recuerde dar sus datos precisos para
            poder ser identificado
          </v-card-subtitle>
          <v-card-actions>
            <v-row class="justify-center">

              <!--COMENTARIO: rules = numeros, hace que la contraseña sea solo de tipo numerica-->

              <v-col class="col-sm-7 col-lg-4">
                <v-text-field
                  v-model="usuario2"
                  placeholder="Codigo"
                  solo
                  flat
                  :rules="numeroRules" 
                />
                
              </v-col>
              <v-col class="col-sm-7 col-lg-4">
                <v-text-field
                  v-model="contrasena2"
                  placeholder="Contraseña"
                  solo
                  flat
                  :rules="numeroRules"
                  :append-icon="show1 ? 'fas fa-eye' : 'fas fa-eye-slash'"
                  :type="show1 ? 'text' : 'password'"
                  @click:append="show1 = !show1"
                  @keyup.enter="session(usuario2,contrasena2)"
                />
              </v-col>
              <v-col class="col-sm-7 col-lg-4">
                <v-btn
                  color="primary"
                  x-large
                  style="font-weitgh:lighter;font-family:Arial"
                  @click="session(usuario2,contrasena2)"
                >Ingresar</v-btn>
              </v-col>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>


  <!--INGRESO LABORATORISTA-->
    <v-row class="mb-n1 mt-2">
      <v-col class="col-sm-12 col-lg-3">
        <v-card color="#424242" style="height:100%" dark>
          <v-card-title class="justify-center" style="color:#FFFFFF">Ingreso Laboratorista</v-card-title>
          <v-card-subtitle>Como personal Administrativo tienes acceso a los laboratorios desde aqui</v-card-subtitle>
          <v-card-actions>
            <v-container>
              <v-row>
                <v-text-field
                  v-model="usuario3"
                  placeholder="Usuario"
                  solo
                  flat
                  :rules="numeroRules"
                />
              </v-row>
              <v-row>
                <v-text-field
                  v-model="contrasena3"
                  placeholder="Contraseña"
                  solo
                  flat
                  :append-icon="show2 ? 'fas fa-eye' : 'fas fa-eye-slash'"
                  :type="show2 ? 'text' : 'password'"
                  @click:append="show2 = !show2"
                  :rules="numeroRules"
                   @keyup.enter="session(usuario3,contrasena3)"
                />
              </v-row>

              <v-row>
                <v-btn
                  color="primary"
                  x-large
                  style="font-weitgh:lighter;font-family:Arial"
                  @click="session(usuario3,contrasena3)"
                >Ingresar</v-btn>
              </v-row>
            </v-container>
          </v-card-actions>
        </v-card>
      </v-col>

<!--INGRESO ADMINISTRATIVO-->
      <v-col class="col-sm-12 col-lg-3">
        <v-card color="#424242" style="height:100%" dark>
          <v-card-title class="justify-center" style="color:#FFFFFF">Ingreso Administrativo</v-card-title>
          <v-card-subtitle>Como personal Administrativo tienes acceso a los laboratorios desde aqui</v-card-subtitle>
          <v-card-actions>
            <v-container>
              <v-row>
                <v-text-field
                  v-model="usuario"
                  placeholder="Usuario"
                  solo
                  flat
                  :rules="numeroRules"
                />
              </v-row>

              <v-row>
                <v-text-field
                  v-model="contrasena"
                  placeholder="Contraseña"
                  solo
                  flat
                  :append-icon="show3 ? 'fas fa-eye' : 'fas fa-eye-slash'"
                  :type="show3 ? 'text' : 'password'"
                  @click:append="show3 = !show3"
                  :rules="numeroRules"
                   @keyup.enter="session(usuario,contrasena)"
                />
              </v-row>

              <v-row>
                <v-btn
                  color="primary"
                  x-large
                  style="font-weitgh:lighter;font-family:Arial"
                  @click="session(usuario,contrasena)"
                >Ingresar</v-btn>
              </v-row>
            </v-container>
          </v-card-actions>
        </v-card>
      </v-col>

    <!--CALENDARIO -->
      <v-col class="col-sm-12 col-lg-3">
        <v-card color="#424242" dark style="padding:20px">
          <h1 align="center" style="color:#FFFFFF">Calendario</h1>
          <v-sheet height="364.5">
            <v-calendar
              ref="calendar"
              v-model="focus"
              :weekdays="weekday"
              color="primary"
              :events="events"
              :event-color="getEventColor"
              type="month"
            />
          </v-sheet>
        </v-card>
      </v-col>

<!--REGLAMENTO -->
      <v-col class="col-sm-12 col-lg-3">
        <v-card color="#424242" style="height:100%">
          <v-card-title class="justify-center" style="color:white;">NOTAS</v-card-title>
          <v-card-subtitle class="center" style="color:#A0A0A0;font-size:18px" dark>
            Antes de realizar la consulta o cancelacion del laboratorio los
            invitamos a que lean las reglas del laboratorio las cuales se
            encuentran en el siguiente
            <v-card-text style="color:#FFFFFF;width:100%">REGLAMENTO DEL LABORATORIO</v-card-text>
          </v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Headerhome from "@/components/Headerhome.vue";
import jwt_decode from "jwt-decode";
export default {
  components: {
    Headerhome
  },
  data: () => ({
    today: "2019-01-08",
    show1: false,
    show2: false,
    show3: false,
    numeroRules: [
      v => !!v || "Se requiere un código",
      v => /^[0-9]*$/.test(v) || "El código debe ser válido"
    ],
    correoRules: [
      v => !!v || "Se requiere un Correo",
      v => /.+@.+/.test(v) || "El correo debe ser válido"
    ],
    usuario: "",
    contrasena: "",
    usuario2: "",
    contrasena2: "",
    usuario3: "",
    contrasena3: ""
  }),
  methods: {
    session(usuarioL, contrasenaL) {
      console.log(usuarioL, contrasenaL)
      let objeto = this;
      this.axios
        .post(
          "http://" +
            objeto.$serverURI +
            ":" +
            objeto.$serverPort +
            "/Usuario/login",
          {
            usuario: usuarioL,
            contrasena: contrasenaL
          },          
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          var respuesta = response.data.status;
          if(respuesta=='1'){
          console.log("Este es el token: ");

          let token = response.data.data.jwt;
          let decoded = jwt_decode(token);
          console.log(decoded);

          objeto.$cookies.set(
              "jwt",
              token,
              60 * response.data.data.tiempo,
              null,
              null,
              null,
              true
            );


          //localStorage.identificacion= usuarioL; //TENER CUIDADO PARA PRUEBA



//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////                      TODO ESTO DEBE IRSE POR SEGURIDAD                                       //////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
          if (respuesta == "1") {
            let encriptado = objeto.$Crypto.AES.encrypt(
              //objeto.usuarioL,
              usuarioL,
              response.data.data.token
            );


            objeto.$cookies.set(
              "user_session",
              encriptado.toString(),
              60 * 100,
              null,
              null,
              null,
              true
            );
            // console.log("COOKIE HOME1: ",objeto.$cookies.get("user_session"));

            localStorage.cdcb0830cc2dd220 = response.data.data.token;
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////

            objeto.$router.replace({ name: response.data.data.addr });
          }
          }else {          
            alert("El usuario no existe.");
          }
        })
        .catch(function(error) {
           alert("Error");
        });
    }
  }

};
</script>