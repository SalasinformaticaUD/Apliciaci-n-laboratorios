<template>
  <v-container fluid>
    <Headerestudiantes />
    <v-row>
      <v-col>

    <v-data-table
      :headers="headers"
      :items="usuariolab"
      sort-by="calories"
      class="elevation-1"
      color="background"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Edición y eliminación</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on }">
              <v-btn
                color="primary"
                dark
                class="mb-2"
                v-on="on"
                to="/reservaestudiante"
              >Nueva reserva</v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-combobox v-model="editedItem.elemento" :items="Elementos" label="Seleccionar..." multiple
                         ></v-combobox>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="save(item)">Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>

          <v-dialog v-model="dialogFicha" max-width="700px">
            <v-card>
              <v-card-title>
                <span class="headline">Ficha de laboratorio</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="3">
                      <v-text-field
                        v-model="infoItem.fecha_adicional"
                        :disabled="true"
                        label="Fecha adicional"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="3">
                      <v-text-field
                        v-model="infoItem.hora"
                        :disabled="true"
                        label="Hora del adicional"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="3">
                      <v-text-field
                        v-model="infoItem.sala"
                        :disabled="true"
                        label="Laboratorio adicional"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="3">
                      <v-text-field
                        v-model="infoItem.banco"
                        :disabled="true"
                        label="Banco del laboratorio"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-divider></v-divider>
                  <v-row no-gutters class="pa-1">
                    <v-col cols="12" sm="1" class="text-sm-center font-weight-black">
                      No.
                    </v-col>
                    <v-col></v-col>
                    <v-col cols="12" sm="8" class="font-weight-black">
                      Elementos
                    </v-col>
                    <v-col cols="12" sm="2" class="text-sm-center font-weight-black">
                      Eliminar
                    </v-col>
                  </v-row>
                  <v-row no-gutters>
                    <v-col v-for= "(item,index) in infoItem.elemento" :key="index" cols="12" sm="12">
                      <v-divider></v-divider>  
                      <v-row no-gutters class="pa-1">
                        <v-col cols="12" sm="1" class="text-sm-center">
                          {{index+1}}.
                        </v-col>
                        <v-col></v-col>
                        <v-col cols="12" sm="8">
                          {{item}}
                        </v-col>
                        <v-col cols="12" sm="2" class="text-sm-center">
                          <v-icon 
                            small 
                            @click="infoItem.elemento = infoItem.elemento.filter((i) => i !== item)"
                          > 
                            fas fa-trash-alt</v-icon>
                          </v-col>
                      </v-row>
                    </v-col>                  
                  </v-row>
                  <v-divider></v-divider>  
                </v-container>
                <v-card-actions class="justify-end">
                  <v-btn rounded color="primary" dark @click="guardarFichaEdit()">
                    Guardar     
                    </v-btn>
                </v-card-actions>
              </v-card-text>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>

      <template v-slot:[`item.actions`]="{ item }">
        <v-icon 
          class="mr-2" 
          small 
          @click="fichaItem(item)"
        >
          fas fa-info-circle
        </v-icon>
        <v-icon
          small
          class="mr-2"
          @click="editItem(item)"
        >
          fas fa-edit
        </v-icon>
        <v-icon
          small
          @click="deleteItem(item)"
        >
          fas fa-trash
        </v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>
    </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Headerestudiantes from "@/components/Headerestudiantes.vue";
