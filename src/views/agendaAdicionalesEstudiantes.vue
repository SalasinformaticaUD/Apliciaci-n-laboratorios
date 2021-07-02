<template>
  <v-container fluid>
    <Headerestudiantes/>

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
                    :disabled="weekNumberNow == weekNumberCalendar ? true : false"
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
                    :disabled="weekNumberNow+1 == weekNumberCalendar ? true : false"
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
        ref="calendarEstudiantes"
        v-model="modelCalendar"
        type="week"
        :weekdays="weekdaysCalendar"
        :short-weekdays="false"
        :events="calendarAdicionales"
        color="primary"
        interval-minutes="120"
        first-time="06:00"
        interval-count="7"
        :interval-height="70"
        :show-interval-label="showIntervalLabel"
        :interval-format="intervalFormat"
        @click:event ="clickInHorarioAdicional"
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
        v-model="menuInfoAdicional"
        :close-on-content-click="false"
        :open-on-click="false"
        :activator="divElementAdicional"
        offset-x
      >
        <v-card color="grey lighten-4" width="320px" flat>
          <v-toolbar :color="selectedAdicional.color" dark>
            <v-toolbar-title v-html="selectedAdicional.name"></v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon large @click.prevent="menuInfoAdicional = false">
              <v-icon>fas fa-times</v-icon>
            </v-btn>
          </v-toolbar>
          <v-card-title class="my-n1">Información del laboratorio</v-card-title>    
          <v-card-text>
            <v-alert 
              type="warning" 
              color="amber accent-4"
              outlined 
              dense 
              elevation="4" 
              class="text-subtitle-2 mb-5" 
              prominent
              v-if="selectedAdicional.state !== true && selectedAdicional.state !== false"
            >
              Tiene registrado un
              <router-link :to="{
                name: 'consulta'}">
                <span @click="sendReservaToVistaConsulta">
                  adicional {{selectedAdicional.state}}
                </span>
              </router-link>
              en este horario.
            </v-alert>
            <v-divider></v-divider>
            <v-row no-gutters class="mb-2 ml-2 mt-2">
              <v-col cols="12" sm="4" class="text-subtitle-2">
                Día: {{weekdaysString[selectedAdicional.weekday-1]}}
              </v-col>
              <v-col cols="12" sm="6" offset="2" class="text-subtitle-2">
                Horario: {{selectedAdicional.hour}}:00 - {{selectedAdicional.hour+2}}:00
              </v-col>
            </v-row>
            <v-row no-gutters class="mb-1 ml-2 mt-3 text-subtitle-2" v-if="auxEstadoBancos.habilitados.length>0">
              Bancos disponibles para reserva:
            </v-row>
            <v-row no-gutters class="mx-2">
              <v-col cols="12" sm="4" v-for="(item,index) in auxEstadoBancos.habilitados" :key="index">
                <ul v-if="auxEstadoBancos.ocupados[index] === false">
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
            <v-row no-gutters v-if="enableBtnSolicitarReserva()" justify="center" class="px-4 mb-3 mt-n2">
              <v-btn block :color="selectedAdicional.color" dark @click="setFormReserva">
                Solicitud de reserva
              </v-btn>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-menu>
    </v-sheet>
    <v-sheet  tile  min-height="50px" class="mb-4  rounded-b-xl">
    </v-sheet>
      
    <v-dialog v-model="menuFormReserva" max-width="530px">
      <v-card color="grey lighten-4">
        <v-toolbar :color="selectedAdicional.color" dark>
          <v-toolbar-title class="text-h6">Reserva de laboratorio adicional</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon large @click.prevent="menuFormReserva = false">
            <v-icon>fas fa-times</v-icon>
          </v-btn>
        </v-toolbar>

        <v-stepper  tile non-linear v-model="modelStepperReserva">
          <v-stepper-header class="mt-n3" flat>
            <v-stepper-step :complete="modelStepperReserva > 1" step="1" :color="selectedAdicional.color" editable>
              Información  
              <hr>
              del adicional
            </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step step="2" :color="selectedAdicional.color" editable>
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
                        :value="formReserva.diaSemana"
                        outlined
                        dense
                        disabled
                        class="text-subtitle-1 font-weight-medium ml-4 mt-1 mr-4"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" class="text-subtitle-1 pl-3">
                      4. Franja Horaria
                      <v-text-field
                        :value="`${formReserva.hora}:00 - ${formReserva.hora+2}:00`"
                        outlined
                        dense
                        disabled
                        class="text-subtitle-1 font-weight-medium ml-4 mt-1 mr-4"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-form ref="formReserva" v-model="modelFormReserva" lazy-validation>
                    <v-row class="mt-n3" no-gutters>
                      <v-col cols="12" sm="6" class="text-subtitle-1 pr-3">
                        5. Número de banco
                        <v-select              
                          ref="banco"  
                          v-model="formReserva.banco"
                          :items="auxEstadoBancos.libres"
                          :label="formReserva.banco==null?'Seleccione...':''"
                          :rules="[rulesFormReserva.required]"
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
                          :rules="[rulesFormReserva.required]"
                          placeholder="p. ej. Electrónica 1"
                          required
                          dense
                          outlined        
                          class="text-subtitle-1 ml-4 mt-1 mr-4"
                          @keyup.enter="modelStepperReserva=2"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-form>
                </v-card-text>            
                <v-card-actions class="mx-6 mb-n2 mt-n3">
                  <v-row no-gutters>
                    <v-btn large block :color="selectedAdicional.color" @click="modelStepperReserva=2" dark>
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
                        label="Ingrese un elemento adicional (máx. 10)"
                        hide-details="auto"
                        v-model = "inputElementoAdicional"
                        dense
                        @keyup.enter="addElementoAdicional()"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="2" align-self="center" class="pl-4">
                      <v-btn :color="selectedAdicional.color" outlined elevation="1" tile medium class="px-2 py-1" @click="addElementoAdicional()">
                        Agregar
                      </v-btn>
                    </v-col>
                  </v-row>      
                  <v-card elevation="4" class="mt-4 pa-2 mx-3 scroll"  v-if="formReserva.elementos.length !== 0" max-height="160">
                    <v-card-text>
                      <v-row no-gutters v-for= "(elemento,index) in formReserva.elementos" :key="index">
                        <v-col cols="12" sm="10">
                          <v-divider></v-divider>
                          <ol>
                            <dt align="left">
                              {{index+1}}. {{elemento.nombre}}
                            </dt>
                          </ol>
                        </v-col>
                        <v-col cols="12" sm="2" align="center">
                          <v-divider></v-divider>
                          <v-icon small @click="formReserva.elementos.splice(index,1)"> 
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
                    <v-btn large block :color="selectedAdicional.color" :dark="modelFormReserva" :disabled="!modelFormReserva"
                    @click="checkFormReserva">
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
import jwt_decode from "jwt-decode";

