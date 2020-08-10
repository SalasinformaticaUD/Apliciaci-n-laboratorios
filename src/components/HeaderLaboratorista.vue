<template fluid>
  <v-row>
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
      <v-card color="background" dense class="pa-6" dark>
        <div class="text-center">
          <v-avatar color="red" size="100">
            <v-icon dark class="fas fa-user-circle"></v-icon>
          </v-avatar>
        </div>
        <div class="text-center">
 <p>{{$usuario}}</p>
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
                    <v-list-item-title>Reportes</v-list-item-title>
                  </v-list-item-content>
                </template>

                <v-list-item v-for="(Report, i) in Reports" :key="i" link>
                  <v-list-item-title v-text="Report[0]"></v-list-item-title>
                  <v-list-item-icon>
                    <v-icon v-text="Report[1]"></v-icon>
                  </v-list-item-icon>
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
    Consultainvs: [
      ["Nuevo Equipo", "/addequipo", "", "", "fas fa-plus"],
      ["Consultar Inventario", "/busquedainventario", "", "", "fas fa-search"],
      ["Solicitudes de Traslado", "/busquedainventario", "6", "green", ""]
    ],
    Consultahor: [["Consultar horarios", "/horarios"]],
    Consultapres: [
      ["Nuevo Prestamo", ""],
      ["Gestionar Prestamos", ""],
      ["Gestionar reserva", "/consultareslabo"]
    ],
    Consultasalas: [
      ["Nueva Sala", ""],
      ["Gestionar Salas", ""]
    ],
    Consultasanc: [
      ["Nueva Sanción", ""],
      ["Gestionar Sanciones", ""]
    ],
    Reports: [["Generación de informes", ""]],
    GestionProfiles: [
      ["Editar datos", "/editprofilelab"],
      ["Cambiar contraseña", "/labpass"]
    ],
    drawer: false
  }),
    mounted(){
    this.initialize();
  },
  methods: {
    initialize() {
    this.buscar();
    },
    cerrarSesion() {
      localStorage.autorizado = null;
      this.$router.replace({ name: "home" });
    },
    buscar() {
      let objeto = this;
      objeto.token = localStorage.cdcb0830cc2dd220;
      let encrypted = objeto.$cookies.get("user_session");
      let desen = objeto.$Crypto.AES.decrypt(encrypted, objeto.token);
      let codlab = desen.toString(objeto.$Crypto.enc.Utf8);
      objeto.codigoLab = codlab;
      this.axios
        .post(
          "http://" +
            objeto.$serverURI +
            ":" +
            objeto.$serverPort +
            "/Usuario/consultaeditlabo",
          {
            codigo: objeto.codigoLab
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          objeto.prototype.$usuario="";
          objeto.$usuario = response.data.data[0].usuario;          
        })
        .catch(function(error) {
          objeto.output = error;
        });
    },

  }
};
</script>
