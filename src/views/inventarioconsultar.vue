<template>
  <v-container fluid>
    <HeaderLaboratorista />

    <v-data-table :headers="headers" :items="equipolab" class="elevation-1" color="background">
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Consulta inventario equipos</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{on}">
              <v-btn
                color="primary"
                v-on="on"
                dark
                class="mb-2"
                to="/addequipo"
              >Agregar nuevo elemento</v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="8" md="8">
                      <v-text-field v-model="editedItem.sala" label="Ubicación"></v-text-field>
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
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">fas fa-edit</v-icon>
        <v-icon small class="mr-2" @click="activeItem(item)">fas fa-check-circle</v-icon>
        <v-icon small class="mr-2" @click="desactiveItem(item)">fas fa-times-circle</v-icon>
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
    headers: [
      {
        text: "Placa",
        align: "start",
        sortable: false,
        value: "placa"
      },
      { text: "Nombre equipo", value: "nombre" },
      { text: "Marca", value: "marca" },
      { text: "Serial", value: "serial" },
      { text: "Estado", value: "estado" },
      { text: "Sala", value: "sala" },
      { text: "Acción", value: "actions", sortable: false }
    ],
    equipolab: [],
    editedIndex: -1,
    editedItem: {},
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
      (this.equipolab = []), this.buscar();
    },

    editItem(item) {
      this.editedIndex = this.equipolab.indexOf(item);

      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    desactiveItem(item) {
      var confirmacion = confirm("¿Esta seguro de desactivar este usuario?");

      if (confirmacion) {
        const index = this.equipolab.indexOf(item);
        this.placa = this.equipolab[index].placa;

        let objeto = this;
        this.axios
          .post(
            "http://" +
              objeto.$serverURI +
              ":" +
              objeto.$serverPort +
              "/Usuario/desactivarEquipo",
            {
              placa: objeto.placa
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
              //   objeto.equipolab.splice(index, 1);
              objeto.buscar();
            }
          })

          .catch(function(error) {
            alert(error);
          });
      }
    },

    activeItem(item) {
      var confirmacion = confirm("¿Esta seguro de activar este usuario?");

      if (confirmacion) {
        const index = this.equipolab.indexOf(item);
        this.placa = this.equipolab[index].placa;

        let objeto = this;
        this.axios
          .post(
            "http://" +
              objeto.$serverURI +
              ":" +
              objeto.$serverPort +
              "/Usuario/activarEquipo",
            {
              placa: objeto.placa
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
              //   objeto.equipolab.splice(index, 1);
              objeto.buscar();
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

      this.placa = this.editedItem.placa;
      this.sala = this.editedItem.sala;

      if (confirmacion) {
        let objeto = this;
        this.axios
          .post(
            "http://" +
              objeto.$serverURI +
              ":" +
              objeto.$serverPort +
              "/Usuario/editarequipo",
            {
              placa: objeto.placa,
              sala: objeto.sala.toUpperCase()
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
              //   objeto.equipolab.splice(index, 1);
            }
          })
          .catch(function(error) {
            alert(error);
          });
      }
      this.buscar();
      this.close();
    },
    buscar() {
      let objeto = this;
      this.axios
        .get(
          "http://" +
            objeto.$serverURI +
            ":" +
            objeto.$serverPort +
            "/Usuario/consultarEquipo",
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          objeto.equipolab = response.data.data;
          console.log(objeto.equipolab);
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>
