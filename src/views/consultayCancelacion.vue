<template>
  <v-container fluid>
    <Headerestudiantes />

    <v-row class="my-4" justify="center">
      <v-col v-if="modelDataTable">
        <v-data-table
          :headers="headers"
          :items="reservasUser"
          :custom-sort="customSortTable"
          :sort-by="['fecha_adicional']"
          class="elevation-1"
          color="background"
          :search="filterDataTable"
        >
          <template v-slot:top>
            <v-toolbar class="pa-0" flat height="90px">
              <v-toolbar-title> Consulta de horarios adicionales </v-toolbar-title>
              <v-divider class="mx-4" inset vertical></v-divider>
              <v-spacer></v-spacer>
              <v-spacer></v-spacer>
              <v-spacer></v-spacer>
              <v-text-field
                v-model="filterDataTable"
                label="Buscar adicionales por..."
                clearable
                single-line
                hide-details
                clear-icon="fas fa-times"
                prepend-icon="fas fa-search"
              ></v-text-field>
            </v-toolbar>
            <v-divider></v-divider>
          </template>

          <template v-slot:[`item.actions`]="{ item }">
            <v-tooltip top nudge-bottom="10">
              <template v-slot:activator="{ on, attrs }">
                <v-btn 
                  v-bind="attrs"
                  v-on="on"
                  @click="clickInFichaAdicional(item)"
                  :disabled="item.estado==='CANCELADO'" 
                  icon
                >
                  <v-icon class=""> fas fa-edit </v-icon>
                </v-btn>
              </template>
              <span>Ver ficha adicional</span>
            </v-tooltip> 
            <v-tooltip top nudge-bottom="10" v-if="item.flagCancelar">
              <template v-slot:activator="{ on, attrs }" v-if="item.flagCancelar">
                <v-btn 
                  v-bind="attrs"
                  v-on="on"
                  @click="cancelarAdicional(item)"
                  icon
                >
                  <v-icon class=""> fas fa-trash </v-icon>
                </v-btn>
              </template>
              <span>Cancelar el adicional</span>
            </v-tooltip> 
          </template>

          <template v-slot:[`item.estado`]="{ item }">
            <v-chip :color="getColorChips(item.estado)" dark> {{ item.estado }} </v-chip>
          </template>

          <template v-slot:[`item.asistencia`]="{ item }">
            <v-chip v-if="item.asistencia=='CANCELADO'" :color="getColorChips(item.asistencia)" dark>{{ item.asistencia }}</v-chip>
            <v-chip v-if="item.asistencia=='PENDIENTE'" :color="getColorChips(item.asistencia)" dark>{{ item.asistencia }}</v-chip>
            <v-chip v-if="item.asistencia=='SI'" color="success" dark class="px-4">
              SI 
              <v-icon right> fas fa-check-circle </v-icon>
            </v-chip>
            <v-chip v-if="item.asistencia=='NO'" color="error" dark>
              NO 
              <v-icon right> fas fa-times-circle </v-icon>
            </v-chip>
          </template>

          <template v-slot:no-data>
            <v-row justify="center" no-gutters class="my-3 text-subtitle-1">
              {{msgResponseServer}}
            </v-row>
            <v-row justify="center" no-gutters class="my-3">
              <v-btn color="primary" @click="getReservasUser"> Reset </v-btn>
            </v-row>
          </template>
        </v-data-table>
      </v-col>
    </v-row>

    <v-dialog v-model="modelCardFicha" max-width="700px">
      <v-card>
        <v-card-title>
          <span class="text-h5">Ficha de laboratorio</span>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text>
          <v-container>
            <v-row class="mt-n1">
              <v-col cols="12" sm="8">
                <v-text-field
                  v-model="selectedAdicional.usuario"
                  disabled
                  label="Nombre del estudiante"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="selectedAdicional.codigo"
                  disabled
                  label="Código del estudiante"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row class="mt-n6">
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="selectedAdicional.fecha_adicional"
                  disabled
                  label="Fecha del adicional"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="selectedAdicional.sala"
                  disabled
                  label="Laboratorio adicional"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="2">
                <v-text-field
                  v-model="selectedAdicional.hora"
                  disabled
                  label="Hora del adicional"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="2">                      
                <v-text-field
                  v-model="selectedAdicional.banco"
                  disabled
                  label="Banco"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row class="mt-n6">
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="selectedAdicional.practica"
                  disabled
                  label="Nombre de la práctica"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="selectedAdicional.estado"
                  disabled
                  label="Estado del adicional"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="selectedAdicional.asistencia"
                  disabled
                  label="Asistencia"
                ></v-text-field>
              </v-col>
            </v-row>
            
            <v-row class="pb-2 ma-2 mt-n2" align="center" align-content="center" v-if="selectedAdicional.flagAddElementos">
              <v-col cols="12" sm="10">
                <v-text-field
                  label="Ingrese un elemento adicional (máx. 10)"
                  hide-details="auto"
                  dense
                  @keyup.enter="addElementoAdicional()"
                  v-model = "inputElemento"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="2" align-self="center" class="text-right">
                <v-btn rounded color="primary" dark small
                @click="addElementoAdicional()"
                >Agregar</v-btn>
              </v-col>
            </v-row>      
            
            <div v-if="selectedAdicional.elementos && selectedAdicional.elementos.length>0">
              <v-divider></v-divider>

              <v-row no-gutters class="pa-1" align="center">
                <v-col cols="12" sm="1" class="text-sm-center font-weight-black">
                  No.
                </v-col>
                <v-col cols="12" sm="5" class="font-weight-black pl-5">
                  Elementos
                </v-col>
                <v-col cols="12" sm="4" v-if="selectedAdicional.flagAddElementos"></v-col>
                <v-col cols="12" sm="4" class="font-weight-black pl-5" v-else>
                  Observaciones
                </v-col>
                <v-col cols="12" sm="2" class="text-sm-center font-weight-black" v-if="selectedAdicional.flagAddElementos">
                  Eliminar
                </v-col>
                <v-col cols="12" sm="2" class="text-sm-center font-weight-black" v-else>
                  No. Placa
                </v-col>
              </v-row>

              <v-divider></v-divider>

              <v-row no-gutters align="center">
                <v-col v-for= "(elemento, index) in selectedAdicional.elementos" :key="index" cols="12" sm="12">  
                  <v-row no-gutters class="pa-1" align="center">
                    <v-col cols="12" sm="1" class="text-sm-center">
                      {{index+1}}.
                    </v-col>
                    <v-col></v-col>
                    <v-col cols="12" sm="5" class="pl-5">
                      {{elemento.nombre}}
                    </v-col>
                    <v-col cols="12" sm="4" v-if="selectedAdicional.flagAddElementos">
                    </v-col>
                    <v-col cols="12" sm="4" v-else class="pl-5">
                      {{elemento.estado}}
                    </v-col>
                    <v-col cols="12" sm="2" class="text-sm-center pl-5 pr-5" v-if="selectedAdicional.flagAddElementos">
                      <v-btn @click="deleteElementoAdicional(index)" icon x-small>
                        <v-icon> fas fa-trash-alt </v-icon>
                      </v-btn>
                    </v-col>
                    <v-col cols="12" sm="2" class="text-sm-center pl-5 pr-5" v-else>
                      <v-text-field
                        dense
                        class="centered-input"
                        hide-details
                        label="# Placa"
                        single-line
                        v-model="elemento.placa"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-divider></v-divider>
                </v-col>                  
              </v-row>
            </div>    
            <v-row no-gutters align="center" v-if="selectedAdicional.observacionesGenerales && selectedAdicional.observacionesGenerales.length > 0">
              <v-col cols="12" sm="12">
                <v-text-field
                  v-model="selectedAdicional.observacionesGenerales"
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
              <v-btn color="primary" dark @click="saveFichaAdicional()" large block>
                Guardar     
              </v-btn>
            </v-col>              
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<style scoped>
    .centered-input >>> input {
      text-align: center
    }
