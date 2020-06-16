<template>
  <v-container fluid>
    <HeaderLaboratorista />
    <v-card style="padding:25px" color="background">

    <v-data-table
      :headers="headers"
      :items="reserva"
      sort-by="Usuario"
      class="elevation-1"
      color="background"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Consulta y Cancelación</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on }">
              <v-btn color="primary" dark class="mb-2" v-on="on"
                >Nueva reserva</v-btn
              >
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.name"
                        label="Dessert name"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.calories"
                        label="Calories"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.fat"
                        label="Fat (g)"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.carbs"
                        label="Carbs (g)"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.protein"
                        label="Protein (g)"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancelar</v-btn>
                <v-btn color="blue darken-1" text @click="save">Guardar</v-btn>
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
    headers: [
      {
        text: "correo",
        align: "start",
        sortable: false,
        value: "correo"
      },
      { text: "Usuario", value: "usuario" },
      { text: "Identificación", value: "identificacion" },
      { text: "Hora", value: "Hora" },
      { text: "Banco", value: "" },
      { text: "Actions", value: "actions", sortable: false }
    ],
    reserva: [],
    editedIndex: -1,
    editedItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0
    },
    defaultItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0
    }
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Nueva reserva" : "Editar ";
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
      this.reserva = [
            ],
      this.buscar();       
    },

    editItem(item) {
      this.editedIndex = this.reserva.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.reserva.indexOf(item);
      confirm("¿Esta seguro de eliminar esta reserva?") &&
        this.reserva.splice(index, 1);
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.reserva[this.editedIndex], this.editedItem);
      } else {
        this.reserva.push(this.editedItem);
      }
      this.close();
    },
     buscar() {
      let objeto = this;
      this.axios
        .get(
          "http://giovannygz.ddns.net:5000/Usuario/registrar",
            {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          objeto.reserva=response.data.data
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>
