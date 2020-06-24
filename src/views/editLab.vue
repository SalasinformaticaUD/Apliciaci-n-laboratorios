<template>
  <v-container fluid>
    <HeaderAdmin />

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
              <v-btn color="primary" dark class="mb-2" v-on="on">Nuevo usuario</v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.name" label="Nombre Laboratorista"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.calories" label="Correo"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.fat" label="Telefono"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.carbs" label="Identificación"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.protein" label="Clave"></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="save">Save</v-btn>
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
  </v-container>
</template>

<script>
import HeaderAdmin from "@/components/HeaderAdmin.vue";
export default {
  components: {
    HeaderAdmin
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
      { text: "Identificacion", value: "identificacion" },
      { text: "Estado", value: "estado" },
      { text: "Actions", value: "actions", sortable: false }
    ],
    usuariolab: [],
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
  mounted(){
  this.$verificarLogin();
  },

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
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      var confirmacion = confirm("¿Esta seguro de eliminar este usuario?");

      if (confirmacion) {
        const index = this.usuariolab.indexOf(item);
        this.usuario = this.usuariolab[index].usuario;

        let objeto = this;
        this.axios
          .post(
            "http://giovannygz.ddns.net:5000/Usuario/borrar",
            {
              usuario: objeto.usuario
              
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
      if (this.editedIndex > -1) {
        Object.assign(this.usuariolab[this.editedIndex], this.editedItem);
      } else {
        this.usuariolab.push(this.editedItem);
      }
      this.close();
    },
    buscar() {
      let objeto = this;
      this.axios
        .get("http://giovannygz.ddns.net:5000/Usuario/consultarLabo", {
          headers: {
            "Content-Type": "application/json"
          }
        })
        .then(function(response) {
          objeto.usuariolab = response.data.data;
          console.log( objeto.usuariolab);
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>
