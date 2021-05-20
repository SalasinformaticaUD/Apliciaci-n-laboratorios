<template>
  <v-container fluid>
    <Headerestudiantes />

    <v-row justify="center">
        <v-col class="col-sm-10 col-lg-6" align="center">
          <v-card color="#424242" style="padding:30px">
            <v-card-title
              class="justify-center"
              style="color:white;font-weigth:bolder;"
            >Actualizar Contraseña</v-card-title>

 <p class="red--text" v-if="errors.length">
            <b>Error(es):</b>
            <ul>
              <li v-for="(err,index) in errors" :key="index">{{ err }}</li>
            </ul>
          </p>


            <v-text-field
              solo
              flat
              placeholder="Contraseña actual"
              v-model="contraseñaactual"
              :rules="[rules.required]"
              :append-icon="show1 ? 'fas fa-eye' : 'fas fa-eye-slash'"
              :type="show1 ? 'text' : 'password'"
              @click:append="show1 = !show1"
            >contraseña actual</v-text-field>

            <v-text-field
              solo
              flatç
              placeholder="Nueva contraseña"
              v-model="nuevacontraseña"
              :rules="[rules.required]"
              :append-icon="show2 ? 'fas fa-eye' : 'fas fa-eye-slash'"
              :type="show2 ? 'text' : 'password'"
              @click:append="show2 = !show2"
            >nueva contraseña</v-text-field>

            <v-text-field
              solo
              flat
              placeholder="Confirmar contraseña"
              v-model="confirmcontraseña"
              :rules="[rules.required, rules.pass]"
              :append-icon="show3 ? 'fas fa-eye' : 'fas fa-eye-slash'"
              :type="show3 ? 'text' : 'password'"
              @click:append="show3 = !show3"
            >confirmar contraseña</v-text-field>

            <v-btn
              color="primary"
              x-large
              @click="formSubmit"
              style="font-weitgh:lighter;font-family:Arial;width:100%"
            >Guardar cambios</v-btn>
          </v-card>
        </v-col>
    </v-row>
  </v-container>
</template>


<script>
import Headerestudiantes from "@/components/Headerestudiantes.vue";
export default {
  components: {
    Headerestudiantes
  },
  data: () => {
    return {
        show1: false,
      show2: false,
      show3: false,
      contraseñaactual: "",
      nuevacontraseña: "",
      errors:[],
      rules: {
        required: value => !!value || "Requerido.",
        pass: value =>
          ((this.nuevacontraseña === value)&&(this.confirmcontraseña === value)) || "No corresponden las contraseñas",
        
        }
      }
    },
    mounted(){
  this.$verificarLogin();
  },
  
  methods: {
     clear() {
      this.contraseñaactual = "";
      this.nuevacontraseña = "";
      this.confirmcontraseña = "";
    },
    formSubmit() {
      this.errors = [];
        
      if (
         this.contraseñaactual &&
        this.nuevacontraseña &&
        this.confirmcontraseña
        ) {
          
        //let currentObj = this.$refs.form;
        let objeto = this;
        this.axios

          .post(
            "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/editpass",
            {
              codigo: "20132005988",          
              nuevacontraseña: this.nuevacontraseña,
              contraseña: this.contraseñaactual  
            },
            {
              headers: {
                "Content-Type": "application/json"
              }
            }
          )
        .then(function(response) {
            var respuesta = response.data.mensaje;
            var status = response.data.status;
            if (status == "1") {
              alert(respuesta);
              //   objeto.usuariolab.splice(index, 1);
            }
          })
          .catch(function(error) {
            objeto.output = error;
          });
      } else {
         if (!this.contraseñaactual) this.errors.push("Es necesaria la contraseña actual.");
        if ((!this.nuevacontraseña)||(!this.form.confirmcontraseña)) this.errors.push("Contraseña requerida.")
        else 
          if (!((this.form.nuevacontraseña)===(this.form.confirmcontraseña))) this.errors.push("Las contraseñas no coinciden.")
          this.errors.push("Las contraseñas no coinciden.");
      }
    }
  }
};
</script>