<template>
  <v-container class="grey darken-4" dark fluid>
    <HeaderAdmin />
    <v-row align="center">
      <v-col align="center">
        <v-col class="col-sm-10 col-lg-6">
          <v-card color="#424242" style="padding:30px">
            <v-card-title
              class="justify-center"
              style="color:white;font-weigth:bolder;"
            >Crear Nuevo usuario</v-card-title>

 <p class="red--text" v-if="errors.length">
            <b>Error(es):</b>
            <ul>
              <li v-for="(err,index) in errors" :key="index">{{ err }}</li>
            </ul>
          </p>

            <v-form ref="form" v-model="valid">
              <v-card-actions>
                <v-container>
                  <v-row>
                    <v-col cols="12">
                      <v-text-field
                        solo
                        flat
                        placeholder="Nombre del Laboratorista"
                        v-model="usuario"
                           :rules="[rules.required, rules.usuario]"
                      />
                    </v-col>
                    <v-col cols="12">
                      <v-text-field
                        solo
                        flat
                        placeholder="Código del laboratorista"
                        v-model="identificacion"
                        :rules="[rules.required, rules.identificacion]"
                      />
                    </v-col>
                    <v-col cols="12">
                      <v-text-field
                        solo
                        flat
                        placeholder="Correo del laboratorista"
                        v-model="correo"
                        :rules="[rules.required, rules.email]"
                      />
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-btn
                        color="primary"
                        x-large
                        @click="formSubmit"
                        style="font-weitgh:lighter;font-family:Arial;width:100%"
                      >Registrar</v-btn>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="12">
                      <v-alert :value="vista" type="success">{{ output }}</v-alert>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-actions>
            </v-form>
          </v-card>
        </v-col>
      </v-col>
    </v-row>
  </v-container>
</template>





<script>
import HeaderAdmin from "@/components/HeaderAdmin.vue";
export default {
  mounted() {
    console.log("Ready");
  },
    components: {
    HeaderAdmin
  },
  data() {
    return {
      valid: true,
      usuario: "",
      identificacion: "",
      correo: "",
      estado:"A",
      proyecto:"LABORATORIOS",
      tipousuario:"Laboratorista",
      output: "",
      vista: false,
      tipo: "success",
      errors:[],
      rules: {
        required: value => !!value || "Requerido.",
      email: value => {const pattern =  /(?:\w+@udistrital.edu.co)|(?:(?:correo\.udistrital\.edu\.co))/
          return pattern.test(value) || 'Email invalido.'},
      usuario:  value => {const pattern = /\w+/
            return pattern.test(value) || 'Ingrese un nombre.'},
      identificacion: value => {const pattern =/\d.{7,}/
            return pattern.test(value) || 'Ingrese una Identificación valida.'},
      
      }
    };
  },
  // mounted(){
  // this.$verificarLogin();
  // },
  methods: {
    formSubmit() {
  this.errors=[]
  this.rules.email.value
  if (
          this.usuario &&
          this.identificacion &&
          this.correo&&
          this.rules.email
      ){

          //let currentObj = this.$refs.form;
          let objeto = this;
          this.axios
            .post(
             "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/registrar",
              {
                usuario: this.usuario.toUpperCase(),
                identificacion: this.identificacion,
                correo: this.correo,
                estado: this.estado,
                proyecto: this.proyecto,
                contraseña: this.identificacion,
                tipousuario: this.tipousuario

              },
              {
                headers: {
                  "Content-Type": "application/json",
                  "Authorization": this.$cookies.get("jwt") ? "Bearer " + this.$cookies.get("jwt") : "",
                }
              }
            )
            .then(function(response) {
              console.log("Status:" + response.data.status);
              console.log("Mns:" + response.data.mensaje);
              if (response.data.status == 1) {
                objeto.vista = true;
                console.log("regista 1");
                objeto.output = response.data.mensaje;
              } else if (response.data.status == 2) {
                objeto.vista = true;
                console.log("regista 2");
                objeto.output = response.data.mensaje;
              } else if (response.data.status == 401) {                                
                objeto.$router.push('/');
                alert("Error de sesion");
                
              } else {
                objeto.vista = true;
                console.log("regista 3");
                objeto.output = "Ha ocurrido un error";
              }
            })
            .catch(function(error) {
              objeto.output = error;
            });
        }
        else{

        if (!this.usuario) this.errors.push("Nombre de usuario requerido.")
        if (!this.identificacion) this.errors.push("Identificación requerida.")
        if (!this.correo) this.errors.push("Dirección de correo requerida.")
        if (!this.rules.email.value) this.errors.push("Dirección de correo invalida.")

        }
    }
  }
};
</script>
