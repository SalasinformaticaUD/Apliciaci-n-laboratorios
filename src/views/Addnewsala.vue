<template>
  <v-container class="grey darken-4" dark fluid>
    <HeaderLaboratorista />
 <v-col cols="12" align="center">

<v-col cols="6">



    <v-card color="#424242" style="padding:30px">
     
        <v-card-title
          class="justify-center"
          style="color:white;font-weigth:bolder;"
        >Agregar nueva sala</v-card-title>

        <v-row>
          <v-col cols="6">
            <v-text-field label="Nombre de la sala" solo></v-text-field>
          </v-col>
          <v-col cols="6">
            <v-text-field label="Área" solo></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6">
            <v-text-field label="Sede" solo></v-text-field>
          </v-col>
          <v-col cols="6">
            <v-text-field label="Puestos de trabajo" solo></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6">
            <v-text-field label="Piso" solo></v-text-field>
          </v-col>
          <v-col cols="6">
            <v-text-field label="Observaciones" solo></v-text-field>
          </v-col>
        </v-row>
        <div class="text-center">
          <v-btn rounded color="primary" dark>Agregar</v-btn>
        </div>
    </v-card>
      </v-col>
      </v-col>
  
  </v-container>
</template>

<script>
import HeaderLaboratorista from "@/components/HeaderLaboratorista.vue";
export default {
  components: {
    HeaderLaboratorista
  },
  data: () => ({
    //
  })
};
</script>
