<template>
    <v-container>
        <v-card color="#424242" style="padding:30px">
          <v-card-title
            class="justify-center"
            style="color:white;font-weigth:bolder;"
            >Busqueda usuario</v-card-title
          >
          <v-form ref="form" v-model="valid">
            <v-card-actions>
              <v-container>

                <v-row>
                  <v-col cols="12">
                       <select style="display:none;"  id="miSelect">
                         <option value="">Escriba texto</option>
                       </select>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12">
                       <v-text-field
                      solo
                      flat
                      placeholder="Nombre"
                      v-model="Nombre"
                    />
                  </v-col>
                </v-row>

              </v-container>
            </v-card-actions>
          </v-form>
        </v-card>
    </v-container>
</template>
<style scoped>
@import "../assets/select2/css/select2.min.css";
</style>
<script>
export default {
  data: () => ({
    selected: 'A',
    options: [],
    Nombre:''
  }),
  mounted(){

    const $ = require('jquery')
    // Lo declaramos globalmente
    window.$ = $
    let self = this; // ámbito de vue
    $(document).ready(function(){ //esto se usa para ajustar las propiedades css del select2
      $(".select2").css("width","500px");
      $(".select2").css("height","50px");
    });
    
    let objeto =this;
    // inicializas select2
    $( "#miSelect" ).select2({        
      ajax: {
          url: "http://200.69.103.13:5000/ConsultaSelect2",
          method: 'post',
          delay: 250,
          data: function (params) {
              return {
                  q: params.term // search term
              };
          },
          processResults: function (data) {
              return {
                  results: data
              };
          },
          cache: true
      },
      minimumInputLength: 3
    }).on('change', function (e){
      console.log($('#miSelect').select2('data')[0].id);
        objeto.Nombre=$('#miSelect').select2('data')[0].identificacion;
    });
  },
  
}
</script>