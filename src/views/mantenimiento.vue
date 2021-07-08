<template>
  <v-container class="grey darken-4" dark fluid>
    <HeaderLaboratorista />
    <v-col cols="12" align="center">
      <v-col class="col-sm-12 col-lg-8">
        <h1 style="color:white;">Añadir mantenimiento</h1>

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
                >Inicio o detección del mantenimiento</v-card-title>

                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <select style="display:none;"  id="selectUsuario" v-model="codUsu" >
                          <option value="">Buscar por codigo o nombre de laboratorista</option>
                    </select>
                  </v-col>

                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="nomUsu" label="Nombre Usuario *" readonly disabled='true'></v-text-field>
                  </v-col>
                </v-row>


                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <select style="display:none;"  id="selectPlaca" v-model="placa" >
                         <option value="">Buscar elemento por placa, nombre o ubicacion</option>
                    </select>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="nomEqu" label="Nombre Equipo *"  readonly disabled='true'></v-text-field>
                  </v-col>

                  
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="numInterno" label="Número Interno"  readonly disabled='true'></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="sala" label="Sala *" readonly disabled='true'></v-text-field>
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
                          label="Fecha inicio o detección *"
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

                    <!-- <v-text-field v-model="Horario" label="Horario" ></v-text-field> -->


                    <v-menu
                      ref="HorarioMantenimiento"
                      v-model="SeleccionarHorario"
                      :close-on-content-click="false"
                      :nudge-right="40"
                      :return-value.sync="Horario"
                      transition="scale-transition"
                      offset-y
                      max-width="290px"
                      min-width="290px"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          v-model="Horario"
                          label="Hora *"
                          prepend-icon="far fa-clock"
                          readonly
                          v-bind="attrs"
                          v-on="on"
                        ></v-text-field>
                      </template>
                      <v-time-picker
                        v-if="SeleccionarHorario"
                        v-model="Horario"
                        color="#008B8B"
                        full-width
                        @click:minute="$refs.HorarioMantenimiento.save(Horario)"
                      ></v-time-picker>
                    </v-menu>


                  </v-col>
                  <v-col>
                    <v-select v-model="Estado" label="Estado *" :items="estados"></v-select>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-select
                      v-model="Tipo_De_Mantenimiento"
                      :items="mantenimientos"
                      label="Tipo de Mantenimiento *"
                      
                    ></v-select>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field
                      v-model="descDano"
                      label="Descripcion Daño *"
                      
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-card>
              <v-btn rounded color="primary" dark @click="e1 = 2">Siguiente</v-btn>
              <v-btn text @click="volverpag()">Cancelar</v-btn>
            </v-stepper-content>

          
            <v-stepper-content  step="2" >
              <v-card color="#424242" style="padding:30px" class="mb-12">
                <v-card-title
                  class="justify-center"
                  style="color:white;font-weigth:bolder;"
                >Mantenimiento</v-card-title>

                <v-row>
                  <!-- REALIZACIÓN DEL MANTENIMIENTO" -->
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
                          label="Fecha de finalización del mantenimiento"
                          readonly
                          prepend-icon = "far fa-calendar-alt"
                          v-bind="attrs"
                          v-on="on"
                          
                        ></v-text-field>
                      </template>
                      <v-date-picker v-model="fechaReal" no-title scrollable>
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="menu2 = false">Cancel</v-btn>
                        <v-btn text color="primary" @click="$refs.menu2.save(fechaReal)">OK</v-btn>
                      </v-date-picker>
                    </v-menu>
                  </v-col>

                  <v-col class="col-sm-12 col-lg-6" v-if="this.mantenimientoExterno">
                    <v-text-field v-model="nomEmpresa" label="Nombre de la empresa contratada *" ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6" v-if="this.mantenimientoExterno">
                    <v-text-field v-model="nit" label="NIT *" ></v-text-field>
                  </v-col>
