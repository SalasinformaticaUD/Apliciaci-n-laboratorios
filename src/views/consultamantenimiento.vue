<template>
  <v-container fluid>
    <HeaderLaboratorista />

    <v-col align="center">
    <v-data-table :headers="headers" :items="equipolab" :search="search" class="elevation-1" color="background" dark>
      <template v-slot:top>
        <v-toolbar flat dark>
          <v-toolbar-title>Consulta Mantenimientos</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>

          <v-text-field
            v-model="search"
            ref="form"
            append-icon="fas far-search"
            label="Buscar"
            single-line
            hide-details
            
            dark
            @keyup.enter="initialize"
          ></v-text-field>
          
          <!--BOTÓN BUSCAR-->
          <v-btn color="primary" @click="initialize">Buscar</v-btn>
          
          <v-spacer></v-spacer>          
          <v-btn color="primary" @click="reset">Reset</v-btn>
          <v-spacer></v-spacer>



          
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{on}">
              <v-btn
                color="primary"
                v-on="on"
                dark
                class="mb-2"
                to="/mantenimiento"
              >Agregar nuevo mantenimiento</v-btn>
            </template>
            <v-card dark>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col class="col-sm-8 col-lg-8">
                      <v-text-field v-model="editedItem.espacioFisico" label="Ubicación"></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancelar</v-btn>
                <v-btn color="blue darken-1" text @click="save(item)">Guardar</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>

          <!-- Información del mantenimiento -->
          <v-dialog v-model="dialog2" max-width="1400px">
            <v-card dark>
              <v-card-title>
                <span class="headline">Mantenimiento </span>
              </v-card-title>
              
              <v-card-text>
                <v-container>
                <v-card-title>
                  <span class="headline">Reporte Mantenimiento Interno</span>
                </v-card-title>
                  <v-col class="col-sm-12 col-lg-10">
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.placa"
                          :disabled="true"
                          label="Placa"
                        ></v-text-field>
                      </v-col>

                      <v-col>
                        <v-text-field
                          v-model="infoItem.tipoMantenimiento"
                          :disabled="true"
                          label="Tipo de Mantenimiento"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.laboratorista"
                          :disabled="true"
                          label="Laboratorista"
                        ></v-text-field>
                      </v-col>
                
                    </v-row>                    
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.fechaMantenimiento"
                          :disabled="true"
                          label="Fecha inicio o detección"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.hora"
                          :disabled="true"
                          label="Hora"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.sala"
                          :disabled="true"
                          label="Sala"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.numeroInterno"
                          :disabled="true"
                          label="Número Interno"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.estado"
                          :disabled="true"
                          label="Estado"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.dano"
                          :disabled="true"
                          label="Daño"
                        ></v-text-field>
                      </v-col>
       
                    </v-row>

              <v-card-title>
                <span class="headline">Reporte Mantenimiento Externo</span>
              </v-card-title>

                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.fechaReal"
                          :disabled="true"
                          label="Fecha de finalización del mantenimiento"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.nomEmpresa"
                          :disabled="true"
                          label="Nombre empresa contratada"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.NIT"
                          :disabled="true"
                          label="NIT"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.tiempGar"
                          :disabled="true"
                          label="Tiempo garantía"
                        ></v-text-field>
                      </v-col>                      
       
                    </v-row>

                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.costMant"
                          :disabled="true"
                          label="Costo Mantenimiento COP"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.numOrdServ"
                          :disabled="true"
                          label="Número Orden de servicio"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.vigencia"
                          :disabled="true"
                          label="Vigencia"
                        ></v-text-field>                        
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.supervisor"
                          :disabled="true"
                          label="Supervisor"
                        ></v-text-field>                        
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.proxMant"
                          :disabled="true"
                          label="Proximo Mantenimiento"
                        ></v-text-field>                        
                      </v-col>
                      
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.repuestos"
                          :disabled="true"
                          label="Repuestos"
                        ></v-text-field>                        
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-textarea
                        v-model="infoItem.espMantReal"
                          :disabled="true"
                          label="Especificaciones del mantenimiento"
                        >
                        </v-textarea>
                                              
                      </v-col>
              
                      <v-col>
                        <v-textarea
                          v-model="infoItem.observaciones"
                          :disabled="true"
                          label="Observaciones"
                        ></v-textarea>                        
                      </v-col>
                   
                    </v-row>

                  </v-col>
                </v-container>
                 <v-row justify="space-around">
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    
                    <v-btn outlined color="blue darken-1" text @click="close2">Cerrar</v-btn>
                  </v-card-actions>
                </v-row>
              </v-card-text>
            </v-card>
          </v-dialog>



          <!-- Edición mantenimiento -->
          <v-dialog v-model="dialog3" max-width="1400px">
            <v-card dark>
              <v-card-title>
                <span class="headline">Edición de Mantenimiento </span>
              </v-card-title>
              
              <v-card-text>
                <v-container>
                <v-card-title>
                  <span class="headline">Reporte Mantenimiento Interno</span>
                </v-card-title>
                  <v-col class="col-sm-12 col-lg-10">

                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.placa"
                          :disabled="true"
                          
                          hint="Placa"
                          persistent-hint
                        ></v-text-field>
                      </v-col>

                      

                      <v-col>
                        <v-text-field
                          v-model="infoItem.numInterno"
                          :disabled="true"
                          :label="infoItem.numeroInterno"
                          hint="Número Interno"
                          persistent-hint
                        ></v-text-field>
                      </v-col>




                      <v-col>

                        <!-- <v-text-field
                          v-model="infoItem.fechaMantenimiento"
                          :disabled="false"                         
                          :label="infoItem.fechaMantenimiento"
                          hint="Fecha de Mantenimiento"
                          persistent-hint
                        ></v-text-field> -->

                        <v-text-field
                          v-model="infoItem.fechaMantenimiento"
                          :disabled="true"                         
                          label="DD/MM/AA"
                          hint="Fecha de inicio o detección"
                          persistent-hint
                          readonly
                        ></v-text-field>




                      </v-col>

                      <v-col>
                        <v-text-field
                          v-model="infoItem.Horario"
                          :disabled="true"
                          :label="infoItem.hora"
                          hint="Hora"
                          persistent-hint
                        ></v-text-field>
                      </v-col>

                      <v-col>
                        <v-text-field
                          v-model="infoItem.sala"
                          :disabled="true"
                          :label="infoItem.sala"
                          hint="Sala"
                          persistent-hint
                        ></v-text-field>
                      </v-col>

                      <v-col>
                        <v-text-field
                          v-model="infoItem.laboratorista"
                          :disabled="true"                          
                          hint="Laboratorista"
                          persistent-hint
                        ></v-text-field>
                      </v-col>
                
                    </v-row>                    
                    <v-row>

                      <v-col>
                        <v-select
                          v-model="infoItem.tipoMantenimiento"
                          :disabled="true"
                          label="Tipo de mantenimiento"
                          :item-value="infoItem.tipoMantenimiento"
                          :items="mantenimientos"
                          
                         
                          
                        ></v-select>
                      </v-col>

                      
                      
                      <v-col>
                        <v-select
                          v-model="infoItem.estado"
                          
                          label="Estado"                          
                          :items="estados">
                        </v-select>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.dano"
                          :disabled="false"
                          label="Daño"
                          
                        ></v-text-field>
                      </v-col>
       
                    </v-row>

              <v-card-title>
                <span class="headline">Reporte Mantenimiento Externo</span>
              </v-card-title>

                    <v-row>

                      <v-col>

                        <!-- <v-menu
                          ref="menu3"
                          v-model="menu3"
                          :close-on-content-click="false"
                          transition="scale-transition"
                          offset-y
                          max-width="290px"
                          min-width="auto"
                        >
                          <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                              v-model="infoItem.fechaReal"
                              label="MM/DD/YYYY"
                              hint="Fecha inicio o detección"
                              persistent-hint
                              prepend-icon="mdi-calendar"
                              v-bind="attrs"
                              @blur="date = parseDate(this.infoItem.fechaReal)"
                              v-on="on"
                              :disabled="true"
                            ></v-text-field>
                          </template>
                          <v-date-picker
                            v-model="date"
                            no-title
                            @input="menu3 = false"
                          ></v-date-picker>
                        </v-menu> -->




                        <!-- <v-text-field
                          v-model="infoItem.fechaReal"
                          :disabled="false"                         
                          :label="infoItem.fechaReal"
                          hint="Fecha de realización del mantenimiento"
                          persistent-hint
                        ></v-text-field> -->

                        <v-menu
                          ref="menu3"
                          v-model="menu3"
                          :close-on-content-click="false"
                          transition="scale-transition"
                          offset-y
                          max-width="290px"
                          min-width="auto"
                        >
                          <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                              v-model="infoItem.fechaReal"
                              label="DD/MM/YYYY"
                              hint="Fecha de finalización del mantenimiento"
                              persistent-hint
                              prepend-icon="fa fa-calendar"
                              v-bind="attrs"
                              @blur="date = parseDate(this.infoItem.fechaReal)"
                              v-on="on"
                              :disabled="false"
                              readonly
                            ></v-text-field>
                          </template>
                          <v-date-picker
                            v-model="date"
                            no-title
                            @input="menu3 = false"
                          ></v-date-picker>
                        </v-menu>


                      </v-col>




                      <!-- <v-col>
                        <v-text-field
                          v-model="infoItem.fechaReal"
                          :disabled="true"
                          label="Fecha de realización del mantenimiento"
                        ></v-text-field>
                      </v-col> -->

                      



                      <v-col>
                        <v-text-field
                          v-model="infoItem.nomEmpresa"
                          :disabled="false"
                          label="Nombre empresa contratada"
                        ></v-text-field>
                      </v-col>

                      <v-col>
                        <v-text-field
                          v-model="infoItem.NIT"
                          :disabled="false"
                          label="NIT"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <!-- <v-text-field
                          v-model="infoItem.tiempGar"
                          :disabled="false"
                          label="Tiempo garantía"
                        ></v-text-field> -->
