<template>
  <v-container fluid>
    <Headerestudiantes />

    <v-row class="mt-8 mb-4 mx-n2" justify="center">
      <v-col cols="12" sm="9" lg="3" order-lg="-1" order-md="2">
        <v-sheet tile max-height="110px" min-height="50px" class="rounded-t-xl">
          <v-row no-gutters align="center" justify="center" v-if="$refs.calendarMonitores" class="py-3">
            <v-col cols="12" sm="3" align-self="center" align="center">
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
            <v-col cols="12" sm="6" align="center" class="text-h6">
              {{ formatTitle($refs.calendarMonitores.title) }} 
              <br>
              Semana {{weekNumberCalendar}}
            </v-col>    
            <v-col cols="12" sm="3" align-self="center" align="center">
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
        </v-sheet>
        <v-sheet>
          <v-calendar 
            ref="calendarMonitores"
            v-model="modelCalendar"
            type="day"
            color = "primary"
            interval-minutes = "120"
            first-time = "06:00"
            interval-count = "7"
            :interval-height = "70"
            :show-interval-label="showIntervalLabel"
            :interval-format="intervalFormat" 
            :short-weekdays="false"
            :events = "calendarHorariosAdicionales"
            class="botton"
            @click:event="clickInHorarioAdicional"
          >
            <template v-slot:day-body="{ date }">
              <div
                class="v-current-time"
                :style="{ top: nowY, width: dateNow === date ? '100%' : '0%' }"
              ></div>
              <div
                class="v-current-time2"
                :style="{ top: nowY, width: dateNow === date ? '12px': '0px'}"
              ></div>
            </template>
          </v-calendar>
        </v-sheet>
        <v-sheet tile min-height="50px" class="rounded-b-xl">
        </v-sheet>
      </v-col>

      <v-col cols="12" sm="9" v-if="cardInfoLaboratorio" order-lg="2" order-md="-1">  
        <v-row class="mt-0" justify="center" align="start">
          <v-expand-x-transition appear>
            <v-card class="rounded-xl mx-5" width="100%">
              <v-card-title class="text-h5">
                Información del laboratorio
              </v-card-title>
              <v-card-subtitle class="text-subtitle-1">
                <v-row no-gutters class="mt-4" justify="center">
                  <v-col cols="12" sm="4">
                    Sala: {{queryLaboratorioAdicional}}
                  </v-col>
                  <v-col cols="12" sm="3">
                    Fecha: {{queryFechaAdicional}}
                  </v-col>
                  <v-col cols="12" sm="3" offset="1">
                    Horario: {{queryHoraAdicional}}:00 - {{queryHoraAdicional+2}}:00
                  </v-col>
                </v-row>
                <v-row no-gutters class="mt-2" justify="center">
                  <v-col cols="12" sm="4">
                    Bancos habilitados: {{infoBancosLab.habilitados}}
                  </v-col>
                  <v-col cols="12" sm="3">
                    Bancos aprobados: {{infoBancosLab.reservados}}
                  </v-col>
                  <v-col cols="12" sm="3"  offset="1">
                    Bancos pendientes: {{infoBancosLab.pendientes}}
                  </v-col>
                </v-row>
              </v-card-subtitle>
              <v-card-text v-if="displayTableLab===true" class="mt-5">
                <v-divider></v-divider>
                <v-data-table
                  :headers="headers"
                  :items="selectedLabAdicional"
                  hide-default-footer
                >
                  <template v-slot:[`item.estado`]="{ item }">
                    <v-chip :color="getColorChips(item.estado)" dark>{{ item.estado }}</v-chip>
                  </template>
                  <template v-slot:[`item.asistencia`]="{ item }">
                    <v-chip v-if="item.asistencia=='PENDIENTE'" color="orange" dark>{{ item.asistencia }}</v-chip>
                    <v-chip v-if="item.asistencia=='SI'" color="success" dark class="px-4">
                      SI 
                      <v-icon right> fas fa-check-circle </v-icon>
                    </v-chip>
                    <v-chip v-if="item.asistencia=='NO'" color="error" dark>
                      NO 
                      <v-icon right> fas fa-times-circle </v-icon>
                    </v-chip>
                  </template>
                  <template v-slot:[`item.actions`]="{ item }">
                    <v-btn 
                      @click="showDialogFichaAdicional(item)"
                      small 
                      icon
                      >
                      <v-icon class="mr-2">
                        fas fa-edit
                      </v-icon>
                    </v-btn>
                  </template>                
                </v-data-table>        
                <v-divider></v-divider>                   
              </v-card-text>
              <v-card-text v-if="displayTableLab===false" class="mt-8">
                <v-row justify="center" class="my-3">
                  <v-alert type="success" outlined prominent elevation="5">
                    No hay adicionales registrados para esta franja horaria.
                  </v-alert>
                </v-row>
              </v-card-text>
              <v-card-actions v-if="displayTableLab===true">
                <v-row no-gutters justify="center" class="my-3">
                  <v-col cols="12" sm="6">
                  <v-btn block color="primary" dark @click="showAsistenciaAdicional()" large>
                    Asistencia del laboratorio
                  </v-btn>
                  </v-col>
                </v-row>
              </v-card-actions>
            </v-card>
          </v-expand-x-transition>
        </v-row>
      </v-col>
      <v-col cols="12" sm="9" align-self="center" v-if="cardInfoLaboratorio===false" order-lg="2" order-md="-1">
        <v-row class="mt-0" justify="center">
          <v-card class="rounded-xl mx-5" width="60%">
            <v-card-text>
              <div class="text-h6">
                Seleccione uno de los horarios adicionales para revisar la información del laboratorio.
              </div>
              <div class="text-subtitle-2 mt-3">
                <ul>
                  <li>
                    Por favor comunique a un laboratorista en caso de que un estudiante tenga el estado del adicional como PENDIENTE.
                  </li>
                  <li>
                    No olvide firmar la asistencia para cada estudiante del laboratorio.
                  </li>
                </ul>
              </div>
            </v-card-text>
          </v-card>
        </v-row>
      </v-col>
    </v-row>

    <v-dialog v-model="modelUserFichaAdicional" max-width="700px">
      <v-card>
        <v-card-title>
          <span class="text-h5">Ficha de laboratorio</span>
        </v-card-title>
        <v-alert v-if="msgInfoFichaAdicional.length>0" type="warning" color="red" class="mx-10 mt-2 mb-5 text-subtitle-1" outlined prominent>
          <ul>
            <li>
              {{msgInfoFichaAdicional}}
            </li>
          </ul>
        </v-alert>
        <v-divider></v-divider>
        <v-card-text>
          <v-container>
            <v-row class="mt-n1">
              <v-col cols="12" sm="8">
                <v-text-field
                  v-model="selectedUserLab.usuario"
                  disabled
                  label="Nombre del estudiante"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="selectedUserLab.codigo"
                  disabled
                  label="Código del estudiante"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row class="mt-n6">
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="selectedUserLab.fecha_adicional"
                  disabled
                  label="Fecha del adicional"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="selectedUserLab.sala"
                  disabled
                  label="Laboratorio adicional"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="2">
                <v-text-field
                  v-model="selectedUserLab.hora"
                  disabled
                  label="Hora"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="2">                      
                <v-text-field
                  v-model="selectedUserLab.banco"
                  disabled
                  label="No. Banco"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row class="mt-n6">
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="selectedUserLab.practica"
                  disabled
                  label="Nombre de la práctica"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="selectedUserLab.estado"
                  disabled
                  label="Estado del adicional"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="selectedUserLab.asistencia"
                  disabled
                  label="Asistencia"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row class="pb-2 ma-2 mt-n2" align="center" align-content="center">
              <v-col cols="12" sm="10">
                <v-text-field
                  label="Ingrese un elemento adicional (máx. 10)"
                  hide-details="auto"
                  dense
                  @keyup.enter="addElementoAdicional()"
                  v-model = "inputElemento"
                  :disabled="!estadoUserLab"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="2" align-self="center" class="text-right">
                <v-btn :disabled="!estadoUserLab" color="primary" :dark="estadoUserLab" small block @click="addElementoAdicional()">
                  Agregar
                </v-btn>
              </v-col>
            </v-row>      
            <div v-if="selectedUserLab.elementos && selectedUserLab.elementos.length>0">
              <v-divider></v-divider>
              
              <v-row no-gutters class="pa-1" align="center">
                <v-col cols="12" sm="1" class="text-sm-center font-weight-black">
                  No.
                </v-col>
                <v-col cols="12" sm="5" class="font-weight-black pl-5">
                  Elementos
                </v-col>              
                <v-col cols="12" sm="4" class="font-weight-black pl-5">
                  Observaciones
                </v-col>                          
                <v-col cols="12" sm="2" class="text-sm-center font-weight-black">
                  No. Placa
                </v-col>
              </v-row>

              <v-divider></v-divider>

              <v-row no-gutters align="center">
                <v-col v-for= "(elemento,index) in selectedUserLab.elementos" :key="index" cols="12" sm="12">
                  <v-row no-gutters class="pa-1" align="center">
                    <v-col cols="12" sm="1" class="text-sm-center">
                      {{index+1}}.
                    </v-col>
                    <v-col></v-col>
                    <v-col cols="12" sm="5" class="pl-5">
                      {{elemento.nombre}}
                    </v-col>
                    <v-col cols="12" sm="4" class="pl-5">
                      {{elemento.estado}}
                    </v-col>
                    <v-col cols="12" sm="2" class="text-sm-center pl-5 pr-5">
                      <v-text-field
                        dense
                        class="centered-input"
                        hide-details
                        label="# Placa"
                        single-line
                        :disabled="!estadoUserLab"
                        v-model="elemento.placa"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-divider></v-divider>  
                </v-col>                  
              </v-row>
            </div>            
            <v-row no-gutters align="center" class="mt-5" v-if="selectedUserLab.observacionesGenerales && selectedUserLab.observacionesGenerales.length>0">   
              <v-col cols="12" sm="12">
                <v-text-field
                  v-model="selectedUserLab.observacionesGenerales"
                  :disabled="true"
                  label="Observaciones Generales"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-row class="justify-center mb-1 mt-n4">
            <v-col cols="12" sm="6">
              <v-btn :disabled="!estadoUserLab" color="primary" :dark="estadoUserLab" @click="saveFichaAdicional()" large block>
                Guardar los cambios
              </v-btn>
            </v-col>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogUsersAsistencia" max-width="800px">
      <v-card>
        <v-card-title>
          <span class="headline">Verificación de la asistencia en el laboratorio</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-divider></v-divider>
            <v-row no-gutters align="center">
              <v-col cols="12" sm="1" class="text-sm-center font-weight-black">
                No. Banco                
              </v-col>
              <v-col cols="12" sm="3" class="text-sm-center font-weight-black">
                Estudiante
              </v-col>
              <v-col cols="12" sm="2" class="text-sm-center font-weight-black">
                Código
              </v-col>
              <v-col cols="12" sm="3" class="text-sm-center font-weight-black">
                Firma Monitor
              </v-col>
              <v-col cols="12" sm="3" class="text-sm-center font-weight-black">
                Asistencia
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-row no-gutters align="center">
              <v-col v-for= "(item,index) in infoUsersAsistencia" :key="index" cols="12" sm="12">
                <v-row no-gutters class="py-3" align="center">
                  <v-col cols="12" sm="1" class="text-sm-center">
                    {{item.banco}}
                  </v-col>
                  <v-col cols="12" sm="3" class="text-sm-center px-5">
                    {{item.usuario}}
                  </v-col>
                  <v-col cols="12" sm="2" class="text-sm-center">
                    {{item.codigo}}
                  </v-col>
                  <v-col cols="12" sm="3" class="text-sm-center px-5" v-if="item.estado">
                    {{item.monitor}}
                  </v-col>
                  <v-col cols="12" sm="6" v-else class="mb-n4 px-5">
                    <v-alert type="warning" color="red" outlined dense>
                      Estado del adicional PENDIENTE
                    </v-alert>
                  </v-col>
                  <v-col cols="12" sm="1" offset="1" class="text-sm-left ml-12" v-if="item.estado">
                    <v-btn @click="editAsistenciaBanco(index,'SI')" fab x-small :elevation="(item.asistencia == 'SI')? 10 : 0">
                      <v-icon large :color="(item.asistencia == 'SI') ? 'success':'grey lighten-1'">fas fa-check-circle</v-icon>
                    </v-btn>
                  </v-col>
                  <v-col cols="12" sm="1" class="text-sm-left" v-if="item.estado">
                    <v-btn @click="editAsistenciaBanco(index,'NO')" fab x-small :elevation="(item.asistencia == 'NO')? 10 : 0">
                    <v-icon large :color="(item.asistencia == 'NO') ? 'error':'grey lighten-1'">fas fa-times-circle</v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
                <v-divider></v-divider>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-row class = "mt-n3 ma-2" justify="center">
            <v-col cols="12" sm="6">
              <v-btn block color="primary" dark @click="saveAsistenciaLab()" large>
                Guardar Asistencia
              </v-btn>
            </v-col>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </v-container>
