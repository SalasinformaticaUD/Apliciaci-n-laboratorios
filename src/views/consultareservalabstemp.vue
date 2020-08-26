<template>
  <v-container fluid>
    <HeaderLaboratorista />

    <v-data-table
      :headers="headers"
      :items="reservalab"
      class="elevation-1"
      color="background"
      dark
    >
      <template v-slot:top>
        <v-toolbar flat dark>
          <v-toolbar-title>Consulta reservas</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>

          <v-dialog v-model="dialog" max-width="500px">
            <v-card dark>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col class="col-sm-8 col-lg-8">
                      <v-text-field
                        v-model="agregarUbicacionItem.espacioFisico"
                        :disabled="true"
                        label="Laboratorio"
                      ></v-text-field>
                    </v-col>
                    <v-col class="col-sm-8 col-lg-8">
                      <v-text-field
                        v-model="agregarUbicacionItem.espacioFisico"
                        :disabled="true"
                        label="Banco"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancelar</v-btn>
                <v-btn color="blue darken-1" text @click="save(item)">Enviar</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click="aprobarItem(item)">fas fa-check-circle</v-icon>
        <v-icon small class="mr-2" @click="rechazarItem(item)">fas fa-times-circle</v-icon>
      </template>
      <template v-slot:[`item.estado`]="{ item }">
        <v-chip :color="getColor(item.estado)" dark>{{ item.estado }}</v-chip>
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
        text: "Código",
        align: "start",
        sortable: false,
        value: "codigo"
      },
      { text: "Nombre del estudiante", value: "usuario" },
      { text: "Día", value: "dia" },
      { text: "Hora", value: "hora"},
      { text: "Fecha reserva", value: "fecha_reserva" },
      { text: "Estado de la petición", value: "estado" },
      { text: "Acción", value: "actions", sortable: false }
    ],
    reservalab: [],
    agregarUbicacionIndex: -1,
    agregarUbicacionItem: {},
    infoIndex: -1,
    infoItem: {}
  }),
  // mounted(){
  // this.$verificarLogin();
  // },

  computed: {
    formTitle() {
      return this.agregarUbicacionIndex === -1 ? "New Item" : "Editar Ubicación";
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
    getColor(estado) {
      if (estado == "APROBADO") return "green";
      else if (estado == "PENDIENTE") return "orange";
      else if (estado == "CANCELADO") return "red";
    },
    initialize() {
      (this.reservalab = []), this.buscar();
    },

    inforItem(item) {
      this.infoIndex = this.reservalab.indexOf(item);

      this.infoItem = Object.assign({}, item);
      this.dialog2 = true;
    },
    aprobarItem(item) {
      this.agregarUbicacionIndex = this.reservalab.indexOf(item);
      this.agregarUbicacionItem = Object.assign({}, item);
      this.dialog = true;
    },
    rechazarItem(item) {},

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.agregarUbicacionItem = Object.assign({}, this.defaultItem);
        this.agregarUbicacionIndex = -1;
      });
    },

    save() {
      var confirmacion = confirm("¿Esta seguro de guardar estos cambio?");

      this.placa = this.agregarUbicacionItem.placa;
      this.sala = this.agregarUbicacionItem.sala;

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
              //   objeto.reservalab.splice(index, 1);
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
            "/Usuario/buscarreservalabo",
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          objeto.reservalab = response.data.data;

           console.log(objeto.reservalab);
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>
