<template fluid>
  <v-row class="mb-3">
    <v-app-bar color="red darken-4" dense dark>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>

      <v-flex>
        <v-toolbar-title class="display-1" align="center">
          <b>Portal Laboratorista</b>
        </v-toolbar-title>
      </v-flex>

      <v-card color="white" tile>
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

    <v-navigation-drawer v-model="drawer" absolute temporary color="background" width="280">

      <v-card :style="'border: 1px solid white'" color="#373737" class="ma-2 pa-4" dark>
        <div class="text-center">
          <v-avatar color="red" size="100">
            <v-icon dark class="fas fa-user-circle"></v-icon>
          </v-avatar>
        </div>
        <div class="text-center mt-3">
          <p>{{usuario}}</p>
        </div>
        
      </v-card>

      <v-list nav dense>
        <v-card color="red darken-4" dark>
          <v-list-item-group active-class="white--text text--accent-4">
            <v-card color="red darken-4">
              <v-list-group no-action sub-group active-class="white--text text--accent-4">
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>Inventario</v-list-item-title>
                  </v-list-item-content>
                </template>

                <v-list-item
                  v-for="(consulta, i) in Consultainvs"
                  :key="i"
                  link
                  router
                  :to="consulta[1]"
                >
                  <v-badge :color="consulta[3]" :content="consulta[2]" size="100">
                    <v-list-item-title v-text="consulta[0]"></v-list-item-title>
                  </v-badge>

                  <v-list-item-icon>
                    <v-icon v-text="consulta[4]"></v-icon>
                  </v-list-item-icon>
                </v-list-item>
              </v-list-group>
            </v-card>

      <v-card color="red darken-4">
              <v-list-group no-action sub-group active-class="white--text text--accent-4">
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>Mantenimeinto</v-list-item-title>
                  </v-list-item-content>
                </template>

                <v-list-item
                  v-for="(consulta, i) in Consultamant"
                  :key="i"
                  link
                  router
                  :to="consulta[1]"
                >
                    <v-list-item-title v-text="consulta[0]"></v-list-item-title>

                  <v-list-item-icon>
                    <v-icon v-text="consulta[4]"></v-icon>
                  </v-list-item-icon>
                </v-list-item>
              </v-list-group>
            </v-card>

            <v-card color="red darken-4">
              <v-list-group no-action sub-group active-class="white--text text--accent-4">
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>Horarios</v-list-item-title>
                  </v-list-item-content>
                </template>

                <v-list-item
                  v-for="(consultah, i) in Consultahor"
                  :key="i"
                  link
                  router
                  :to="consultah[1]"
                >
                  <v-list-item-title v-text="consultah[0]"></v-list-item-title>
                </v-list-item>
              </v-list-group>
            </v-card>
            <v-card color="red darken-4">
              <v-list-group no-action sub-group active-class="white--text text--accent-4">
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>Prestamos</v-list-item-title>
                  </v-list-item-content>
                </template>

                <v-list-item
                  v-for="(consulta, i) in Consultapres"
                  :key="i"
                  link
                  router
                  :to="consulta[1]"
                >
                  <v-list-item-title v-text="consulta[0]"></v-list-item-title>
                  <v-list-item-icon>
                    <v-icon v-text="consulta[2]"></v-icon>
                  </v-list-item-icon>
                </v-list-item>
              </v-list-group>
            </v-card>
            <v-card color="red darken-4">
              <v-list-group no-action sub-group active-class="white--text text--accent-4">
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>Asignación Software</v-list-item-title>
                  </v-list-item-content>
                </template>

                <v-list-item
                  v-for="(consulta, i) in Software"
                  :key="i"
                  link
                  router
                  :to="consulta[1]"
                >
                  <v-list-item-title v-text="consulta[0]"></v-list-item-title>
                  <v-list-item-icon>
                    <v-icon v-text="consulta[2]"></v-icon>
                  </v-list-item-icon>
                </v-list-item>
              </v-list-group>
            </v-card>
            <v-card color="red darken-4">
              <v-list-group no-action sub-group active-class="white--text text--accent-4">
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>Informes</v-list-item-title>
                  </v-list-item-content>
                </template>

                <v-list-item 
                  v-for="(item, i) in Reports"
                  :key="i" 
                  link
                  router
                  :to="item[1]">
                  <v-list-item-title v-text="item[0]"></v-list-item-title>
                </v-list-item>
              </v-list-group>
            </v-card>
            <v-card color="red darken-4">
              <v-list-group no-action sub-group active-class="white--text text--accent-4">
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>Salas</v-list-item-title>
                  </v-list-item-content>
                </template>

                <v-list-item v-for="(consulta, i) in Consultasalas" :key="i" link>
                  <v-list-item-title v-text="consulta[0]"></v-list-item-title>
                  <v-list-item-icon>
                    <v-icon v-text="consulta[1]"></v-icon>
                  </v-list-item-icon>
                </v-list-item>
              </v-list-group>
            </v-card>

            <v-card color="red darken-4">
              <v-list-group no-action sub-group active-class="white--text text--accent-4">
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>Gestion de Mi Perfi</v-list-item-title>
                  </v-list-item-content>
                </template>

                <v-list-item
                  v-for="(Gestion, i) in GestionProfiles"
                  :key="i"
                  link
                  router
                  :to="Gestion[1]"
                >
                  <v-list-item-title v-text="Gestion[0]"></v-list-item-title>

                  <v-list-item-icon>
                    <v-icon v-text="Gestion[2]"></v-icon>
                  </v-list-item-icon>
                </v-list-item>
              </v-list-group>
            </v-card>

            <v-card color="red darken-4">
              <v-list-group no-action sub-group active-class="white--text text--accent-4">
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>Sanciones</v-list-item-title>
                  </v-list-item-content>
                </template>

                <v-list-item v-for="(consulta, i) in Consultasanc" :key="i" link>
                  <v-list-item-title v-text="consulta[0]"></v-list-item-title>
                  <v-list-item-icon>
                    <v-icon v-text="consulta[1]"></v-icon>
                  </v-list-item-icon>
                </v-list-item>
              </v-list-group>
            </v-card>

            <v-card color="red darken-4">
              <v-list-item @click="cerrarSesion()">
                <v-list-item-icon>
                  <v-icon></v-icon>
                </v-list-item-icon>
                <v-list-item-title>Finalizar sesión</v-list-item-title>
              </v-list-item>
            </v-card>
          </v-list-item-group>
        </v-card>
      </v-list>
    </v-navigation-drawer>
  </v-row>
