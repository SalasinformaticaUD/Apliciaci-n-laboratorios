<template>
  <v-container fluid>
    <Headerestudiantes />

    <v-col align="center" class="mt-2">
      <v-container fluid>
        <v-row justify="center">
          <v-col cols="6" sm="2" align="center" v-for="(item,index) in urlSoftware" :key="index">
            <v-card max-width="160px" height="160px" class="pt-1" align="center" shaped>
              <v-img
                contain
                height="150"
                width="150"
                :src = item
              ></v-img>
            </v-card>
          </v-col>
        </v-row>
      </v-container>

      <v-container fluid>
        <v-col align="center">
            <v-card color="grey darken-3" dark style="padding:30px" max-width="700px">
              <h1 align="center">Solicitud de licencias de software</h1>            
              <p align="justify">
                Siga los pasos que se muestran a continuación para realizar la solicitud de una licencia:
              </p>

              <p align="justify">1. Ingrese su nombre completo</p>
            <v-form ref="form" v-model="validForm" lazy-validation>
              <v-row no-gutters class="pa-2 mb-3 mt-n5">
                <v-text-field
                  label="Tu respuesta"
                  persistent-hint
                  hide-details="auto"
                  v-model = "form.nombre"
                  dense
                  single-line
                  dark
                  :rules="[rules.required]"
                ></v-text-field>
              </v-row>

              <p align="justify">2. Ingrese su código estudiantil</p>
              <v-row no-gutters class="pa-2 mb-3 mt-n5">
                <v-text-field
                  label="Tu respuesta"
                  persistent-hint
                  hide-details="auto"
                  v-model = "form.codigo"
                  dense
                  single-line
                  dark
                  :rules="[rules.required]"
                ></v-text-field>
              </v-row>

              <p align="justify">3. Ingrese su correo institucional</p>
              <v-row no-gutters class="pa-2 mb-3 mt-n5">
                <v-text-field
                  label="Tu respuesta"
                  persistent-hint
                  hide-details="auto"
                  v-model = "form.correo"
                  dense
                  single-line
                  dark
                  :rules="[rules.required]"
                ></v-text-field>
              </v-row>

              <p align="justify">4. Documento de identidad</p>
              <v-row no-gutters class="pa-2 mb-3 mt-n5">
                <v-text-field
                  label="Tu respuesta"
                  persistent-hint
                  hide-details="auto"
                  v-model = "form.documento"
                  dense
                  single-line
                  dark
                  :rules="[rules.required]"
                ></v-text-field>
              </v-row>

              <p align="justify">5. Proyecto curricular</p>
              <v-row no-gutters class="pa-2 mb-3 mt-n5">
                <v-text-field
                  label="Tu respuesta"
                  persistent-hint
                  hide-details="auto"
                  v-model = "form.proyecto"
                  dense
                  single-line
                  dark
                  :rules="[rules.required]"
                ></v-text-field>
              </v-row>

              <p align="justify">6. Tipo de usuario</p>
              <v-row no-gutters class="pa-2 mt-n8">
                <v-autocomplete
                  v-model="form.tipoUsuario"
                  :rules="[rules.required]"
                  single-line
                  :items = "tiposUsuario"
                  placeholder="Seleccionar..."
                  required
                ></v-autocomplete>
              </v-row>

              <p align="justify">7. Facultad</p>
              <v-row no-gutters class="pa-2 mt-n8">
                <v-autocomplete
                  v-model="form.facultad"
                  :rules="[rules.required]"
                  single-line
                  :items = "facultades"
                  placeholder="Seleccionar..."
                  required
                ></v-autocomplete>
              </v-row>

              <p align="justify">8. Software interesado</p>
              <v-row no-gutters class="pa-2 mt-n8">
                <v-autocomplete
                  v-model="form.software"
                  :rules="[rules.required]"
                  single-line
                  :items = "software"
                  placeholder="Seleccionar..."
                  required
                ></v-autocomplete>
              </v-row>

              <p align="justify">9. ¿Cuál es el motivo y la finalidad de la solicitud de software?</p>
              <v-row no-gutters class="pa-2 mt-n8">
                <v-autocomplete
                  v-model="form.motivo"
                  :rules="[rules.required]"
                  single-line
                  :items = "motivos"
                  placeholder="Seleccionar..."
                  required
                ></v-autocomplete>
              </v-row>
              </v-form>

            </v-card>
          </v-col>
      </v-container>
    
      <v-container fluid>
        <v-row class="px-10 mx-10 text-center" justify="center">
          <v-col cols="12" sm="1" class="mt-3">
            <v-btn rounded color="primary" dark @click="send()">
              Enviar
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-col>  
  </v-container>
</template>

<style scoped>
    .centered-input >>> input {
      text-align: center
    }
</style>

<script>
import Headerestudiantes from "@/components/Headerestudiantes.vue";
export default {
  components: {
    Headerestudiantes
  },
  data() {
    return {    

      urlSoftware:{
        psim: "http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/psimLogo",
        solidWorks: "http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/solidWorksLogo",
        xirio: "http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/xirioLogo",
        altium: "http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/altiumLogo",
      },

      tiposUsuario: ["Administrativo", "Estudiante", "Profesor"],
      facultades: ["ASAB", "Ciencias y Educación", "Ingeniería", "Medio Ambiente y Recursos Naturales", "Tecnológica"],
      software: ["PSIM2021a", "Solidworks 2020", "XIRIO", "Altium"],
      motivos: ["Extensión", "Investigación", "Academico", "Tesis"],

      validForm: false,

      form:{
        nombre: "",
        codigo: "",
        correo: "",
        documento: "",
        proyecto: "",
        tipoUsuario: "",
        facultad: "",
        software: "",
        motivo: "",
      },

      rules:{
        required: value => !!value || "Este espacio es requerido.",
      }, 
      
    }
  },
  created(){
  },

  mounted(){   
    console.log(this.imgSoftware);
  },

  watch:{
  },

  methods:{
    send(){
      if(this.$refs.form.validate()){
        this.buscarAdicionales();
      }
    },
    buscarAdicionales(){
      let objeto = this;
      this.axios.post("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/licenciasEstudiantes",
        {
          form: objeto.form
        },
        {
          headers: {
            "Content-Type": "application/json",
            "Authorization": this.$cookies.get("jwt") ? "Bearer " + this.$cookies.get("jwt") : "",
          }
        })
      .then(function(response) {
        if (response.data.status == 401) {                                
          objeto.$router.push('/');
          alert("Error de sesion");                
        }
        console.log(response.data.mensaje);
        alert("Solicitud de licencia enviada.")
      })
      .catch(function(error) {
        objeto.output = error;
      });
    }
  },
};
</script>