</template>

<script>
import Headerestudiantes from "@/components/Headerestudiantes.vue";
export default {
  components: {
    Headerestudiantes
  },
  data() {
    return {
      modelCalendar: "",
      readyCalendar: false,
      weekNumberCalendar: 22,
      calendarHorariosAdicionales: [],

      infoLabsStore:[],           //  (se trae desde vuex ./store/index.js)      

      dateNow: null,              // formato: año-mes-dia
      
      queryFechaAdicional: null,
      queryLaboratorioAdicional: null,
      queryHoraAdicional: null,

      selectedLabAdicional: [],

      infoBancosLab:{
        habilitados: 0,           // Cantidad de bancos habilitados para reserva
        reservados: 0,            // Cantidad de bancos con reserva aprobada
        pendientes: 0,            // Cantidad de bancos con reserva pendiente
      },

      cardInfoLaboratorio: false,
      displayTableLab: false,
      
      headers: [
        {text: "No. Banco",           value: 'banco',      sortable: false,  align: 'center'},
        {text: "Estudiante",          value: 'usuario',    sortable: false,  align: 'center'},
        {text: "Código",              value: 'codigo',     sortable: false,  align: 'center'},
        {text: "Estado",              value: 'estado',     sortable: false,  align: 'center'},
        {text: "Asistencia",          value: 'asistencia', sortable: false,  align: 'center'},
        {text: "Ficha del adicional", value: "actions",    sortable: false,  align: 'center'},
      ],      

      dialogUsersAsistencia: false,
      infoUsersAsistencia: [],

      modelUserFichaAdicional: false,
      selectedUserLab: {},
      estadoUserLab: false,
      msgInfoFichaAdicional: "",
      inputElemento:"",

      nameUserMonitor : "",
    }
  },

  created(){
    this.dateNow = this.conversionDate();
    this.infoLabsStore = this.$store.getters.infoLabs;
    this.nameUserMonitor = localStorage.usuario;
  },

  mounted(){   
    this.getHorariosAdicionales();
    this.readyCalendar = true;
  },

  watch:{
  },

  computed: {
    cal () {
      // Retorna el objeto $refs.calendarMonitores cuando el componente v-calendar se ha renderizado
      return this.readyCalendar ? this.$refs.calendarMonitores : null
    },
    nowY () {
      // Luego de renderizar el v-calendar, retorna la hora actual para hacer la línea del day-body
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
      // Esta función toma una fecha dada la función Date() de JS y retorna una fecha en el formato año-mes-dia. Esto se realiza para evitar utilizar la función Date().toISOString ya que esta última no tiene en cuenta la zona horaria y en horas de la noche toma la fecha como la del dia siguiente. 
      let date = new Date();
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
    changeWeek(val){
      if(val==0){
        this.$refs.calendarMonitores.prev();
      }else{
        this.$refs.calendarMonitores.next();
      }
    },
    clickInHorarioAdicional({event}){
      // Para el evento seleccionado, revisa la información de los bancos
      let {start, name, hour, bancos} = event;
      this.queryFechaAdicional = this.formatDate(start.split(" ")[0]);
      this.queryLaboratorioAdicional = name;
      this.queryHoraAdicional = hour;

      this.infoBancosLab = {
        habilitados: bancos.length - bancos.filter(banco => banco === "No Disponible").length,
        reservados:  bancos.filter(banco => banco === "Reservado").length,
        pendientes:  bancos.filter(banco => banco === "Pendiente").length,
      }
      
      if(this.infoBancosLab.reservados>0 || this.infoBancosLab.pendientes>0){
        this.getReservasLaboratorio();
      }else{
        this.cardInfoLaboratorio = true;
        this.displayTableLab = false;
      }
    },
    addElementoAdicional(){
      // Valida que el elemento agregado en el input del adicional no sea un espacio en blanco o vacío
      if (this.inputElemento.length>0){
        if(this.inputElemento.replace(/ /g, "").length>0){
          if(this.selectedUserLab.elementos.length<10){
            this.selectedUserLab.elementos.push({
              nombre: this.inputElemento,
              estado: "PENDIENTE",              
              placa: ""
            });
          }else{
            alert("Solo se permite un máximo 10 elementos.");
          }
        }
      }            
      this.inputElemento = "";
    },

    getColorChips(estado) {
      if (estado == "APROBADO") return "green";                  // Identifica el color para los v-chip del  
      else if (estado == "PENDIENTE") return "orange";           // estado de la asistencia en el v-data-table
      else if (estado == "CANCELADO") return "red";
    },

    showDialogFichaAdicional(adicional){
      // Esta función copia el objeto del adicional seleccionado para hacer la ficha del laboratorio. 
      let filterUserLab = this.selectedLabAdicional.find(item => item.banco == adicional.banco);
      this.selectedUserLab = JSON.parse(JSON.stringify(filterUserLab));
      
      let {estado, asistencia} = this.selectedUserLab;
      
      this.msgInfoFichaAdicional = "";
      if (estado==="APROBADO" && asistencia==="PENDIENTE"){
          this.msgInfoFichaAdicional = `La asistencia del estudiante se encuentra ${asistencia}.`
      }
      if(estado!=="APROBADO"){
        this.msgInfoFichaAdicional = `El estado del adicional se encuentra ${estado}.`;
      } 

      this.estadoUserLab = (estado=="APROBADO");
      this.modelUserFichaAdicional = true;
    },

    showAsistenciaAdicional(){
      // Se recorre cada uno de los bancos y se toma en un vector auxiliar (infoUsersAsistencia) la informacion a mostrar y a editar en el v-dialog de asistencia
      this.infoUsersAsistencia = this.selectedLabAdicional.map(function(userLab){
        let {banco, usuario, codigo, asistencia, monitor} = userLab;
        let estado = (userLab.estado === "APROBADO");
        return {banco, usuario, codigo, asistencia, monitor, estado}
      });
    
      this.dialogUsersAsistencia = true;
    },  

    editAsistenciaBanco(index,state){
      // Se modifica la asistencia con el state enviado (SI o NO). Se adjunta la firma del monitor. 
      // Se utiliza $set ya que es la forma de actualizar un array conservando la reactividad de vue

      let temp = this.infoUsersAsistencia[index];
      temp.asistencia = state;
      temp.monitor = this.nameUserMonitor;

      this.$set(this.infoUsersAsistencia, index, temp); 
    },

    saveAsistenciaLab(){
      // Se recorre registrosLaboratorio y se modifican con la información de asistencia y el nombre del monitor
      let confirmacion = confirm("¿Esta seguro de guardar estos cambio?");
      if (confirmacion) {
        let lengthBancos = this.selectedLabAdicional.length;
        for(let i=0; i<lengthBancos; i++){
          let infoBanco = this.infoUsersAsistencia.find(item => item.banco == this.selectedLabAdicional[i].banco)
          this.selectedLabAdicional[i].asistencia = infoBanco.asistencia;
          this.selectedLabAdicional[i].monitor = infoBanco.monitor;
        }
        this.saveFichaAdicionalServer();
      }
    },

    saveFichaAdicional(){
      let confirmacion = confirm("¿Esta seguro de guardar estos cambio?");
      if (confirmacion) {
        // Se toma la información editada en la ficha de laboratorio (selectedUserLab) y se sobreescribe en la posicion dada de los registros de laboratorio
        let filterBanco = this.selectedLabAdicional.find(item => item.banco == this.selectedUserLab.banco);
        let indexItem = this.selectedLabAdicional.indexOf(filterBanco);
        this.selectedLabAdicional[indexItem] = JSON.parse(JSON.stringify(this.selectedUserLab));
        this.saveFichaAdicionalServer();
      }
    },

    saveFichaAdicionalServer(){
      // En el backend se manda de nuevo la información de todos los bancos y se guarda (esto se hace para utilizar la misma función tanto para la asistencia como para la edicion de elementos de un solo banco)
      this.axios.post("http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/editarAdicionalesMonitor",
        {
          datos: this.selectedLabAdicional,
        },
        {
          headers: {
            "Content-Type": "application/json"
          }
        })
      .then(response => {
        let {status, mensaje} = response.data;
        if (status === 1) {
          alert(mensaje);
          this.selectedUserLab = {};
          this.modelUserFichaAdicional = false;
          this.infoUsersAsistencia = [];
          this.dialogUsersAsistencia = false;
        }
      })
      .catch(error => {
        alert(error);
      });
    },

    getReservasLaboratorio(){
      this.axios.post("http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/getReservasLaboratorio",
        {
          fecha_laboratorio: this.queryFechaAdicional,
          sala_laboratorio: this.queryLaboratorioAdicional,
          hora_laboratorio: this.queryHoraAdicional
        },
        {
          headers: {
            "Content-Type": "application/json"
          }
        })
      .then(response => {
        let {status, data} = response.data;
        this.selectedLabAdicional = [];
        if (status === 1){
          let sortBancos = data.map(item => item.banco).sort((a,b)=>(a-b));
          let lengthBancos = sortBancos.length;
          for(let i=0; i<lengthBancos; i++){
            this.selectedLabAdicional[i] = data.find(item => item.banco === sortBancos[i]);
          }
          this.displayTableLab = true;
        }else{
          this.displayTableLab = false;
        }
        this.cardInfoLaboratorio = true;
      })
      .catch(error => {
        alert(error);
      });
    },
    getHorariosAdicionales(){
      this.axios.get("http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/getHorariosAdicionales",
        {
          headers: {
            "Content-Type": "application/json"
          }
        })
      .then(response => {
        let {data} = response.data;
        this.calendarHorariosAdicionales = [];
        if (data.length > 0){
          this.setColorAdicionales(data);
        } 
      })
      .catch(function(error) {
        alert("Ha ocurrido un error en el servidor. Por favor intentar de nuevo en un momento.")
      });
    },
    setColorAdicionales(adicionales){        
      let lengthAdicionales = adicionales.length;
      for (let i=0; i<lengthAdicionales; i++){        
        let {color, colorLight} = this.infoLabsStore.find(item => item.name == adicionales[i].name);
        if(adicionales[i].state){
          adicionales[i].color = color;
        }else{
          adicionales[i].color = colorLight;
        }
      }
      this.calendarHorariosAdicionales = adicionales;
    },
  },
};
</script>


<style scoped>
  .botton >>> button{
    font-size: 1.2rem;
  }
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
  .scroll {
    overflow-y: scroll
  }
  .centered-input >>> input {
    text-align: center
  }
</style>