<template>
    <v-container>
{{output}}
<v-button @click="buscar" x-large color="success" dark >
  Buscar
</v-button>

    </v-container>
</template>



<script>
export default {
  data() {
    return {
     output: ""
    };
  },
  methods: {
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
          objeto.output=response.data.data[0].Correo
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>
