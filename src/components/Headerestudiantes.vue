<template fluid>
  <v-row class="mb-3">
    <v-app-bar color="red darken-4" dense dark>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-flex>
        <v-toolbar-title class="display-1 mx-auto text-center">
          <b>Portal Estudiantes</b>
        </v-toolbar-title>
      </v-flex>
      <v-card color="white" tile align="left">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://labing.udistrital.edu.co/wp-content/uploads/2018/05/cropped-logo-laboratorio-01-1.png"
          transition="scale-transition"
          width="138"
        />
      </v-card>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute temporary dark color="background">
      <v-list nav dense>
        <v-list-item-group
     
          active-class="red darken-4--text text--accent-4"
        >
          <div class="text-center">
            <v-card :style="'border: 1px solid white'" color="#373737" class="pa-2" dark>
              <v-avatar>
                <v-icon block>far fa-user</v-icon>
              </v-avatar>
              <p class="display-1 text-center">Estudiante</p>
              
              <p class="px-5">{{usuario}}</p>
              
            </v-card>
          </div>        

          <v-card color="red darken-4" class="mt-4">
            <v-list-item to="/Monitores">
              <v-list-item-icon>
                <v-icon>fas fa-users</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Monitorias</v-list-item-title>
            </v-list-item>  
            
            <v-list-item to="/agendaadicionalesM">
              <v-list-item-icon>
                <v-icon>fas fa-plus</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Reservar laboratorio</v-list-item-title>
            </v-list-item>

            <v-list-item to="/consulta">
              <v-list-item-icon>
                <v-icon>far fa-calendar-alt</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Consultar laboratorios</v-list-item-title>
            </v-list-item>

            <v-list-item to="/licenciasEstudiantes">
              <v-list-item-icon>
                <v-icon>fas fa-laptop-code</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Solicitud licencias</v-list-item-title>
            </v-list-item>

            <v-list-item to="/studentpass">
              <v-list-item-icon>
                <v-icon>fa fa-key</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Cambio de contraseña</v-list-item-title>
            </v-list-item>

            <v-list-item @click ="cerrarSesion()" >
              <v-list-item-icon>
                <v-icon>fas fa-sign-out-alt</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Salir</v-list-item-title>
            </v-list-item>
          </v-card>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-row>
</template>

<script>
export default {
  data: () => ({
    drawer: false,
    token:"",
    usuario:"",
    codigoLab:"",
  }),
  created(){
    this.initialize();    
  },
  
  methods: {
    initialize() {
      this.buscar();
    },
    cerrarSesion() {
      localStorage.autorizado = null;
      this.$router.replace({ name: "home" });
      localStorage.usuario= null;
      let objeto = this;
      objeto.$cookies.remove(objeto.token);      
      objeto.$cookies.keys().forEach(cookie => objeto.$cookies.remove(cookie));
    },
    buscar() {
      
      let objeto = this;
      objeto.token = localStorage.cdcb0830cc2dd220;
      
      var encrypted = objeto.$cookies.get("user_session");      
      var desen = objeto.$Crypto.AES.decrypt(encrypted, objeto.token);
      var codlab = desen.toString(objeto.$Crypto.enc.Utf8);
      objeto.codigoLab = objeto.$Crypto.AES.decrypt(objeto.$cookies.get("user_session"), objeto.token);
      //objeto.codigoLab = localStorage.identificacion;
      
      
      
      // console.log("Método buscar header laboratorista linea 277");
      // console.log("token: ",objeto.token)
      // console.log("ENCRYPTED 1: ",objeto.encrypted);
      // console.log("ENCRYPTED 2: ",objeto.$cookies.get("user_session"));
      // console.log("DESENCRYPTED 1: ",objeto.desen);
      // console.log("DESENCRYPTED 2: ",objeto.$Crypto.AES.decrypt(objeto.$cookies.get("user_session"), objeto.token));
      // console.log("codlab 1: ",objeto.codlab);
      // console.log("codigolab : ",objeto.codigoLab);
      //console.log("codlab 2: ",objeto.codigoLab.toString(objeto.$Crypto.enc.Utf8));
      objeto.codigoLab=objeto.codigoLab.toString(objeto.$Crypto.enc.Utf8);
      // console.log("AQUÍ EL CODIGO $: ",objeto.codigoLab);
      //console.log("AQUÍ EL CODIGO: ",objeto.codigoLab)
      
      this.axios
        .post(
          "http://" +
            objeto.$serverURI +
            ":" +
            objeto.$serverPort +
            "/Usuario/consultaeditlabo",
          {
            codigo: objeto.codigoLab,
            tipo: "Estudiante",                      
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          
          localStorage.usuario = response.data.data[0].usuario;  
          objeto.usuario = response.data.data[0].usuario;
          // console.log("AUYUDAAA VUE");

        })
        .catch(function(error) {
          objeto.output = error;
        });
    },
  },
};
</script>