</template>

<script>
export default {
  data: () => ({
    token:"",
    usuario:"",
    conca:"",
    codigoLab:"",
    
    Consultainvs: [
      ["Nuevo Equipo", "/addequipo", "", "", "fas fa-plus"],
      ["Consultar Inventario", "/busquedainventario", "", "", "fas fa-search"],
      ["Solicitudes de Traslado", "/busquedainventario", "6", "green", ""]
    ],
     Consultamant: [
      ["Nuevo mantenimeinto", "/mantenimiento"],
      ["Consultar mantenimientos", "/consultamantenimiento"],
     
    ],
    Consultahor: [["Consultar horarios", "/horarios"]],
    Consultapres: [
      
      ["Gestionar Prestamos", "/consultareservalabstemp"],
      ["Gestionar reserva", "/consultareslabo"]
    ],
    Software:[
      ["Solicitudes Software","/LicenciasSoftware"],
      ["Solicitudes VPN"]
    ],
    Consultasalas: [
      ["Nueva Sala", ""],
      ["Gestionar Salas", ""]
    ],
    Consultasanc: [
      ["Nueva Sanción", ""],
      ["Gestionar Sanciones", ""]
    ],
    Reports: [
      ["Informes Elementos", "/informesElementos"],
      ["Informes Horarios", "/informesHorarios"],
      ["Informes Prestamos", "/informesPrestamos"],
    ],
    GestionProfiles: [
      ["Editar datos", "/editprofilelab"],
      ["Cambiar contraseña", "/labpass"]
    ],
    drawer: false
  }),
    mounted(){    
    this.initialize();
    this.buscar();
    
  },
  methods: {
    initialize() {
    this.buscar();
    },
    cerrarSesion() {
      localStorage.autorizado = null;
      localStorage.usuario= null;
      this.$router.replace({ name: "home" });
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
      
      
      
      console.log("Método buscar header laboratorista linea 277");
      console.log("token: ",objeto.token)
      console.log("ENCRYPTED 1: ",objeto.encrypted);
      console.log("ENCRYPTED 2: ",objeto.$cookies.get("user_session"));
      console.log("DESENCRYPTED 1: ",objeto.desen);
      console.log("DESENCRYPTED 2: ",objeto.$Crypto.AES.decrypt(objeto.$cookies.get("user_session"), objeto.token));
      console.log("codlab 1: ",objeto.codlab);
      console.log("codigolab : ",objeto.codigoLab);
      //console.log("codlab 2: ",objeto.codigoLab.toString(objeto.$Crypto.enc.Utf8));
      objeto.codigoLab=objeto.codigoLab.toString(objeto.$Crypto.enc.Utf8);
      console.log("AQUÍ EL CODIGO $: ",objeto.codigoLab);
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
            tipo: "Laboratorista",                  
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
          console.log("AUYUDAAA VUE");

        })
        .catch(function(error) {
          objeto.output = error;
        });
    },

  }
};
</script>
