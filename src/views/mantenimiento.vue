<template>
  <v-container class="grey darken-4" dark fluid>
    <HeaderLaboratorista />
    <v-col cols="12" align="center">
      <v-col class="col-sm-12 col-lg-8">
        <h1 style="color:white;">Añadir mante</h1>

        <v-stepper v-model="e1" dark>
          <v-stepper-header>
            <v-stepper-step :complete="e1 > 1" step="1" :editable="editable">Pagina 1</v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step :complete="e1 > 2" step="2"  :editable="editable">Pagina 2</v-stepper-step>

            
          </v-stepper-header>

          <v-stepper-items>
            <v-stepper-content step="1">
              <v-card color="#424242" style="padding:30px" class="mb-12">
                <v-card-title
                  class="justify-center"
                  style="color:white;font-weigth:bolder;"
                >Mantenimiento</v-card-title>

                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <select style="display:none;"  id="selectPlaca" v-model="placa" solo>
                         <option value="">Buscar por placa, nombre o ubicacion</option>
                    </select>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                  <select style="display:none;"  id="selectUsuario" v-model="codUsu" solo>
                         <option value="">Buscar por codigo o nombre</option>
                  </select>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="numInterno" label="Número Interno" solo readonly></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="nomUsu" label="Nombre Usuario" solo readonly></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="nomEqu" label="Nombre Equipo" solo readonly></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="sala" label="Sala" solo readonly></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-menu
                      ref="menu"
                      v-model="menu"
                      :close-on-content-click="false"
                      :return-value.sync="fecha"
                      transition="scale-transition"
                      
                      offset-y
                      dark
                      min-width="290px"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          v-model="fechaForm"
                          label="Fecha"
                          readonly
                          v-bind="attrs"
                          prepend-icon = "far fa-calendar-alt"
                          v-on="on"
                        ></v-text-field>
                      </template>
                      <v-date-picker v-model="fecha" no-title scrollable>
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                        <v-btn text color="primary" @click="$refs.menu.save(fecha)">OK</v-btn>
                      </v-date-picker>
                    </v-menu>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="numeroInterno" label="Horario" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-select
                      :items="mantenimientos"
                      label="Tipo de Mantenimiento"
                      solo
                    ></v-select>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field
                      v-model="descDano"
                      label="Descripcion Daño"
                      solo
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-card>
              <v-btn rounded color="primary" dark @click="e1 = 2">Siguiente</v-btn>
              <v-btn text>Cancel</v-btn>
            </v-stepper-content>

            <v-stepper-content step="2">
              <v-card color="#424242" style="padding:30px" class="mb-12">
                <v-card-title
                  class="justify-center"
                  style="color:white;font-weigth:bolder;"
                >Mantenimiento</v-card-title>

                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-menu
                      ref="menu2"
                      v-model="menu2"
                      :close-on-content-click="false"
                      :return-value.sync="fechaReal"
                      transition="scale-transition"
                      offset-y
                      dark
                      min-width="290px"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          v-model="fechaRealForm"
                          label="Fecha Realizacion"
                          readonly
                          prepend-icon = "far fa-calendar-alt"
                          v-bind="attrs"
                          v-on="on"
                          solo
                        ></v-text-field>
                      </template>
                      <v-date-picker v-model="fechaReal" no-title scrollable>
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="menu2 = false">Cancel</v-btn>
                        <v-btn text color="primary" @click="$refs.menu2.save(fechaReal)">OK</v-btn>
                      </v-date-picker>
                    </v-menu>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="nomEmpresa" label="Nombre de la empresa contratada" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="nit" label="NIT" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="tiempGar" label="Tiempo de Garantía" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="costMant" label="Costo Mantenimiento" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="numOrdServ" label="No Orden de servicio" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="vigencia" label="Vigencia" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="supervisor" label="Supervisor" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="repuestos" label="Repuestos" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="proxMant" label="Proximo Mantenimiento" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-12">
                    <v-textarea v-model="espMantReal" label="Especificaciones mantenimiento realizado" solo></v-textarea>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-12">
                    <v-textarea v-model="observaciones" label="Observaciones" solo></v-textarea>
                  </v-col>
                </v-row>
              </v-card>
              <v-btn rounded color="primary" dark @click="formSubmit">Guardar</v-btn>
              <v-btn text>Cancel</v-btn>
            </v-stepper-content>

          </v-stepper-items>
        </v-stepper>
      </v-col>
    </v-col>
  </v-container>
