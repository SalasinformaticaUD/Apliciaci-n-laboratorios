<template>
  <v-container fluid>
    <Headerestudiantes/>

    <v-sheet  tile  min-height="110px" class="d-flex mt-7">
      <v-row no-gutters align="center"> 
        <v-col cols="12" sm="3">          
          <v-row class="mt-4 pl-5" no-gutters>
            <p class="text-h6 font-weight-medium"> Laboratorios de Ingeniería</p>
          </v-row>
          <v-row class="mt-n5 pl-5" no-gutters>
            <p class="text-h6 font-weight-medium"> Horarios Adicionales </p>
          </v-row>
        </v-col>
        <v-divider vertical></v-divider>
        <v-col cols="12" sm="6" class="pl-3">
          <v-row no-gutters class="text-body-2">
            1. Seleccione uno de los horarios disponibles para laboratorio adicional.
          </v-row>
          <v-row no-gutters class="text-body-2">
            2. Verifique la disponibilidad de los bancos habilitados para reserva.
          </v-row>
          <v-row no-gutters class="text-body-2">
            3. De click en "Solicitud de reserva" y complete la información.
          </v-row>
          <v-row no-gutters class="text-body-2">
            4. La solicitud queda en espera a la aprobación de un laboratorista.
          </v-row>
        </v-col>
        <v-col cols="12" sm="3" class="mt-6 px-8">
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
        type="week"
        :weekdays="[1,2,3,4,5,6,0]"
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
      >
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

        <v-stepper v-model="step" tile>
          <v-stepper-header class="mt-n3" flat>
            <v-stepper-step :complete="step > 1" step="1" :color="selectedEvent.color">
              Información  
              <hr>
              del adicional
            </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step :complete="step > 2" step="2" :color="selectedEvent.color">
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
                          @keyup.enter="nextStep()"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-form>
                </v-card-text>            
                <v-card-actions class="mx-6 mb-n2 mt-n3">
                  <v-row no-gutters>
                    <v-btn large block :color="selectedEvent.color" :dark="validForm" :disabled="!validForm" @click="nextStep">
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
                    <v-btn large block :color="selectedEvent.color" dark @click="sendReserva">
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
      todaydate: "",    // Fecha actual en formato dia/mes/año

      // Información de los laboratorios  
      labs:[
        {name: "Electrónica A",      color: "red darken-2",     bancos:8},
        {name: "Electrónica B",      color: "indigo darken-2",  bancos:6},
        {name: "Máquinas",           color: "green darken-3",   bancos:8},
        {name: "Circuitos",          color: "amber darken-2",   bancos:12},
        {name: "Comunicaciones",     color: "cyan accent-4",    bancos:6},
        {name: "Electrónica básica", color: "lime darken-2",    bancos:8},        
      ],

      // v-model del v-select de laboratorio. Por defecto se inicializar en Ver todos
      labSelectArray: [],
      labSelect: "Ver todos",

      // auxEstadoBancos se utiliza para mostrar en la información del adicional el estado de los bancos
      auxEstadoBancos:{
        Disponibles: [],
        Ocupados: [],
        Libres: [],
      },      

      // En all events se tienen todos los adicionales de la base de datos. En events se relacionan los adicionales que se visualizan en el v-calendar.
      allEvents:[],
      events: [],

      // En selectedEvent se almacena la información del evento seleccionado
      selectedEvent: {},
      menuShowEvent: false,
      elementShowEvent: null,

      menuFormulario: false,
      weekdays: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],

      stringHorario: "",

      formReserva:{
        fecha_adicional: "",
        sala: "",
        hora: "",
        diaSemana: "",
        banco: "",
        practica: "",
        elemento: [],
      },

      step: 1,
      validForm: true,
      rules:{
        required: value => !!value || "Este espacio es requerido.",
      },     

      inputElementoAdicional: "",
    }
  },
  created(){
  },

  computed:{
  },

  mounted(){   
    // De acuerdo al vectos de labs, se toma el campo name para hacer el v-select de filtrado. También se agrega la opción de "Ver todos".
    this.labSelectArray = this.labs.map(item => item.name);
    this.labSelectArray.push("Ver todos");
    this.todaydate = this.formatDate(this.conversionDate(new Date()));
    // Trae todos los adicionales de la base de datos
    this.getHorariosAdicionales();
  },
  watch:{
    menuFormulario: function(val){
      if(val==false){
        this.$refs.form.reset();
      }
    },
    labSelect: function(){
      // Esta función hace el filtro asociado al v-select de Laboratorio
      this.selectShowEvents();
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
    formatDate(date) {
      // Esta función toma una fecha en el formato año-mes-dia (formato v-calendar) y la convierte al formato dia/mes/año (formato utilizado en el proyecto)
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${day}/${month}/${year}`;
    },
    showIntervalLabel(interval) {
      // Esta función permite visualizar el primer dato de tiempo (06:00) en el v-calendar
      return interval.minute === 0;
    },
    intervalFormat(interval) {
      // Esta función modifica el formato de visualización de las horas en el v-calendar a hh:mm
      return interval.time
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
      console.log("fcn clickShowEvent");
      // Define una función open local que se ejecuta en caso de que menuShowEvent sea false.
      const open = () => {        
        // Se toma en selectedEvent la información del evento seleccionado
        let fecha = event.start.split(" ")[0].split("-");
        this.selectedEvent = {
          name: event.name,
          color: event.color,
          bancos: event.bancos,
          weekday: event.weekday,
          hour: event.hour,
          fecha: fecha[2] + "/" + fecha[1] + "/" + fecha[0],
        };
        // En selectedElement se toma el <div> sobre el cual se dio click
        this.elementShowEvent = nativeEvent.target;
        // Se obtiene del evento el estado de los bancos
        this.getEstadoBancos(this.selectedEvent);
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
      // Recibe un objeto de evento y toma la posición en la cual los bancos estan disponibles (true). 
      this.auxEstadoBancos = {
        Disponibles: [],
        Ocupados: [],
        Libres: [],
      };
      for(let i=0;i<event.bancos.length;i++){
        if(event.bancos[i]!=="No Disponible"){
          this.auxEstadoBancos.Disponibles.push(i+1);
          if(event.bancos[i]=="Pendiente" || event.bancos[i]=="Reservado"){
            this.auxEstadoBancos.Ocupados.push(true)
          }else{
            this.auxEstadoBancos.Libres.push(i+1);
            this.auxEstadoBancos.Ocupados.push(false)
          }
        }
      }
    },
    solicitudReserva(){
      this.formReserva = {
        fecha_adicional: this.selectedEvent.fecha,
        sala: this.selectedEvent.name,
        hora: this.selectedEvent.hour,
        diaSemana: this.selectedEvent.weekday,
        banco: null,
        practica: null,
        elemento: [],
      }
      let horaAdicional = this.selectedEvent.hour;
      this.stringHorario = horaAdicional.toString() + ":00 - " + (horaAdicional+2).toString() + ":00";
      this.step = 1;
      this.menuShowEvent = false;
      this.menuFormulario = true;
    },
    nextStep(){
      if(this.$refs.form.validate()){
        this.step = 2;
      }
    },
    agregarElementoAdicional(){
      // Valida que el elemento agregado en el input del adicional no sea un espacio en blanco o vacío. Luego, lo agrega al vector Elemento del formulario. Finalmente vacía el input para poder agregar otro elemento
      if (this.inputElementoAdicional.length>0){
        if(this.inputElementoAdicional.replace(/ /g, "").length>0){
          this.formReserva.elemento.push(this.inputElementoAdicional);
        }
      }            
      this.inputElementoAdicional = "";
    },
    sendReserva(){
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
          date_user: this.todaydate,
          hour_user: new Date().getHours(),
          minutes_user: new Date().getMinutes()
        },
        {
          headers: {
            "Content-Type": "application/json"
          }
        }
      )
      .then(function(response) {
        if(response.data.status == 1){
          objeto.selectedEvent.bancos[objeto.formReserva.banco - 1] = "Pendiente";
          objeto.getEstadoBancos(objeto.selectedEvent);
          objeto.menuFormulario = false;
          objeto.addHorarioAdicional();
          alert(response.data.mensaje)
        }else{
          alert(response.data.mensaje)
        }
      })
      .catch(function(error) {
        objeto.output = error;
      });
    },
    addHorarioAdicional(){      
      let objeto = this;
      this.axios.post("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/addHorarioAdicional",
        {
          name: this.selectedEvent.name,
          bancos: this.selectedEvent.bancos,
          dia: this.selectedEvent.weekday,
          hora: this.selectedEvent.hour
        },
        {
          headers: {
            "Content-Type": "application/json"
          }
        })
      .then(function(response) {        
        objeto.getHorariosAdicionales();
      })
      .catch(function(error) {
        objeto.output = error;
      });
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
        objeto.enableEvents();
        objeto.selectShowEvents();
      })
      .catch(function(error) {
        objeto.output = error;
      });
    },
    enableEvents(){
      console.log("enableEvents");

      let weekday = new Date().getDay();
      let hour = new Date().getHours();
      let minutes = new Date().getMinutes();


      for (let i=0;i<this.allEvents.length;i++){
        let condition1 = (weekday < this.allEvents[i].weekday);
        let condition2 = (weekday == this.allEvents[i].weekday &&  hour*60+minutes < (this.allEvents[i].hour*60)+20);

        if(condition1 || condition2){
          this.allEvents[i].color = this.labs.find(item => item.name == this.allEvents[i].name).color;
          this.allEvents[i].enable = true;
        }else{
          this.allEvents[i].color = "grey darken-1";
          this.allEvents[i].enable = false;
        }
      } 

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
  .v-card--reveal {
    bottom: 0;
    opacity: 1 !important;
    position: absolute;
    width: 100%;
  }
  .v-application .pl-1 {
    padding-left: 6px !important;
  }
  .scroll{
    overflow-y: scroll
  }
</style>