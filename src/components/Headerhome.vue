<template>
  <v-toolbar
     color="red darken-4"
      cards
      dark
      flat
    >

   <v-card color="white" tile>
        <v-btn text x-large href="https://labing.udistrital.edu.co/">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://labing.udistrital.edu.co/wp-content/uploads/2018/05/cropped-logo-laboratorio-01-1.png"
          transition="scale-transition"
          width="225"
        />
        </v-btn>
      </v-card>
      <v-flex>
      <div class="text-right">
        <v-btn text href="https://labing.udistrital.edu.co/">HOME</v-btn>
        <v-btn text href="https://labing.udistrital.edu.co/index.php/noticias/">NOTICIAS</v-btn>
      </div>
      </v-flex>
   
    </v-toolbar>
</template>