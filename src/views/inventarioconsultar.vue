<template>
  <v-container fluid>

    <HeaderLaboratorista />
    

    <v-data-table :headers="headers" :items="equipolab" :search="search" class="elevation-1" color="background" dark>
      <template v-slot:top>
        <v-toolbar flat dark>
          <v-toolbar-title>Consulta inventario equipos</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          
          <!--BARRA DE BUSQUEDA-->
          <v-text-field
            v-model="search"
            ref="form"
            append-icon="fas far-search"
            label="Buscar"
            single-line
            hide-details
            
            dark
            @keyup.enter="initialize"
          ></v-text-field>
          
          <!--BOTÓN BUSCAR-->
          <v-btn color="primary" @click="initialize">Buscar</v-btn>
          
          <v-spacer></v-spacer>          
          <v-btn color="primary" @click="reset">Reset</v-btn>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{on}">
              <v-btn
                color="primary"
                
                
                to="/addequipo"
              >Agregar nuevo elemento</v-btn>
            </template>

            

            <v-card dark>            

              <!-- <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title> -->

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col class="col-sm-12 col-lg-6">
                      <v-text-field v-model="editedItem.sede" :disabled="true" label="Sede"></v-text-field>
                    </v-col>
                    <v-col class="col-sm-12 col-lg-6">                       
                      <v-text-field v-model="editedItem.idSede" :disabled="true" label="Id sede"></v-text-field>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col class="col-sm-12 col-lg-6">
                      <v-text-field                    
                          v-model="editedItem.dependencia" :disabled="true" label="Dependencia"                        
                      ></v-text-field>
                    </v-col>

                    <v-col class="col-sm-12 col-lg-6">
                      
                      <v-autocomplete
                        v-model="editedItem.espacioFisico"
                        :items="ubicaciones"
                        dense
                        filled
                        label="Ubicación Actual"
                        
                      ></v-autocomplete>
                    </v-col>

                  </v-row>
                  <v-row>
                    <v-col class="col-sm-12 col-lg-6">
                      <v-autocomplete
                        v-model="editedItem.tipo"
                        :items="T_ubicaciones"
                        dense
                        filled
                        label="Tipo de ubicación"
                        
                      ></v-autocomplete>

                      <!--<v-text-field v-model="editedItem.espacioFisico" :disabled="false" label="Ubicación Actual"></v-text-field>-->
                    </v-col>

                    <v-col class="col-sm-12 col-lg-6">
                      <v-autocomplete
                        v-model="editedItem.numero"
                        :items="N_ubicaciones"
                        dense
                        filled
                        label="Número"
                        
                      ></v-autocomplete>                      
                    </v-col>

                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancelar</v-btn>
                <v-btn color="blue darken-1" text @click="save(item)">Enviar</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>

          <v-dialog v-model="dialog2" max-width="1400px">
            <v-card dark>
              <v-card-title>
                <span class="headline">Información Básica</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-col class="col-sm-12 col-lg-10">
                    <v-row>
                      <v-col>
                        <v-text-field v-model="infoItem.placa" :disabled="true" label="Placa"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field v-model="infoItem.serial" :disabled="true" label="Serial"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.nombreEquipo"
                          :disabled="true"
                          label="Nombre del equipo"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field v-model="infoItem.modelo" :disabled="true" label="Modelo"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field v-model="infoItem.estado" :disabled="true" label="Estado"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field v-model="infoItem.serie" :disabled="true" label="Serie"></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field v-model="infoItem.marca" :disabled="true" label="Marca"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.numeroInterno"
                          :disabled="true"
                          label="Número interno"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.nombreFuncionario"
                          :disabled="true"
                          label="Nombre del funcionario"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.documentoFuncionario"
                          :disabled="true"
                          label="Documento del funcionario"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-col>
                </v-container>
              </v-card-text>
            </v-card>
            <v-card dark>
              <v-card-title>
                <span class="headline">Ubicación</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-col class="col-sm-12 col-lg-10">
                    <v-row>
                      <v-col>
                        <v-text-field v-model="infoItem.sede" :disabled="true" label="Sede"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field v-model="infoItem.idSede" :disabled="true" label="Id sede"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.dependencia"
                          :disabled="true"
                          label="Dependencia"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.idUbicacion"
                          :disabled="true"
                          label="Id ubicación"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.espacioFisico"
                          :disabled="true"
                          label="Espacio fisico"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-col>
                </v-container>
              </v-card-text>
            </v-card>
            <v-card dark>
              <v-card-title>
                <span class="headline">Detalles de compra</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-col class="col-sm-12 col-lg-10">
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.proveedor"
                          :disabled="true"
                          label="Proveedor"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.valorElemento"
                          :disabled="true"
                          label="Valor elemento"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field v-model="infoItem.nit" :disabled="true" label="Nit"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.ivaAplicado"
                          :disabled="true"
                          label="Iva aplicado"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.tipoContrato"
                          :disabled="true"
                          label="Tipo de contrato"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.totalValorelemento"
                          :disabled="true"
                          label="Total valor del elemento"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field v-model="infoItem.vigencia" :disabled="true" label="Vigencia"></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.cantidadAsignada"
                          :disabled="true"
                          label="Cantidad asignada"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.fechaAdquisicion"
                          :disabled="true"
                          label="Fecha de adquisición"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.numeroContrato"
                          :disabled="true"
                          label="Número de contrato"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.numeroFactura"
                          :disabled="true"
                          label="Número de factura de compra"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.tiempoGarantia"
                          :disabled="true"
                          label="Tiempo de garantia"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-col>
                </v-container>
              </v-card-text>
            </v-card>
            <v-card dark>
              <v-card-title>
                <span class="headline">Caracteristicas del Equipo</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-col class="col-sm-12 col-lg-10">
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.frecuenciaMantenimiento"
                          :disabled="true"
                          label="Frecuencia de mantenimiento"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.manual"
                          :disabled="true"
                          label="Cuenta con manual"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.tiempoVidautil"
                          :disabled="true"
                          label="Tiempo de vida útil"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.tipoUso"
                          :disabled="true"
                          label="Tipo de uso"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.potenciaElectrica"
                          :disabled="true"
                          label="Potencia eléctrica"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.tipoUso_otro"
                          :disabled="true"
                          label="Tipo de uso-otro"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.paisOrigen"
                          :disabled="true"
                          label="País de origen"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="infoItem.impactoEquipo"
                          :disabled="true"
                          label="Impacto del equipo"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-textarea
                          v-model="infoItem.especificacionesTecnicas"
                          :disabled="true"
                          auto-grow
                          outlined
                          rows="1"
                          label="Especificaciones técnicas"
                        ></v-textarea>
                      </v-col>
                      <v-col>
                        <v-textarea
                          v-model="infoItem.accesorios"
                          :disabled="true"
                          auto-grow
                          outlined
                          rows="1"
                          label="Accesorios"
                        ></v-textarea>
                      </v-col>
                    </v-row>
                  </v-col>
                </v-container>
                <v-row justify="space-around">
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    
                    <v-btn outlined color="blue darken-1" text @click="close2">Cerrar</v-btn>
                  </v-card-actions>
                </v-row>
              </v-card-text>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <!-- FORMA CORRECTA: -->
      <!-- <template v-slot:[`item.actions`]="{ item }"> -->
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">fas fa-edit</v-icon>
        <v-icon small class="mr-2" @click="activeItem(item)">fas fa-check-circle</v-icon>
        <v-icon small class="mr-2" @click="desactiveItem(item)">fas fa-times-circle</v-icon>
        <v-icon small class="mr-2" @click="inforItem(item)">fas fa-info-circle</v-icon>
      </template>
      
    </v-data-table>
  </v-container>