<!-- TIEMPO GARANTÍA -->
                        <v-menu
                          ref="menuTiemGar"
                          v-model="menuTiemGar"
                          :close-on-content-click="false"
                          transition="scale-transition"
                          offset-y
                          max-width="290px"
                          min-width="auto"
                        >
                          <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                              v-model="infoItem.tiempGar"
                              label="DD/MM/YYYY"
                              hint="Tiempo garantía"
                              persistent-hint
                              prepend-icon="fa fa-calendar"
                              v-bind="attrs"
                              @blur="dateGarantia = parseDate(this.infoItem.tiempGar)"
                              v-on="on"
                              :disabled="false"
                              readonly
                            ></v-text-field>
                          </template>
                          <v-date-picker
                            v-model="dateGarantia"
                            no-title
                            @input="menuTiemGar = false"
                          ></v-date-picker>
                        </v-menu>


                      </v-col>                      
       
                    </v-row>

                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.costMant"
                          :disabled="false"
                          label="Costo Mantenimiento COP"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.numOrdServ"
                          :disabled="false"
                          label="Número Orden de servicio"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.vigencia"
                          :disabled="false"
                          label="Vigencia"
                        ></v-text-field>                        
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.supervisor"
                          :disabled="false"
                          label="Supervisor"
                        ></v-text-field>                        
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.proxMant"
                          :disabled="false"
                          label="Proximo Mantenimiento"
                        ></v-text-field>                        
                      </v-col>
                      
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.repuestos"
                          :disabled="false"
                          label="Repuestos"
                        ></v-text-field>                        
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-textarea
                          v-model="infoItem.espMantReal"
                          :disabled="false"
                          label="Especificaciones del mantenimiento"
                        ></v-textarea>                        
                      </v-col>
              
                      <v-col>
                        <v-textarea
                          v-model="infoItem.observaciones"
                          :disabled="false"
                          label="Observaciones"
                        ></v-textarea>                        
                      </v-col>
                   
                    </v-row>

                  </v-col>
                </v-container>
                 <v-row justify="space-around">
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    
                    <v-btn  rounded color="blue darken-1" dark @click="close2">Cerrar</v-btn>
                    <!-- <v-btn outlined rounded dark color="primary" text @click="close2">Guardar Cambios</v-btn> -->
                    <v-btn rounded color="primary" dark @click="actualizar">Guardar</v-btn>
                  </v-card-actions>
                </v-row>
              </v-card-text>
            </v-card>
          </v-dialog>

        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click="inforItem(item)">fas fa-info-circle</v-icon>
        <v-icon small class="mr-2" @click="editItem(item)">fas fa-edit</v-icon>
        <v-icon small class="mr-2" @click="deleteItem(item)">fas fa-trash</v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>
    </v-data-table>
    </v-col>
  </v-container>