</template>
<style scoped>
@import "../assets/select2/css/select2.css";
</style>
<script>
import HeaderLaboratorista from "@/components/HeaderLaboratorista.vue";
export default {
  components: {
    HeaderLaboratorista
  },
  data() {
    return {
      e1: 1,
      menu:false,
      fecha : new Date().toISOString().substr(0, 10),
      fechaForm:this.formatDate(new Date().toISOString().substr(0, 10)),
      menu2:false,
      fechaReal : new Date().toISOString().substr(0, 10),
      fechaRealForm:this.formatDate(new Date().toISOString().substr(0, 10)),
      mantenimientos:['Interno Correctivo','Externo Correctivo','Interno Predictivo','Externo Predictivo','Interno Preventivo','Externo Preventivo'],
      editable: true,
      placa:'',
      codUsu:'',
      numInterno:'',
      nomUsu:'',
      nomEqu:'',
      sala:'',
      numeroInterno:'',
      descDano:'',
      nomEmpresa:'',
      nit:'',
      tiempGar:'',
      costMant:'',
      numOrdServ:'',
      vigencia:'',
      supervisor:'',
      repuestos:'',
      proxMant:'',
      espMantReal:'',
      observaciones:'',
    };
  },
  mounted(){
    const $ = require('jquery')
    // Lo declaramos globalmente
    window.$ = $
    let self = this; // ámbito de vue
    $(document).ready(function(){ //esto se usa para ajustar las propiedades css del select2
      $(".select2").css("width","100%");
      $(".select2-selection").css("height","48px");
    });
    
    let objeto =this;
    // inicializas select2
    $( "#selectPlaca" ).select2({        
      ajax: {
          url: "http://200.69.103.13:5000/consAddMantPlaca",
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
      objeto.numInterno=$('#selectPlaca').select2('data')[0].numInterno;
      objeto.nomEqu=$('#selectPlaca').select2('data')[0].nomEqu;
      objeto.sala=$('#selectPlaca').select2('data')[0].sala;
      objeto.placa=$('#selectPlaca').select2('data')[0].id;
    });
    
    $( "#selectUsuario" ).select2({        
      ajax: {
          url: "http://200.69.103.13:5000/consAddMantLab",
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
        objeto.nomUsu=$('#selectUsuario').select2('data')[0].nombre;
        objeto.codUsu=$('#selectUsuario').select2('data')[0].id;
    });
  },
  watch: {
    fecha (val) {
      this.fechaForm = this.formatDate(this.fecha)
    },
    fechaReal (val){
      this.fechaRealForm = this.formatDate(this.fechaReal)
    }
  },
  methods: {
    formatDate (date) {
        if (!date) return null

        const [year, month, day] = date.split('-')
        return `${day}/${month}/${year}`
    },
    formSubmit() {
      
      if (
        this.fechaForm &&
        this.fechaRealForm &&
        this.placa &&
        this.codUsu &&
        this.numInterno &&
        this.nomUsu &&
        this.nomEqu &&
        this.sala &&
        this.numeroInterno &&
        this.descDano &&
        this.nomEmpresa &&
        this.nit &&
        this.tiempGar &&
        this.costMant &&
        this.numOrdServ &&
        this.vigencia &&
        this.supervisor &&
        this.repuestos &&
        this.proxMant &&
        this.espMantReal &&
        this.observaciones
      ) {
        let objeto = this;
        this.axios
          .post(
            "http://" +
              objeto.$serverURI +
              ":" +
              objeto.$serverPort +
              "/Usuario/registrarMant",
            {
              fecha :this.fechaForm,
              fechaReal:this.fechaRealForm,
              placa:this.placa,
              codUsu:this.codUsu,
              numInterno:this.numInterno,
              nomUsu:this.nomUsu,
              nomEqu:this.nomEqu,
              sala:this.sala,
              numeroInterno:this.numeroInterno,
              descDano:this.descDano,
              nomEmpresa:this.nomEmpresa,
              nit:this.nit,
              tiempoGar:this.tiempGar,
              costMan:this.costMant,
              numOrdServ:this.numOrdServ,
              vigencia:this.vigencia,
              supervisor:this.supervisor,
              repuestos:this.repuestos ,
              proxMant:this.proxMant ,
              espMantReal:this.espMantReal ,
              observaciones:this.observaciones
            },
            {
              headers: {
                "Content-Type": "application/json"
              }
            }
          )
          .then(function(response) {
            if (response.data.status == 1) {
              var respuesta = response.data.mensaje;
              alert(respuesta);
            } else if (response.data.status == 2) {
              alert(response.data.status);
            } else {
              alert(response.data.status);
            }
          })
          .catch(function(error) {
            objeto.output = error;
          });
      }else{
        alert('Falta un campo');
      }
    }
  }
};
</script>