</template>

<script>
import HeaderLaboratorista from "@/components/HeaderLaboratorista.vue";
export default {
  components: {
    HeaderLaboratorista
  },
  data: () => ({
    ubicaciones: ["ALMACEN", "LABORATORIO DE CIRCUITOS", "LABORATORIO DE ELECTRONICA A","LABORATORIO DE ELECTRONICA B","LABORATORIO DE BASICA","LABORATORIO DE DIGITALES","LABORATORIO DE COMUNICACIONES","LABORATORIO DE CONTROL","LABORATORIO DE MAQUINAS","LABORATORIO FESTO","FISICA 509","FISICA 510","SALA DE SISTEMAS 500","SALA DE SISTEMAS 501","SALA DE SISTEMAS 502","SALA DE SISTEMAS 503","SALA DE SISTEMAS 504","SALA DE SISTEMAS 505","SALA DE SISTEMAS 506","SALA DE SISTEMAS 507","SALA DE SISTEMAS 508","SALA DE SISTEMAS 601","SALA DE SISTEMAS 701","SALA DE SISTEMAS 702","SALA DE SISTEMAS 703","SALA DE SISTEMAS 704","SALA DE SISTEMAS 706","SALA DE SISTEMAS 707"],
    T_ubicaciones: ["PUESTO","BANCO","STAND","ARMARIO"],
    N_ubicaciones:["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"],
    return: {
      search: "",
      TipoUbicacion: "",   
      idUbicacion:"",   
    },
    dialog: false,
    dialog2: false,
    headers: [
      {
        text: "Placa",
        align: "start",
        sortable: false,
        value: "placa"
      },
      { text: "Nombre equipo", value: "nombreEquipo" },
      { text: "Marca", value: "marca" },
      { text: "Serial", value: "serial" },
      { text: "Estado", value: "estado" },
      { text: "Sala", value: "espacioFisico" },
      { text: "Acción", value: "actions", sortable: false }
    ],
    equipolab: [],
    editedIndex: -1,
    editedItem: {},
    infoIndex: -1,
    infoItem: {},

    defaultItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0
    }
  }),
  // mounted(){
  // this.$verificarLogin();
  // },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Editar Ubicación";
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
      (this.equipolab = []), this.buscar();
    },

    reset () {
        this.$refs.form.reset(), this.initialize();
      },

    editItem(item) {
      this.editedIndex = this.equipolab.indexOf(item);

      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    inforItem(item) {
      this.infoIndex = this.equipolab.indexOf(item);

      this.infoItem = Object.assign({}, item);
      this.dialog2 = true;
    },
    desactiveItem(item) {
      var confirmacion = confirm("¿Esta seguro de desactivar este elemento?");

      if (confirmacion) {
        const index = this.equipolab.indexOf(item);
        this.placa = this.equipolab[index].placa;

        let objeto = this;
        this.axios
          .post(
            "http://" +
              objeto.$serverURI +
              ":" +
              objeto.$serverPort +
              "/Usuario/desactivarEquipo",
            {
              placa: objeto.placa
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
              //   objeto.equipolab.splice(index, 1);
              objeto.buscar();
            }
          })

          .catch(function(error) {
            alert(error);
          });
      }
    },

    activeItem(item) {
      var confirmacion = confirm("¿Esta seguro de activar este elemento?");

      if (confirmacion) {
        const index = this.equipolab.indexOf(item);
        this.placa = this.equipolab[index].placa;

        let objeto = this;
        this.axios
          .post(
            "http://" +
              objeto.$serverURI +
              ":" +
              objeto.$serverPort +
              "/Usuario/activarEquipo",
            {
              placa: objeto.placa
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
              //   objeto.equipolab.splice(index, 1);
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


    close2() {
      this.dialog2 = false;
      this.$nextTick(() => {
        this.infoItem = Object.assign({}, this.defaultItem);
        this.infoIndex = -1;
      });
    },

    save() {
      
      let objeto2 = this;
      this.placa = this.editedItem.placa;
      this.sala = this.editedItem.espacioFisico;
      var tipo_u = this.editedItem.tipo;
      var numero_u = this.editedItem.numero;
      objeto2.idUbicacion= tipo_u + " " + numero_u;
      console.log("idUbicación: ",objeto2.idUbicacion);
      

      var confirmacion = confirm("¿Esta seguro de guardar estos cambios?");

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
              sala: objeto.sala,
              iUbicacion: objeto2.idUbicacion,
              
            },
            //toUpperCase convierte la cadena de String a mayusculas
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
              //   objeto.equipolab.splice(index, 1);
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
            "/Usuario/consultarEquipo",
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          objeto.equipolab = response.data.data;
          
          // console.log(objeto.equipolab);
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>
