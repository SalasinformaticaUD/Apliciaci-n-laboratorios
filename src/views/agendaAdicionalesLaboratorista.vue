<template>
  <v-container fluid>
    <HeaderLaboratorista />

    <v-sheet  tile  min-height="110px" class="d-flex mt-7">
      <v-row no-gutters align="center">
        <v-col cols="12" sm="4" lg="3" class="mr-sm-n8 pl-lg-8 mr-lg-n15">          
          <v-row class="mt-4 pl-6" no-gutters>
            <p class="text-h6 font-weight-medium"> Laboratorios de Ingeniería</p>
          </v-row>
          <v-row class="mt-n5 pl-6" no-gutters>
            <p class="text-h6 font-weight-medium"> Horarios Adicionales </p>
          </v-row>
        </v-col>
        <v-col cols="12" sm="3" lg="3" offset-lg="2" v-if="$refs.calendar">
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
                  >
                    <v-icon>fas fa-chevron-left</v-icon>
                  </v-btn>
                </template>
                <span>Semana anterior</span>
              </v-tooltip>         
            </v-col>      
            <v-col cols="12" sm="8" align="center" class="text-h6 mx-lg-n2">
              {{ formatTitle($refs.calendar.title) }} 
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
                @click="actualWeek" 
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
        <v-col cols="12" sm="4" lg="3" class="mt-sm-6 px-sm-10">
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
        ref="calendar"
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
        @click:time ="clickAddEvent" 
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
        :activator="selectedElement"
        offset-x
      >
        <v-card color="grey lighten-4" width="320px" flat>
          <v-toolbar :color="selectedEventShow.color" dark>
            <v-toolbar-title v-html="selectedEventShow.name"></v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon @click.prevent="menuShowEventEdit">
              <v-icon>fas fa-pencil-alt</v-icon>
            </v-btn>
            <v-btn icon @click.prevent="deleteHorarioAdicional">
              <v-icon>fas fa-trash-alt</v-icon>
            </v-btn>
            <v-btn icon large @click.prevent="menuShowEvent = false">
              <v-icon>fas fa-times</v-icon>
            </v-btn>
          </v-toolbar>
          <v-card-title class="my-n1">Información del laboratorio</v-card-title>    
          <v-card-text>
            <v-divider></v-divider>
            <v-row no-gutters class="mb-2 ml-2 mt-2">
              <v-col cols="12" sm="4" class="text-subtitle-2">
                Día: {{weekdays[selectedEventShow.weekday-1]}}
              </v-col>
              <v-col cols="12" sm="6" offset="2" class="text-subtitle-2">
                Horario: {{selectedEventShow.hour}}:00 - {{selectedEventShow.hour+2}}:00
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
            <v-row no-gutters class="mb-1 ml-2 mt-3 text-subtitle-2" v-if="auxEstadoBancos.Pendientes.length>0">
              Bancos con reserva pendiente:
            </v-row>
            <v-row no-gutters class="mx-2">                
              <v-col cols="12" sm="4" v-for="(item,index) in auxEstadoBancos.Pendientes" :key="index">
                <ul>
                  <li>
                    <router-link :to="{
                      name: 'consultareservalabstemp'}">
                      <span @click="sendConsultaPendiente(item)">
                      Banco {{item}}
                      </span>
                    </router-link>
                  </li>
                </ul>
              </v-col>
            </v-row>
            <v-row no-gutters class="mb-1 ml-2 mt-3 text-subtitle-2" v-if="auxEstadoBancos.Reservados.length>0">
              Bancos con reserva aprobada:
            </v-row>
            <v-row no-gutters class="mx-2">                
              <v-col cols="12" sm="4" v-for="(item,index) in auxEstadoBancos.Reservados" :key="index">
                <ul>
                  <li>Banco {{item}} </li>
                </ul>
              </v-col>
            </v-row>
            <v-divider class="mt-3"></v-divider>
          </v-card-text>            
        </v-card>
      </v-menu>
    </v-sheet>

    <v-sheet  tile  min-height="50px">
    </v-sheet>

    <v-dialog v-model="menuCreatedEvent" max-width="420px">
      <v-card color="grey lighten-4">
        <v-toolbar
          :color="createdEvent.color ? createdEvent.color : 'blue-grey darken-2'"
          dark  
          dense
        >
          <v-toolbar-title class="font-weight-bold" v-html="createdEvent.name ? 'Laboratorio: ' + createdEvent.name : 'Laboratorio'"></v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon large @click="menuCreatedEvent=false">
            <v-icon>fas fa-times</v-icon>
          </v-btn>
        </v-toolbar>
        <v-card-title class="mt-n2">Información del adicional</v-card-title>
        <v-card-text>
          <v-row no-gutters class="text-body-2 font-weight-medium pr-3">
            1. Seleccione un laboratorio
          </v-row>
          <v-row no-gutters>
            <v-select
              v-model="stringNameLab"
              :items="labs"
              label="Seleccione un laboratorio"
              solo
              dense
              item-text="name"
              class="mx-3 mt-1 mb-n2 text-body-1 font-weight-normal"
              v-if="stringNameLabEnable"
            ></v-select>
            <v-text-field v-else dense disabled solo class="mt-1 mx-3 mb-n2 text-body-1 font-weight-medium" v-model="stringNameLab">
            </v-text-field>
          </v-row>
          <v-row no-gutters class="text-body-2 font-weight-medium pr-3">
            2. Horario del adicional
          </v-row>
          <v-row no-gutters>
            <v-text-field dense disabled solo class="mt-2 px-3 mb-n1 text-body-1 font-weight-medium" v-model="stringHorario">
            </v-text-field>
          </v-row>
          <v-row no-gutters class="text-body-2 font-weight-medium">
            3. Seleccione los bancos que desea habilitar
          </v-row>
          <v-row no-gutters class="ml-4 mt-2">
            <v-col cols="12" sm="4" class="my-n4" v-for="(item,index) in createdEvent.bancos" :key="index">
              <v-checkbox
                v-model="createdEvent.bancos[index]"
                :label="`Banco ${index+1}`"
                :color="createdEvent.color"
              >
              </v-checkbox>
            </v-col>
          </v-row>
          <v-row no-gutters v-if="createdEvent.name">
            <v-col cols="12" sm="7" class="my-n4 ml-4">
              <v-checkbox
                v-model="selectAllBancos"
                :label="`Seleccionar todos`"
                :color="createdEvent.color"
                @click="createdEvent.bancos.fill(selectAllBancos)"
              >
              </v-checkbox>
            </v-col>
          </v-row>
          <v-row no-gutters justify="center" class="text--secondary" v-else>
            Favor seleccione un laboratorio.
          </v-row>
          <v-row no-gutters class="text-body-2 font-weight-medium pr-3 mt-3" v-if="createdEvent.name">
            4. ¿Desea repetir esta configuración semanalmente?
          </v-row>
          <v-row no-gutters v-if="createdEvent.name">
            <v-col cols="12" sm="2" offset="1">
              <v-switch
                v-model="createdEvent.repeat"
                :label="createdEvent.repeat ? 'Si' : 'No' "
                :color="createdEvent.color"                
              ></v-switch>
            </v-col>
            <v-col cols="12" sm="6" offset="2">
              <v-menu
                v-model="menuCalendarPicker"
                :close-on-content-click="false"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="290px"
              >
              <template v-slot:activator="{ on, attrs }" >                                  
                <v-text-field
                  v-model="modelCalendarInput"
                  class="mt-3"
                  label="Repetir hasta la fecha:"                  
                  prepend-icon="far fa-calendar-minus"
                  v-bind="attrs"
                  v-on="on" 
                  readonly
                  outlined
                  dense
                  :disabled="!createdEvent.repeat"
                ></v-text-field>
              </template>
                <v-date-picker 
                  v-model="modelCalendarPicker" 
                  no-title 
                  @input="menuCalendarPicker = false" 
                  :min=minCalendarPicker
                  first-day-of-week="1"
                >
                </v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-row no-gutters class="justify-center mt-n6 mb-2">
            <v-col cols="12" sm="10">
              <v-btn           
                medium        
                block 
                :dark="createdEvent.name==null ? false:true"
                :disabled="createdEvent.name==null ? true:false"
                :color="createdEvent.color"
                @click="verificarBancosSeleccionados"
              >
                Guardar los cambios
              </v-btn>
            </v-col>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>      

  </v-container>
