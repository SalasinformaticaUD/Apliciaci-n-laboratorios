<template>
  <v-container fluid>
    <HeaderLaboratorista />

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
                <span class="headline">Mantenimiento</span>
              </v-card-title>
              <v-card-text>
                <v-container>
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
                          v-model="infoItem.dano"
                          :disabled="true"
                          label="Daño"
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
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>
    </v-data-table>
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
      search: ""
    },
    dialog: false,
    dialog2: false,
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
  
    close2() {
      this.dialog2 = false;
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
