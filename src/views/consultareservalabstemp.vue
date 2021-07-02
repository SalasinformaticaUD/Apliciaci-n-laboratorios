<template>
  <v-container fluid>
    <HeaderLaboratorista/>
    <v-card>
      <v-card-title>
        Reservas
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          ref="form"
          append-icon="fas far-search"
          label="Search"
          single-line
          hide-details
          @keyup.enter="initialize"
        ></v-text-field>

        <v-btn color="primary" @click="initialize">Buscar</v-btn>
        <v-spacer></v-spacer>
        <v-btn color="primary" @click="reset">Reset</v-btn>

        <v-spacer></v-spacer>
      </v-card-title>

      <v-data-table
        :headers="headers"
        :items="reservasLab"
        :custom-sort="customSortTable"
        :sort-by="['fecha_adicional']"
        class="elevation-1"
        color="background"
        dark
        :search="search"
      >
        <template v-slot:top>
          <v-toolbar class="pa-0" flat dark height="90px">
            <v-toolbar-title> Consulta reservas </v-toolbar-title>
            <v-divider class="mx-4" inset vertical></v-divider>
            <v-spacer></v-spacer>
            <v-text-field
              v-model="search"
              ref="form"
              append-icon="fas fa-search"
              label="Buscar..."
              single-line
              hide-details
              @keyup.enter="initialize"
            ></v-text-field>
            <v-btn class="ml-3" color="primary" @click="initialize">Buscar</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="reset">Reset</v-btn>
            <v-spacer></v-spacer>
          </v-toolbar>
        </template>

        <template v-slot:[`item.estado`]="{ item }">
          <v-chip :color="getColorEstado(item.estado)" dark>{{ item.estado }}</v-chip>
        </template>

        <template v-slot:[`item.actions`]="{ item }">
          <v-tooltip top nudge-bottom="10">
            <template v-slot:activator="{ on, attrs }">
              <v-icon v-bind="attrs" v-on="on" small class="mx-2" @click="showInfoReserva(item)">
                fas fa-info-circle
              </v-icon>
            </template>
            <span>Ver ficha adicional</span>
          </v-tooltip>
          <v-tooltip top nudge-bottom="10">
            <template v-slot:activator="{ on, attrs }">
              <v-icon v-bind="attrs" v-on="on" small class="mx-2" @click="deleteItem(item)">
                fas fa-trash
              </v-icon>
            </template>
            <span>Eliminar adicional</span>
          </v-tooltip> 
        </template>

        <template v-slot:[`item.reserva`]="{item}">
          <router-link :to="{name: 'consulta'}" style="color: white;">
            <span @click="gotoMonitores(item)">
              Ver adicional
            </span>
          </router-link>
        </template>

        <template v-slot:no-data>
          <v-btn color="primary" @click="initialize">Reset</v-btn>
        </template>
      </v-data-table>
    </v-card>

    <v-dialog v-model="modelCardFicha" max-width="1000px">
      <v-card dark>
        <v-card-title> Información de la reserva </v-card-title>
        <v-divider></v-divider>
        <v-card-text>
          <v-container>
            <v-row class="mt-n1">
              <v-col>
                <v-text-field v-model="infoReserva.codigo" label="Código Usuario" disabled></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="infoReserva.usuario" label="Nombre Usuario" disabled></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="infoReserva.estado" label="Estado petición" disabled></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="infoReserva.fecha_adicional" label="Fecha del adicional" disabled></v-text-field>
              </v-col>
            </v-row>
            <v-row class="mt-n4">
              <v-col>
                <v-text-field v-model="infoReserva.sala" label="Sala" disabled></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="infoReserva.hora" label="Hora" disabled></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="infoReserva.dia" label="Día" disabled></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="infoReserva.banco" label="Banco" disabled></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="infoReserva.practica" label="Practica" disabled></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="infoReserva.fecha_reserva" label="Fecha de la reserva" disabled></v-text-field>
              </v-col>
            </v-row>

            <div v-if="infoReserva.elementos && infoReserva.elementos.length>0" class="my-4">
              <v-divider></v-divider>
              <v-row no-gutters class="pa-1" align="center">
                <v-col cols="12" sm="1" class="text-sm-center font-weight-black">
                  No.
                </v-col>
                <v-col cols="12" sm="6" class="font-weight-black pl-5">
                  Elementos
                </v-col>
                <v-col cols="12" sm="3" class="text-sm-center font-weight-black">
                  Acciones
                </v-col>
                <v-col cols="12" sm="2" class="text-sm-center font-weight-black">
                  Estado elemento
                </v-col>
              </v-row>
              <v-divider></v-divider>
              <v-row no-gutters align="center">
                <v-col v-for= "(elemento,index) in infoReserva.elementos" :key="index" cols="12" sm="12">
                  <v-row no-gutters class="pa-1" align="center">
                    <v-col cols="12" sm="1" class="text-sm-center">
                      {{index+1}}
                    </v-col>
                    <v-col cols="12" sm="6" class="pl-5">
                      {{elemento.nombre}}
                    </v-col>
                    <v-col cols="12" sm="3" class="text-sm-center">
                      <v-tooltip top nudge-bottom="10">
                        <template v-slot:activator="{ on, attrs }">
                          <v-icon v-bind="attrs" v-on="on" small class="mx-2" @click="setEstadoElemento(index, elemento, 'APROBADO')"> 
                            fas fa-check-circle 
                          </v-icon>
                        </template>
                        <span> Aprobar </span>
                      </v-tooltip>
                      <v-tooltip top nudge-bottom="10">
                        <template v-slot:activator="{ on, attrs }">
                          <v-icon v-bind="attrs" v-on="on" small class="mx-2" @click="setEstadoElemento(index, elemento, 'NO APROBADO')"> 
                            fas fa-times-circle 
                          </v-icon>
                        </template>
                        <span> No Aprobar </span>
                      </v-tooltip>
                      <v-tooltip top nudge-bottom="10">
                        <template v-slot:activator="{ on, attrs }">
                          <v-icon v-bind="attrs" v-on="on" small class="mx-2" @click="deleteElemento(index)"> 
                            fas fa-trash-alt 
                          </v-icon>
                        </template>
                        <span> Eliminar </span>
                      </v-tooltip>
                    </v-col>
                    <v-col cols="12" sm="2" class="text-sm-center">
                      <v-text-field
                        dense
                        hide-details
                        label="Estado"
                        single-line
                        v-model="elemento.estado"
                        class="centered-input"
                      ></v-text-field>                    
                    </v-col>
                  </v-row>
                  <v-divider></v-divider>
                </v-col>
              </v-row>
            </div>
            <div v-else class="my-5">
              <v-row justify="center">
                <v-col cols="12" sm="5">
                  <v-alert outlined text class="text-center">No hay elementos registrados</v-alert>
                </v-col>
              </v-row>
            </div>
            <v-row no-gutters>
              <v-textarea
              v-model="infoReserva.observacionesGenerales"
              label="Observaciones adicionales"
              auto-grow
              solo
              rows="2"
              row-height="30"
              outlined>
              </v-textarea>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-row class="justify-center mb-1 mt-n12">
            <v-col cols="12" sm="3" class="text-sm-center">
              <v-btn color="green" @click="saveEstadoReserva('APROBADO')"> Aprobar </v-btn>
            </v-col>
            <v-col cols="12" sm="4" class="text-sm-center">
              <v-btn color="primary" @click="saveEstadoReserva('CANCELADO')"> Cancelar </v-btn>
            </v-col>          
            <v-col cols="12" sm="4" class="text-sm-center">
              <v-btn color="orange" @click="saveEstadoReserva('PENDIENTE')"> Pendiente </v-btn>
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
  data: () => ({
    headers: [
      { text: "Código", value: "codigo", sortable: false},
      { text: "Nombre del estudiante", value: "usuario"},
      { text: "Fecha adicional", value: "fecha_adicional"},
      { text: "Hora", value: "hora", sortable: false},
      { text: "Día", value: "dia"},
      { text: "Laboratorio", value: "sala"},
      { text: "Banco", value: "banco", sortable: false, align: "center"},
      { text: "Estado de la petición", value: "estado", align: "center"},
      { text: "Acción", value: "actions", sortable: false, align: "center"},
      { text: "Reserva", value: "reserva", align: "center"}
    ],

    modelCardFicha: false,

    infoReserva: {},
    search: "",
    
    reservasLab: [],
    indexReserva: null,
    
    agregarUbicacionIndex: -1,
    agregarUbicacionItem: {},

    sala: '',
    hora: '',
    fecha_adicional:'',
    banco:'',
    aprobar:'',

    weekdaysString: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],
  }),

  watch: {
  },

  created(){
    this.initialize();
  },

  methods:{
    
    initialize() {
      this.reservasLab = [];
      this.buscar();
    },

    customSortTable(adicionales, key, isDescending){      
      adicionales.sort((a,b) => {
        if(key[0]==='dia'){
          return this.sortByDay(a[key], b[key], isDescending[0]);
        }
        if(key[0]==='fecha_adicional' || key[0]==='fecha_reserva'){
          return this.sortByDate(a[key], b[key], isDescending[0]);
        }
        if(key[0]==='sala' || key[0]==='estado' || key[0]==='usuario'){
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
      return b.toLowerCase().localeCompare(a.toLowerCase());      
    },

    reset () {
      this.search="";
      this.$refs.form.reset();
      this.initialize();
    },

    getColorEstado(estado) {
      if (estado == "APROBADO") return "green";
      else if (estado == "PENDIENTE") return "orange";
      else if (estado == "CANCELADO") return "red";
    },

    showInfoReserva(reserva){
      this.indexReserva = this.reservasLab.indexOf(reserva);
      this.infoReserva = JSON.parse(JSON.stringify(reserva));
      this.modelCardFicha = true;
    },

    setEstadoElemento(index, elemento, estado){
      elemento.estado = estado;
      this.$set(this.infoReserva.elementos, index, elemento);
    },

    deleteElemento(index){
      this.infoReserva.elementos.splice(index,1);
    },

    gotoMonitores(adicional){
      console.log(adicional);
    },

    mail(infoReserva){
      this.axios.post("http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/send_mail",
        {
          usuario: infoReserva.usuario,
          fecha_adicional: infoReserva.fecha_adicional,
          laboratorio: infoReserva.sala,
          hora: infoReserva.hora,
          opcion: this.aprobar,
          
          revisionElementos: this.revisionElementos,
          elementos: this.infoReserva.elemento,
        },
        {
          headers: {
            "Content-Type": "application/json"
          }
      })
      .then(response => {
        let {mensaje} = response.data;
        console.log(mensaje);
      })
      .catch(error => {
      alert(error);
    });      
    },
  
    asistencia(item,opc) {
      let objeto = this;

      if (opc){
        this.aprobar='SI';
      }else{
        this.aprobar='NO';
      }

      
      console.log("ASISTIÓ??");
      console.log(this.aprobar);

      var confirmacion = confirm("¿Esta seguro que el usuario "+this.aprobar+" asistió?");

      if (confirmacion) {

        const index = this.reservasLab.indexOf(item);
        //  this.agregarUbicacionItem = Object.assign({}, item);        
      
        this.hora = this.reservasLab[index].hora;
        this.sala = this.reservasLab[index].sala;
        this.fecha_adicional = this.reservasLab[index].fecha_adicional;
        this.banco = this.reservasLab[index].banco;
      
        console.log(index, this.sala);

        
          this.axios
            .post(
              "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/asistenciareserva",
              {
                fecha_adicional: this.fecha_adicional,
                sala: this.sala,
                hora: this.hora,
                banco: this.banco,
                aprobar: this.aprobar
              },
              {
                headers: {
                  "Content-Type": "application/json"
                }
              }
            )
            .then(function(response) {
              var respuesta = response.data.mensaje;
              var status = response.data.status;
              if (status == "1") {
                alert(respuesta);
                objeto.reservasLab.splice(index, 1);
              }
            })
            .catch(function(error) {
            alert(error);
          });      
      }
    },

    deleteItem(adicional){
      let confirmacion = confirm("¿Esta seguro de eliminar este laboratorio?");
      console.log(adicional);

      if (confirmacion){
        let {sala, banco, fecha_adicional, hora, codigo} = adicional;
        let index = this.reservasLab.indexOf(adicional);
        this.axios.post("http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/borrarreserva",
          {
            codigo: codigo,
            sala: sala,
            banco: banco,
            fecha_adicional: fecha_adicional,
            hora: hora
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          })
        .then(response => {
          let {mensaje, status} = response.data;
          if (status == 1){
            this.reservasLab.splice(index, 1);
            alert(mensaje);
          }
        })
        .catch(error => {
          alert(error);
        });
      }
    },

    buscar(){
      this.axios.get("http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/buscarreservalabo",
        {
          headers: {
            "Content-Type": "application/json"
          }
        })
      .then(response => {
        let {status, data, mensaje} = response.data;
        if (status == 1){
          this.reservasLab = data;
        }else{
          alert(mensaje);
        }
      })
      .catch(error => {
        this.output = error;
      });
    },

    saveEstadoReserva(newEstado){
      let confirmacion = confirm("¿Esta seguro de marcar este laboratorio como " + newEstado + "?");

      if(confirmacion){
        let {hora, sala, fecha_adicional, banco, elementos, observacionesGenerales} = this.infoReserva;
      
        this.axios.post("http://" + this.$serverURI + ":" + this.$serverPort + "/Usuario/editarReserva",
          {
            datos: {hora, sala, fecha_adicional, banco, elementos, observacionesGenerales},
            newEstado: newEstado,
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          })
        .then(response => {
          let {status, mensaje} = response.data;
          if (status == 1) {
            this.reservasLab.splice(this.indexReserva, 1);
            alert(mensaje);
            this.modelCardFicha = false;
            if(newEstado == "APROBADO" || newEstado == "CANCELADO"){
              // this.mail(this.infoReserva);
            }
          }else{
            alert(mensaje);
          }
        })
        .catch(error => {
          alert(error);
        });
      }
    },

  }
};
</script>

<style scoped>
    .centered-input >>> input {
      text-align: center
    }
</style>