<template>
  <v-app>
    <v-main style="background-color:#212121">
      <router-view />
    </v-main>

    <v-footer
      class="font-weight-medium"
      color="red darken-4"
      dense
      dark
      padless
    >
      <!-- src="C:\Users\Angie\Desktop\AplicaciónLabs\Prueba-monitor\src\assets\computadores.PNG" -->
      <!-- gradient="to top right, rgba(53,50,48), rgba(30,30,30)" -->
      <v-row no-gutters>
        
        <v-col cols="3" class="text-justify">
          <v-img
            src="https://www.udistrital.edu.co/themes/custom/versh/images/default/preloader.png"
            max-width="150"
          ></v-img>
        </v-col>

        <v-spacer />
        <v-col cols="5" class="text-center">
          <br />
          <br />
          <br />
          Copyright {{ new Date().getFullYear() }} —
          <strong
            >Sitio creado y administrado por los laboratorios de
            Ingeniería</strong
          >
        </v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script>
//import Header from "@/components/Header.vue";
export default {
  components: {
    //Footer
  },
  name: "App",
  data: () => ({
    //
  })
};
</script>
