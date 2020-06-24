<template>
  <v-container fluid>
    <Headerhome/>
    <v-row>
      <v-col>
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
            <v-row>
              <v-col>
                <v-text-field v-model="usuario2"
                placeholder="Codigo" solo flat :rules="numeroRules" />
              </v-col>
              <v-col>
                <v-text-field v-model="contrasena2"
                  type="password"
                  placeholder="Identificacion"
                  solo
                  flat
                  :rules="numeroRules" />
              </v-col>
              <v-col>
                <v-btn
                  color="primary"
                  x-large
                  style="font-weitgh:lighter;font-family:Arial"
                  @click="session2"
                >Ingresar</v-btn>
              </v-col>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="3">
        <v-card color="#424242" style="padding:20px" dark>
          <v-card-title class="justify-center" style="color:#FFFFFF">Ingreso  Laboratorista</v-card-title>
          <v-card-subtitle>Como personal Administrativo tienes acceso a los laboratorios desde aqui</v-card-subtitle>
          <v-card-actions>
            <v-container>
              <v-row>
                <v-text-field 
                v-model= "usuario3"
                placeholder="Usuario" solo flat :rules="numeroRules" />
              </v-row>
              <v-row>
                <v-text-field
                  v-model="contrasena3"
                  type="password"
                  placeholder="Contraseña"
                  solo
                  flat
                  :rules="numeroRules"
                />
              </v-row>

              <v-row>
                <v-btn
                  color="primary"
                  x-large
                  style="font-weitgh:lighter;font-family:Arial"
                  @click="session3"
                >Ingresar</v-btn>
              </v-row>
            </v-container>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card color="#424242" style="padding:20px" dark>
          <v-card-title class="justify-center" style="color:#FFFFFF">Ingreso  Administrativo</v-card-title>
          <v-card-subtitle>Como personal Administrativo tienes acceso a los laboratorios desde aqui</v-card-subtitle>
          <v-card-actions>
            <v-container>
              <v-row>
                <v-text-field 
                v-model= "usuario"
                placeholder="Usuario" solo flat :rules="numeroRules" />
              </v-row>
              <v-row>
                <v-text-field
                  v-model="contrasena"
                  type="password"
                  placeholder="Contraseña"
                  solo
                  flat
                  :rules="numeroRules"
                />
              </v-row>

              <v-row>
                <v-btn
                  color="primary"
                  x-large
                  style="font-weitgh:lighter;font-family:Arial"
                  @click="session"
                >Ingresar</v-btn>
              </v-row>
            </v-container>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card color="#424242" style="padding:20px">
          <v-card-title class="justify-center" style="color:#FFFFFF">CALENDARIO</v-card-title>
          <v-card-actions>
            <v-calendar :now="today" type="month" />
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="3">
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
export default {
    components: {
    Headerhome
  },
  data: () => ({
    today: "2019-01-08",
    numeroRules: [
      v => !!v || "Se requiere un código",
      v => /^[0-9]*$/.test(v) || "El código debe ser válido"
    ],
    correoRules: [
      v => !!v || "Se requiere un Correo",
      v => /.+@.+/.test(v) || "El correo debe ser válido"
    ],
    usuario:"",
    contrasena:"",
    usuario2:"",
    contrasena2:"",
    usuario3:"",
    contrasena3:""
  }),
    methods: {
    session() {
      let objeto = this;
      this.axios
        .post("http://"+objeto.$serverURI+":"+objeto.$serverPort+"/login", {
          usuario: this.usuario,
          contrasena: this.contrasena
        },{
          headers: {
            "Content-Type": "application/json"
          }
        })
        .then(function(response) {
          var respuesta = response.data.mensaje;
          if (respuesta == "1") {
            localStorage.autorizado = true;
            objeto.$router.replace({name:'HomeAdmin'});
          }else{
              confirm("No existe")
          }
        })
        .catch(function(error) {
          alert(error);
        });
    },
    session2() {
      let objeto = this;
      this.axios
        .post("http://"+objeto.$serverURI+":"+objeto.$serverPort+"/login", {
          usuario: this.usuario2,
          contrasena: this.contrasena2
        },{
          headers: {
            "Content-Type": "application/json"
          }
        })
        .then(function(response) {
          var respuesta = response.data.mensaje;
          if (respuesta == "1") {
            localStorage.autorizado = true;
            objeto.$router.replace({name:'reservaestudiante'});
          }else{
              confirm("No existe")
          }
        })
        .catch(function(error) {
          alert(error);
        });
    }
    ,
    session3() {
      let objeto = this;
      this.axios
        .post("http://"+objeto.$serverURI+":"+objeto.$serverPort+"/login", {
          usuario: this.usuario3,
          contrasena: this.contrasena3
        },{
          headers: {
            "Content-Type": "application/json"
          }
        })
        .then(function(response) {
          var respuesta = response.data.mensaje;
          if (respuesta == "1") {
            localStorage.autorizado = true;
            objeto.$router.replace({name:'HomeLaboratorista'});
          }else{
              confirm("No existe")
          }
        })
        .catch(function(error) {
          alert(error);
        });
    }
  }

};
</script>