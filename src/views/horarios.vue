<template>
  <v-container fluid>
    <HeaderLaboratorista />
    <v-card>
      <v-card-title>
      Horarios
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
          <v-toolbar-title>Horarios </v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          
        </v-toolbar>
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
        text: "Asignatura",
        align: "start",
        sortable: false,
        value: "asignatura"
      },
      { text: "Docente", value: "docente" },
      { text: "Proyecto", value: "proyecto" },
      { text: "Grupo", value: "grupo" },
      { text: "Día", value: "dia" },
      { text: "Grupo", value: "grupo" },
      { text: "Horario", value: "horario" },
      { text: "Sala", value: "sala" },
      { text: "Fecha", value: "fecha" },
      
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
  mounted(){
  this.$verificarLogin();
  },

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
    buscar() {
      let objeto = this;
      this.axios
        .get("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/buscarhorarios", {
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
