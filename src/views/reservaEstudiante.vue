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
            :min=minCalendar :max="maxDateCalendar()" :allowed-dates="allowedDates(6)"></v-date-picker>
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
                    @click="form.Elemento.splice(index,1)"
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
          
          <v-combobox v-if="showInputPractica==false" v-model="practicaSelect" :items="Practicas" label="Seleccionar..."
          ></v-combobox>
          <v-row no-gutters v-if="showInputPractica" align="center">
            <v-col cols="12" sm="2">
              <v-combobox v-model="practicaSelect" :items="Practicas" label="Seleccionar..."
              ></v-combobox>
            </v-col>
            <v-col cols="12" sm="10" class="pl-5 mb-1">
              <v-text-field
                label="Ingrese el nombre de la práctica"
                hide-details="auto"
                v-model = "inputPractica"
                dense
              ></v-text-field>
            </v-col>
          </v-row>

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
    Dias: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"],
    diaSemana: "",
    HorasDis: [],
    Bancos: ["1","2","3","4","5","6"],
    errors:[],

    inputElemento: "",

    date: "",                                                   // Fecha para el v-model del calendar
    dateFormatted: "",                                          // Fecha para el v-model del v-text
    todaydate: vm.formatDate(vm.conversionDate(new Date())),    // Fecha actual en formato dia/mes/año
    menu1: false,                                               // Menu del v-calendar   
    minCalendar: "",                                            // Fecha mínima permitida en el v-calendar
    day: new Date().getDay(),                                   // Día actual
    hour: new Date().getHours(),                                // Hora actual


    output: "",                                                 // Respuesta de la peticion a reserva     
    output2: "",                                                // Respuesta de la petición a consultabanco
    vista: false,                                               // Validacion de la vista output
    vistaType: "success",                                       // Formatos de la vista output 
    bandera: "1",                                               // Para verificar si el banco esta ocupado

    value: "",

    Practicas: [
      "Motores",
      "Com. Digitales",
      "Electrónica 1",
      "Electrónica 2",
      "Electrónica 3",
      "Circuitos 1",
      "Proyecto de Grado",
      "Otro"  
    ],
    practicaSelect: "",                                          
    showInputPractica: "",
    inputPractica: "",

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
    // Se evalua si el dia actual es domingo. Si sí, se suma un día para que se tome la fecha del lunes. En caso contrario, se utiliza la fecha actual del sistema. Se le debe indicar las 00:00 para evitar que se corra el día debido a la diferencia horaria que utilizada con el formato ISO.
    // También en el caso de que en el día actual sean más de las 6pm, se aumenta en +1 el dia. 
    let dateToday = new Date(this.parseDate(this.todaydate)+" 00:00");
    if (dateToday.getDay() === 0 || 18 <= this.hour){
      dateToday = dateToday.setDate(dateToday.getDate() + 1); 
    }
    this.dateFormatted = this.formatDate(this.conversionDate(new Date(dateToday)));
    this.date = this.conversionDate(new Date(dateToday))
    this.minCalendar = this.date;
  },
  watch: {
    date(val) {
      // Watcher de la variable date (v-model del calendar) para detectar el cambio de día en la fecha y modificar también en el v-text del formulario. 
      this.dateFormatted = this.formatDate(this.date);
    },
    dateFormatted(val){
      // Watcher de la variable dateFormatted (v-model del v-text del calendar) para detectar el cambio de fecha y automáticamente validar las horas disponibles de laboratorio
      // Por otro lado se identifica el día de la semana
      this.verificarHorasAdicional();     
    },
    hour(val){
      // Watcher de la variable hour (hora actual) para detectar el cambio de hora y automáticamente validar las horas disponibles en el laboratorio
      this.verificarHorasAdicional();
    },
    practicaSelect(val){    
      // Watcher para el v-model del seleccionador de la práctica. En caso de seleccionar la opción "Otro" se debe mostrar un input para ingresar una opción de texto abierta. Esto se realiza habilitando la variable showInputPractica. 
      if(this.practicaSelect==="Otro"){
        this.showInputPractica = true;
      }else{
        this.showInputPractica = false;
      }   
    }
  },
  methods: {
    allowedDates(n) {
      // Esta función recibe un número entero n para restringir la selección dle día domingo en el v-calendar
      return val => ![n].includes(new Date(val).getDay());
    },
    conversionDate(date){
      // Esta función toma una fecha dada la función Date() de JS y retorna una fecha en el formato año-mes-dia. Esto se realiza para evitar utilizar la función Date().toISOString ya que esta última no tiene en cuenta la zona horaria y en horas de la noche toma la fecha como la del dia siguiente. 
      let year = date.getFullYear().toString();
      let month = (date.getMonth()+1).toString();
      let day = date.getDate().toString();
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    formatDate(date) {
      // Esta función toma una fecha en el formato año-mes-dia (formato v-calendar) y la convierte al formato dia/mes/año (formato utilizado en el proyecto)
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${day}/${month}/${year}`;
    },
    parseDate(date) {
      // Esta funcion toma una fecha en el formato dia/mes/año (formato utilizado en el proyecto) y la convierte al formato año-mes-dia (formato v-calendar)
      if (!date) return null
      const [day, month, year] = date.split('/')
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    maxDateCalendar(){
      // Esta función limita la selección máxima de días en el calendario. A la fecha actual se le suman 7 días y se retorna la fecha en formato año-mes-dia (formato v-calendar).
      var date = new Date();
      date = date.setDate(date.getDate() + 7);
      date = this.conversionDate(new Date(date));
      return date;
    },
    verificarHorasAdicional(){
      // Esta función toma el día de la semana actual e identifica si es o no sabado para hacer la asignación de horasAdicional. Luego, dependiendo si es el mismo día o no hace la asignación de las horas disponibles del adicional teniendo en cuenta que solo se puede seleccionar una franja horaria hasta 30 minutos antes de la hora. 
      var n = 0;
      let minutes = new Date().getMinutes();
      let dayOfWeek = new Date(this.parseDate(this.dateFormatted)+" 00:00").getDay();
      var horasAdicional = [];
      this.form.Hora = "";
      if(dayOfWeek!==6){
        horasAdicional = [6, 8, 10, 12, 14, 16, 18];
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
      // Se toma el día de la semana en la que se reserva el adicional
      this.diaSemana = this.Dias[dayOfWeek-1];
    },
    agregarElementoAdicional(){
      // Valida que el elemento agregado en el input del adicional no sea un espacio en blanco o vacío. Luego, lo agrega al vector Elemento del formulario. Finalmente vacía el input para poder agregar otro elemento
      if (this.inputElemento.length>0){
        if(this.inputElemento.replace(/ /g, "").length>0){
          this.form.Elemento.push(this.inputElemento);
        }
      }      
      this.inputElemento = [];
    },
    verBanco(form){
      // Esta función se encarga de validar que el banco no este ocupado por otro adicional. Se utiliza una bandera en '1' para indicar si se encuentra ya reservado o ha ocurrido un error. 
      let objeto = this;
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
      // Se valida si el nombre de la practica ha sido ingresada por el input (opcion otro) o es una de las seleccionadas del vector Practicas.  
      // Se valida que ningún campo se encuentre vacío y que la bandera sea diferente a '1' para indicar que el banco se encuentra disponible
      this.verBanco(form)
      this.vista = false;
      this.errors=[];
      if(this.showInputPractica==true){
        this.form.Practica = this.inputPractica;
      }else{
        this.form.Practica = this.practicaSelect;
      }
      if(
        this.form.Hora &&
        this.form.Laboratorio &&
        this.form.Banco &&
        this.dateFormatted &&
        this.form.Practica &&
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
              practica: this.form.Practica,
              diaSemana: this.diaSemana
            },
            {
              headers: {
                "Content-Type": "application/json"
              }
            }
          )
          .then(function(response) {
            if (response.data.status == 1) {
              // Si el laboratorio fue registrado correctamente
              objeto.vistaType = "success";
              objeto.vista = true;
              objeto.output = response.data.mensaje;
            } else if (response.data.status == 2) {
              // Si el usuario ya cuenta con más de tres adicionales pendientes o si el usuario ya ha solicitado un adicional para la misma franja horaria. 
              objeto.vistaType = "error";
              objeto.vista = true;
              objeto.output = response.data.mensaje;
            } else {
              // Error con el servidor
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
          if (!this.form.Practica) this.errors.push("Práctica requerida.")
          if (!this.bandera) this.errors.push("Banco Ocupado.")
      } 
    }
  } 
};
</script>