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
              <v-btn color="primary" dark class="mb-2" to='/registrouser'>Nuevo usuario</v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.usuario" label="Nombre Laboratorista"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.correo" label="Correo"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="contraseña" label="Clave"></v-text-field>
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
import HeaderAdmin from "@/components/HeaderAdmin.vue";
export default {
  components: {
    HeaderAdmin
  },
  data: () => ({
    return: {
      contraseña:""      
    },
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
      return this.editedIndex === -1 ? "New Item" : "Editar Usuario";
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
 
      this.contraseña = this.contraseña;

      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    desactiveItem(item) {
      var confirmacion = confirm("¿Esta seguro de desactivar este usuario?");

      if (confirmacion) {
        const index = this.usuariolab.indexOf(item);
        this.codigo = this.usuariolab[index].identificacion;

        let objeto = this;
        this.axios
          .post(
            "http://giovannygz.ddns.net:5000/Usuario/desactivar",
            {
              codigo: objeto.codigo
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
              //   objeto.usuariolab.splice(index, 1);
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
        const index = this.usuariolab.indexOf(item);
        this.codigo = this.usuariolab[index].identificacion;

        let objeto = this;
        this.axios
          .post(
            "http://giovannygz.ddns.net:5000/Usuario/activar",
            {
              codigo: objeto.codigo
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
              //   objeto.usuariolab.splice(index, 1);
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
  
    
      this.usuario = this.editedItem.usuario;
      this.codigo = this.editedItem.identificacion;
      this.correo = this.editedItem.correo;
      
      if (confirmacion) {
        let objeto = this;
        this.axios
          .post(
            "http://giovannygz.ddns.net:5000/Usuario/editaruser",
            {
              codigo: objeto.codigo,
              usuario: objeto.usuario,
              contraseña: objeto.contraseña,
              correo: objeto.correo
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
      this.buscar();
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
          console.log(objeto.usuariolab);
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>
