<template fluid>
  <v-row>
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

    <v-navigation-drawer v-model="drawer" absolute temporary dark>
      <v-list nav dense>
        <v-list-item-group
     
          active-class="red darken-4--text text--accent-4"
        >
          <div class="text-center">
            <v-card color="#373737" class="pa-2" dark>
              <v-avatar>
                <v-icon block>far fa-user</v-icon>
              </v-avatar>
              <p class="display-1 text-center">Estudiantes</p>
            </v-card>
          </div>
          <v-card color="red darken-4">
            <v-list-item to="/reservaestudiante">
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
