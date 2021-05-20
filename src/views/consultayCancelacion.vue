<template>
  <v-container fluid>
    <Headerestudiantes />
    <v-row>
      <v-col>

    <v-data-table
      :headers="headers"
      :items="usuariolab"
      sort-by="calories"
      class="elevation-1"
      color="background"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Edición y eliminación</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>

          <v-dialog v-model="dialogFicha" max-width="700px">
            <v-card>
              <v-card-title>
                <span class="headline">Ficha de laboratorio</span>
              </v-card-title>
              <v-divider></v-divider>
              <v-card-text>
                <v-container>
                  <v-row class="mt-n1">
                    <v-col cols="12" sm="6">
                      <v-text-field
                        v-model="infoItem.usuario"
                        :disabled="true"
                        label="Nombre del estudiante"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="3">
                      <v-text-field
                        v-model="codigoLab"
                        :disabled="true"
                        label="Código del estudiante"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="3">
                      <v-text-field
                        v-model="infoItem.fecha_adicional"
                        :disabled="true"
                        label="Fecha del adicional"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row class="mt-n6">
                    <v-col cols="12" sm="3">
                      <v-text-field
                        v-model="infoItem.sala"
                        :disabled="true"
                        label="Laboratorio adicional"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="3">
                      <v-text-field
                        v-model="infoItem.hora"
                        :disabled="true"
                        label="Hora del adicional"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="3">                      
                      <v-text-field
                        v-model="infoItem.banco"
                        :disabled="true"
                        label="Banco del laboratorio"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="3">
                      <v-text-field
                        v-model="infoItem.estado"
                        :disabled="true"
                        label="Estado del adicional"
                      ></v-text-field>
                    </v-col>
                  </v-row>

                  <v-row class="pb-2 ma-2 mt-n2" align="center" align-content="center" v-if="fichaEdit">
                    <v-col cols="12" sm="10">
                      <v-text-field
                        label="Ingrese un elemento adicional"
                        hide-details="auto"
                        dense
                        @keyup.enter="agregarElementoAdicional()"
                        v-model = "inputElemento"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="2" align-self="center" class="text-right">
                      <v-btn rounded color="primary" dark small
                      @click="agregarElementoAdicional()"
                      >Agregar</v-btn>
                    </v-col>
                  </v-row>      

                  <v-divider></v-divider>
                  <v-row no-gutters class="pa-1" align="center" v-if="fichaEdit">
                    <v-col cols="12" sm="1" class="text-sm-center font-weight-black">
                      No.
                    </v-col>
                    <v-col></v-col>
                    <v-col cols="12" sm="8" class="font-weight-black">
                      Elementos
                    </v-col>
                    <v-col cols="12" sm="2" class="text-sm-center font-weight-black">
                      Eliminar
                    </v-col>
                  </v-row>
                  <v-row no-gutters align="center" v-if="fichaEdit">
                    <v-col v-for= "(itemElemento,index) in infoItem.elemento" :key="index" cols="12" sm="12">
                      <v-divider></v-divider>  
                      <v-row no-gutters class="pa-1" align="center">
                        <v-col cols="12" sm="1" class="text-sm-center">
                          {{index+1}}.
                        </v-col>
                        <v-col></v-col>
                        <v-col cols="12" sm="8">
                          {{itemElemento}}
                        </v-col>
                        <v-col cols="12" sm="2" class="text-sm-center">
                          <v-btn small @click="infoItem.elemento.splice(index,1)" icon>
                            <v-icon> fas fa-trash-alt </v-icon>
                          </v-btn>
                        </v-col>
                      </v-row>
                    </v-col>                  
                  </v-row>

                  <v-row no-gutters class="pa-1" align="center" v-if="fichaPlacas">
                    <v-col cols="12" sm="1" class="text-sm-center font-weight-black">
                      No.
                    </v-col>
                    <v-col></v-col>
                    <v-col cols="12" sm="6" class="font-weight-black">
                      Elementos
                    </v-col>              
                    <v-col cols="12" sm="2" class="font-weight-black">
                      Observaciones
                    </v-col>                          
                    <v-col cols="12" sm="2" class="text-sm-center font-weight-black">
                      No. Placa
                    </v-col>
                  </v-row>
                  <v-row no-gutters align="center" v-if="fichaPlacas">
                    <v-col v-for= "(item,index) in infoItem.elemento" :key="index" cols="12" sm="12">
                      <v-divider></v-divider>  
                      <v-row no-gutters class="pa-1" align="center">
                        <v-col cols="12" sm="1" class="text-sm-center">
                          {{index+1}}.
                        </v-col>
                        <v-col></v-col>
                        <v-col cols="12" sm="6">
                          {{item}}
                        </v-col>
                        <v-col cols="12" sm="2">
                          {{infoItem.estadoElemento[index]}}
                        </v-col>
                        <v-col cols="12" sm="2" class="text-sm-center pl-5 pr-5">
                          <v-text-field
                            dense
                            class="centered-input"
                            hide-details
                            label="# Placa"
                            single-line
                            v-model = "placasElementos[index]"
                          ></v-text-field>
                        </v-col>
                      </v-row>
                    </v-col>                  
                  </v-row>
                  <v-row no-gutters align="center" v-if="fichaPlacas">
                    <v-col cols="12" sm="12" v-if="infoItem.observacionesGenerales.length > 0">
                      <v-text-field
                        v-model="infoItem.observacionesGenerales"
                        :disabled="true"
                        label="Observaciones Generales"
                      ></v-text-field>
                    </v-col>
                  </v-row>

                  <v-divider></v-divider>  
                </v-container>
                <v-card-actions v-if="fichaEdit">
                  <v-row class="ma-3 justify-end">
                    <v-btn rounded color="primary" dark @click="guardarFichaEdit()" small>
                      Guardar     
                    </v-btn>
                  </v-row>
                </v-card-actions>
                <v-card-actions v-if="fichaPlacas">
                  <v-row class="ma-3 justify-end">
                    <v-btn rounded color="primary" dark @click="guardarFichaPlacas()" small>
                      Guardar     
                    </v-btn>
                  </v-row>
                </v-card-actions>
              </v-card-text>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>

      <template v-slot:[`item.actions`]="{ item }">
        <v-btn 
          @click="fichaItem(item)"
          :disabled="item.estado=='CANCELADO'?true:false" 
          small 
          icon
          >
          <v-icon class="mr-2">
            fas fa-edit
          </v-icon>
        </v-btn>
        <v-btn 
          @click="cancelarAdicional(item)" 
          :disabled="item.estado=='CANCELADO'?true:false" 
          small 
          icon
        >
          <v-icon class="ml-2"> fas fa-trash</v-icon>
        </v-btn>
      </template>
      <template v-slot:[`item.estado`]="{ item }">
        <v-chip :color="getColor(item.estado)" dark>{{ item.estado }}</v-chip>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>
    </v-data-table>
      </v-col>
    </v-row>
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
    dialog: false,
    headers: [
      {
        text: "Hora",
        align: "start",
        sortable: false,
        value: "hora"
      },
      { text: "Dia", value: "dia" },
      { text: "Fecha Adicional", value: "fecha_adicional" },
      { text: "Fecha Reserva", value: "fecha_reserva" },
      { text: "Sala", value: "sala" },
      { text: "Banco", value: "banco" },
      { text: "Estado de la petición", value: "estado" },
      { text: "Acciones", value: "actions", sortable: false }
    ],
    usuariolab: [],
    codigo: "20201195009", //QUITAR ESTE
    editedIndex: -1,
    codigoLab:"",
    usuario: "",
    editedItem: {
      elemento: "",
    },
    defaultItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0
    },

    dialogFicha: false,
    infoItem: {},
    inputElemento:"",

    fichaEdit: false,
    fichaPlacas: false,
    placasElementos: []
  }),
  // mounted(){
  // this.$verificarLogin();
  // },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    }
  },

  watch: {
    dialog(val) {
      val || this.close();
    }
  },

  created() {
    this.initialize();
  },

  methods: {
    initialize() {
      (this.usuariolab = []), this.buscar();
    },
    fichaItem(item) {
      // De acuerdo al adicional seleccionado se toma la información y se copia al objeto infoItem
      this.infoItem = JSON.parse(JSON.stringify(item));
      // Se calcula la diferencia en días de la fecha adicional y la fecha actual del sistema
      let difference = this.differenceDays(this.infoItem.fecha_adicional);

      // Hora y minutos actuales
      var hour = new Date().getHours();
      var minutes = new Date().getMinutes();
      
      // Se limpian e inicializan los input de los v-text de las dos fichas.
      // Las variables fichaEdit y fichaPlacas es para distinguir entre las dos fichas
      this.inputElemento = "";
      this.placasElementos = new Array(this.infoItem.elemento.length)
      for (let i=0;i<this.placasElementos.length;i++){
        if(this.infoItem.placaElemento.length==0){
          this.placasElementos[i]="";
        }else{
          this.placasElementos[i]=this.infoItem.placaElemento[i];
        }
      }
      this.fichaEdit = false;
      this.fichaPlacas = false;

      // Con la diferencia de fechas se hace una evaluación para determinar si puede o no editar la ficha de laboratorio. Solo podrá editar la ficha hasta 30 minutos antes del laboratorio siempre y cuando siga pendiente. Luego de esto, unicamente puede llenar la ficha con la placa de los equipos y ver las observaciones agregadas por el laboratorista. 

      // dialogFicha => activa el v-dialog; fichaEdit => edicion de elementos; fichaPlacas => edicion de placas
      if (difference>0 && this.infoItem.estado=="PENDIENTE"){
        this.fichaEdit = true;
      }else if(difference==0){
        if(this.infoItem.hora<(hour+1)){
          this.fichaPlacas = true;
        }else if(this.infoItem.hora===(hour+1) && 30<=minutes){
          this.fichaPlacas = true;
        }else{
          this.fichaEdit = true;
        }
      }else{
        this.fichaPlacas = true;
      }
      this.dialogFicha = true;
    },
    differenceDays(dateAdicional){
      // Se toman las fechas y con la función conversionDate se convierte al formato año-mes-dia sin tener en cuenta las horas. Luego, se obtienen los segundos transcurridos hasta esa fecha. En el caso de la fecha de adicional se utiliza la funcion parseDate para convertir el formato dia/mes/año a año-mes-dia. Luego, se realiza la resta en segundos de las dos fechas y se hace la conversión a días. Con esto se logra saber la diferencia en días del adicional y la fecha actual. 
      let dateToday = this.conversionDate(new Date());
      let dateTodayInSeconds = new Date(dateToday).getTime();

      let date = new Date(this.parseDate(dateAdicional)+" 00:00");
      date = this.conversionDate(date);
      let dateAdicionalInSeconds = new Date(date).getTime();

      // Diferencia en días de la fecha del adicional y la fecha actual
      return (dateAdicionalInSeconds-dateTodayInSeconds)/(1000*60*60*24);
    },
    parseDate(date) {
      if (!date) return null
      const [day, month, year] = date.split('/')
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    conversionDate(date){
      let year = date.getFullYear().toString();
      let month = (date.getMonth()+1).toString();
      let day = date.getDate().toString();
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    agregarElementoAdicional(){
      if (this.inputElemento.length>0){
        if(this.inputElemento.replace(/ /g, "").length>0){
          this.infoItem.elemento.push(this.inputElemento);
        }
      }      
      this.inputElemento = "";
    },
    getColor(estado) {
      if (estado == "APROBADO") return "green";
      else if (estado == "PENDIENTE") return "orange";
      else if (estado == "CANCELADO") return "red";
    },
    cancelarAdicional(item){
      // Toma la fecha actual del sistema y la resta con la fecha del adicional para saber la diferencia en días. El estudiante solo puede cancelar un adicional solo hasta una hora antes del mismo y solo si este se encuentra en estado aprobado o pendiente
      const difference = this.differenceDays(item.fecha_adicional)
      const hora_adicional = item.hora;
      const actualHour = new Date().getHours();

      if(item.estado=="APROBADO" || item.estado=="PENDIENTE"){
        if (difference>0){
          // De acuerdo al adicional seleccionado se toma la información y se copia al objeto infoItem
          this.infoItem = JSON.parse(JSON.stringify(item));
          this.infoItem.estado = "CANCELADO";
          console.log(this.infoItem.estado);
          this.editEstadoReserva();
        }else if(difference == 0){
          if(hora_adicional<=(actualHour+1)){
            console.log("Ya no puede cancelar debido a que el adicional ya paso o falta 1 hora para el adicional")
          }else{
            this.deleteItem(item);
          }
        }else{
          console.log("No puede cancelar porque ya paso el dia")
        }
      }else{
        console.log("No puede cancelar debido a que el adicional ya esta cancelado")
      }
    },
    deleteItem(item) {
      var confirmacion = confirm("¿Esta seguro que desea cancelar este laboratorio?");

      if (confirmacion) {
        const index = this.usuariolab.indexOf(item);
        this.sala = this.usuariolab[index].sala;
        this.banco = this.usuariolab[index].banco;
        this.fecha_adicional = this.usuariolab[index].fecha_adicional;
        this.hora = this.usuariolab[index].hora;
        
        let objeto = this;
        
        objeto.token = localStorage.cdcb0830cc2dd220;
        
        var encrypted = objeto.$cookies.get("user_session");      
        var desen = objeto.$Crypto.AES.decrypt(encrypted, objeto.token);
        var codlab = desen.toString(objeto.$Crypto.enc.Utf8);
        objeto.codigoLab = objeto.$Crypto.AES.decrypt(objeto.$cookies.get("user_session"), objeto.token);
        objeto.codigoLab=objeto.codigoLab.toString(objeto.$Crypto.enc.Utf8);

        this.axios
            .post(
              "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/aprobarreserva",
              {
                fecha_adicional: this.fecha_adicional,
                sala: this.sala,
                hora: this.hora,
                banco: this.banco,
                aprobar: "CANCELADO"
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
                objeto.buscar();
              }
            })
            .catch(function(error) {
            alert(error);
          });      
      }
    },
    editEstadoReserva(item) {
      var confirmacion = confirm("¿Esta seguro que desea cancelar este laboratorio?");

      if (confirmacion){
        let objeto = this;
        this.axios.post("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/aprobarreserva",
              {
                fecha_adicional: this.infoItem.fecha_adicional,
                sala: this.infoItem.sala,
                hora: this.infoItem.hora,
                banco: this.infoItem.banco,
                aprobar: this.infoItem.estado
              },
              {
                headers: {
                  "Content-Type": "application/json"
                }
              }
          )
          .then(function(response) {
            objeto.infoItem = {};
            var respuesta = response.data.mensaje;
            var status = response.data.status;
            if (status == "1") {
              alert(respuesta);
              objeto.buscar();
            }
          })
          .catch(function(error) {
            alert(error);
          });
      }
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    guardarFichaPlacas(){
      this.infoItem.placaElemento = this.placasElementos;
      this.placasElementos = "";
      this.guardarFichaEdit();
      this.dialogFicha = false;
    },

    guardarFichaEdit() {
      var confirmacion = confirm("¿Esta seguro de guardar estos cambio?");

      if (confirmacion) {
        let objeto = this;
        
        objeto.token = localStorage.cdcb0830cc2dd220;
      
        var encrypted = objeto.$cookies.get("user_session");      
        var desen = objeto.$Crypto.AES.decrypt(encrypted, objeto.token);
        var codlab = desen.toString(objeto.$Crypto.enc.Utf8);
        objeto.codigoLab = objeto.$Crypto.AES.decrypt(objeto.$cookies.get("user_session"), objeto.token);
        objeto.codigoLab=objeto.codigoLab.toString(objeto.$Crypto.enc.Utf8);

        this.axios
          .post(
            "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/editarreserva",
            {
              codigo: this.codigoLab,
              hora: objeto.infoItem.hora,
              dia: objeto.infoItem.dia,
              fecha_adicional: objeto.infoItem.fecha_adicional,
              fecha_reserva: objeto.infoItem.fecha_reserva,
              sala: objeto.infoItem.sala,
              banco: objeto.infoItem.banco,
              elemento: objeto.infoItem.elemento,
              estadoElemento: objeto.infoItem.estadoElemento,
              placaElemento: objeto.infoItem.placaElemento,
              observacionesGenerales: objeto.infoItem.observacionesGenerales,
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
              objeto.dialogFicha = false;
              objeto.buscar();
            }
          })
          .catch(function(error) {
            alert(error);
          });
      }
      this.close();
    },
    buscar() {
      let objeto = this;
      

      objeto.token = localStorage.cdcb0830cc2dd220;
      
      var encrypted = objeto.$cookies.get("user_session");      
      var desen = objeto.$Crypto.AES.decrypt(encrypted, objeto.token);
      var codlab = desen.toString(objeto.$Crypto.enc.Utf8);
      objeto.codigoLab = objeto.$Crypto.AES.decrypt(objeto.$cookies.get("user_session"), objeto.token);
      objeto.codigoLab=objeto.codigoLab.toString(objeto.$Crypto.enc.Utf8);

      console.log("Buscar reserva: ",objeto.codigoLab);

      this.axios
        .post(
          "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/buscarreserva",
          {
            codigo: objeto.codigoLab
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          objeto.usuariolab = response.data.data;
          console.log("Respuesta Busqueda: ",objeto.usuariolab);
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>