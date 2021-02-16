<template fluid>
  <v-row>
    <v-app-bar color="red darken-4" dense dark>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>

      <v-flex>
        <v-toolbar-title class="display-1" align="center">
          <b>Portal Administración</b>
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

    <v-navigation-drawer v-model="drawer" absolute temporary color="background">
      <v-card color="background" dense class="pa-5" dark>
        <div class="text-center">
          <v-avatar color="red" size="100">
            <v-icon dark class="fas fa-user-circle"></v-icon>
          </v-avatar>
        </div>
      </v-card>

      <v-list nav dense>
        <v-card color="red darken-4" dark>
          <v-list-item-group
            active-class="white--text text--accent-4"
          >
            <v-card color="red darken-4">
              <v-list-item >
                <v-list-item-icon>
                  <v-icon>mdi-home</v-icon>
                </v-list-item-icon>
                <v-list-item-title>Gestion Salas</v-list-item-title>
              </v-list-item>
            </v-card>
            <v-card color="red darken-4">
              <v-list-group
                no-action
                sub-group
                active-class="white--text text--accent-4"
              >
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>Gestion Inventario</v-list-item-title>
                  </v-list-item-content>
                </template>

                <v-list-item
                  v-for="(consulta, i) in Consultainvs"
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

<!--            <v-card color="red darken-4">
              <v-list-group
                no-action
                sub-group
                active-class="white--text text--accent-4"
              >
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
            </v-card> -->

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
              <v-list-group
                no-action
                sub-group
                active-class="white--text text--accent-4"
              >
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>Gestion de Perfiles</v-list-item-title>
                  </v-list-item-content>
                </template>

                <v-list-item
                  v-for="(Gestion, i) in GestionProfiles"
                  :key="i"
                  link
                  router :to = Gestion[1]
                 
                >
                  <v-list-item-title v-text="Gestion[0]"></v-list-item-title>

                  <v-list-item-icon>
                    <v-icon v-text="Gestion[2]"></v-icon>
                  </v-list-item-icon>
                </v-list-item>
              </v-list-group>
            </v-card>

            <v-card color="red darken-4">
              <v-list-item
              @click ="cerrarSesion()"
              >
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
    Consultainvs: [
      ["Consultar Inventario", "/busquedainventario"],
      ["Nuevo Equipo", "/addequipo"],
      ["Deshabilitar Articulos", ""],
      ["Modificación de Articulo", ""]
    ],
    Reports: [
      ["Informes Elementos", "/informesElementos"],
      ["Informes Horarios", "/informesHorarios"],
      ["Informes Prestamos", "/informesPrestamos"],
    ],
    GestionProfiles: [
      ["Crear usuario", '/registrouser'],
      ["Modificar usuario",  '/edituser'],
      ["Editar mi perfil",  '/editadmin'],
      ["Cambiar mi contraseña",  '/editpassadmin']
      
    ],
    drawer: false
  }),
  methods:{
    cerrarSesion(){
      localStorage.autorizado = null;
      this.$router.replace({name:'home'});
    }
  }
};
</script>
