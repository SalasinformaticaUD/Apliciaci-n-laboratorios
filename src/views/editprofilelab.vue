<template>
  <v-container fluid>
    <HeaderLaboratorista />

    <v-row align="center">
      <v-col align="center">
        <v-col class="col-sm-10 col-lg-6">
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
import HeaderLaboratorista from "@/components/HeaderLaboratorista.vue";
export default {
  components: {
    HeaderLaboratorista
  },
  data: () => ({
    usuario:"",
    correo:"",
    token:"",
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
    this.initialize();
  },
  watch: {
    dialog(val) {
      val ;
    }
  },


  created() {
    
  },
  methods: {
    initialize() {
       this.buscar();
    },

    save() {
      var confirmacion = confirm("¿Esta seguro de guardar estos cambio?");

      if (confirmacion) {
        let objeto = this;
        let codigoLab = objeto.codigoLab
        this.axios
          .post(
            "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/editaruserlab",
            {
              codigo: codigoLab,
              usuario: this.usuario.toUpperCase(),
              correo: this.correo
            },
            {
              headers: {
                "Content-Type": "application/json",
                "Authorization": this.$cookies.get("jwt") ? "Bearer " + this.$cookies.get("jwt") : "",
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
            }else if (response.data.status == 401) {                                
              objeto.$router.push('/');
              alert("Error de sesion");                
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
      objeto.token = localStorage.cdcb0830cc2dd220;
      let encrypted = objeto.$cookies.get("user_session");
      let desen = objeto.$Crypto.AES.decrypt(encrypted, objeto.token);
      let codlab = desen.toString(objeto.$Crypto.enc.Utf8)
      objeto.codigoLab = codlab;
      this.axios
        .post(
         "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/consultaeditlabo",
          {
            codigo: objeto.codigoLab
          },
          {
            headers: {
              "Content-Type": "application/json",
              "Authorization": this.$cookies.get("jwt") ? "Bearer " + this.$cookies.get("jwt") : "",
            }
          }
        )
        .then(function(response) {
          if (response.data.status == 401) {                                
            objeto.$router.push('/');
            alert("Error de sesion");                
          }
          objeto.usuario=response.data.data[0].usuario
          objeto.correo=response.data.data[0].correo
        })
        .catch(function(error) {
          objeto.output = error;
        });
    },
   
  }
};
</script>

