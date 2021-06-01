<template>
  <v-container fluid>
    <HeaderLaboratorista />
    <v-card>
    <v-card-title>
      Reservas
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="fas far-search"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      
      :headers="headers"
      :items="reservalab"
      :search="search"
      class="elevation-1"
      color="background"
      dark
    >

      <template v-slot:top>
        <v-toolbar flat dark>
          <v-toolbar-title>Consulta reservas</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-dialog v-model="dialog" max-width="500px">
            <v-card dark>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col class="col-sm-8 col-lg-8">
                      <v-text-field
                        v-model="agregarUbicacionItem.espacioFisico"
                        :disabled="true"
                        label="Laboratorio"
                      ></v-text-field>
                    </v-col>
                    <v-col class="col-sm-8 col-lg-8">
                      <v-text-field
                        v-model="agregarUbicacionItem.espacioFisico"
                        :disabled="true"
                        label="Banco"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancelar</v-btn>
                <v-btn color="blue darken-1" text @click="save(item)">Enviar</v-btn>
              </v-card-actions>

              <v-card-asistencia>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancelar</v-btn>
                <v-btn color="blue darken-1" text @click="save(item)">Enviar</v-btn>
              </v-card-asistencia>
            </v-card>
          </v-dialog>
          <v-dialog ref="form" v-model="dialog2" max-width="1400px" >
            <v-card dark>
              <v-card-title>
                <span class="headline">Información de la reserva</span>
              </v-card-title>
              
              <v-card-text>
                <v-container>
                  <v-col class="col-sm-12 col-lg-12">
                    <v-row>
                      <v-col>
                        <v-text-field v-model="infoItem.fecha_adicional" :disabled="true" label="Fecha del adicional"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field v-model="infoItem.hora" :disabled="true" label="Hora"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field v-model="infoItem.dia" :disabled="true" label="Día"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field v-model="infoItem.sala" :disabled="true" label="Sala"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field v-model="infoItem.banco" :disabled="true" label="Banco"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.practica"
                          :disabled="true"
                          label="Practica"
                        ></v-text-field>
                      </v-col>

                    </v-row>     
                    <v-row>
                      <v-col>
                        <v-text-field v-model="infoItem.codigo" :disabled="true" label="Código Usuario"></v-text-field>
                      </v-col>                      
                      <v-col>
                        <v-text-field v-model="infoItem.usuario" :disabled="true" label="Nombre Usuario"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field v-model="infoItem.estado" :disabled="true" label="Estado petición"></v-text-field>
                      </v-col>    
                      <v-col>
                        <v-text-field v-model="infoItem.fecha_reserva" :disabled="true" label="Fecha de la reserva"></v-text-field>
                      </v-col>                  
                    </v-row>

                    <v-row>                      
                      <v-col>
                        <v-text-field v-model="infoItem.elemento" :disabled="true" label="Elementos"></v-text-field>
                      </v-col>
                    </v-row>



                    <v-divider></v-divider>
                    <v-row no-gutters class="pa-1" align="center">
                      <v-col cols="12" sm="1" class="text-sm-center font-weight-black">
                        No.
                      </v-col>
                      
                      <v-col cols="12" sm="7" class="font-weight-black">
                        Elementos
                      </v-col>
                      <v-col cols="12" sm="2" class="text-sm-center font-weight-black" v-if=true>
                        Acciones
                      </v-col>
                      <v-col cols="12" sm="2" class="text-sm-center font-weight-black" v-if=true>
                        Estado Item
                      </v-col>
                    </v-row>
                    

                    <v-row no-gutters align="center">
                      <v-col v-for= "(item,index) in infoItem.elemento" :key="index" cols="12" sm="12">
                        <v-divider></v-divider>  
                        <v-row no-gutters class="pa-1" align="center">
                          <v-col cols="12" sm="1" class="text-sm-center">
                            {{index+1}}.
                          </v-col>
                          
                          <v-col cols="12" sm="7">
                            {{item}}
                          </v-col>


                          <v-col cols="12" sm="2" class="text-sm-center" v-if=true>
                            <v-icon small class="mr-2" @click="aprobarReserva(index,true)">fas fa-check-circle</v-icon>
                            <v-icon small class="mr-2" @click="aprobarReserva(index,false)">fas fa-times-circle</v-icon>
                            <v-icon small class="mr-2" @click="eliminarElemento(index)">fas fa-trash-alt</v-icon>
                                                       
                          </v-col>
                          
                            <v-col cols="12" sm="2" class="text-sm-center" v-if=true>
                            
                            <v-text-field
                              dense
                              hide-details
                              label="Pendiente"
                              single-line
                              v-model = "revisionElementos[index]"
                            ></v-text-field>
                            
                                                       
                          </v-col>

                        </v-row>

                      </v-col>                  
                    </v-row>

                    <v-divider></v-divider>
                    <v-row>
                      <v-col cols="12" sm="4" class="text-sm-center">
                        <v-btn color="green" @click="aprobarItem(objItem,'1')">Aprobar</v-btn>
                      </v-col>
                      <v-col cols="12" sm="4" class="text-sm-center">
                        <v-btn color="primary" @click="aprobarItem(objItem,'2')">Cancelar</v-btn>
                      </v-col>          
                      <v-col cols="12" sm="4" class="text-sm-center">
                        <v-btn color="orange" @click="aprobarItem(objItem,'3')">Pendiente</v-btn>
                      </v-col>           
                    </v-row>

                  </v-col>
                </v-container>
              </v-card-text>

              
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click="inforItem(item)">fas fa-info-circle</v-icon>
        <v-icon small class="mr-2" @click="ficha()">fas fa-edit</v-icon>
        <v-icon small class="mr-2" @click="deleteItem(item)">fas fa-trash</v-icon>
      </template>
      <template v-slot:[`item.asistencia`]="{ item }">
        <v-icon small class="mr-2" @click="asistencia(item,true)">fas fa-check-circle</v-icon>
        <v-icon small class="mr-2" @click="asistencia(item,false)">fas fa-times-circle</v-icon>

      </template>
      <template v-slot:[`item.estado`]="{ item }">
        <v-chip :color="getColor(item.estado)" dark>{{ item.estado }}</v-chip>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>


    </v-data-table>
    </v-card>
  </v-container>