</style>

<script>
import Headerestudiantes from "@/components/Headerestudiantes.vue";
export default {
  components: {
    Headerestudiantes
  },
  data: () => ({
    headers: [
      { text: "Hora",                     value: "hora",            align: "center",  sortable: false},
      { text: "Dia",                      value: "dia",             align: "center",  sortable: true},
      { text: "Fecha del adicional",      value: "fecha_adicional", align: "center",  sortable: true},
      // { text: "Fecha Reserva", value: "fecha_reserva" },
      { text: "Sala",                     value: "sala",            align: "center",  sortable: true},
      { text: "Banco",                    value: "banco",           align: "center",  sortable: false},
      { text: "Estado de la petición",    value: "estado",          align: "center",  sortable: true},
      { text: "Asistencia del adicional", value: "asistencia",      align: "center",  sortable: true},
      { text: "Acciones",                 value: "actions",         align: "center",  sortable: false}
    ],

    reservasUser: [],
    msgResponseServer: "",
    modelDataTable: false,    

    modelCardFicha: false,  
    selectedAdicional: {},         
    indexSelectedAdicional: null,
    inputElemento: "",

    weekdaysString: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],

    filterDataTable: "",
  }),

  computed: {    
  },

  watch: {
  },

  mounted(){
  },

  created(){     
    this.getReservasUser();
  },

  methods: {

    customSortTable(adicionales, key, isDescending){
      adicionales.sort((a,b) => {
        if(key[0]==='dia'){
          return this.sortByDay(a[key], b[key], isDescending[0]);
        }
        if(key[0]==='fecha_adicional'){
          return this.sortByDate(a[key], b[key], isDescending[0]);
        }
        if(key[0]==='sala' || key[0]==='estado' || key[0]==='asistencia'){
          return this.sortByText(a[key], b[key], isDescending[0]);
        }
      })
      return adicionales   
    },

    sortByDay(a, b, isDescending){
      let aIndex = this.weekdaysString.indexOf(a);
      let bIndex = this.weekdaysString.indexOf(b);
      if (!isDescending){
        return aIndex - bIndex;
      }
      return bIndex - aIndex;
    },

    sortByDate(a, b, isDescending){
      let [a_day, a_month, a_year] = a.split("/");
      let aDate = new Date(a_year, a_month-1, a_day);
      let [b_day, b_month, b_year] = b.split("/");
      let bDate = new Date(b_year, b_month-1, b_day);
      if (!isDescending){
        return bDate - aDate;
      }
      return aDate - bDate;
    },

    sortByText(a, b, isDescending){
      if (!isDescending) {
        return a.toLowerCase().localeCompare(b.toLowerCase());
      }
      else {
        return b.toLowerCase().localeCompare(a.toLowerCase());
      }
    },

    clickInFichaAdicional(adicional){
      // Es posible cancelar los adicionales hasta 1 hora antes del adicional
      // Es posible agregar elementos del adicional hasta 30 minutos antes
      // flagAddElementos: true -> puede agregar elementos; false -> agregar placas elementos
      this.indexSelectedAdicional = this.reservasUser.indexOf(adicional);
      this.selectedAdicional = JSON.parse(JSON.stringify(adicional));      
      this.modelCardFicha = true;
    },
    addElementoAdicional(){
      // Valida que el elemento agregado en el input del adicional no sea un espacio en blanco o vacío
      if (this.inputElemento.length>0){
        if(this.inputElemento.replace(/ /g, "").length>0){
          if(this.selectedAdicional.elementos.length<10){
            this.selectedAdicional.elementos.push({
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

    deleteElementoAdicional(index){
      this.selectedAdicional.elementos.splice(index,1);
    },

    getColorChips(estado) {
      if (estado == "APROBADO") return "green";
      else if (estado == "PENDIENTE") return "orange";
      else if (estado == "CANCELADO") return "red";
    },

    cancelarAdicional(item) {
      var confirmacion = confirm("¿Esta seguro que desea cancelar este laboratorio?");

      if (confirmacion){
        let {sala, banco, fecha_adicional, hora, codigo} = item;
        let index = this.reservasUser.indexOf(item);
        this.axios.post("http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/cancelarAdicionalEstudiante",
          {
            datos: {sala, banco, fecha_adicional, hora, codigo},
          },
          {
            headers: {
              "Content-Type": "application/json",
              "Authorization": this.$cookies.get("jwt") ? "Bearer " + this.$cookies.get("jwt") : "",
            }
          })
          .then(response => {
            let {status, mensaje} = response.data;
            if(status === 1){
              this.updateEstadoReservaUser(index);
            }else if (response.data.status == 401) {                                
              objeto.$router.push('/');
              alert("Error de sesion");                
            }
            alert(mensaje);
          })
          .catch(error => {
          alert(error);
        });
      }
    },

    updateEstadoReservaUser(index){
      this.reservasUser[index].estado = "CANCELADO";
      this.reservasUser[index].asistencia = "CANCELADO";
      this.reservasUser[index].flagCancelar = false;
    },

    saveFichaAdicional() {
      var confirmacion = confirm("¿Esta seguro de guardar estos cambio?");
      if (confirmacion) {
        this.axios.post("http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/editarElementosAdicional",
          {
            datos: this.selectedAdicional,
          },
          {
            headers: {
              "Content-Type": "application/json",
              "Authorization": this.$cookies.get("jwt") ? "Bearer " + this.$cookies.get("jwt") : "",
            }
          })
        .then(response => {
          let {mensaje, status} = response.data;
          if (status === 1){
            this.updateFichaAdicional();
            this.modelCardFicha = false;
          }else if (response.data.status == 401) {                                
            objeto.$router.push('/');
            alert("Error de sesion");                
          }
          alert(mensaje);
        })
        .catch(error => {
          alert(error);
        });
      }
    },

    updateFichaAdicional(){
      this.$set(this.reservasUser, this.indexSelectedAdicional, this.selectedAdicional);
      this.selectedAdicional = {};
    },

    getReservasUser() {
      let token = localStorage.cdcb0830cc2dd220;
      let codigoLab = this.$Crypto.AES.decrypt(this.$cookies.get("user_session"), token);
      codigoLab = codigoLab.toString(this.$Crypto.enc.Utf8);
      this.axios.post("http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/getReservasUser",
        {
          codigo: codigoLab
        },
        {
          headers: {
            "Content-Type": "application/json",
            "Authorization": this.$cookies.get("jwt") ? "Bearer " + this.$cookies.get("jwt") : "",
          }
        }
      )
      .then(response => {
        let {data, status, mensaje} = response.data;
        if(status === 1){
          this.reservasUser = this.filterReservasByAdicional(data);
        }else if (response.data.status == 401) {                                
          objeto.$router.push('/');
          alert("Error de sesion");                
        }else{
          this.reservasUser = [];
          this.msgResponseServer = mensaje;
        }
        this.modelDataTable = true;
      })
      .catch(error => {
        alert(error);
      });
    },
    filterReservasByAdicional(reservas){
      // Determina si se deben mostrar todas las reservas o si debe filtrar un adicional segun el state de vuex
      let date = this.$store.state.date;
      let hour = this.$store.state.hour;     
      if (date === null && hour === null){
        return reservas
      }
      this.$store.state.hour = null;
      this.$store.state.date = null;
      return reservas.filter(adicional => adicional.fecha_adicional === date && adicional.hora === hour);
    },
  }
};
</script>