<!-- AQUI FECHA                   -->
                  <!-- <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="tiempGar" label="Tiempo de Garantía" ></v-text-field>
                  </v-col> -->

                  <v-col class="col-sm-12 col-lg-6" v-if="this.mantenimientoExterno">
                    <v-menu
                      ref="menuTiempGar"
                      v-model="menuTiempGar"
                      :close-on-content-click="false"
                      :return-value.sync="tiempGar"
                      transition="scale-transition"
                      offset-y
                      dark
                      min-width="290px"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          v-model="fechaTiempGar"
                          label="Tiempo de garantía *"
                          readonly
                          prepend-icon = "far fa-calendar-alt"
                          v-bind="attrs"
                          v-on="on"
                          
                        ></v-text-field>
                      </template>
                      <v-date-picker v-model="tiempGar" no-title scrollable>
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="menuTiempGar = false">Cancel</v-btn>
                        <v-btn text color="primary" @click="$refs.menuTiempGar.save(tiempGar)">OK</v-btn>
                      </v-date-picker>
                    </v-menu>
                  </v-col>    


                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-if="this.mantenimientoExterno" v-model="costMant" label="Costo Mantenimiento (COP) *" ></v-text-field>
                    <v-text-field v-else v-model="costMant" label="Costo Mantenimiento (COP)" ></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6" v-if="this.mantenimientoExterno">
                    <v-text-field v-model="numOrdServ" label="No Orden de servicio *" ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6" v-if="this.mantenimientoExterno">
                    <v-text-field v-model="vigencia" label="Vigencia *" ></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6" v-if="this.mantenimientoExterno">
                    <v-text-field v-model="supervisor" label="Supervisor *" ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-if="this.mantenimientoExterno" v-model="repuestos" label="Repuestos *" ></v-text-field>
                    <v-text-field v-else v-model="repuestos" label="Repuestos" ></v-text-field>
                  </v-col>
                  <!-- <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="proxMant" label="Proximo Mantenimiento *" ></v-text-field>
                  </v-col> -->
                  <v-col class="col-sm-12 col-lg-6">
                    <v-menu
                      ref="menuProxMant"
                      v-model="menuProxMant"
                      :close-on-content-click="false"
                      :return-value.sync="proxMant"
                      transition="scale-transition"
                      offset-y
                      dark
                      min-width="290px"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          v-model="fechaproxMant"
                          label="Fecha proximo mantenimiento"
                          readonly
                          prepend-icon = "far fa-calendar-alt"
                          v-bind="attrs"
                          v-on="on"
                          
                        ></v-text-field>
                      </template>
                      <v-date-picker v-model="proxMant" no-title scrollable>
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="menuProxMant = false">Cancel</v-btn>
                        <v-btn text color="primary" @click="$refs.menuProxMant.save(proxMant)">OK</v-btn>
                      </v-date-picker>
                    </v-menu>
                  </v-col>



                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-12">
                    <v-textarea v-model="espMantReal" label="Especificaciones mantenimiento realizado" solo hint="Especificaciones mantenimiento realizado"></v-textarea>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-12">
                    <v-textarea v-model="observaciones" label="Observaciones" solo hint="Observaciones"></v-textarea>
                  </v-col>
                </v-row>
              </v-card>
              <v-btn rounded color="primary" dark @click="formSubmit">Guardar</v-btn>
              <v-btn text @click="volverpag()">Cancelar</v-btn>
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
      SeleccionarHorario:false,
      time:null,
      minute:'',
      
      e1: 1,
      menu:false,
      fecha : new Date().toISOString().substr(0, 10),
      fechaForm:this.formatDate(new Date().toISOString().substr(0, 10)),
      menu2:false,
      menuTiempGar:false,
      menuProxMant:false,
      menuVigencia:false,
      mantenimientoExterno:false,
      fechaReal : new Date().toISOString().substr(0, 10),
      tiempGar: new Date().toISOString().substr(0, 10),
      fechaRealForm:"",
      fechaTiempGar:"",
      mantenimientos:['Interno Correctivo','Externo Correctivo','Interno Predictivo','Externo Predictivo','Interno Preventivo','Externo Preventivo'],
      estados:['EN PROCESO','PENDIENTE','TERMINADO'],
      editable: true,
      placa:'',
      codUsu:'',
      numInterno:'',
      nomUsu:'',
      nomEqu:'',
      sala:'',
      Horario:'',
      Estado:'',
      Tipo_De_Mantenimiento:'',
      descDano:'',
      nomEmpresa:'',
      nit:'',
      
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
    },
    tiempGar (val){
      this.fechaTiempGar = this.formatDate(this.tiempGar)
    },
    proxMant (val){
      this.fechaproxMant = this.formatDate(this.proxMant)
    },
    Tipo_De_Mantenimiento (val){
      this.mantenimientoExterno=(this.Tipo_De_Mantenimiento == this.mantenimientos[1] || this.Tipo_De_Mantenimiento == this.mantenimientos[3] || this.Tipo_De_Mantenimiento == this.mantenimientos[5])
    },    
  },
  methods: {
    volverpag(){
      window.history.back()      
    },
    formatDate (date) {
        if (!date) return null

        const [year, month, day] = date.split('-')
        return `${day}/${month}/${year}`
    },
    formSubmit() {
      console.log("Horario: " + this.Horario);
      let validarDatos=false;
      if (
        this.fechaForm &&        
        this.placa &&
        this.codUsu &&        
        this.nomUsu &&
        this.nomEqu &&
        this.sala &&
        this.Horario &&
        this.Estado &&
        this.descDano 
/*      this.numInterno &&
        this.fechaRealForm &&   
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
        this.observaciones */
      ) {
        if(this.mantenimientoExterno){
          if (
          
          
          this.nomEmpresa &&
          this.nit &&
          this.tiempGar &&
          this.costMant &&
          this.numOrdServ &&
          this.vigencia &&
          this.supervisor &&
          this.repuestos &&
          this.proxMant){      
            validarDatos=true;      
          }else{
            validarDatos=false;
          }
        }else{
          validarDatos=true;
        }
      }else{
        validarDatos=false;
      }






      if (validarDatos) {
        let objeto = this;
        this.axios
          .post(
            "http://" +
              objeto.$serverURI +
              ":" +
              objeto.$serverPort +
              "/Usuario/registrarMant",
            {
              placa:this.placa,
              Numero_Interno:this.numInterno,
              fecha :this.fechaForm,
              codUsu:this.codUsu,
              nomUsu:this.nomUsu,
              sala:this.sala,
              Horario:this.Horario,
              Estado:this.Estado,
              descDano:this.descDano,
              Tipo_De_Mantenimiento:this.Tipo_De_Mantenimiento,
              fechaReal:this.fechaRealForm,
              nomEmpresa:this.nomEmpresa,
              nit:this.nit,
              tiempoGar:this.tiempGar,
              numOrdServ:this.numOrdServ,
              vigencia:this.vigencia,
              supervisor:this.supervisor,
              repuestos:this.repuestos,                           
              costMan:this.costMant,            
              supervisor:this.supervisor,              
              proxMant:this.proxMant ,
              espMantReal:this.espMantReal ,
              observaciones:this.observaciones,
              nomEqu:this.nomEqu
            },
            {
              headers: {
                "Content-Type": "application/json",
                "Authorization": this.$cookies.get("jwt") ? "Bearer " + this.$cookies.get("jwt") : "",
              }
            }
          )
          .then(function(response) {
            if (response.data.status == 1) {
              var respuesta = response.data.mensaje;
              alert(respuesta);
            } else if (response.data.status == 2) {
              alert(response.data.status);
            } else if (response.data.status == 401) {                                
              objeto.$router.push('/');
              alert("Error de sesion");                
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