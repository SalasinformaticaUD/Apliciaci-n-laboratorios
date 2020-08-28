<template>
    <v-container fluid="">
        <v-col>
            <v-row>
                <v-col align="center">
      <v-col class="col-sm-10 col-lg-7">
        <v-card color="grey darken-3" dark style="padding:30px">
          <h1 align="center">Solicitud de Reserva de clases adicionales (Profesores)</h1>

          <p
            align="justify"
          >Siga los pasos que se muestran a continuación para realizar la solicitud de la reserva de la clase adicional:</p>

           <p align="justify">1. Complete los datos de la materia:</p>

           <p align="justify">Nombre del profesor:</p>
           <v-textarea
           :rules="[rules.required, rules.string]"
           v-model = form.Usuario
            no-resize
            rows="1"
           /> 

           <p align="justify">Nombre de la práctica:</p>
           <v-textarea
           :rules="[rules.required, rules.string]"
           v-model = form.Usuario
            no-resize
            rows="1"
           /> 

           <p align="justify">Carrera:</p>
           <v-textarea
           :rules="[rules.required, rules.string]"
           v-model = form.Usuario
            no-resize
            rows="1"
           /> 

           <p align="justify">Justificación de la práctica:</p>
           <v-textarea
           :rules="[rules.required, rules.codigo]"
            v-model = form.Codigo
            no-resize
            rows="1"
           /> 
           
          <p align="justify">Listado de estudiantes:</p>
           <v-file-input v-model= form.image accept="image/*"></v-file-input>

          <p align="justify">2. Escoja el día que desea realizar la práctica:</p>

          <v-menu
            ref="menu1"
            v-model="menu1"
            :close-on-content-click="false"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
            v-on ="horasdisponibles(Horas,dateFormatted,hour,todaydate,HorasDis)"
          >
            <template v-slot:activator="{ on, attrs }" >
              <v-text-field
                v-model="dateFormatted"
                :rules="[rules.required]"
                label="Fecha"
                prepend-icon="far fa-calendar-minus"
                v-bind="attrs"
                v-on="on" 
              ></v-text-field>
            </template>
            <v-date-picker v-model="date" no-title @input="menu1 = false" 
            :min= min max="2020-09-05"
            ></v-date-picker>
          </v-menu>

          <p align="justify" >3. Escoja el bloque horario:</p>

          <v-autocomplete
            ref="Hora"
            v-model="form.Hora"
            :rules="[rules.required]"
            label="Horas"
            :items = "HorasDis"
            placeholder="Seleccionar..."
            required
          ></v-autocomplete>

          <p
            align="justify"
          >4. Seleccione los elementos adicionales que desee agregar al laboratorio:</p>

          <v-combobox v-model="form.Elemento" :items="Elementos" label="Seleccionar..." multiple
          ></v-combobox>

          <p class="red--text" v-if="errors.length">
            <b>Errore(s):</b>
            <ul>
              <li v-for="(err,index) in errors" :key="index">{{ err }}</li>
            </ul>
          </p>

          <div class="text-right">
            <v-btn rounded color="primary" dark
               v-on="verBanco(form)"
               @click="formSubmit(form)"
            >Siguiente</v-btn>
          </div>
          <v-col cols="12">
            <v-alert :value="vista" type="success">{{ output }}</v-alert>
          </v-col>
        </v-card>
      </v-col>
    </v-col>
            </v-row>
        </v-col>
    </v-container>
</template>

