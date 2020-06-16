<template>
  <v-container fluid>
    <Headerestudiantes />

    <v-card color="grey darken-3" dark style="padding:30px"> 
    
   
      <h1 align="center">Reserva de laboratorios adicionales</h1>
                
                  <p align="justify">
                    Siga los pasos que se muestran a continuación pra realizar la adición del laboratotio:
                  </p>


                   <p align="justify">
                    1. Escoja el día que desea realizar el adicional:
                  </p>
    
    <v-autocomplete
            ref="Dia"
            v-model="Dia"
            :rules="[() => !!Dia || 'Este espacio es requerido']"
            :items="Dias"
            label="Dia"
            placeholder="Seleccionar..."
            required
          ></v-autocomplete>
    
                   <p align="justify">
                    2. Escoja el bloque de horas:
                  </p>
   
<v-autocomplete
            ref="Hora"
            v-model="Hora"
            :rules="[() => !!Hora || 'Este espacio es requerido']"
            :items="Horas"
            label="Horas"
            placeholder="Seleccionar..."
            required
          ></v-autocomplete>
                                            
                   <p align="justify">
                    3. Estos son los laboratorios disponibles en la fecha y bloque seleccionados, seleccione uno:
                  </p>

<v-autocomplete
            ref="Laboratorio"
            v-model="Laboratorio"
            :rules="[() => !!Laboratorio || 'Este espacio es requerido']"
            :items="Laboratorios"
            label="Laboratorio"
            placeholder="Seleccionar..."
            required
          ></v-autocomplete>



<div class="text-right">
      <v-btn rounded color="primary" dark>siguiente</v-btn>
</div>
    </v-card> 
 
  </v-container>
</template>

<script>
import Headerestudiantes from "@/components/Headerestudiantes.vue";
export default {
  components: {
    Headerestudiantes
  },
  data: () => ({
      Laboratorios:['Electronica A','Electronica B', 'Electronica Basica','Maquinas','Comunicaciones','Circuitos'],
      Dias:['Lunes','Martes','Miercoles','Jueves','Viernes','sabado'],
      Horas:['6-8','8-10','10-12','12-14','14-16','16-18']    
  })
};
</script>