</template>

<script>
import HeaderLaboratorista from "@/components/HeaderLaboratorista.vue";
export default {
  components: {
    HeaderLaboratorista
  },
  data: () => ({
    return: {
      search: ""
    },
    dialog: false,
    dialog2: false,
    infoItem: {},
    search: "",
    revisionElementos:[],
    headers: [
      {
        text: "Código",
        align: "start",
        sortable: false,
        value: "codigo"
      },
      { text: "Nombre del estudiante", value: "usuario" },
      { text: "Día", value: "dia" },
      { text: "Hora", value: "hora"},
      { text: "Fecha reserva", value: "fecha_reserva" },
      { text: "Fecha adicional", value: "fecha_adicional" },
      { text: "Laboratorio", value: "sala"},
      { text: "Banco", value: "banco"},
      { text: "Estado de la petición", value: "estado" },      
      { text: "Acción", value: "actions", sortable: false },
      { text: "Asistencia", value: "asistencia", sortable: false }
    ],
    reservalab: [],
    reservasLabAll: [],
    infoIndex: -1,
    objItem: "",
    agregarUbicacionIndex: -1,
    agregarUbicacionItem: {},
    infoIndex: -1,

    sala: '',
    hora: '',
    fecha_adicional:'',
    banco:'',
    aprobar:''
  }),
  mounted(){
  },

  computed: {
    formTitle() {
      return this.agregarUbicacionIndex === -1 ? "New Item" : "Editar Ubicación";
    }
  },

  watch: {
    dialog(val) {
      val || this.close();
    }
  },

  created() {
    console.log("Este es el created");
    this.initialize();
  },

  methods: {
    getColor(estado) {
      if (estado == "APROBADO") return "green";
      else if (estado == "PENDIENTE") return "orange";
      else if (estado == "CANCELADO") return "red";
    },
    initialize() {
      (this.reservalab = []), this.buscar();
    },

    aprobarReserva(item,opc){
      console.log("ITEM: ", item);
      console.log("Valor: ", opc);
      this.revisionElementos[item]=opc;
      console.log(this.revisionElementos);
      
      
      //this.$refs.form.reset();
      
    },
    ficha(){
      alert("AQUI VA LA FICHA");
    },
    mail(infoItem){
      let objeto = this;
      this.axios
          .post(
            "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/send_mail",
            {
              usuario: infoItem.usuario,
              fecha_adicional: infoItem.fecha_adicional,
              laboratorio: infoItem.sala,
              hora: infoItem.hora,
              opcion: this.aprobar
            },
            {
              headers: {
                "Content-Type": "application/json"
              }
            }
          )
          .then(function(response) {
            var respuesta = response.data;
            console.log(respuesta.mensaje);
          })
          .catch(function(error) {
          alert(error);
        });      
    },

    inforItem(item) {
      console.log("SOLICITA INFO");
      this.objItem=item;
      this.infoIndex = this.reservalab.indexOf(item);
      this.infoItem = Object.assign({}, item);
      this.dialog2 = true;



      this.revisionElementos = new Array(this.infoItem.elemento.length)
      for (let i=0;i<this.revisionElementos.length;i++){
        this.revisionElementos[i]="";
      }


    },

    eliminarElemento(index){
      this.infoItem.elemento.splice(index,1);
      this.revisionElementos.splice(index,1);
      
    },
    
    aprobarItem(item,opc) {
      let objeto = this;

      if (opc == '1'){
        this.aprobar='APROBADO';
        this.mail(this.infoItem);
      }
      if (opc == '2'){
        this.aprobar='CANCELADO';
        this.mail(this.infoItem);
      }
      if (opc == '3'){
        this.aprobar='PENDIENTE';
      }
      console.log("# ITEM: ",this.reservalab.indexOf(item));
      
      console.log(this.aprobar);

      var confirmacion = confirm("¿Esta seguro de marcar este laboratorio como "+this.aprobar+"?");

      if (confirmacion) {

        const index = this.reservalab.indexOf(item);
        //  this.agregarUbicacionItem = Object.assign({}, item);
        //  this.dialog = true;
      
        this.hora = this.reservalab[index].hora;
        this.sala = this.reservalab[index].sala;
        this.fecha_adicional = this.reservalab[index].fecha_adicional;
        this.banco = this.reservalab[index].banco;
      
        console.log(index, this.sala);

        
          this.axios
            .post(
              "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/aprobarreserva",
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
                objeto.reservalab.splice(index, 1);
              }
            })
            .catch(function(error) {
            alert(error);
          });      
      }
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

        const index = this.reservalab.indexOf(item);
        //  this.agregarUbicacionItem = Object.assign({}, item);
        //  this.dialog = true;
      
        this.hora = this.reservalab[index].hora;
        this.sala = this.reservalab[index].sala;
        this.fecha_adicional = this.reservalab[index].fecha_adicional;
        this.banco = this.reservalab[index].banco;
      
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
                objeto.reservalab.splice(index, 1);
              }
            })
            .catch(function(error) {
            alert(error);
          });      
      }
    },



    deleteItem(item) {
      var confirmacion = confirm("¿Esta seguro de eliminar este laboratorio?");

      if (confirmacion) {
        console.log("Entra a confirmación");
        const index = this.reservalab.indexOf(item);
        this.sala = this.reservalab[index].sala;
        this.banco = this.reservalab[index].banco;
        this.fecha_adicional = this.reservalab[index].fecha_adicional;
        this.hora = this.reservalab[index].hora;
        this.codigo = this.reservalab[index].codigo;
        
        console.log("Antes de definir OBJ");        

        let objeto = this;



        this.axios
          .post(
            "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/borrarreserva",
            {
              codigo: this.codigo,
              sala: this.sala,
              banco: this.banco,
              fecha_adicional: this.fecha_adicional,
              hora: this.hora
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
              objeto.reservalab.splice(index, 1);
            }
            
            console.log("Status: ", status, "Mensaje: ", respuesta);
          })
          .catch(function(error) {
            alert(error);
          });
      }
    },

    rechazarItem(item) {},

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.agregarUbicacionItem = Object.assign({}, this.defaultItem);
        this.agregarUbicacionIndex = -1;
      });
    },

    save() {
      var confirmacion = confirm("¿Esta seguro de guardar estos cambio?");

      this.placa = this.agregarUbicacionItem.placa;
      this.sala = this.agregarUbicacionItem.sala;

      if (confirmacion) {
        let objeto = this;
        this.axios
          .post(
            "http://" +
              objeto.$serverURI +
              ":" +
              objeto.$serverPort +
              "/Usuario/editarequipo",
            {
              placa: objeto.placa,
              sala: objeto.sala.toUpperCase()
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
              //   objeto.reservalab.splice(index, 1);
            }
          })
          .catch(function(error) {
            alert(error);
          });
      }
      this.buscar();
      this.close();
    },
    buscar() {
      let objeto = this;
      this.axios
        .get(
          "http://" +
            objeto.$serverURI +
            ":" +
            objeto.$serverPort +
            "/Usuario/buscarreservalabo",
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          objeto.reservasLabAll = response.data.data;
          objeto.verificarBusqueda();
        })
        .catch(function(error) {
          objeto.output = error;
        });
    },
    verificarBusqueda(){
      console.log("Funcion desde la vista Consultar");
      let date = this.$store.state.date;
      let hour = this.$store.state.hour;
      let banco = this.$store.state.banco;
      if (date !== null && hour !== null && banco !== null){
        this.reservalab = this.reservasLabAll.filter(item => item.fecha_adicional == date && item.hora == hour && item.banco == banco);
        this.$store.state.hour = null;
        this.$store.state.date = null;
        this.$store.state.banco = null;
      }else{
        this.reservalab = this.reservasLabAll;
      }
      console.log(this.$store.state.date);
    }
  }
};
</script>