export default {
  components: {
    Headerestudiantes
  },
  data: () => ({
    dialog: false,
    headers: [
      {
        text: "Hora",
        align: "start",
        sortable: false,
        value: "hora"
      },
      { text: "Dia", value: "dia" },
      { text: "Fecha Adicional", value: "fecha_adicional" },
      { text: "Fecha Reserva", value: "fecha_reserva" },
      { text: "Sala", value: "sala" },
      { text: "Banco", value: "banco" },
      { text: "Elemento", value: "elemento" },
      { text: "Acciones", value: "actions", sortable: false }
    ],
    Elementos: [
      "Osciloscopio",
      "Generador de Señales",
      "Fuente DC",
      "Multímetro",
      "Luxómetro",
      "Variac"
    ],
    usuariolab: [],
    codigo: "20201195009", //QUITAR ESTE
    editedIndex: -1,
    codigoLab:"",
    usuario: "",
    editedItem: {
      elemento: "",
    },
    defaultItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0
    },

    dialogFicha: false,
    infoIndex: -1,
    infoItem: {},
  }),
  // mounted(){
  // this.$verificarLogin();
  // },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
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
      (this.usuariolab = []), this.buscar();
    },

    editItem(item) {
      this.editedIndex = this.usuariolab.indexOf(item);
      this.editedItem = Object.assign({},item);
      this.dialog = true;
    },
    fichaItem(item) {
      var date = new Date();
      var hour = date.getHours();
      var minutes = date.getMinutes();
      date = date.getTime();
      // var date = this.conversionDate(new Date(date));
      this.infoIndex = this.usuariolab.indexOf(item);
      this.infoItem = Object.assign({}, item);
      this.dialogFicha = true;
      console.log(new Date(this.parseDate(this.infoItem.fecha_adicional)))
      // console.log(date.getTime() - new Date("2021-02-25").getTime())
      if(this.infoItem.fecha_adicional===date && this.infoItem.hora>(hour+1)){
        console.log("Misma fecha")
      }
      
      console.log(date)
      console.log(hour+1)
      console.log(minutes)
      console.log(this.infoItem.hora)
    },
    parseDate(date) {
      if (!date) return null
      const [day, month, year] = date.split('/')
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    deleteItem(item) {
      var confirmacion = confirm("¿Esta seguro de eliminar este laboratorio?");

      if (confirmacion) {
        const index = this.usuariolab.indexOf(item);
        this.sala = this.usuariolab[index].sala;
        this.banco = this.usuariolab[index].banco;
        this.fecha_adicional = this.usuariolab[index].fecha_adicional;
        this.hora = this.usuariolab[index].hora;
        

        let objeto = this;
        
        objeto.token = localStorage.cdcb0830cc2dd220;
        
        var encrypted = objeto.$cookies.get("user_session");      
        var desen = objeto.$Crypto.AES.decrypt(encrypted, objeto.token);
        var codlab = desen.toString(objeto.$Crypto.enc.Utf8);
        objeto.codigoLab = objeto.$Crypto.AES.decrypt(objeto.$cookies.get("user_session"), objeto.token);
        objeto.codigoLab=objeto.codigoLab.toString(objeto.$Crypto.enc.Utf8);

        console.log(objeto.codigoLab,this.sala,this.banco,this.fecha_adicional,this.hora);

        this.axios
          .post(
            "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/borrarreserva",
            {
              codigo: objeto.codigoLab,
              sala: this.sala,
              banco: this.banco,
              fecha_adicional: this.fecha_adicional,
              hora: this.hora
            },
            {
              headers: {
                "Content-Type": "application/json"
              }
            }
          )
          .then(function(response) {
            var respuesta = response.data.mensaje;
            var status = response.data.status;
            if (status == "1") {
              alert(respuesta);
              objeto.usuariolab.splice(index, 1);
            }
          })
          .catch(function(error) {
            alert(error);
          });
      }
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    guardarFichaEdit() {
      var confirmacion = confirm("¿Esta seguro de guardar estos cambio?");
      this.elemento = this.infoItem.elemento;
      this.hora = this.infoItem.hora;
      this.dia = this.infoItem.dia;
      this.fecha_adicional = this.infoItem.fecha_adicional;
      this.fecha_reserva = this.infoItem.fecha_reserva;
      this.sala = this.infoItem.sala;
      this.banco = this.infoItem.banco;
    

      if (confirmacion) {
        let objeto = this;
        
        objeto.token = localStorage.cdcb0830cc2dd220;
      
        var encrypted = objeto.$cookies.get("user_session");      
        var desen = objeto.$Crypto.AES.decrypt(encrypted, objeto.token);
        var codlab = desen.toString(objeto.$Crypto.enc.Utf8);
        objeto.codigoLab = objeto.$Crypto.AES.decrypt(objeto.$cookies.get("user_session"), objeto.token);
        objeto.codigoLab=objeto.codigoLab.toString(objeto.$Crypto.enc.Utf8);

        this.axios
          .post(
            "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/editarreserva",
            {
              codigo: this.codigoLab,
              hora: this.hora,
              dia: this.dia,
              fecha_adicional: this.fecha_adicional,
              fecha_reserva: this.fecha_reserva,
              sala: this.sala,
              banco: this.banco,
              elemento: this.elemento
            },
            {
              headers: {
                "Content-Type": "application/json"
              }
            }
          )
          .then(function(response) {
            var respuesta = response.data.mensaje;
            var status = response.data.status;
            if (status == "1") {
              alert(respuesta);
              objeto.dialogFicha = false;
              objeto.buscar();
              //   objeto.usuariolab.splice(index, 1);
            }
          })
          .catch(function(error) {
            alert(error);
          });
      }
      this.close();
    },
    buscar() {
      let objeto = this;
      
      
      objeto.token = localStorage.cdcb0830cc2dd220;
      
      var encrypted = objeto.$cookies.get("user_session");      
      var desen = objeto.$Crypto.AES.decrypt(encrypted, objeto.token);
      var codlab = desen.toString(objeto.$Crypto.enc.Utf8);
      objeto.codigoLab = objeto.$Crypto.AES.decrypt(objeto.$cookies.get("user_session"), objeto.token);
      objeto.codigoLab=objeto.codigoLab.toString(objeto.$Crypto.enc.Utf8);

      this.axios
        .post(
          "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/buscarreserva",
          {
            codigo: objeto.codigoLab
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          objeto.usuariolab = response.data.data;
          console.log(objeto.usuariolab);
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>