<script>
import Headerestudiantes from "@/components/Headerestudiantes.vue";
export default {
  components: {
    Headerestudiantes,
  },
  data: vm => ({
    Laboratorios: [
      "Electronica A",
      "Electronica B",
      "Electronica Basica",
      "Maquinas",
      "Comunicaciones",
      "Circuitos"
    ],
    Dias: ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"],
    Horas: [6, 8, 10, 12, 14, 16, 18, 20],
    HorasDis: [],
    Bancos: ["1","2","3","4","5","6"],
    Elementos: [
      "Osciloscopio",
      "Generador de Señales",
      "Fuente DC",
      "Multímetro",
      "Luxómetro",
      "Variac"
    ],
    errors:[],
    date: new Date().toISOString().substr(0, 10),
    dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
    todaydate: vm.formatDate(new Date().toISOString().substr(0, 10)),
    menu1: false,
    menu2: false,
    min: vm.formatMin(new Date().toISOString().substr(0, 10)),
    day: new Date().getDay(),
    hour: new Date().getHours(),
    output: "",
    output2: "",
    vista: false,
    valid: true,
    tipo: "success",
    Codigo: "",
    Usuario: "",
    value: "",
    bandera: "1",
    form: {
    Hora: "",
    Laboratorio: "",
    Banco: "",
    Elemento: []
    },
    rules:{
      required: value => !!value || "Este espacio es requerido.",
      string:  value => {const pattern = /[a-zA-Z]/g
            return pattern.test(value) || 'Ingrese un nombre.'},
      codigo: value => {const pattern =/\d.{7,}/
            return pattern.test(value) || 'Ingrese un código valido.'},
    
  } 
    
  }),
  mounted(){
  this.$verificarLogin();
  },
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    }
  },
  watch: {
    date(val) {
      this.dateFormatted = this.formatDate(this.date);
    }    
  },
  methods: {
    allowedDates: val => { weekdays: [5, 7] },
    formatDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${day}/${month}/${year}`;
    },
    formatMin(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${year}-${month}-${day}`;
    },
    horasdisponibles(Horas,dateFormatted,hour,todaydate,HorasDis){
    var a = 0
    if (dateFormatted == todaydate){
      for (var key in Horas){
        if (Horas[key] > hour){
          HorasDis[a] = Horas[key]
          a++
        }
          }
    }
    else {
      this.HorasDis = Horas
    }
    console.log(HorasDis)
    },
    verBanco(form){
      let objeto = this;
      this.axios
        .post(
          "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/consultabanco",
          {
            hora: this.form.Hora,
            fecha_adicional: this.dateFormatted,
            usuario: this.form.Usuario,
            codigo: this.form.codigo
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          if (response.data.status == 1) {
            objeto.output2 = response.data.mensaje;
              objeto.bandera = ""
          } else if (response.data.status == 2) {
            objeto.output2 = response.data.status;
            objeto.bandera = "1"
          } else {
            objeto.output2 = "Ha ocurrido un error";
            objeto.bandera = "1"
          }
        })
        .catch(function(error) {
          objeto.output2 = error;
        });
    },
    formSubmit(form) {
      this.verBanco(form)
      this.errors=[]
      if (
        this.form.Hora &&
        this.form.Usuario &&
        this.form.Codigo &&
        this.dateFormatted &&
        this.bandera
      ){
      let objeto = this;
      this.axios
        .post(
          "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/reserva",
          {
            hora: this.form.Hora,
            fecha_adicional: this.dateFormatted,
            codigo: this.form.Codigo,
            usuario: this.form.Usuario,
            sala: "Por Asignar",
            banco: "Por Asignar",
            elemento: this.form.image
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          if (response.data.status == 1) {
            objeto.vista = true;
            objeto.output = response.data.mensaje;
          } else if (response.data.status == 2) {
            objeto.vista = true;
            objeto.output = response.data.mensaje;
          } else {
            objeto.vista = true;
            objeto.output = "Ha ocurrido un error";
          }
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
     else {
        if (!this.form.Hora) this.errors.push("Hora requerida.")
        if (!this.dateFormatted) this.errors.push("Fecha requerida.")
        if (!this.form.Usuario) this.errors.push("Usuario requerido.")
        if (!this.form.Codigo) this.errors.push("Codigo requerido.")
        if (!this.bandera) this.errors.push("Banco Ocupado.")
      }
      }
  }
};
</script>