export default {
  components: {
    Headerestudiantes,
  },
  data() {
    return {    
      modelCalendar: "",
      readyCalendar: false,
      weekNumberCalendar: null,

      allAdicionales:[],
      calendarAdicionales: [],

      dateNow: "",                          // formato año-mes-dia
      weekNumberNow: null,                  // Numero de semana ISO (1 to 52 or 53)

      weekdaysCalendar: [1,2,3,4,5,6,0],    // 1 -> Lunes, 0 -> Domingo
      weekdaysString: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],
      
      infoLabsStore:[],                     //  (se trae desde vuex ./store/index.js)      
      nameLabSelectArray: [],
      nameLabSelected: "Ver todos",

      auxEstadoBancos:{
        habilitados: [],            // Bancos disponibles habilitados para reserva
        ocupados: [],               // Bancos habilitados que ya tienen relacionada una reserva
        libres: [],                 // Bancos habilitados que pueden ser ocupados
      },      

      selectedAdicional: {
        bancos: [],
        color: "",
        date: "",
        hour: null,
        name: "",
        start: "",
        state: null,
        weekday: null,
      },
      
      menuInfoAdicional: false,
      divElementAdicional: null,

      menuFormReserva: false,

      formReserva:{
        fecha_adicional: "",              // Fecha del adicional en formato dia/mes/año 
        sala: "",                         // Nombre de la sala de laboratorio
        hora: "",                         // Hora de inicio de la franja horaria
        diaSemana: "",                    // Día de la semana
        banco: "",                        // Numero de banco
        practica: "",                     // Nombre de la practica
        elementos: [],                    // Elementos solicitados
      },
      inputElementoAdicional: "",
      rulesFormReserva:{
        required: value => !!value || "Este espacio es requerido.",
      },     
      modelFormReserva: true,
      modelStepperReserva: 1,
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
    menuFormReserva: function(val){
      // Identifica el momento en que se cierra el menu del formulario y reinicia las variables del form
      val === false ? this.$refs.formReserva.reset() : null;
    },
    nameLabSelected: function(){
      this.filterHorariosAdicionalesByName();
    },
  },
  computed: {
    cal () {
      // Retorna el objeto $refs.calendarEstudiantes cuando el componente v-calendar se ha renderizado
      return this.readyCalendar ? this.$refs.calendarEstudiantes : null
    },
    nowY () {
      // Luego de renderizar el v-calendar, retorna la hora actual para hacer la línea del day-body
      return this.cal ? this.cal.timeToY(this.cal.times.now) + 'px' : '-10px'
    },
  },
  methods:{

    conversionDate(){
      // Esta función toma la fecha dada la función Date() de JS y retorna una fecha en el formato año-mes-dia. Esto se realiza para evitar utilizar la función Date().toISOString ya que esta última no tiene en cuenta la zona horaria y en horas de la noche toma la fecha como la del dia siguiente. 
      let date = new Date();
      let year = date.getFullYear().toString();
      let month = (date.getMonth()+1).toString();
      let day = date.getDate().toString();
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },

    showIntervalLabel(interval) {
      // Esta función permite visualizar el primer dato de tiempo (06:00) en el v-calendar
      return interval.minute === 0
    },

    intervalFormat(interval) {
      // Esta función modifica el formato de visualización de las horas en el v-calendar a hh:mm
      return interval.time
    },

    formatTitle(title){
      // Funcion que pone la primera letra en mayuscula para un string
      return title.charAt(0).toUpperCase() + title.slice(1);
    },

    changeWeek(val){
      // Funcion para los botones de cambiar la semana en el header del v-calendar
      if(val===0){
        this.$refs.calendarEstudiantes.prev();
      }else{
        this.$refs.calendarEstudiantes.next();
      }
      let [year, month, day] = this.modelCalendar.split('-');
      this.weekNumberCalendar = this.findWeekNumberFromDate(year, month-1, day);
    },

    gotoWeekNowCalendar(){
      // Lleva la vista del calendario a la semana actual
      this.modelCalendar = "";       // Se debe limpiar el model del v-calendar 
      this.weekNumberCalendar = this.weekNumberNow;
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

    filterHorariosAdicionalesByName(){
      // Se hace el filtro de los eventos de acuerdo al valor de labSelect
      if(this.nameLabSelected === "Ver todos"){
        this.calendarAdicionales = this.allAdicionales;
      }else{
        this.calendarAdicionales = this.allAdicionales.filter(lab => lab.name === this.nameLabSelected);
      }
    },    

    clickInHorarioAdicional ({ nativeEvent, event }){
      // Se toma en selectedAdicional la información de interes del adicional seleccionado
      const open = () => {
        let [year, month, day] = event.start.split(" ")[0].split("-");
        let {end, ...restOfAdicional} = event;
        this.selectedAdicional = {...restOfAdicional, date: `${day}/${month}/${year}`};
        this.divElementAdicional = nativeEvent.target;
        this.getEstadoBancos(this.selectedAdicional);
        requestAnimationFrame(() => requestAnimationFrame(() => this.menuInfoAdicional = true));
      }      
      if (this.menuInfoAdicional) {
        this.menuInfoAdicional = false;
        requestAnimationFrame(() => requestAnimationFrame(() => open()));
      } else {
        open();
      }
      nativeEvent.stopPropagation();
    },

    getEstadoBancos(adicional){    
      // Recibe un objeto del adicional y toma la información de los bancos según corresponda
      // Posibles valores de de adicional.bancos: No Disponible, Disponible, Pendiente, Reservado
      this.auxEstadoBancos = {
        habilitados: [],
        ocupados: [],
        libres: [],
      };
      let lengthBancosEvent = adicional.bancos.length;
      for(let i=0; i<lengthBancosEvent; i++){
        let estado = adicional.bancos[i];
        if(estado !== "No Disponible"){
          this.auxEstadoBancos.habilitados.push(i+1);       // Bancos habilitados para reserva
          if(estado === "Pendiente" || estado === "Reservado"){
            this.auxEstadoBancos.ocupados.push(true);       // Bancos para reserva ocupados
          }else{
            this.auxEstadoBancos.ocupados.push(false);      // Bancos para reserva libres
            this.auxEstadoBancos.libres.push(i+1);          // Bancos libres para reserva   
          }
        }
      }      
    },

    enableBtnSolicitarReserva(){
      // Habilita el btn de solicitar reserva solo si el adicional tiene bancos libres y si el state es true
      return this.auxEstadoBancos.libres.length>0 && this.selectedAdicional.state === true
    },

    sendReservaToVistaConsulta(){
      // Guarda en el store de Vuex la fecha y hora del adicional para hacer el filtrado en /consulta
      this.$store.state.date = this.selectedAdicional.date;
      this.$store.state.hour = this.selectedAdicional.hour;
    },

    setFormReserva(){
      // Toma la información para llenar el formulario e información de interés para enviar al servidor
      let {date, name, hour, weekday} = this.selectedAdicional;
      this.formReserva = {
        fecha_adicional: date,
        sala: name,
        hora: hour,
        diaSemana: this.weekdaysString[weekday - 1],
        banco: null,
        practica: null,
        elementos: [],
      }
      this.modelStepperReserva = 1;
      this.menuInfoAdicional = false;
      this.menuFormReserva = true;
    },

    addElementoAdicional(){
      // Valida que el elemento agregado en el input del adicional no sea un espacio en blanco o vacío
      if(this.inputElementoAdicional.length>0){
        if(this.inputElementoAdicional.replace(/ /g, "").length>0){
          if(this.formReserva.elementos.length<10){
            this.formReserva.elementos.push({
              nombre: this.inputElementoAdicional,
              estado: "PENDIENTE",
              placa: ""
            });
          }else{
            alert("Solo se permite un máximo 10 elementos.")
          }
        }
      }            
      this.inputElementoAdicional = "";
    },

    checkFormReserva(){
      // Se valida si los campos de banco y practica han sido llenados
      if(this.$refs.formReserva.validate()){
        this.sendFormReservaToServer();
      }else{
        this.modelStepperReserva = 1;
      }
    },

    sendFormReservaToServer(){
      let cod_encrypted = this.$cookies.get("user_session");
      let codigoLab = this.$Crypto.AES.decrypt(cod_encrypted, localStorage.cdcb0830cc2dd220);
      codigoLab = codigoLab.toString(this.$Crypto.enc.Utf8);
      this.axios.post("http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/addReservaEstudiante",
        { 
          codigoUser: codigoLab,
          usuario: localStorage.usuario,
          datos: this.formReserva,

          dateUser: this.dateNow,
          hourUser: new Date().getHours(),
          minutesUser: new Date().getMinutes()
        },
        {
          headers: {
            "Content-Type": "application/json"
          }
        }
      )
      .then((response) => {
        let {status, mensaje} = response.data;
        if(status === 1){                          // status = 1 -> Reserva registrada correctamente
          this.getHorariosAdicionales();
          this.menuFormReserva = false;
          alert(mensaje);
        }else if(status === 2){                    // status = 2 -> Si el banco solicitado ya esta ocupado
          this.getHorariosAdicionalesAwait(mensaje);
        }else{                                     // status = 3 -> Si ya tiene 3 adicionales en la semana
          this.menuFormReserva = false;
          alert(mensaje);
        }
      })
      .catch((error) => {
        this.output = error;
      });
    },

    getHorariosAdicionalesAwait: async function(mensaje){
      // Se hace una funcion async para esperar y actualizar correctamente el laboratorio seleccionado
      await this.getHorariosAdicionales();
      this.updateEventsAdicionales();
      this.formReserva.banco = null;
      this.modelStepperReserva = 1;
      alert(mensaje);
    },

    updateEventsAdicionales(){
      // En caso de haber agregado el adicional, se actualizan las variables de los bancos para ese adicional seleccionado
      let {start, name} = this.selectedAdicional;
      let filterAdicional = this.allAdicionales.find(adicional => adicional.start === start && adicional.name === name);
      this.selectedAdicional = JSON.parse(JSON.stringify(filterAdicional));
      this.getEstadoBancos(this.selectedAdicional);
    },

    getHorariosAdicionales: async function(){
      // Trae del servidor, los adicionales para la semana actual y hasta ocho días después de la fecha actual
      let cod_encrypted = this.$cookies.get("user_session");
      let codigoUser = this.$Crypto.AES.decrypt(cod_encrypted, localStorage.cdcb0830cc2dd220);
      codigoUser = codigoUser.toString(this.$Crypto.enc.Utf8);

      await this.axios.post("http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/getHorariosAdicionalesEstudiantes",
        {
          codigoUser: codigoUser,
        },
        {
          headers: {
            "Content-Type": "application/json"
          }
        })
      .then(response => {
        this.allAdicionales = this.setColorEventsAdicionales(response.data.data);
        this.filterHorariosAdicionalesByName();
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
        }else if(adicionales[i].state === false){           // state = false -> laboratorio no disponible
          adicionales[i].color = colorLight;
        }else{                                              // state -> franja con reserva registrada
          adicionales[i].color = "grey lighten-1";
          // Si el estado para un adicional es PENDIENTE o APROBADO, también se debe restringir cualquier otro evento que se encuentre en la misma franja horaria.
          if (adicionales[i].state === "PENDIENTE" || adicionales[i].state === "APROBADO"){
            let {start, state, color} = adicionales[i];
            adicionales.filter(eventAdicional => {
              if(eventAdicional.start === start){
                eventAdicional.state = state;
                eventAdicional.color = color;
              }
            })
          }
        }
      }
      return adicionales
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
    
    height: 12px;
    border-radius: 50%;
    margin-top: -5px;
    margin-left: -6.5px;
    position: absolute;
  }
  .botton >>> button{
    font-size: 0.96rem;
  }
  .v-event{
    padding-left: 4px !important;
    font-size: 13px;
  }
</style>