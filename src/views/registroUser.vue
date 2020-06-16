<template>
  <v-container class="grey darken-4" dark fluid>
 <HeaderAdmin />
    <v-row align="center">
      <v-col cols="12" align="center">
        <v-col cols="4" >

          
        <v-card color="#424242" style="padding:30px">
          <v-card-title
            class="justify-center"
            style="color:white;font-weigth:bolder;"
            >Crear Nuevo usuario</v-card-title
          >
          <v-form ref="form" v-model="valid">
            <v-card-actions>
              <v-container>
                <v-row>
                  <v-col cols="12">
                    <v-text-field
                      solo
                      flat
                      placeholder="Usuario"
                      v-model="usuario"
                    />
                  </v-col>
                  <v-col cols="12">
                    <v-text-field
                      solo
                      flat
                      placeholder="Identificacion"
                      v-model="identificacion"
                    />
                  </v-col>
                  <v-col cols="12">
                    <v-text-field
                      solo
                      flat
                      placeholder="Correo"
                      v-model="correo"
                    />
                  </v-col>
                  <v-col cols="12">
                    <v-text-field
                      solo
                      flat
                      placeholder="Telefono"
                      v-model="telefono"
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
                      >Registrar
                    </v-btn>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12">
                    <v-alert :value="vista" type="success">
                      {{ output }}
                    </v-alert>
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
      telefono: "",
      output: "",
      vista: false,
      tipo: "success"
    };
  },
  methods: {
    formSubmit() {
      //let currentObj = this.$refs.form;
      let objeto = this;
      this.axios
        .post(
          "http://giovannygz.ddns.net:5000/Usuario/registrar",
          {
            usuario: this.usuario,
            identificacion: this.identificacion,
            correo: this.correo,
            telefono: this.telefono
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          if (response.data.status == 1) {
            objeto.vista = true;
            objeto.output = response.data.mensaje;
          } else if (response.data.status == 2) {
            objeto.vista = true;
            objeto.output = response.data.status;
          } else {
            objeto.vista = true;
            objeto.output = "Ha ocurrido un error";
          }
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>
