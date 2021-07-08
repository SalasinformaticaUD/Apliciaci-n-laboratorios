<template>
  <v-container fluid>
    <HeaderLaboratorista/>

    <v-sheet tile class="mt-7 rounded-t-xl">
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
        <v-col cols="12" sm="3" v-if="$refs.calendarLaboratorista" class="ml-sm-n8">
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
              {{ formatTitle($refs.calendarLaboratorista.title) }} 
              <br>
              Semana {{weekNumberCalendar}}
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
                @click="gotoWeekNowCalendar" 
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
            v-model="nameLabSelected"
            :items="nameLabSelectArray"
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
        ref="calendarLaboratorista"
        v-model="modelCalendar"
        type="week"          
        :weekdays="weekdaysCalendar"
        :short-weekdays="false"
        :events = "calendarAdicionales"
        color = "primary"
        interval-minutes = "120"
        first-time = "06:00"
        interval-count = "7"
        :interval-height = "70"
        :show-interval-label="showIntervalLabel"
        :interval-format="intervalFormat" 

        @click:event ="clickShowEvent"
        @click:time ="clickCreateAdicional" 
        class="botton"
      >
        <template v-slot:day-body="{ date }">
          <div
            class="v-current-time"
            :style="{ top: nowY, width: dateNow === date ? '100%' : '0%' }"
          > 
          </div>
          <div
            class="v-current-time2"
            :style="{ top: nowY, width: dateNow === date ? '12px': '0px'}"
          >
          </div>
        </template>
      </v-calendar>
        
      <v-menu
        v-model="menuShowEvent"
        :close-on-content-click="false"
        :open-on-click="false"
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

    <v-sheet  tile  min-height="50px" class="mb-4  rounded-b-xl">
    </v-sheet>

    <v-dialog v-model="menuCreatedAdicional" max-width="420px">
      <v-card color="grey lighten-4">
        <v-toolbar
          :color="createdAdicional.color ? createdAdicional.color : 'blue-grey darken-2'"
          dark  
          dense
        >
          <v-toolbar-title class="font-weight-bold" v-html="createdAdicional.name ? 'Laboratorio: ' + createdAdicional.name : 'Laboratorio'"></v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon large @click="menuCreatedAdicional=false">
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
              v-model="createdAdicional.name"
              :items="infoLabsStore"
              label="Seleccione un laboratorio"
              solo
              dense
              item-text="name"
              class="mx-3 mt-1 mb-n2 text-body-1 font-weight-normal"
            ></v-select>
          </v-row>
          <v-row no-gutters class="text-body-2 font-weight-medium pr-3">
            2. Horario del adicional
          </v-row>
          <v-row no-gutters>
            <v-text-field dense disabled solo class="mt-2 px-3 mb-n1 text-body-1 font-weight-medium" 
            :value="`${weekdays[createdAdicional.weekday-1]} ${createdAdicional.hour}:00 - ${createdAdicional.hour+2}:00`">
            </v-text-field>
          </v-row>
          <v-row no-gutters class="text-body-2 font-weight-medium">
            3. Seleccione los bancos que desea habilitar
          </v-row>
          <v-row no-gutters class="ml-4 mt-2">
            <v-col cols="12" sm="4" class="my-n4" v-for="(item,index) in createdAdicional.bancos" :key="index">
              <v-checkbox
                v-model="createdAdicional.bancos[index]"
                :label="`Banco ${index+1}`"
                :color="createdAdicional.color"
              >
              </v-checkbox>
            </v-col>
          </v-row>
          <v-row no-gutters v-if="createdAdicional.name">
            <v-col cols="12" sm="7" class="my-n4 ml-4">
              <v-checkbox
                v-model="selectAllBancos"
                :label="`Seleccionar todos`"
                :color="createdAdicional.color"
                @click="createdAdicional.bancos.fill(selectAllBancos)"
              >
              </v-checkbox>
            </v-col>
          </v-row>
          <v-row no-gutters justify="center" class="text--secondary" v-else>
            Favor seleccione un laboratorio.
          </v-row>
          <v-row no-gutters class="text-body-2 font-weight-medium pr-3 mt-3" v-if="createdAdicional.name">
            4. ¿Desea repetir esta configuración semanalmente?
          </v-row>
          <v-row no-gutters v-if="createdAdicional.name">
            <v-col cols="12" sm="2" offset="1">
              <v-switch
                v-model="createdAdicional.repeat"
                :label="createdAdicional.repeat ? 'Si' : 'No' "
                :color="createdAdicional.color"                
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
                  :disabled="!createdAdicional.repeat"
                ></v-text-field>
              </template>
                <v-date-picker 
                  v-model="modelCalendarPicker" 
                  no-title 
                  @input="menuCalendarPicker = false" 
                  :min="createdAdicional.dateStart"
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
                :dark="createdAdicional.name==null ? false:true"
                :disabled="createdAdicional.name==null ? true:false"
                :color="createdAdicional.color"
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

      dateNow: null,
      weekNumberNow: null,
      weekNumberCalendar: null,

      // Orden de los dias de la semana (Lunes - Domingo) en el v-calendar
      weekdaysCalendar: [1,2,3,4,5,6,0],
      
      // Vector para identificar los días de la semana según el número
      weekdays: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],

      // Información de los laboratorios  (se trae de vuex ./store/index.js)
      infoLabsStore:[],

      // v-model del v-select de laboratorio. Por defecto se inicializar en Ver todos
      nameLabSelectArray: [],
      nameLabSelected: "Ver todos",

      // Este objeto se utiliza para mostrar la información de los bancos en cada menu de informacion
      auxEstadoBancos:{
        Disponibles: [],
        Ocupados: [],
        Pendientes: [],
        Reservados: [],
      },

      // Variable para seleccionar todos los bancos del laboratorio en los checkbox
      selectAllBancos: false,
    
      // En all calendarAdicionales se tienen todos los adicionales de la base de datos. En calendarAdicionales se relacionan los adicionales que se visualizan en el v-calendar en caso de utilizar el filtro del laboratorio
      allAdicionales:[],
      calendarAdicionales: [],      

      // En selectedEventShow se almacena la informacion del evento seleccionado para ver informacion
      selectedEventShow: {
        name: "",
        color: "",
        bancos: "",
        weekday: "",
        hour: "",
        repeat: "",
      },

      // En createdAdicional se almacena la información del evento a crear. 
      createdAdicional: {
        name: "",
        color: "",
        bancos: "",
        weekday: "",
        hour: "",
        repeat: "",
        dateStart: "",
      },

      // elemento <div> seleccionado al dar click para ver información del adicional
      selectedElement: null,
      // variable relacionada con el menu que muestra la informacion del adicional
      menuShowEvent: false,

      // Variable que controla el v-dialog que permite agregar un nuevo adicional
      menuCreatedAdicional: false,

      // string que indica la franja horaria en el menu de crear adicional
      stringHorario: "",

      // Bandera para identificar si el menu de edicion del adicional se esta creando un nuevo o se esta editando uno ya existente
      flagEdicion: false,

      // variables relacionadas al calendario para seleccionar la fecha maxima de repeticion del adicional
      modelCalendarInput: "",
      modelCalendarPicker: "",
      menuCalendarPicker: false,
    }
  },

  created(){
    this.dateNow = this.conversionDate();
    let [year, month, day] = this.dateNow.split("-");
    this.weekNumberNow = this.findWeekNumberFromDate(year, month-1, day);
    this.weekNumberCalendar = this.weekNumberNow;

    this.infoLabsStore = this.$store.getters.infoLabs;
    this.nameLabSelectArray = this.infoLabsStore.map(lab => lab.name);
    this.nameLabSelectArray.push("Ver todos");
  },

  mounted(){ 
    this.getHorariosAdicionales();
    this.readyCalendar = true;
  },

  watch:{
    'createdAdicional.bancos': function(){
      console.log("%c Watcher Bancos", "font-size: 1rem");
      // Se hace un filtro para determinar si todos los bancos han sido seleccionados. En ese caso se habilita automáticamente la opción selectAllBancos.
      if(this.createdAdicional.bancos !== []){
        let bancosDisponibles = this.createdAdicional.bancos.filter(item => item===true).length;
        if(bancosDisponibles == this.createdAdicional.bancos.length){
          this.selectAllBancos = true;
        }else{
          this.selectAllBancos = false;
        }
      }
    },

    'createdAdicional.name': function(val){
      console.log("%c Watcher Nombre adicional", "font-size: 1rem");
      // Se hace un filtrado con el laboratorio seleccionado en los menús para tomar el nombre y el color
      // Se identifica con flagEdicion si se debe crear un vector de bancos nuevo (adicion de evento) o si se deben dejar los valores que ya existen (en el caso de editar un adicional)
      if (val!==""){
        let {name, color, bancos} = this.infoLabsStore.find(lab => lab.name === val);
        this.createdAdicional.name = name;
        this.createdAdicional.color = color;
        if (this.flagEdicion === false){
          this.createdAdicional.bancos = new Array(bancos).fill(false);
        }
      }
    },

    nameLabSelected: function(){
      console.log("%c Watcher nameLabSelected", "font-size: 1rem");
      // Esta función hace el filtro asociado al v-select de Laboratorio
      this.filterHorariosAdicionalesByName();
    },

    menuCreatedAdicional: function(val){
      console.log("%c Watcher menuCreatedAdicional", "font-size: 1rem");
      // watcher para identificar el cierre del menu de crear un evento para resetear algunas variables
      if(val===false){        
        this.flagEdicion = false;
        this.stringHorario = "";
      }
    },

    modelCalendarPicker: function(val) {
      console.log("%c Watcher modelCalendarPicker", "font-size: 1rem");
      // v-model del calendarPicker para detectar el cambio en la fecha y modificar también en el v-text
      this.modelCalendarInput = this.formatDate(val);
    },

  },
  computed: {
    cal () {
      return this.readyCalendar ? this.$refs.calendarLaboratorista : null
    },
    nowY () {
      return this.cal ? this.cal.timeToY(this.cal.times.now) + 'px' : '-10px'
    },
  },

  methods:{
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

    conversionDate(){
      // Esta función toma la fecha dada la función Date() de JS y retorna una fecha en el formato año-mes-dia. Esto se realiza para evitar utilizar la función Date().toISOString ya que esta última no tiene en cuenta la zona horaria y en horas de la noche toma la fecha como la del dia siguiente. 
      let date = new Date();
      let year = date.getFullYear().toString();
      let month = (date.getMonth()+1).toString();
      let day = date.getDate().toString();
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },

    gotoWeekNowCalendar(){
      // Lleva la vista del calendario a la semana actual
      this.modelCalendar = "";       // Se debe limpiar el model del v-calendar 
      this.weekNumberCalendar = this.weekNumberNow;
    },

    changeWeek(val){
      // Funcion para los botones de cambiar la semana en el header del v-calendar
      if(val==0){
        this.$refs.calendarLaboratorista.prev();
      }else{
        this.$refs.calendarLaboratorista.next();
      }
      let [year, month, day] = this.modelCalendar.split('-');
      this.weekNumberCalendar = this.findWeekNumberFromDate(year, month-1, day);
    },

    findWeekNumberFromDate(year, month, day){
      // Funcion que a partir de una fecha, identifica el número de la semana del año según formato ISO.
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

    formatDate(date) {
      // Convierte del formato año-mes-dia al formato dia/mes/año
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${day}/${month}/${year}`;
    },

    clickCreateAdicional(data){
      // En esta función se toma el evento de click:time en algún espacio libre del calendario
      //  - Se verifica si el día es diferente a domingo (!==0)
      //  - Se verifica que el menú de mostrar la info del adicional sea falso
      // En la variable "data" esta toda la información del espacio libre del calendario

      let {weekday, hour, date} = data;
          
      if (weekday!==0 && this.menuShowEvent==false){
        
        let startHour = hour;
        if(hour%2 == 1){
          startHour -= 1;           // Si la hora es impar se debe restar una hora
        }

        this.createdAdicional = {
          name: null,
          color: null,
          bancos: [],
          weekday: weekday,         // Numero: Lunes = 1 ... Sabado = 6
          hour: startHour,          // Numero: De acuerdo a la hora de inicio
          repeat: false,            // Bandera para repetir semanalmente el evento
          dateStart: date
        }

        // Inicializa las fechas del calendarPicker acorde al día seleccionado
        this.modelCalendarPicker = date;

        this.menuCreatedAdicional = true;
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
      // Se copia el objeto seleccionado a createdAdicional para reutilizar el v-dialog.
      this.createdAdicional = JSON.parse(JSON.stringify(this.selectedEventShow));

      // this.disponibilidadBancos = this.createdAdicional.bancos.map(item => item!=="No Disponible"?true:false)

      // Se crea el string del horario y se toma el string del nombre para visualizar en el menu
      this.createStringHorario(this.weekdays[this.createdAdicional.weekday-1], this.createdAdicional.hour);
      this.flagEdicion = true;              // Se activa la bandera de edicion
      this.menuCreatedAdicional = true;         // Se habilita el menu de crear evento
    },
    verificarBancosSeleccionados(){
      // Antes de guardar el adicional se verifica que al menos un banco haya sido seleccionado como valido
      let numBancosDisponibles = this.createdAdicional.bancos.filter(item => item==true).length;
      if(numBancosDisponibles > 0){
        if (this.flagEdicion === true){
          // Como se edito, se deben actualizar los bancos disponibles y el objeto de visualiacion
          this.getBancosDisponibles(this.createdAdicional);
          this.selectedEventShow = JSON.parse(JSON.stringify(this.createdAdicional));
        }else{
          this.addHorarioAdicional();
        }
      }else{
        alert("Debe seleccionar al menos un banco.");
      }
    },

    filterHorariosAdicionalesByName(){
      // Se hace el filtro de los eventos de acuerdo al valor de nameLabSelected
      if(this.nameLabSelected !== "Ver todos"){
        this.calendarAdicionales = this.allAdicionales.filter(lab => lab.name == this.nameLabSelected);
      }else{
        this.calendarAdicionales = this.allAdicionales;
      }
    },

    addHorarioAdicional(){     
      let objeto = this;
      this.axios.post("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/addHorarioAdicional",
        {
          name: this.createdAdicional.name,
          bancos: this.createdAdicional.bancos.map(item => item===true?"Disponible":"No Disponible"),
          dia: this.createdAdicional.weekday,
          hora: this.createdAdicional.hour,
          repeat: this.createdAdicional.repeat,
          dateRepeat: this.modelCalendarInput,
          dateClick: this.createdEvent.dateStart
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
        objeto.menuCreatedAdicional = false;
        objeto.menuShowEvent = false;
        alert(response.data.mensaje);
        objeto.getHorariosAdicionales();
      })
      .catch(function(error) {
        objeto.output = error;
      });
    },
    deleteHorarioAdicional(){      
      // this.createdAdicional = JSON.parse(JSON.stringify(this.selectedEventShow));
      // let confirmacion = confirm("¿Esta seguro que desea eliminar el adicional?");
      // console.log(this.createdAdicional);
      // if(confirmacion){
      //   let objeto = this;
      //   this.axios.post("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/deleteHorarioAdicional",
      //     {
      //       name: this.createdAdicional.name,
      //       bancos: this.createdAdicional.bancos,
      //       dia: this.createdAdicional.weekday,
      //       hora: this.createdAdicional.hour
      //     },
      //     {
      //       headers: {
      //         "Content-Type": "application/json"
      //       }
      //     })
      //   .then(function(response) {
      //     objeto.menuShowEvent = false; 
      //     objeto.menuCreatedAdicional = false;       
      //     alert(response.data.mensaje);
      //     objeto.getHorariosAdicionales();
      //   })
      //   .catch(function(error) {
      //     objeto.output = error;
      //   });
      // }
    },

    getHorariosAdicionales(){
      // const authHeader = this.$cookies.get('jwt') ? { 'Authorization': 'Bearer ' + this.$cookies.get('jwt') } : {}
      this.axios.get("http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/getHorariosAdicionales",
        {
          headers: {
            // ...authHeader,
            "Authorization": this.$cookies.get("jwt") ? "Bearer " + this.$cookies.get("jwt") : "",
            "Content-Type": "application/json"
          }
        })
      .then(response => {
        let {data, mensaje, status} = response.data;
        this.allAdicionales = this.setColorEventsAdicionales(data);
        this.filterHorariosAdicionalesByName();
        if (status == 0){
          alert(mensaje);
        }else if (response.data.status == 401) {                                
          objeto.$router.push('/');
          alert("Error de sesion");                
        }
      })
      .catch(error => {
        alert(error)
      });
    },

    setColorEventsAdicionales(adicionales){
      // Función que identifica el color del adicional según el estado retornado del servidor
      let lengthAdicionales = adicionales.length;
      for (let i=0; i<lengthAdicionales; i++){
        let {color, colorLight} = this.infoLabsStore.find(lab => lab.name === adicionales[i].name);

        if(adicionales[i].state === true){                  // state = true  -> laboratorio disponible
          adicionales[i].color = color;
        }else
          adicionales[i].color = colorLight;
      }
      return adicionales
    },

    sendConsultaPendiente(banco){
      console.log("Metodo en agenda adicional");
      console.log(this.selectedEventShow);
      let date = this.selectedEventShow.date.split(" ")[0];
      this.$store.state.date = this.formatDate(date);
      this.$store.state.hour = this.selectedEventShow.hour;
      this.$store.state.banco = banco;
      console.log("Fecha que se envía al store: " + date);
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
    
    height: 12px;
    border-radius: 50%;
    margin-top: -5px;
    margin-left: -6.5px;
    position: absolute;
  }
  .botton >>> button{
    font-size: 0.96rem;
  }
</style>