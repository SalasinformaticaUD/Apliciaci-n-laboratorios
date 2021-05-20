<template>
  <v-container fluid>
    <HeaderLaboratorista />

    <v-container fluid> 
      <v-sheet
        tile
        height="80"
        class="d-flex"
      >
        <v-row no-gutters align="center">
          <v-col cols="12" sm="3">
            <v-row class="ml-6">
              <h3 class="font-weight-medium"> Laboratorios de Ingeniería</h3>
            </v-row>
            <v-row class="ml-6">
              <h3 class="font-weight-medium"> Horarios Adicionales </h3>
            </v-row>
          </v-col>
          <v-col cols="12" sm="3" class="ml-5">
              <v-select                
                v-model="labSelect"
                :items="labSelectArray"
                label="Filtrar por"
                outlined
                dense                
                class="ma-3 mb-n2"
              ></v-select>
          </v-col>
        </v-row>
      </v-sheet>

      <v-sheet height="520" tile>
        <v-calendar
          ref="calendar"
          type="week"
          :weekdays="[1,2,3,4,5,6,0]"
          :short-weekdays="false"
          :events = "events"
          color = "primary"
          interval-minutes = "120"
          first-time = "06:00"
          interval-count = "7"
          :interval-height = "60"
          :show-interval-label="showIntervalLabel"
          :interval-format="intervalFormat"

          @click:event ="clickShowEvent"
          @click:time ="clickAddEvent"          
        >
        </v-calendar>
        

        <v-menu
          v-model="menuShowEvent"
          :close-on-content-click="false"
          :activator="selectedElement"
          offset-x
        >
          <v-card
            color="grey lighten-4"
            width="350px"
            flat
          >
            <v-toolbar
              :color="selectedEventShow.color"
              dark
            >
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
            <v-card-title>Información del adicional</v-card-title>    
            <v-card-text>
              <v-divider></v-divider>
              <v-row no-gutters class="mb-2 ml-3 mt-3">
                <v-col cols="12" sm="4">
                  Día: {{weekdays[selectedEventShow.weekday-1]}}
                </v-col>
                <v-col cols="12" sm="6" offset="2">
                  Horario: {{selectedEventShow.hour}}:00 - {{selectedEventShow.hour+2}}:00
                </v-col>
              </v-row>
              <v-row no-gutters class="mb-2 ml-3">
                Bancos disponibles:
              </v-row>
              <v-row no-gutters>
                <v-col cols="12" sm="4" v-for="(item,index) in auxEstadoBancos" :key="index">
                  <ul>
                    <li>Banco: {{auxEstadoBancos[index]+1}} </li>
                  </ul>
                </v-col>
              </v-row>              
              <v-divider></v-divider>
            </v-card-text>            
          </v-card>
        </v-menu>
      </v-sheet>

      <v-dialog v-model="menuCreatedEvent" max-width="400px">
        <v-card
          color="grey lighten-4"            
          flat
        >
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
          <v-card-title>Información del adicional</v-card-title>
          <v-card-text>
            <h4>1. Seleccione un laboratorio</h4>
            <v-select
              v-model="stringNameLab"
              :items="labs"
              label="Seleccione un laboratorio"
              solo
              dense
              item-text="name"
              class="ma-3 mb-n2"
              v-if="stringNameLabEnable"
            ></v-select>
            <v-text-field v-else dense disabled solo class="mt-2 px-3 mb-n1" v-model="stringNameLab">
            </v-text-field>
            <h4>2. Horario del adicional</h4>
            <v-text-field dense disabled solo class="mt-2 px-3 mb-n1" v-model="stringHorario">
            </v-text-field>
            <h4>3. Seleccione los bancos disponibles</h4>
            <v-row no-gutters class="mx-2 mt-2">
              <v-col cols="12" sm="4" class="my-n3" v-for="(item,index) in createdEvent.bancos" :key="index">
                <v-checkbox
                  v-model="createdEvent.bancos[index]"
                  :label="`Banco ${index+1}`"
                  :color="createdEvent.color"
                >
                </v-checkbox>
              </v-col>
            </v-row>
            <v-row no-gutters v-if="createdEvent.name">
              <v-col cols="12" sm="7" class="my-n3 mx-2">
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
          </v-card-text>
          <v-card-actions>
            <v-row class="justify-center mb-1 mt-n5">
              <v-col cols="12" sm="6">
                <v-btn           
                  medium        
                  block 
                  :dark="createdEvent.name==null ? false:true"
                  :disabled="createdEvent.name==null ? true:false"
                  :color="createdEvent.color"
                  @click="saveAdicional"
                >
                  Guardar
                </v-btn>
              </v-col>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-dialog>      

    </v-container>
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
      // Información de los laboratorios  
      labs:[
        {name: "Electrónica A",      color: "red darken-2",           bancos:8},
        {name: "Electrónica B",      color: "indigo darken-2",         bancos:6},
        {name: "Máquinas",           color: "green darken-3",   bancos:8},
        {name: "Circuitos",          color: "amber darken-2",         bancos:12},
        {name: "Comunicaciones",     color: "cyan accent-4",          bancos:6},
        {name: "Electrónica básica", color: "lime darken-2",   bancos:8},        
      ],

      // v-model del v-select de laboratorio. Por defecto se inicializar en Ver todos
      labSelectArray: [],
      labSelect: "Ver todos",

      // Esta variable auxiliar se utiliza para mostrar en la información de la ficha solo los bancos con estado true (disponibles)
      auxEstadoBancos:[],

      // Variable para seleccionar todos los bancos del laboratorio
      selectAllBancos: false,
    
      // En all events se tienen todos los adicionales de la base de datos. En events se relacionan los adicionales que se visualizan en el v-calendar.
      allEvents:[],
      events: [],

      // En createdEvent se almacena temporalmente la información del evento a agregar. 
      selectedEventShow: {
        name: "",
        color: "",
        bancos: "",
        weekday: "",
        hour: "",
      },
      createdEvent: {
        name: "",
        color: "",
        bancos: "",
        weekday: "",
        hour: "",
      },

      // Variable que controla el v-dialog que permite agregar un nuevo adicional
      menuCreatedEvent: false,

      selectedElement: null,
      menuShowEvent: false,
      weekdays: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],

      stringNameLab: "",
      stringNameLabEnable: false,
      stringHorario: "",

      flagEdicion: false,
    }
  },
  created(){
  },

  mounted(){   
    // De acuerdo al vectos de labs, se toma el campo name para hacer el v-select de filtrado. También se agrega la opción de "Ver todos".
    this.labSelectArray = this.labs.map(item => item.name);
    this.labSelectArray.push("Ver todos");
    // Trae todos los adicionales de la base de datos
    this.getHorariosAdicionales();
  },
  watch:{
    'createdEvent.bancos': function(){
      // Se hace un filtro para determinar si todos los bancos han sido seleccionados. En ese caso se habilita automáticamente la opción selectAlBancos.
      if(this.createdEvent.bancos !== null){
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
      if(val===false){
        this.stringNameLabEnable = false;
        this.flagEdicion = false;
        this.stringNameLab = "";
        this.stringHorario = "";
      }
    }
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
    clickAddEvent(data){
      // En esta función se toma el evento de click:time en algún espacio libre del calendario. 
      //  - Se verifica si el día es diferente a domingo (!==0) 
      //  - Se verifica que el menú de mostrar el evento sea falso.
      // En la variable "data" esta toda la información del espacio libre del calendario.
          
      if (data.weekday!==0 && this.menuShowEvent==false){
        // Se determina la hora de inicio del adicional. Se revisa si el espacio pulsado es hora par o impar.

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
          bancos: null,
          weekday: data.weekday,        // Numero: Lunes = 1 ... Sabado = 6
          hour: startHour               // Numero: De acuerdo a la hora de inicio
        }
        
        // stringNameLabEnable habilita el v-select de los menus para seleccionar un adicional
        if(this.labSelect == "Ver todos"){
          this.stringNameLabEnable = true;
        }else{
          this.stringNameLab = this.labSelect;
          this.stringNameLabEnable = false;
        }
      
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
      this.auxEstadoBancos = [];
      for(let i=0;i<event.bancos.length;i++){
        if(event.bancos[i]===true){
          this.auxEstadoBancos.push(i);
        }
      }
    },
    menuShowEventEdit(){      
      // Se copia el objeto seleccionado a createdEvent para reutilizar el v-dialog.
      this.createdEvent = JSON.parse(JSON.stringify(this.selectedEventShow));
      // Se crea el string del horario y se toma el string del nombre para visualizar en el menu
      this.createStringHorario(this.weekdays[this.createdEvent.weekday-1], this.createdEvent.hour);
      this.stringNameLab = this.createdEvent.name;
      this.stringNameLabEnable = false;     // Se desabilita el v-select del laboratorio
      this.flagEdicion = true;              // Se activa la bandera de edicion
      this.menuCreatedEvent = true;         // Se habilita el menu de crear evento
    },
    saveAdicional(){      
      // Antes de guardar el adicional se verifica que al menos un banco haya sido seleccionado como valido
      let numBancosDisponibles = this.createdEvent.bancos.filter(item => item==true).length;
      if(numBancosDisponibles > 0){
        // Si se esta agregando un nuevo laboratorio se verifica si coincide con alguno de los eventos para no repetir laboratorio en la misma franja horaria. Si es edición, no hay necesidad de verificar
        if (this.flagEdicion === true){
          // Como se edito, se deben actualizar los bancos disponibles y el objeto de visualiacion
          this.getBancosDisponibles(this.createdEvent);
          this.selectedEventShow = JSON.parse(JSON.stringify(this.createdEvent));
          this.addHorarioAdicional();
        }else{          
          // La verificación se hace con nombre, dia y horario del laboratorio
          let verificacion = this.allEvents.filter(item => item.name == this.createdEvent.name && item.weekday == this.createdEvent.weekday && item.hour == this.createdEvent.hour)
          if(verificacion.length==0){
            this.addHorarioAdicional();
          }else{
            alert("Ya tienen un adicional para " + this.createdEvent.name + " en este horario");  
          } 
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
          bancos: this.createdEvent.bancos,
          dia: this.createdEvent.weekday,
          hora: this.createdEvent.hour
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
      let confirmacion = confirm("¿Esta seguro que desea eliminar el adicional?");
      if(confirmacion){
        let objeto = this;
        this.axios.post("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/deleteHorarioAdicional",
          {
            name: this.createdEvent.name,
            bancos: this.createdEvent.bancos,
            dia: this.createdEvent.weekday,
            hora: this.createdEvent.hour
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          })
        .then(function(response) {
          objeto.menuShowEvent = false;        
          alert(response.data.mensaje);
          objeto.getHorariosAdicionales();
        })
        .catch(function(error) {
          objeto.output = error;
        });
      }
    },
    getHorariosAdicionales(){
      let objeto = this;
      this.axios.get("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/getHorariosAdicionales",
        {
          headers: {
            "Content-Type": "application/json"
          }
        })
      .then(function(response) {
        objeto.allEvents = response.data.data;
        for (let i=0;i<objeto.allEvents.length;i++){
          objeto.allEvents[i].color = objeto.labs.find(item => item.name == objeto.allEvents[i].name).color;
        }
        objeto.selectShowEvents();
      })
      .catch(function(error) {
        objeto.output = error;
      });
    },
  },
};
</script>

<style>
  .v-calendar-daily__interval-text{
    font-weight: bold;
    position: relative;
    top: 1px;
    font-size: 12px;
  }
  .v-calendar-daily__interval::after{
    width: 15px;
  }
  .v-calendar-daily_head-weekday{
    font-size: 12px;
    text-transform: capitalize;
  }
</style>