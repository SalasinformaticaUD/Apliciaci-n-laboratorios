<template>
  <v-container fluid>
    <Headerestudiantes/>

    <v-sheet tile class="mt-7">
      <v-row no-gutters class="text-h5 py-3" justify="center" align="center">
        Laboratorios de Ingeniería - Horarios Adicionales
      </v-row>
      <v-divider></v-divider>
      <v-row no-gutters align="center" class="py-2">
        <v-col cols="12" sm="5" lg="5" class="pr-sm-12 pl-sm-3 pl-lg-5 text-body-2">          
          1. Seleccione uno de los horarios disponibles para laboratorio adicional.
          <br>
          2. Verifique la disponibilidad de los bancos habilitados para reserva.
          <br>
          3. De click en "Solicitud de reserva" y complete la información.
          <br>
          4. La solicitud quedará en espera a la aprobación de un laboratorista.
        </v-col>
        <v-col cols="12" sm="3" v-if="$refs.calendarEstudiantes" class="ml-sm-n8">
          <v-row no-gutters>
            <v-col cols="12" sm="2" align-self="center" align="center">
              <v-tooltip bottom nudge-top="10">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn 
                    v-bind="attrs"
                    v-on="on"
                    icon 
                    large 
                    @click="changeWeek(0)"
                    :disabled="actualWeek == weekCalendar ? true : false"
                  >
                    <v-icon>fas fa-chevron-left</v-icon>
                  </v-btn>
                </template>
                <span>Semana anterior</span>
              </v-tooltip>         
            </v-col>      
            <v-col cols="12" sm="8" align="center" class="text-h6 mx-lg-n2">
              {{ formatTitle($refs.calendarEstudiantes.title) }} 
              <br>
              Semana {{weekCalendar}}
            </v-col>    
            <v-col cols="12" sm="2" align-self="center" align="center">
              <v-tooltip bottom nudge-top="10">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn 
                    v-bind="attrs"
                    v-on="on"
                    icon 
                    large 
                    @click="changeWeek(1)"
                    :disabled="actualWeek+1 == weekCalendar ? true : false"
                  >
                    <v-icon>fas fa-chevron-right</v-icon>
                  </v-btn>
                </template>
                <span>Semana siguiente</span>
              </v-tooltip>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="12" sm="1" align="center" class="ml-sm-5">
          <v-tooltip bottom nudge-top="5">
            <template v-slot:activator="{ on, attrs }">
              <v-btn 
                v-bind="attrs"
                v-on="on"
                @click="gotoWeekNow" 
                outlined 
                elevation="1"
              >
                Hoy
              </v-btn>
            </template>
            <span>Ir al día actual</span>
          </v-tooltip> 
        </v-col>
        <v-spacer></v-spacer>
        <v-col cols="12" sm="3" class="mt-sm-6 px-sm-5">
          <v-select                
            v-model="labSelect"
            :items="labSelectArray"
            label="Filtrar por laboratorio"
            outlined
            dense                
            append-icon="fas fa-filter"
          ></v-select>
        </v-col>
      </v-row>
    </v-sheet> 
    <v-sheet tile>
      <v-calendar
        ref="calendarEstudiantes"
        v-model="modelCalendar"
        type="week"
        :weekdays="weekdaysCalendar"
        :short-weekdays="false"
        :events = "events"
        color = "primary"
        interval-minutes = "120"
        first-time = "06:00"
        interval-count = "7"
        :interval-height = "70"
        :show-interval-label="showIntervalLabel"
        :interval-format="intervalFormat"
        @click:event ="clickShowEvent"
        class="botton"
      >
        <template v-slot:day-body="{ date }">
          <div
            class="v-current-time"
            :style="{ top: nowY, width: actualDate === date ? '100%' : '0%' }"
          > 
          </div>
          <div
            class="v-current-time2"
            :style="{ top: nowY, position: actualDate === date ? 'absolute': 'relative'}"
          >
          </div>
        </template>
      </v-calendar>

      <v-menu
        v-model="menuShowEvent"
        :close-on-content-click="false"
        :activator="elementShowEvent"
        offset-x
      >
        <v-card color="grey lighten-4" width="320px" flat>
          <v-toolbar :color="selectedEvent.color" dark>
            <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon large @click.prevent="menuShowEvent = false">
              <v-icon>fas fa-times</v-icon>
            </v-btn>
          </v-toolbar>
          <v-card-title class="my-n1">Información del laboratorio</v-card-title>    
          <v-card-text>
            <v-divider></v-divider>
            <v-row no-gutters class="mb-2 ml-2 mt-2">
              <v-col cols="12" sm="4" class="text-subtitle-2">
                Día: {{weekdays[selectedEvent.weekday-1]}}
              </v-col>
              <v-col cols="12" sm="6" offset="2" class="text-subtitle-2">
                Horario: {{selectedEvent.hour}}:00 - {{selectedEvent.hour+2}}:00
              </v-col>
            </v-row>
            <v-row no-gutters class="mb-1 ml-2 mt-3 text-subtitle-2" v-if="auxEstadoBancos.Disponibles.length>0">
              Bancos disponibles para reserva:
            </v-row>
            <v-row no-gutters class="mx-2">
              <v-col cols="12" sm="4" v-for="(item,index) in auxEstadoBancos.Disponibles" :key="index">
                <ul v-if="auxEstadoBancos.Ocupados[index] === false">
                  <li>Banco {{item}} </li>
                </ul>
                <ul v-else class="text-decoration-line-through">
                  <li>Banco {{item}} </li>
                </ul>
              </v-col>
            </v-row>              
            <v-divider class="mt-2"></v-divider>
          </v-card-text>            
          <v-card-actions>
            <v-row no-gutters v-if="auxEstadoBancos.Libres.length>0" justify="center" class="px-4 mb-3 mt-n2">
              <v-btn block :color="selectedEvent.color" dark @click="solicitudReserva">
                Solicitud de reserva
              </v-btn>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-menu>
    </v-sheet>

    <v-sheet  tile  min-height="50px">
    </v-sheet>
      
    <v-dialog v-model="menuFormulario" max-width="530px">
      <v-card color="grey lighten-4">
        <v-toolbar :color="selectedEvent.color" dark>
          <v-toolbar-title class="text-h6">Reserva de laboratorio adicional</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon large @click.prevent="menuFormulario = false">
            <v-icon>fas fa-times</v-icon>
          </v-btn>
        </v-toolbar>

        <v-stepper  tile non-linear v-model="step">
          <v-stepper-header class="mt-n3" flat>
            <v-stepper-step :complete="step > 1" step="1" :color="selectedEvent.color" editable               
              >
              Información  
              <hr>
              del adicional
            </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step step="2" :color="selectedEvent.color" editable>
              Elementos 
              <hr>
              Adicionales
            </v-stepper-step>
          </v-stepper-header>

          <v-stepper-items>
            <v-stepper-content step="1">
              <v-card height="330">
                <v-card-text>
                  <v-row class="mt-n4" no-gutters>
                    <v-col cols="12" sm="6" class="text-subtitle-1 pr-3">
                      1. Fecha del adicional
                      <v-text-field
                        :value="formReserva.fecha_adicional"
                        outlined
                        dense
                        disabled
                        class="text-subtitle-1 font-weight-medium ml-4 mt-1 mr-4"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" class="text-subtitle-1 pl-3">
                      2. Laboratorio del adicional
                      <v-text-field
                        :value="formReserva.sala"
                        outlined
                        dense
                        disabled
                        class="text-subtitle-1 font-weight-medium ml-4 mt-1 mr-4"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row class="mt-n3" no-gutters>
                    <v-col cols="12" sm="6" class="text-subtitle-1 pr-3">
                      3. Dia del adicional
                      <v-text-field
                        :value="weekdays[formReserva.diaSemana-1]"
                        outlined
                        dense
                        disabled
                        class="text-subtitle-1 font-weight-medium ml-4 mt-1 mr-4"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" class="text-subtitle-1 pl-3">
                      4. Franja Horaria
                      <v-text-field
                        :value="stringHorario"
                        outlined
                        dense
                        disabled
                        class="text-subtitle-1 font-weight-medium ml-4 mt-1 mr-4"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-form ref="form" v-model="validForm" lazy-validation>
                    <v-row class="mt-n3" no-gutters>
                      <v-col cols="12" sm="6" class="text-subtitle-1 pr-3">
                        5. Número de banco
                        <v-select              
                          ref="banco"  
                          v-model="formReserva.banco"
                          :items="auxEstadoBancos.Libres"
                          :label="formReserva.banco==null?'Seleccione...':''"
                          :rules="[rules.required]"
                          required
                          dense
                          outlined        
                          class="text-subtitle-1 ml-4 mt-1 mr-4"
                        ></v-select>
                      </v-col>
                      <v-col cols="12" sm="6" class="text-subtitle-1 pl-3">
                        6. Práctica relacionada
                        <v-text-field
                          ref="practica"
                          v-model="formReserva.practica"
                          :rules="[rules.required]"
                          placeholder="p. ej. Electrónica 1"
                          required
                          dense
                          outlined        
                          class="text-subtitle-1 ml-4 mt-1 mr-4"
                          @keyup.enter="step=2"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-form>
                </v-card-text>            
                <v-card-actions class="mx-6 mb-n2 mt-n3">
                  <v-row no-gutters>
                    <v-btn large block :color="selectedEvent.color" @click="step=2" dark>
                      Siguiente
                    </v-btn>
                  </v-row>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <v-stepper-content step="2">
              <v-card height="330" class="d-flex flex-column">
                <v-card-text class="grow">
                  <v-row class="mt-n4" no-gutters>
                    <p class="text-subtitle-1 ">
                      7. Ingrese los elementos adicionales (opcional).
                    </p>
                  </v-row>
                  <v-row no-gutters class="px-3">
                    <v-col cols="12" sm="9">
                      <v-text-field
                        label="Ingrese un elemento adicional"
                        hide-details="auto"
                        v-model = "inputElementoAdicional"
                        dense
                        @keyup.enter="agregarElementoAdicional()"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="2" align-self="center" class="pl-4">
                      <v-btn :color="selectedEvent.color" outlined elevation="1" tile medium class="px-2 py-1"
                        @click="agregarElementoAdicional()"
                      >Agregar</v-btn>
                    </v-col>
                  </v-row>      
                  <v-card elevation="4" class="mt-4 pa-2 mx-3 scroll"  v-if="formReserva.elemento.length != 0" max-height="160">
                    <v-card-text>
                  <v-row no-gutters v-for= "(item,index) in formReserva.elemento" :key="index">
                    <v-col cols="12" sm="10">
                      <v-divider></v-divider>
                      <ol>
                        <dt align="left">
                          {{index+1}}. {{item}}
                        </dt>
                      </ol>
                    </v-col>
                    <v-col cols="12" sm="2" align="center">
                      <v-divider></v-divider>
                      <v-icon small @click="formReserva.elemento.splice(index,1)"> 
                        fas fa-trash-alt
                      </v-icon>
                    </v-col>
                  </v-row>
                  <v-divider></v-divider>
                  </v-card-text>
                </v-card>          
                </v-card-text>                
                <v-card-actions class="mx-5 mb-n2">
                  <v-row no-gutters>
                    <v-btn large block :color="selectedEvent.color" :dark="validForm" :disabled="!validForm"
                    @click="sendReserva">
                      Enviar
                    </v-btn>
                  </v-row>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
          </v-stepper-items>
        </v-stepper>
      </v-card>
    </v-dialog>      
  </v-container>
