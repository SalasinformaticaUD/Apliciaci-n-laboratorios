<template>
  <v-container fluid>
    <HeaderLaboratorista />

    <v-card>
    <v-card-title>
      Reservas
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="fas far-search"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="usuariolab"
      :search="search"
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
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">fas fa-edit</v-icon>
        <v-icon small @click="deleteItem(item)">fas fa-trash</v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>
    </v-data-table>
    </v-card>
  </v-container>
</template>

<script>
import HeaderLaboratorista from "@/components/HeaderLaboratorista.vue";
export default {
  components: {
    HeaderLaboratorista
  },
  data: () => ({
    dialog: false,
    search: "",
    headers: [
      {
        text: "Usuario",
        align: "start",
        sortable: false,
        value: "usuario"
      },
      { text: "Codigo", value: "codigo" },
      { text: "Hora", value: "hora" },
      { text: "Dia", value: "dia" },
      { text: "Fecha Adicional", value: "fecha_adicional" },
      { text: "Fecha Reserva", value: "fecha_reserva" },
      { text: "Sala", value: "sala" },
      { text: "Banco", value: "banco" },
      { text: "Elemento", value: "elemento" },
      { text: "Actions", value: "actions", sortable: false }
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
    codigo: "20201195009",
    editedIndex: -1,
    editedItem: {
      elemento: "",
    },
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

    deleteItem(item) {
      var confirmacion = confirm("¿Esta seguro de eliminar este laboratorio?");

      if (confirmacion) {
        const index = this.usuariolab.indexOf(item);
        this.sala = this.usuariolab[index].sala;
        this.banco = this.usuariolab[index].banco;
        

        let objeto = this;
        this.axios
          .post(
            "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/borrarreserva",
            {
              codigo: "20201195009",
              sala: objeto.sala,
              banco: objeto.banco,
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

    save() {
      var confirmacion = confirm("¿Esta seguro de guardar estos cambio?");
      this.elemento = this.editedItem.elemento;
      this.hora = this.editedItem.hora;
      this.dia = this.editedItem.dia;
      this.fecha_adicional = this.editedItem.fecha_adicional;
      this.fecha_reserva = this.editedItem.fecha_reserva;
      this.sala = this.editedItem.sala;
      this.banco = this.editedItem.banco;
      
      if (confirmacion) {
        let objeto = this;
        this.axios
          .post(
            "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/editarreserva",
            {
              codigo: "20201195009",
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
      this.axios
        .get(
         "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/buscarreservalabo",
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