</template>

<script>
import HeaderLaboratorista from "@/components/HeaderLaboratorista.vue";

export default {
  components: {
    HeaderLaboratorista
  },
  data() {
    return {    
      // v-model del calendar
      modelCalendar: '',     

      // Variable que identifica cuando ya se ha renderizado el calendario
      readyCalendar: false,

      // Fecha actual (variable fija)
      actualDate: null,
      
      // No. de semana del calendar 
      weekCalendar: null,

      // Orden de los dias de la semana (Lunes - Domingo) en el v-calendar
      weekdaysCalendar: [1,2,3,4,5,6,0],
      
      // Vector para identificar los días de la semana según el número
      weekdays: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],

      // Información de los laboratorios  (se trae de vuex ./store/index.js)
      labs:[],

      // v-model del v-select de laboratorio. Por defecto se inicializar en Ver todos
      labSelectArray: [],
      labSelect: "Ver todos",

      // Este objeto se utiliza para mostrar la información de los bancos en cada menu de informacion
      auxEstadoBancos:{
        Disponibles: [],
        Ocupados: [],
        Pendientes: [],
        Reservados: [],
      },

      // Variable para seleccionar todos los bancos del laboratorio en los checkbox
      selectAllBancos: false,
    
      // En all events se tienen todos los adicionales de la base de datos. En events se relacionan los adicionales que se visualizan en el v-calendar en caso de utilizar el filtro del laboratorio
      allEvents:[],
      events: [],      

      // En selectedEventShow se almacena la informacion del evento seleccionado para ver informacion
      selectedEventShow: {
        name: "",
        color: "",
        bancos: "",
        weekday: "",
        hour: "",
        repeat: "",
      },

      // En createdEvent se almacena la información del evento a crear. 
      createdEvent: {
        name: "",
        color: "",
        bancos: "",
        weekday: "",
        hour: "",
        repeat: "",
        dateClick: "",
      },

      // elemento <div> seleccionado al dar click para ver información del adicional
      selectedElement: null,
      // variable relacionada con el menu que muestra la informacion del adicional
      menuShowEvent: false,

      // Variable que controla el v-dialog que permite agregar un nuevo adicional
      menuCreatedEvent: false,
      // string que indica el nombre del laboratorio seleccionado en el menu de crear adicional
      stringNameLab: "",
      stringNameLabEnable: false,
      // string que indica la franja horaria en el menu de crear adicional
      stringHorario: "",

      // Bandera para identificar si el menu de edicion del adicional se esta creando un nuevo o se esta editando uno ya existente
      flagEdicion: false,

      // variables relacionadas al calendario para seleccionar la fecha maxima de repeticion del adicional
      modelCalendarInput: "",
      modelCalendarPicker: "",
      minCalendarPicker: "",
      menuCalendarPicker: false,
    }
  },
  created(){
    // Se toman y convierten las fechas para los calendarios. Para el v-calendar en formato año-mes-dia; para el input y la base de datos en formato dia/mes/año
    this.actualDate = this.conversionDate(new Date());
  },

  mounted(){ 
    // Trae la información de los laboratorios desde vuex
    this.labs = this.$store.getters.infoLabs;

    // De acuerdo al vectos de labs, se toma el campo 'name' para hacer el v-select de filtrado. También se agrega la opción de "Ver todos".
    this.labSelectArray = this.labs.map(item => item.name);
    this.labSelectArray.push("Ver todos");

    // Con la fecha actual, se identifica el número de la semana
    this.actualWeek();

    // Trae todos los adicionales de la base de datos
    this.getHorariosAdicionales();
    
    // Identifica que se ha renderizado el calendario
    this.readyCalendar = true;
  },
  watch:{
    'createdEvent.bancos': function(){
      // Se hace un filtro para determinar si todos los bancos han sido seleccionados. En ese caso se habilita automáticamente la opción selectAllBancos.
      if(this.createdEvent.bancos !== []){
        let bancosDisponibles = this.createdEvent.bancos.filter(item => item===true).length;
        if(bancosDisponibles == this.createdEvent.bancos.length){
          this.selectAllBancos = true;
        }else{
          this.selectAllBancos = false;
        }
      }
    },
    stringNameLab: function(val){
      // Se hace un filtrado con el laboratorio seleccionado en los menús para tomar el nombre y el color.
      // Se identifica con flagEdicion si se debe crear un vector de bancos nuevo (adicion de evento) o si se deben dejar los valores que ya existen (en el caso de editar un adicional).
      if (val!==""){
        let filterInfoLab = this.labs.find(item => item.name === val);
        this.createdEvent.name = filterInfoLab.name;
        this.createdEvent.color = filterInfoLab.color;
        if (this.flagEdicion === false){          
          this.createdEvent.bancos = new Array(filterInfoLab.bancos).fill(false);
        }
      }
    },
    labSelect: function(){
      // Esta función hace el filtro asociado al v-select de Laboratorio
      this.selectShowEvents();
    },
    menuCreatedEvent: function(val){
      // watcher para identificar el cierre del menu de crear un evento para resetear algunas variables
      if(val===false){
        this.stringNameLabEnable = false;
        this.flagEdicion = false;
        this.stringNameLab = "";
        this.stringHorario = "";
      }
    },
    modelCalendarPicker: function(val) {
      // v-model del calendarPicker para detectar el cambio en la fecha y modificar también en el v-text
      this.modelCalendarInput = this.formatDate(val);
    },
  },
  computed: {
    cal () {
      return this.readyCalendar ? this.$refs.calendar : null
    },
    nowY () {
      return this.cal ? this.cal.timeToY(this.cal.times.now) + 'px' : '-10px'
    },
  },
  methods:{
    sendConsultaPendiente(banco){
      console.log("Metodo en agenda adicional");
      console.log(this.selectedEventShow);
      let date = this.selectedEventShow.date.split(" ")[0];
      this.$store.state.date = this.formatDate(date);
      this.$store.state.hour = this.selectedEventShow.hour;
      this.$store.state.banco = banco;
      console.log("Fecha que se envía al store: " + date);
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
      // Funcion para los botones de cambiar la semana. Además se identifica el nùmero de la semana a la cual se cambia
      if(val==0){
        this.$refs.calendar.prev();
      }else{
        this.$refs.calendar.next();
      }
      let date = this.modelCalendar.split('-');
      this.weekCalendar = this.searchWeek(date[0], date[1]-1, date[2]);
    },
    actualWeek(){
      // Funcion del boton 'Hoy' que regresa el calendario a la semana actual. Se limpia el model del calendar y ademàs se vuelve a identificar la semana del año actual
      let now = new Date();
      this.modelCalendar = '';
      this.weekCalendar = this.searchWeek(now.getFullYear(),now.getMonth(),now.getDate());
    },
    conversionDate(date){
      // Esta función toma una fecha dada la función Date() de JS y retorna una fecha en el formato año-mes-dia. Esto se realiza para evitar utilizar la función Date().toISOString ya que esta última no tiene en cuenta la zona horaria y en horas de la noche toma la fecha como la del dia siguiente. 
      let year = date.getFullYear().toString();
      let month = (date.getMonth()+1).toString();
      let day = date.getDate().toString();
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    formatDate(date) {
      // Convierte del formato año-mes-dia al formato dia/mes/año
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${day}/${month}/${year}`;
    },
    clickAddEvent(data){
      // En esta función se toma el evento de click:time en algún espacio libre del calendario. 
      //  - Se verifica si el día es diferente a domingo (!==0) 
      //  - Se verifica que el menú de mostrar la info del adicional sea falso.
      // En la variable "data" esta toda la información del espacio libre del calendario.
          
      if (data.weekday!==0 && this.menuShowEvent==false){
        // Se revisa si el espacio pulsado es hora par o impar y se determina la hora de inicio del adicional

        let startHour = null;        

        if(data.hour%2 == 0){        
          startHour = data.hour;        // Si la hora es par se toma la misma.
        }else{
          startHour = data.hour - 1;    // La hora es impar se debe restar una hora.
        }    

        // Se crea un string para mostrar en los v-dialog el horario seleccionado.
        this.createStringHorario(this.weekdays[data.weekday-1], startHour);

        // En el objeto createdEvent se guarda el día de la semana y la hora de inicio del adicional. 
        this.createdEvent = {
          name: null,
          color: null,
          bancos: [],
          weekday: data.weekday,         // Numero: Lunes = 1 ... Sabado = 6
          hour: startHour,               // Numero: De acuerdo a la hora de inicio
          repeat: false,                 // Bandera para repetir semanalmente el evento
          dateClick: data.date
        }
        
        // stringNameLabEnable habilita el v-select de los menus para seleccionar un adicional
        // En caso de que se tenga ya filtrado por laboratorio se toma ese nombre
        if(this.labSelect == "Ver todos"){
          this.stringNameLabEnable = true;
        }else{
          this.stringNameLab = this.labSelect;    
          this.stringNameLabEnable = false;
        }

        // Inicializa las fechas del calendarPicker acorde al día seleccionado
        this.minCalendarPicker = data.date;
        this.modelCalendarPicker = this.minCalendarPicker;

        // Activa el menu
        this.menuCreatedEvent = true;
      }
    },
    createStringHorario(week,hour){
      // Se crea un string para mostrar en los v-dialog el horario seleccionado.
      this.stringHorario = week + " " + hour.toString() + ":00" + " - " + (hour+2).toString() + ":00";
    },
    clickShowEvent ({ nativeEvent, event }) {
      // Define una función open local que se ejecuta en caso de que menuShowEvent sea false.
      const open = () => {        
        // Se toma en selectedEventShow la información del evento seleccionado. La información se debe tomar en otro objeto diferente a createEvent ya que si se da más de dos veces click sobre el mismo elemento no se recarga la función. 
        this.selectedEventShow = {

          date: event.start,

          name: event.name,
          color: event.color,
          bancos: event.bancos,
          weekday: event.weekday,
          hour: event.hour,
        };
        // En selectedElement se toma el <div> sobre el cual se dio click
        this.selectedElement = nativeEvent.target;
        // Se busca para este evento cuales bancos estan disponibles
        this.getBancosDisponibles(this.selectedEventShow);
        // Se hace la petición de la animación y se activa el v-menu
        requestAnimationFrame(() => requestAnimationFrame(() => this.menuShowEvent = true));
      }

      if (this.menuShowEvent) {
        this.menuShowEvent = false;
        requestAnimationFrame(() => requestAnimationFrame(() => open()));
      } else {
        open();
      }
      nativeEvent.stopPropagation();
    },
    getBancosDisponibles(event){      
      // Recibe un objeto de evento y toma la posición en la cual los bancos estan disponibles (true). 
      this.auxEstadoBancos = {
        Disponibles: [],
        Ocupados: [],
        Pendientes: [],
        Reservados: [],
      };
      for(let i=0;i<event.bancos.length;i++){
        if(event.bancos[i]!=="No Disponible"){
          this.auxEstadoBancos.Disponibles.push(i+1);
          if(event.bancos[i]=="Pendiente" || event.bancos[i]=="Reservado"){
            if(event.bancos[i]=="Pendiente"){
              this.auxEstadoBancos.Pendientes.push(i+1)
            }else{
              this.auxEstadoBancos.Reservados.push(i+1)
            }
            this.auxEstadoBancos.Ocupados.push(true)
          }else{
            this.auxEstadoBancos.Ocupados.push(false)
          }
        }
      }
    },
    menuShowEventEdit(){      
      // Se copia el objeto seleccionado a createdEvent para reutilizar el v-dialog.
      this.createdEvent = JSON.parse(JSON.stringify(this.selectedEventShow));

      // this.disponibilidadBancos = this.createdEvent.bancos.map(item => item!=="No Disponible"?true:false)

      // Se crea el string del horario y se toma el string del nombre para visualizar en el menu
      this.createStringHorario(this.weekdays[this.createdEvent.weekday-1], this.createdEvent.hour);
      this.stringNameLab = this.createdEvent.name;
      this.stringNameLabEnable = false;     // Se desabilita el v-select del laboratorio
      this.flagEdicion = true;              // Se activa la bandera de edicion
      // this.menuCreatedEvent = true;         // Se habilita el menu de crear evento
    },
    verificarBancosSeleccionados(){
      // Antes de guardar el adicional se verifica que al menos un banco haya sido seleccionado como valido
      let numBancosDisponibles = this.createdEvent.bancos.filter(item => item==true).length;
      if(numBancosDisponibles > 0){
        if (this.flagEdicion === true){
          // Como se edito, se deben actualizar los bancos disponibles y el objeto de visualiacion
          this.getBancosDisponibles(this.createdEvent);
          this.selectedEventShow = JSON.parse(JSON.stringify(this.createdEvent));
        }else{
          this.addHorarioAdicional();
        }
      }else{
        alert("Debe seleccionar al menos un banco.");
      }
    },
    selectShowEvents(){
      // Se hace el filtro de los eventos de acuerdo al valor de labSelect
      if(this.labSelect !== "Ver todos"){
        this.events = this.allEvents.filter(item => item.name == this.labSelect);
      }else{
        this.events= this.allEvents;
      }
    },
    addHorarioAdicional(){     
      let objeto = this;
      this.axios.post("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/addHorarioAdicional",
        {
          name: this.createdEvent.name,
          bancos: this.createdEvent.bancos.map(item => item===true?"Disponible":"No Disponible"),
          dia: this.createdEvent.weekday,
          hora: this.createdEvent.hour,
          repeat: this.createdEvent.repeat,
          dateRepeat: this.modelCalendarInput,
          dateClick: this.createdEvent.dateClick
        },
        {
          headers: {
            "Content-Type": "application/json"
          }
        })
      .then(function(response) {                
        objeto.menuCreatedEvent = false;
        objeto.menuShowEvent = false;
        alert(response.data.mensaje);
        objeto.getHorariosAdicionales();
      })
      .catch(function(error) {
        objeto.output = error;
      });
    },
    deleteHorarioAdicional(){      
      // this.createdEvent = JSON.parse(JSON.stringify(this.selectedEventShow));
      // let confirmacion = confirm("¿Esta seguro que desea eliminar el adicional?");
      // console.log(this.createdEvent);
      // if(confirmacion){
      //   let objeto = this;
      //   this.axios.post("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/deleteHorarioAdicional",
      //     {
      //       name: this.createdEvent.name,
      //       bancos: this.createdEvent.bancos,
      //       dia: this.createdEvent.weekday,
      //       hora: this.createdEvent.hour
      //     },
      //     {
      //       headers: {
      //         "Content-Type": "application/json"
      //       }
      //     })
      //   .then(function(response) {
      //     objeto.menuShowEvent = false; 
      //     objeto.menuCreatedEvent = false;       
      //     alert(response.data.mensaje);
      //     objeto.getHorariosAdicionales();
      //   })
      //   .catch(function(error) {
      //     objeto.output = error;
      //   });
      // }
    },
    getHorariosAdicionales(){
      // Trae todos los adicionales de la base de datos
      let objeto = this;
      this.axios.get("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/getHorariosAdicionales",
        {
          headers: {
            "Content-Type": "application/json"
          }
        })
      .then(function(response) {        
        objeto.enableEvents(response.data.data);
        objeto.selectShowEvents();
      })
      .catch(function(error) {
        alert("Ha ocurrido un error en el servidor. Por favor intentar de nuevo en un momento.")
      });
    },
    enableEvents(dataEvents){

      let dateNow = this.conversionDate(new Date());
      let hourNow = new Date().getHours();

      for (let i=0; i < dataEvents.length; i++){
        let dateAdicional = dataEvents[i].start.split(" ")[0];
        let condition1 = (dateNow < dateAdicional);
        let condition2 = (dateNow == dateAdicional &&  hourNow < dataEvents[i].hour);

        let infoSala = this.labs.find(item => item.name == dataEvents[i].name);

        if(condition1 || condition2){
          dataEvents[i].color = infoSala.color;
        }else{
          dataEvents[i].color = infoSala.colorLight;          
        }
      }
      this.allEvents = dataEvents;
    },
  },
};
</script>

<style>
  .v-calendar-daily__interval-text{
    font-weight: bold;
    position: relative;
    top: 0px;
    font-size: 13px;
  }
  .v-calendar-daily_head-weekday{
    font-size: 14px;
    text-transform: capitalize;
  }
  .scroll{
    overflow-y: scroll
  }  
  .v-calendar .v-event-timed {
    font-size: 13px;
  }
</style>

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