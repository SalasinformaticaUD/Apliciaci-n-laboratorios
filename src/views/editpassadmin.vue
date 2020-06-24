<template>
  <v-container fluid>
    <HeaderAdmin />

    <v-row align="center">
      <v-col cols="12" align="center">
        <v-col cols="3" align="center">
          <v-card color="#424242" style="padding:30px">
            <v-card-title
              class="justify-center"
              style="color:white;font-weigth:bolder;"
            >Actualizar Contraseña</v-card-title>
            <v-text-field
              solo
              flat
              placeholder="Contraseña actual"
              v-model="contraseñaactual"
              :rules="[rules.required]"
            >contraseña actual</v-text-field>

            <v-text-field
              solo
              flatç
              placeholder="Nueva contraseña"
              v-model="nuevacontraseña"
              :rules="[rules.required]"
            >nueva contraseña</v-text-field>

            <v-text-field
              solo
              flat
              placeholder="Confirmar contraseña"
              v-model="confirmcontraseña"
              :rules="[rules.required, rules.pass]"
            >confirmar contraseña</v-text-field>

            <v-btn
              color="primary"
              x-large
              @click="formSubmit"
              style="font-weitgh:lighter;font-family:Arial;width:100%"
            >Guardar cambios</v-btn>
          </v-card>
        </v-col>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import HeaderAdmin from "@/components/HeaderAdmin.vue";
export default {
  components: {
    HeaderAdmin
  },
  data: () => {
    return {
      contraseñaactual: "",
      nuevacontraseña: "",
      confirmcontraseña:"",
      rules: {
        required: value => !!value || "Requerido.",
        pass: value =>
          (this.contraseñaactual === value &&
            this.nuevacontraseña === value) ||
          "No corresponden las contraseñas",
        
        }
      }
    },
  
  methods: {
    formSubmit() {
      this.errors = [];
        var confirmacion = confirm("¿Esta seguro de esta acción?");
      if (confirmacion) {
          
        //let currentObj = this.$refs.form;
        let objeto = this;
        this.axios

          .post(
            "http://giovannygz.ddns.net:5000/Usuario/editpass",
            {
              codigo: "79950025",          
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
        scroll(0, 0);
        if (!this.contraseñaactual) this.errors.push("Es necesaria la contraseña actual.")
        if (!this.correo) this.errors.push("Dirección de correo requerida.")
        if ((!this.nuevacontraseña)||(!this.nuevacontraseña)) this.errors.push("Contraseña requerida.")
        else 
          if (!((this.nuevacontraseña)===(this.confirmcontraseña))) this.errors.push("Las contraseñas no coinciden.")
      }
    }
  }
};
</script>