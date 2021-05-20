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
                          label="Fecha Mantenimiento Laboratorista"
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
                          label="Fecha Mantenimiento externo"
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
                        <v-text-field
                          v-model="infoItem.espMantReal"
                          :disabled="true"
                          label="Especificaciones del mantenimiento"
                        ></v-text-field>                        
                      </v-col>
              
                      <v-col>
                        <v-text-field
                          v-model="infoItem.observaciones"
                          :disabled="true"
                          label="Observaciones"
                        ></v-text-field>                        
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
                      <v-col class="col-sm-12 col-lg-6">
                        <v-select
                          v-model="Tipo_De_Mantenimiento"
                          :items="mantenimientos"
                          label="Tipo de Mantenimiento"
                          solo
                        ></v-select>
                      </v-col>
                    </v-row>

                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.placa"
                          :disabled="false"
                          label="Placa"
                        ></v-text-field>
                      </v-col>


                      <v-col>
                        <v-select
                          v-model="infoItem.tipoMantenimiento"
                          :disabled="false"
                          :items="mantenimientos"
                          
                          label="Tipo de Mantenimiento"
                        ></v-select>
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
                          label="Fecha Mantenimiento Laboratorista"
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
                          label="Fecha Mantenimiento externo"
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
                        <v-text-field
                          v-model="infoItem.espMantReal"
                          :disabled="true"
                          label="Especificaciones del mantenimiento"
                        ></v-text-field>                        
                      </v-col>
              
                      <v-col>
                        <v-text-field
                          v-model="infoItem.observaciones"
                          :disabled="true"
                          label="Observaciones"
                        ></v-text-field>                        
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
  data: () => ({
    return: {
      search: "",
      Tipo_De_Mantenimiento:'',
      
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
    }
  },

  watch: {
    dialog(val) {
      val || this.close();
    }
  },

  created() {
    this.initialize();
  },

  methods: {
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

  
    close2() {
      this.dialog2 = false;
      this.dialog3 = false;
      this.$nextTick(() => {
        this.infoItem = Object.assign({}, this.defaultItem);
        this.infoIndex = -1;
      });
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
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
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
