<template>
  <v-container fluid>
    <Headerestudiantes />
    <v-col align="center">
      <v-col class="col-sm-10 col-lg-7">
        <v-card color="grey darken-3" dark style="padding:30px">
          <h1 align="center">Reserva de laboratorios adicionales</h1>

          <p
            align="justify"
          >Siga los pasos que se muestran a continuación para realizar la adición del laboratotio:</p>

          <p align="justify">1. Escoja el día que desea realizar el adicional:</p>

          <v-menu
            ref="menu1"
            v-model="menu1"
            :close-on-content-click="false"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }" >
              <v-text-field
                v-model="dateFormatted"
                :rules="[rules.required]"
                label="Fecha"
                persistent-hint
                prepend-icon="far fa-calendar-minus"
                v-bind="attrs"
                v-on="on" 
                readonly
              ></v-text-field>
            </template>
            <v-date-picker v-model="date" no-title @input="menu1 = false" 
            :min=min :max="maxDateCalendar()" :allowed-dates="allowedDates(6)"></v-date-picker>
          </v-menu>

          <p align="justify" >2. Escoja el bloque de horas:</p>

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
          >3. Selecciones un Laboratorio:</p>

          <v-autocomplete
            ref="Laboratorio"
            v-model="form.Laboratorio"
            :rules="[rules.required]"  
            :items="Laboratorios"
            label="Laboratorio"
            placeholder="Seleccionar..."
            required
          ></v-autocomplete>

          <p
            align="justify"
          >4. Selecciones un Banco:</p>

          <v-autocomplete
            ref="Bancos"
            v-model="form.Banco"
            :rules="[rules.required]"       
            :items="Bancos"
            label="Banco"
            placeholder="Seleccionar..."
            required
          ></v-autocomplete>

          <p
            align="justify"
          >5. Seleccione los elementos adicionales que desee agregar al laboratorio:</p>

          <v-row no-gutters>
            <v-col cols="12" sm="10">
              <v-text-field
                label="Ingrese un elemento adicional"
                hide-details="auto"
                v-model = "inputElemento"
                dense
                @keyup.enter="agregarElementoAdicional()"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="2" align-self="center" class="text-right">
              <v-btn rounded color="primary" dark
                @click="agregarElementoAdicional()"
              >Agregar</v-btn>
            </v-col>
          </v-row>      
          <p></p>
          <v-card shaped elevation="5" color="grey darken-3" dark style="padding:30px" v-if="form.Elemento.length != 0">
            <p align="justify" >Listado de los elementos adicionales: </p>
            <v-row no-gutters v-for= "(item,index) in form.Elemento" :key="index">
              <v-col cols="12" sm="10">
                <v-divider></v-divider>
                <ol>
                  <dt align="left">
                    {{index+1}}. {{item}}
                  </dt>
                </ol>
              </v-col>
              <v-col cols="12" sm="2">
                <v-divider></v-divider>
                  <v-icon 
                    dark 
                    small 
                    @click="form.Elemento = form.Elemento.filter((i) => i !== item)"
                  > 
                  fas fa-trash-alt</v-icon>
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <p></p>
            <v-card-actions class="justify-end">
              <v-btn rounded color="primary" dark @click="form.Elemento=[]">
                Limpiar todo     
                <v-icon dark small right> fas fa-trash-alt</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>          
          <p></p>
          <p align="justify">6. Seleccione la práctica:</p>

          <v-combobox v-model="form.Practica" :items="Practicas" label="Seleccionar..."
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
            <v-alert :value="vista" :type="vistaType">{{ output }}</v-alert>
          </v-col>
        </v-card>
      </v-col>
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
    HorasDis: [],
    Bancos: ["1","2","3","4","5","6"],
    Elementos: [
      "Osciloscopio",
      "Generador de Señales",
      "Fuente DC",
      "Multímetro",
      "Luxómetro",
      "Variac",
      "Caimanes"
    ],
    Practicas: [
      "Motores",
      "Com. Digitales",
      "Electrónica 1",
      "Electrónica 2",
      "Electrónica 3",
      "Circuitos 1"      
    ],
    errors:[],
    elementosBase: [],
    inputElemento: "",
    date: "",
    dateFormatted: "",
    todaydate: vm.formatDate(vm.conversionDate(new Date())),
    menu1: false,
    menu2: false,
    min: "",
    day: new Date().getDay(),
    hour: new Date().getHours(),
    output: "",
    output2: "",

    vista: false,
    vistaType: "success",

    Codigo: "",
    value: "",
    bandera: "1",
    form: {
      Hora: "",
      Laboratorio: "",
      Banco: "",
      Practica: "",
      Elemento: [],
      codigoLab:"",
      usuario: "",
    },
    rules:{
      required: value => !!value || "Este espacio es requerido.",
  } 
    
  }),
  mounted(){
  // this.$verificarLogin();
  },
  created(){
    // Se evalua si el dia actual es domingo. Si sí, se suma un día para que se tome la fecha del lunes. En caso contrario, se utiliza la fecha actual del sistema. Se le debe indicar las 00:00 para evitar qeu se corra el día debido a la diferencia de usa con el formato ISO.
    // También en el caso de que en el día actual sean más de las 8pm, se aumenta en +1 el dia. 
    let dateToday = new Date(this.parseDate(this.todaydate)+" 00:00");
    if (dateToday.getDay() === 0 || this.hour > 20){
      dateToday = dateToday.setDate(dateToday.getDate() + 1); 
    }
    this.dateFormatted = this.formatDate(this.conversionDate(new Date(dateToday)));
    this.date = this.conversionDate(new Date(dateToday))
    this.min = this.date;
  },
  computed: {
    computedDateFormatted(){
      return this.formatDate(this.date);
    }
  },
  watch: {
    date(val) {
      this.dateFormatted = this.formatDate(this.date);
    },
    dateFormatted(val){
      this.verificarHorasAdicional();     
    },
    hour(val){
      this.verificarHorasAdicional();
    }
  },
  methods: {
    allowedDates(n) {
      return val => ![n].includes(new Date(val).getDay());
    },
    conversionDate(date){
      let year = date.getFullYear().toString();
      let month = (date.getMonth()+1).toString();
      let day = date.getDate().toString();
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    formatDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${day}/${month}/${year}`;
    },
    parseDate(date) {
      // Esta funcion esta asociada a los v-text-input para modificar los v-calendar a partir de fechas ingresados por teclado.
      if (!date) return null
      const [day, month, year] = date.split('/')
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    maxDateCalendar(date){
      var date = new Date();
      date = date.setDate(date.getDate() + 7);
      date = this.conversionDate(new Date(date));
      return date;
    },
    verificarHorasAdicional(){
      var n = 0;
      let minutes = new Date().getMinutes();
      let dayOfWeek = new Date(this.parseDate(this.dateFormatted)+" 00:00").getDay();
      var horasAdicional = [];
      this.form.Hora = "";
      if(dayOfWeek!==6){
        horasAdicional = [6, 8, 10, 12, 14, 16, 18, 20];
      }else{
        horasAdicional = [6, 8, 10, 12, 14];
      }
      if (this.dateFormatted === this.todaydate){
        this.HorasDis = [];
        for(var key in horasAdicional){
          if(horasAdicional[key] > this.hour+1){   
              this.HorasDis[n] = horasAdicional[key];
              n++;
          }else{
            if(horasAdicional[key] === this.hour+1 && minutes<30){   
              this.HorasDis[n] = horasAdicional[key];
              n++;
            }
          }
        }
      }
      else {
        this.HorasDis = horasAdicional;
      }
    },
    agregarElementoAdicional(){
      // Valida que el elemento agregado en el input del adicional no sea un espacio en blanco o vacío. 
      if (this.inputElemento.length>0){
        if(this.inputElemento.replace(/ /g, "").length>0){
          this.form.Elemento.push(this.inputElemento);
        }
      }      
      this.inputElemento = [];
    },
    verBanco(form){
      let objeto = this;
      console.log(this.form.Elemento)
      console.log(this.form.Hora)
      console.log(this.HorasDis)
      this.axios
        .post(
          "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/consultabanco",
          {
            hora: this.form.Hora,
            fecha_adicional: this.dateFormatted,
            sala: this.form.Laboratorio,
            banco: this.form.Banco
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
      this.vista = false;
      this.errors=[]
      if (
        this.form.Hora &&
        this.form.Laboratorio &&
        this.form.Banco &&
        this.dateFormatted &&
        this.bandera
      ){
      
      // Desencriptar el código del usuario
      let objeto = this;      
      this.usuario=localStorage.usuario;
      objeto.token = localStorage.cdcb0830cc2dd220;
      
      var encrypted = objeto.$cookies.get("user_session");      
      var desen = objeto.$Crypto.AES.decrypt(encrypted, objeto.token);
      var codlab = desen.toString(objeto.$Crypto.enc.Utf8);
      objeto.codigoLab = objeto.$Crypto.AES.decrypt(objeto.$cookies.get("user_session"), objeto.token);
      objeto.codigoLab=objeto.codigoLab.toString(objeto.$Crypto.enc.Utf8);

      this.axios
        .post(
          "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/reserva",
          {
            hora: this.form.Hora,
            fecha_adicional: this.dateFormatted,
            codigo: objeto.codigoLab,
            usuario: this.usuario,
            sala: this.form.Laboratorio,
            banco: this.form.Banco,
            elemento: this.form.Elemento,
            practica: this.form.Practica
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          if (response.data.status == 1) {
            objeto.vistaType = "success";
            objeto.vista = true;
            objeto.output = response.data.mensaje;
          } else if (response.data.status == 2) {
            objeto.vistaType = "error";
            objeto.vista = true;
            objeto.output = response.data.mensaje;
          } else {
            objeto.vistaType = "error";
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
        if (!this.form.Laboratorio) this.errors.push("Laboratorio requerido.")
        if (!this.form.Banco) this.errors.push("Banco requerido.")
        if (!this.bandera) this.errors.push("Banco Ocupado.")
      }
      }
  }
};
</script>