</template>

<script>
import Headerestudiantes from "@/components/Headerestudiantes.vue";

export default {
  components: {
    Headerestudiantes,
  },
  data() {
    return {    
      // v-model del calendar
      modelCalendar: '',     

      // Variable que identifica cuando ya se ha renderizado el calendario
      readyCalendar: false,

      // Fecha actual (variable constante con formato año-mes-dia)
      actualDate: null,

      // Numero de semana ISO actual (variable constante que retorna desde el servidor en el status)
      actualWeek: null,
      
      // Numero de semana que se visualiza en la cabecera del v-calendar 
      weekCalendar: null,

      // Orden de los dias de la semana (Lunes - Domingo) en el v-calendar
      weekdaysCalendar: [1,2,3,4,5,6,0],

      // Array que permite relacionar el número del día de la semana con un string
      weekdays: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],

      // Información de los laboratorios  (se trae desde vuex ./store/index.js)
      labs:[],

      // v-model del v-select de laboratorio. Por defecto se inicializar en "Ver todos"
      labSelectArray: [],
      labSelect: "Ver todos",

      // auxEstadoBancos se utiliza para mostrar en la información del adicional el estado de los bancos
      auxEstadoBancos:{
        Disponibles: [],
        Ocupados: [],
        Libres: [],
      },      

      // En all events se tienen todos los adicionales de la base de datos. En events se relacionan los adicionales que se visualizan en el v-calendar (de acuerdo al v-select que filtra la informacion)
      allEvents:[],
      events: [],

      // En selectedEvent se almacena la información del evento seleccionado; menuShowEvent se relaciona con el v-menu que muestra la información del adicional; elementShowEvent corresponde al <div> sobre el cual se ejecuta el evento en el calendario para mostrar la información
      selectedEvent: {},
      menuShowEvent: false,
      elementShowEvent: null,

      // Se relaciona con el v-model del v-dialog para solicitar una reserva
      menuFormulario: false,
      
      // Variable para mostrar la franja horaria en el menu de reserva adicional
      stringHorario: "",

      // Variables que se toman en el formulario de reserva y que se envían al servidor
      formReserva:{
        start: "",                        // Hora del evento: año-mes-dia hora:min
        fecha_adicional: "",              // Fecha del adicional en formato dia/mes/año 
        sala: "",                         // Sala de laboratorio del adicional
        hora: "",                         // Hora de inicio de la franja horaria del adicional
        diaSemana: "",                    // Día de la semana del adicional
        banco: "",                        // Numero de banco del adicional
        practica: "",                     // Nombre de la practica del adicional
        elemento: [],                     // Elementos solicitados en el adicional
      },

      // Páginas del v-stepper en el proceso de solicitar un adicional
      step: 1,
      // Variable para la validacion del formulario
      validForm: true,
      // Reglas para los campos del formulario Numero de banco y Nombre de la practica
      rules:{
        required: value => !!value || "Este espacio es requerido.",
      },     
      // v-model del input para ingresar los elementos adicionales
      inputElementoAdicional: "",
    }
  },
  created(){
    this.labs = this.$store.getters.infoLabs;       // Trae la información de los laboratorios desde vuex

    // Se toman y convierten las fechas para los calendarios. Para el v-calendar en formato año-mes-dia; para el input y la base de datos en formato dia/mes/año
    this.actualDate = this.conversionDate(new Date());

    this.gotoWeekNow();       // Con la fecha actual, identifica el numero de la semana ISO

    // Con el vector de labs, se toma el campo 'name' para hacer el v-select de filtrado
    this.labSelectArray = this.labs.map(item => item.name);
    this.labSelectArray.push("Ver todos");        // Se agrega la opción "Ver todos"
  },
  mounted(){   
    this.getHorariosAdicionales();        // Trae todos los adicionales de la base de datos
    this.readyCalendar = true;            // Identifica que se ha renderizado el calendario
  },
  watch:{
    menuFormulario: function(val){
      // Identifica el momento en que se cierra el menu del formulario y reinicia las variables del form
      if(val==false){
        this.$refs.form.reset();
      }
    },
    labSelect: function(){
      // Esta función hace el filtro asociado al v-select de Laboratorio
      this.selectShowEvents();
    },
  },
  computed: {
    cal () {
      // Retorna el objeto $refs.calendarEstudiantes cuando el componente v-calendar se ha renderizado
      return this.readyCalendar ? this.$refs.calendarEstudiantes : null
    },
    nowY () {
      // Luego de renderizar el componente v-calendar, pregunta por la hora actual y retorna el valor para hacer la línea del day-body en el mismo
      return this.cal ? this.cal.timeToY(this.cal.times.now) + 'px' : '-10px'
    },
  },
  methods:{
    conversionDate(date){
      // Esta función toma una fecha dada la función Date() de JS y retorna una fecha en el formato año-mes-dia. Esto se realiza para evitar utilizar la función Date().toISOString ya que esta última no tiene en cuenta la zona horaria y en horas de la noche toma la fecha como la del dia siguiente. 
      let year = date.getFullYear().toString();
      let month = (date.getMonth()+1).toString();
      let day = date.getDate().toString();
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    showIntervalLabel(interval) {
      // Esta función permite visualizar el primer dato de tiempo (06:00) en el v-calendar
      return interval.minute === 0;
    },
    intervalFormat(interval) {
      // Esta función modifica el formato de visualización de las horas en el v-calendar a hh:mm
      return interval.time
    },
    formatTitle(title){
      // Funcion que pone la primera letra en mayús para el titulo del calendario
      return title.charAt(0).toUpperCase() + title.slice(1);
    },
    searchWeek(year,month,day){
      // Funcion que a partir de una fecha, identifica el número de la semana del año según ISO.
      var date = new Date(year,month,day);
      var nDay = (date.getDay() + 6) % 7;
      date.setDate(date.getDate() - nDay + 3);
      var n1stThursday = date.valueOf();
      date.setMonth(0, 1);
      if (date.getDay() !== 4) {
        date.setMonth(0, 1 + ((4 - date.getDay()) + 7) % 7);
      }
      return 1 + Math.ceil((n1stThursday - date) / 604800000);
    },
    changeWeek(val){
      // Funcion para los botones de cambiar la semana en el header del v-calendar 
      if(val==0){
        this.$refs.calendarEstudiantes.prev();
      }else{
        this.$refs.calendarEstudiantes.next();
      }
      // Se identifica el numero de la semana a la cual se cambia
      let date = this.modelCalendar.split('-');
      this.weekCalendar = this.searchWeek(date[0], date[1]-1, date[2]);
    },
    gotoWeekNow(){
      // Funcion que regresa el calendario a la semana actual. 
      this.modelCalendar = '';      // Se debe limpiar el model del v-calendar 
      let now = new Date();         // Se toma la fecha para buscar la semana actual
      this.weekCalendar = this.searchWeek(now.getFullYear(),now.getMonth(),now.getDate());
    },
    selectShowEvents(){
      // Se hace el filtro de los eventos de acuerdo al valor de labSelect
      if(this.labSelect !== "Ver todos"){
        this.events = this.allEvents.filter(item => item.name == this.labSelect);
      }else{
        this.events= this.allEvents;
      }
    },    
    clickShowEvent ({ nativeEvent, event }){  
      // Define una función open local que se ejecuta en caso de que menuShowEvent sea false.
      const open = () => {        
        // Se toma en selectedEvent la información del evento seleccionado
        let fecha = event.start.split(" ")[0].split("-");
        this.selectedEvent = {
          start: event.start,
          name: event.name,
          color: event.color,
          bancos: event.bancos,
          weekday: event.weekday,
          hour: event.hour,
          fecha: fecha[2] + "/" + fecha[1] + "/" + fecha[0],
        };
        this.elementShowEvent = nativeEvent.target;     // Se toma el <div> sobre el cual se dio click
        this.getEstadoBancos(this.selectedEvent);       // Se obtiene el estado de los bancos
        // Se hace la petición de la animación y se activa el v-menu
        requestAnimationFrame(() => requestAnimationFrame(() => this.menuShowEvent = true));
      }
      if(event.enable){
        if (this.menuShowEvent) {
         this.menuShowEvent = false;
          requestAnimationFrame(() => requestAnimationFrame(() => open()));
        } else {
          open();
        }
      }
      nativeEvent.stopPropagation();
    },
    getEstadoBancos(event){    
      // Recibe un objeto de evento y toma la información de los bancos según corresponda
      this.auxEstadoBancos = {
        Disponibles: [],
        Ocupados: [],
        Libres: [],
      };
      for(let i=0;i<event.bancos.length;i++){
        if(event.bancos[i]!=="No Disponible"){
          this.auxEstadoBancos.Disponibles.push(i+1);       // Bancos disponibles para reserva
          if(event.bancos[i]=="Pendiente" || event.bancos[i]=="Reservado"){
            this.auxEstadoBancos.Ocupados.push(true);       // Bancos de reserva ocupado
          }else{
            this.auxEstadoBancos.Libres.push(i+1);          // Bancos libres para reserva        
            this.auxEstadoBancos.Ocupados.push(false);      // Bancos de reserva libre
          }
        }
      }
    },
    solicitudReserva(){
      // Toma la información para llenar el formulario e información de interés para enviar al servidor
      this.formReserva = {
        start: this.selectedEvent.start,
        fecha_adicional: this.selectedEvent.fecha,
        sala: this.selectedEvent.name,
        hora: this.selectedEvent.hour,
        diaSemana: this.selectedEvent.weekday,
        banco: null,
        practica: null,
        elemento: [],
      }
      // Se crea el string del horario a mostrar en la franja horaria
      let horaAdicional = this.selectedEvent.hour;
      this.stringHorario = horaAdicional.toString() + ":00 - " + (horaAdicional+2).toString() + ":00";
      this.step = 1;                          // Para empezar el formulario en el stepper = 1
      this.menuShowEvent = false;             // Cierra el v-menu de informacion
      this.menuFormulario = true;             // Abre el v-dialog del formulario
    },
    agregarElementoAdicional(){
      // Valida que el elemento agregado en el input del adicional no sea un espacio en blanco o vacío
      if (this.inputElementoAdicional.length>0){
        if(this.inputElementoAdicional.replace(/ /g, "").length>0){
          // Lo agrega al vector Elemento del formulario
          this.formReserva.elemento.push(this.inputElementoAdicional);
        }
      }            
      this.inputElementoAdicional = "";       // Se vacía el input para poder agregar otro elemento
    },
    sendReserva(){
      // Se valida si los campos de banco y practica han sido llenados
      if(this.$refs.form.validate()){
        this.sendReservaServer();     // Si estan completos, hace la peticion al servidor
      }else{
        this.step = 1;                // Si no están llenos, regresa a la primera pagina del v-stepper
      }
    },
    sendReservaServer(){
      // Se desencripta y trae la información del usuario
      let cod_encrypted = this.$cookies.get("user_session");      
      let codigoLab = this.$Crypto.AES.decrypt(cod_encrypted, localStorage.cdcb0830cc2dd220);      
      let objeto = this;      
      this.axios.post("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/reserva",
        {
          hora: this.formReserva.hora,
          fecha_adicional: this.formReserva.fecha_adicional,
          codigo: codigoLab.toString(this.$Crypto.enc.Utf8),
          usuario: localStorage.usuario,
          sala: this.formReserva.sala,
          banco: this.formReserva.banco,
          elemento: this.formReserva.elemento,
          practica: this.formReserva.practica,
          diaSemana: this.weekdays[this.formReserva.diaSemana-1],
          date_user: this.actualDate,
          hour_user: new Date().getHours(),
          minutes_user: new Date().getMinutes()
        },
        {
          headers: {
            "Content-Type": "application/json"
          }
        }
      )
      .then(function(response){        
        if(response.data.status == 1){
          objeto.actualizarDatos();          
          alert(response.data.mensaje)
          objeto.menuFormulario = false;
        }else if(response.data.status == 3){            
          alert(response.data.mensaje);
          objeto.actualizarDatos();   
          objeto.formReserva.banco = null;
          objeto.step = 1;

        }else{
          alert(response.data.mensaje)          
          objeto.getHorariosAdicionales();
          objeto.menuFormulario = false;
        }
      })
      .catch(function(error) {
        objeto.output = error;
      });
    },
    actualizarDatos(){
      // En caso de haber agregado el adicional, para no hacer otra petición a la base de datos y traer la información actualizada, se actualizan las variables de los bancos para ese adicional seleccionado.
      this.selectedEvent.bancos[this.formReserva.banco - 1] = "Pendiente";      

      this.allEvents.filter(item => item.name == this.formReserva.sala && item.start == this.formReserva.start ? item.bancos == this.selectedEvent.bancos : item.bancos = item.bancos);

      this.getEstadoBancos(this.selectedEvent);
    },
    getHorariosAdicionales(){
      // Trae del servidor, los adicionales para la semana actual y hasta ocho días después de la fecha actual
      let objeto = this;
      this.axios.get("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/getHorariosAdicionalesEstudiantes",
        {
          headers: {
            "Content-Type": "application/json"
          }
        })
      .then(function(response) {  
        if (response.data.data.length > 0){             // Pregunta si encontro eventos adicionales
          objeto.actualWeek = response.data.status;     // Actualiza la información de semana actual
          objeto.enableEvents(response.data.data);      // Manda los eventos a la funcion enableEvents
          objeto.selectShowEvents();                    // De acuerdo al estado del v-select, filtra los datos
        }else{
          objeto.events = [];                           // Si no hay eventos, inicializa vacío
        }
      })
      .catch(function(error) {
        objeto.output = error;
      });
    },
    enableEvents(dataEvents){
      // Funcion que identifica si el adicional ya no esta disponible. Se verificar hasta 15 minutos luego de la hora de inicio del adicional, se le pone un color más claro y se modifica un enable.
      let dateNow = this.conversionDate(new Date());
      let hourNow = new Date().getHours();
      let minutesNow = new Date().getMinutes();

      for (let i=0; i < dataEvents.length; i++){                 // Recorre todos los eventos
        let dateAdicional = dataEvents[i].start.split(" ")[0];   // Toma la fecha del adicional
        let condition1 = (dateNow < dateAdicional);              // Compara la fecha del adicional con la actual
        let condition2 = (dateNow == dateAdicional &&  hourNow*60+minutesNow < dataEvents[i].hour*60+15);

        // Filtra la información por laboratorios (para tomar los colores)
        let infoSala = this.labs.find(item => item.name == dataEvents[i].name); 

        if(condition1 || condition2){
          dataEvents[i].color = infoSala.color;
          dataEvents[i].enable = true;
        }else{
          dataEvents[i].color = infoSala.colorLight;          
          dataEvents[i].enable = false;
        }
      }
      this.allEvents = dataEvents;    // Actualiza el vector de eventos 
    },
  },
};
</script>

<style scoped>
  .v-current-time {    
    height: 3px;
    background-color: #ea4335;
    position: absolute;
    right: 0px;
    left: -1px;
    pointer-events: none;
  }
  .v-current-time2 {
    content: '';
    background-color: #ea4335;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    margin-top: -5px;
    margin-left: -6.5px;
  }
  .botton >>> button{
    font-size: 0.96rem;
  }
</style>