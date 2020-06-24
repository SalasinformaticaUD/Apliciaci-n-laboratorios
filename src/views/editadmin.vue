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
            >Editar perfil</v-card-title>
            <v-text-field
              solo
              flat
              placeholder="Nombre del usuario"
              v-model="usuario"
              :rules="[rules.required]"
            >Nombre del usuario</v-text-field>

            <v-text-field
              solo
              flat
              placeholder="Correo electrónico"
              v-model="correo"
              :rules="[rules.required]"
            >Correo electrónico</v-text-field>

            <v-btn
              color="primary"
              x-large
              @click="save"
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
  data: () => ({
    usuario:"",
    correo:"",
    usuariolab: [],
    editedIndex: -1,
    editedItem: {
      value: "usuario",
      calories: 0,
      fat: 0
    },
    rules: {
      required: value => !!value || "Requerido.",
      email: value => {
        const pattern = /(?:\w+@udistrital.edu.co)|(?:(?:correo\.udistrital\.edu\.co))/;
        return pattern.test(value) || "Email invalido.";
      },
      usuario: value => {
        const pattern = /\w+/;
        return pattern.test(value) || "Ingrese un nombre.";
      },
      identificacion: value => {
        const pattern = /\d.{7,}/;
        return pattern.test(value) || "Ingrese una Identificación valida.";
      }
    }
  }),
  mounted(){
  this.$verificarLogin();
  },
  watch: {
    dialog(val) {
      val ;
    }
  },


  created() {
    this.initialize();
  },
  methods: {
    initialize() {
      (this.usuariolab = []), this.buscar();
    },
    editItem(item) {
      this.editedIndex = this.usuariolab.indexOf(item);

      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    save() {
      var confirmacion = confirm("¿Esta seguro de guardar estos cambio?");

      if (confirmacion) {
        let objeto = this;
        this.axios
          .post(
            "http://giovannygz.ddns.net:5000/Usuario/editaruserlab",
            {
              codigo: "79950025",
              usuario: this.usuario.toUpperCase(),
              correo: this.correo
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
              objeto.buscar();
              //   objeto.usuariolab.splice(index, 1);
            }
          })
          .catch(function(error) {
            alert(error);
          });
      }
      this.close();
    },
    buscar() {
      let objeto = this;
      this.axios
        .post(
          "http://giovannygz.ddns.net:5000/Usuario/consultaeditadmin",
          {
            codigo: "79950025"
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          objeto.usuariolab = response.data.data;
          console.log(objeto.usuariolab);
          objeto.usuario=response.data.data[0].usuario
          objeto.correo=response.data.data[0].correo
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>