</template>

<script>
import HeaderLaboratorista from "@/components/HeaderLaboratorista.vue";
export default {
  components: {
    HeaderLaboratorista
  },
  data: vm => ({
      date: new Date().toISOString().substr(0, 10),
      dateGarantia: new Date().toISOString().substr(0, 10),
      dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
      //dateFormatted: this.infoItem.fechaMantenimiento,
      menu1: false,
      menu2: false,
    return: {
      search: "",
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
      tiempGar:'',
      costMant:'',
      numOrdServ:'',
      vigencia:'',
      supervisor:'',
      repuestos:'',
      proxMant:'',
      espMantReal:'',
      observaciones:'',
      

      
    },
    dialog: false,
    dialog2: false,
    dialog3: false,
    headers: [
      {
        text: "Placa",
        align: "start",
        sortable: false,
        value: "placa"
      },
      { text: "Numero Interno", value: "numeroInterno" },
      { text: "Fecha", value: "fechaMantenimiento" },
      { text: "Hora", value: "hora" },
      { text: "Laboratorista", value: "laboratorista" }, 
       { text: "Estado del Mantenimiento", value: "estado" }, 
      { text: "Detalles", value: "actions", sortable: false }
    ],
    equipolab: [],
    editedIndex: -1,
    editedItem: {},
    infoIndex: -1,
    infoItem: {},
    mantenimientos:['Interno Correctivo','Externo Correctivo','Interno Predictivo','Externo Predictivo','Interno Preventivo','Externo Preventivo'],
    estados:['EN PROCESO','PENDIENTE','TERMINADO'],
    defaultItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0
    }
  }),
  // mounted(){
  // this.$verificarLogin();
  // },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Editar Ubicación";
    },

    computedDateFormatted () {
      return this.formatDate(this.date)
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },

    date (val) {
      this.infoItem.fechaReal = this.formatDate(this.date)
    },  
    dateGarantia(val){
      this.infoItem.tiempGar = this.formatDate(this.dateGarantia)
    },
  },

  created() {
    this.initialize();
  },

  methods: {
      formatDate (date) {
        if (!date) return null

        const [year, month, day] = date.split('-')
        return `${day}/${month}/${year}`
      },
      
      FechaMant (){
        let objeto = this;
        return objeto.infoItem.infoItem.fechaMantenimiento;
      },


      parseDate (date) {
        if (!date) return null

        const [month, day, year] = date.split('/')
        return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
      },
    


    initialize() {
      (this.equipolab = []);
       this.buscar();
    },

    reset () {
      this.$refs.form.reset(), this.initialize();
    },


    inforItem(item) {
      this.infoIndex = this.equipolab.indexOf(item);

      this.infoItem = Object.assign({}, item);
      this.dialog2 = true;
    },

    editItem(item){
      this.infoIndex = this.equipolab.indexOf(item);

      this.infoItem = Object.assign({}, item);
      this.dialog3 = true;
    },

    BorrarValores(){
      placa='';
      codUsu='';
      numInterno='';
      nomUsu='';
      nomEqu='';
      sala='';
      Horario='';
      Estado='';
      Tipo_De_Mantenimiento='';
      descDano='';
      nomEmpresa='';
      nit='';
      tiempGar='';
      costMant='';
      numOrdServ='';
      vigencia='';
      supervisor='';
      repuestos='';
      proxMant='';
      espMantReal='';
      observaciones='';

    },
  
    close2() {
      let obj=this;
      this.dialog2 = false;
      this.dialog3 = false;
      console.log(obj.infoItem.dano);
      BorrarValores();


      this.$nextTick(() => {
        this.infoItem = Object.assign({}, this.defaultItem);
        this.infoIndex = -1;
      });
    },

    actualizar(){
      
      var confirmacion = confirm("¿Esta seguro de guardar estos cambios?");
      if (confirmacion) {
          
        let objeto=this;
        this.axios
          .post(
            "http://"+objeto.$serverURI+":"+objeto.$serverPort+"/Usuario/actualizarMant",
            {
              placa: objeto.infoItem.placa,
              Tipo_De_Mantenimiento:this.infoItem.tipoMantenimiento,
              nomUsu:this.infoItem.laboratorista,
              fecha :this.infoItem.fechaMantenimiento,
              Horario:this.infoItem.hora,
              sala:this.infoItem.sala,
              Estado:this.infoItem.estado,
              descDano:this.infoItem.dano,
              fechaReal:this.infoItem.fechaReal,
              nomEmpresa:this.infoItem.nomEmpresa,
              nit:this.infoItem.NIT,
              tiempoGar:this.infoItem.tiempGar,
              costMan:this.infoItem.costMant,   
              Numero_Interno:this.infoItem.numeroInterno,
              numOrdServ:this.infoItem.numOrdServ,
              vigencia:this.infoItem.vigencia,
              supervisor:this.infoItem.supervisor,
              repuestos:this.infoItem.repuestos,                           
              supervisor:this.infoItem.supervisor,              
              proxMant:this.infoItem.proxMant ,
              espMantReal:this.infoItem.espMantReal ,
              observaciones:this.infoItem.observaciones,
            },
            {
              headers: {
                "Content-Type": "application/json",
                "Authorization": this.$cookies.get("jwt") ? "Bearer " + this.$cookies.get("jwt") : "",
              }
            }
          )
          .then(function(response) {
              var respuesta = response.data.mensaje;
              var status = response.data.status;
              if (status == "1") {
                alert(respuesta);
                objeto.buscar();
                //   objeto.reservalab.splice(index, 1);
              }else if (response.data.status == 401) {                                
                objeto.$router.push('/');
                alert("Error de sesion");                
              }
          })
          .catch(function(error) {
            objeto.output = error;
          });

      }
    },


    buscar() {
      let objeto = this;
      this.axios
        .get(
          "http://" +
            objeto.$serverURI +
            ":" +
            objeto.$serverPort +
            "/Usuario/consultaMantenimiento",
          {
            headers: {
              "Content-Type": "application/json",
              "Authorization": this.$cookies.get("jwt") ? "Bearer " + this.$cookies.get("jwt") : "",
            }
          }
        )
        .then(function(response) {
          if (response.data.status == 401) {                                
            objeto.$router.push('/');
            alert("Error de sesion");                
          }
          objeto.equipolab = response.data.data;
           console.log("AJI");
           console.log(objeto.equipolab);
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>
