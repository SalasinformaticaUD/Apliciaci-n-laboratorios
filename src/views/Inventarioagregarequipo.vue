<template>
  <v-container class="grey darken-4" dark fluid>
    <HeaderLaboratorista />
    <v-col cols="12" align="center">
      <v-col class="col-sm-12 col-lg-8">
        <h1 style="color:white;">Agregar Equipo</h1>

        <v-stepper v-model="e1" dark>
          <v-stepper-header>
            <v-stepper-step :complete="e1 > 1" step="1" :editable="editable">Información básica</v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step :complete="e1 > 2" step="2" :editable="editable">Ubicación</v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step :complete="e1 > 3" step="3" :editable="editable">Detalles de compra</v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step
              :complete="e1 > 4"
              step="4"
              :editable="editable"
            >Caracteristicas del Equipo</v-stepper-step>
          </v-stepper-header>

          <v-stepper-items>
            <v-stepper-content step="1">
              <v-card color="#424242" style="padding:30px" class="mb-12">
                <v-card-title
                  class="justify-center"
                  style="color:white;font-weigth:bolder;"
                >Información básica</v-card-title>

                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="placa" label="Placa" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="serial" label="Serial" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="nombreEquipo" label="Nombre del equipo" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="modelo" label="Modelo" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-autocomplete :items="estados" v-model="estado" label="Estado" solo
                    :rules="[rules.required]"></v-autocomplete>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="serie" label="Serie" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="marca" label="Marca" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="numeroInterno" label="Número interno" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="nombreFuncionario" label="Nombre del funcionario" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field
                      v-model="documentoFuncionario"
                      label="Documento del funcionario"
                      solo
                      :rules="[rules.required]"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-card>
              <v-btn rounded color="primary" dark @click="e1 = 2">Siguiente</v-btn>
              <v-btn text>Cancel</v-btn>
            </v-stepper-content>

            <v-stepper-content step="2">
              <v-card color="#424242" style="padding:30px" class="mb-12">
                <v-card-title
                  class="justify-center"
                  style="color:white;font-weigth:bolder;"
                >Ubicación</v-card-title>

                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-autocomplete :items="options.opt_sede" v-model="sede" label="Sede" solo
                    :rules="[rules.required]"></v-autocomplete>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-autocomplete
                      :items="filteredDatasedes"
                      v-model="idSede"
                      label="Id sede"
                      solo
                      :rules="[rules.required]"
                    ></v-autocomplete>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-autocomplete  :items="options.opt_dependencia" v-model="dependencia" label="Dependencia" solo
                    :rules="[rules.required]"></v-autocomplete>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="idUbicacion" label="Id ubicación" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-autocomplete
                      :items="filteredDatalabs"
                      v-model="espacioFisico"
                      label="Espacio fisico"
                      solo
                      :rules="[rules.required]"
                    ></v-autocomplete>
                  </v-col>
                </v-row>
              </v-card>
              <v-btn rounded color="primary" dark @click="e1 = 3">Siguiente</v-btn>
              <v-btn text>Cancel</v-btn>
            </v-stepper-content>

            <v-stepper-content step="3">
              <v-card color="#424242" style="padding:30px" class="mb-12">
                <v-card-title
                  class="justify-center"
                  style="color:white;font-weigth:bolder;"
                >Detalles de compra</v-card-title>

                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="proveedor" label="Proveedor" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="valorElemento" label="Valor elemento" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="nit" label="Nit" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="ivaAplicado" label="IVA aplicado" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="tipoContrato" label="Tipo de contrato" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="totalValorelemento" label="Total valor de elemento" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="vigencia" label="Vigencia" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="cantidadAsignada" label="Cantidad asignada" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-menu
                      ref="menu1"
                      v-model="menu1"
                      :close-on-content-click="false"
                      transition="scale-transition"
                      offset-y
                      max-width="290px"
                      min-width="290px"
                      dark
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          v-model="fechaAdquisicion"
                          label="Fecha de adquisición"
                          hint="DD/MM/YYYY"
                          persistent-hint
                          prepend-icon="far fa-calendar-plus"
                          v-bind="attrs"
                          v-on="on"
                          :rules="[rules.required]"
                        ></v-text-field>
                      </template>
                      <v-date-picker v-model="date" no-title @input="menu1 = false"></v-date-picker>
                    </v-menu>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="numeroContrato" label="Número de contrato" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="numeroFactura" label="Número de factura de compra" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-autocomplete
                      :items="tiemposGarantia"
                      v-model="tiempoGarantia"
                      label="Tiempo de garantía"
                      solo
                      :rules="[rules.required]"
                    ></v-autocomplete>
                  </v-col>
                </v-row>
              </v-card>
              <v-btn rounded color="primary" dark @click="e1 = 4">Siguiente</v-btn>
              <v-btn text>Cancel</v-btn>
            </v-stepper-content>

            <v-stepper-content step="4">
              <v-card color="#424242" style="padding:30px" class="mb-12">
                <v-card-title
                  class="justify-center"
                  style="color:white;font-weigth:bolder;"
                >Caracteristicas del Equipo</v-card-title>

                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field
                      v-model="frecuenciaMantenimiento"
                      label="Frecuencia de mantenimiento"
                      solo
                      :rules="[rules.required]"
                    ></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-autocomplete
                      :items="manuales"
                      v-model="manual"
                      label="Cuenta con manual"
                      solo
                      :rules="[rules.required]"
                    ></v-autocomplete>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="tiempoVidautil" label="Tiempo de vida util" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-autocomplete :items="tiposUso" v-model="tipoUso" label="Tipo de uso" solo
                    :rules="[rules.required]"></v-autocomplete>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="potenciaElectrica" label="Potencia Eléctrica" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="tipoUso_otro" label="Tipo de uso-otro" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="paisOrigen" label="País de origen" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="impactoEquipo" label="Impacto del equipo" solo
                    :rules="[rules.required]"></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-textarea
                      v-model="especificacionesTecnicas"
                      label="Especificaciones técnicas"
                      solo
                      :rules="[rules.required]"
                    ></v-textarea>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-textarea v-model="accesorios" label="Accesorios" solo
                    :rules="[rules.required]"></v-textarea>
                  </v-col>
                </v-row>
              </v-card>
               <p class="red--text" v-if="errors.length">
                <b>Error(es):</b>
                <ul>
                  <li v-for="(err,index) in errors" :key="index">{{ err }}</li>
                </ul>
              </p>
              <v-btn rounded color="primary" dark @click="formSubmit">Guardar</v-btn>
              <v-btn text>Cancel</v-btn>
            </v-stepper-content>
          </v-stepper-items>
        </v-stepper>
      </v-col>
    </v-col>
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
      e1: 1,
      editable: true,
      placa: "",
      serial: "",
      nombreEquipo: "",
      modelo: "",
      marca: "",
      numeroInterno: "",
      estados: ["ACTIVO", "NO-ACTIVO"],
      estado: "",
      serie: "",
      sede: "",
      idSede: "",
      dependencia: "",
      idUbicacion: "",
      espacioFisico: "",
      proveedor: "",
      valorElemento: "",
      nit: "",
      ivaAplicado: "",
      tipoContrato: "",
      totalValorelemento: "",
      cantidadAsignada: "",
      vigencia: "",
      date: new Date().toISOString().substr(0, 10),
      fechaAdquisicion: this.formatDate(new Date().toISOString().substr(0, 10)),
      menu1: false,
      numeroContrato: "",
      numeroFactura: "",
      tiempoGarantia: "",
      tiemposGarantia: [
        "MENOS DE 1 AÑO",
        "1 AÑO",
        "2 AÑOS",
        "3 AÑOS",
        "4 AÑOS",
        "5 AÑOS",
        "MÁS DE 5 AÑOS"
      ],
      frecuenciaMantenimiento: "",
      manual: "",
      manuales: ["SI", "NO"],
      tiempoVidautil: "",
      tipoUso: "",
      tiposUso: [
        "ACADÉMICO",
        "INVESTIGACIÓN",
        "EXTENSIÓN",
        "SERVICIOS",
        "OTROS"
      ],
      potenciaElectrica: "",
      tipoUso_otro: "",
      paisOrigen: "",
      impactoEquipo: "",
      especificacionesTecnicas: "",
      accesorios: "",
      documentoFuncionario: "",
      nombreFuncionario: "",
      errors:[],
      rules: {
        required: value => !!value || "Requerido.",      
      },
      support: {
        iden_sedes: "",
        iden_salas: ""
      },
      options: {
        opt_sede: [
          {
            text: "ACADEMIA SUPERIOR ARTES-ASAB",
            value: 1
          },
          {
            text: "ACADEMICA LUIS A. CALVO",
            value: 2
          },
          {
            text: "ADUANILLA DE PAIBA",
            value: 3
          },
          {
            text: "CALLE 34",
            value: 4
          },
          {
            text: "CALLE 40",
            value: 5
          },
          {
            text: "CENTRO CULTURAL NUEVA SANTAFE",
            value: 6
          },
          {
            text: "EMISORA",
            value: 7
          },
          {
            text: "GRUPO DESARROLLO FISICO - PIGA",
            value: 8
          },
          {
            text: "IDEXUD",
            value: 9
          },
          {
            text: "MACARENA - A",
            value: 10
          },
          {
            text: "MACARENA - B",
            value: 11
          },
          {
            text: "PORVENIR BOSA",
            value: 12
          },
          {
            text: "POSGRADOS",
            value: 13
          },
          {
            text: "SECCION DE PUBLICACIONES",
            value: 14
          },
          {
            text: "SOTANOS AVENIDA JIMENEZ",
            value: 15
          },
          {
            text: "TECNOLOGICA",
            value: 16
          },
          {
            text: "TEUSAQUILLO",
            value: 17
          },
          {
            text: "THOMAS JEFFERSON",
            value: 18
          },
          {
            text: "UGI ILUD",
            value: 19
          },
          {
            text: "VIVERO",
            value: 20
          }
        ],
        opt_dependencia: [
          {
            text: "Coordinación laboratorios facultad de ingeniería",
            value: 1
          }
        ],
        opt_idsede: [
          {
            text: "FAAS01",
            value: 1,
            dependency: 1
          },
          {
            text: "FALC01",
            value: 1,
            dependency: 2
          },
          {
            text: "00AP01",
            value: 1,
            dependency: 3
          },
          {
            text: "FMCT01",
            value: 1,
            dependency: 4
          },
          {
            text: "FICC01",
            value: 1,
            dependency: 5
          },
          {
            text: "#N/A",
            value: 1,
            dependency: 6
          },
          {
            text: "00EM01",
            value: 1,
            dependency: 7
          },
          {
            text: "#N/A",
            value: 1,
            dependency: 8
          },
          {
            text: "#N/A",
            value: 1,
            dependency: 9
          },
          {
            text: "FCMAB3",
            value: 1,
            dependency: 10
          },
          {
            text: "FCMB02",
            value: 1,
            dependency: 11
          },
          {
            text: "00POB1",
            value: 1,
            dependency: 12
          },
          {
            text: "FCPO01",
            value: 1,
            dependency: 13
          },
          {
            text: "#N/A",
            value: 1,
            dependency: 14
          },
          {
            text: "FASO01",
            value: 1,
            dependency: 15
          },
          {
            text: "FTTE10",
            value: 1,
            dependency: 16
          },
          {
            text: "#N/A",
            value: 1,
            dependency: 17
          },
          {
            text: "#N/A",
            value: 1,
            dependency: 18
          },
          {
            text: "#N/A",
            value: 1,
            dependency: 19
          },
          {
            text: "FMVI04",
            value: 1,
            dependency: 20
          }
        ],
        opt_salas: [
          {
            text: "LABORATORIO DE CIRCUITOS",
            value: 1,
            dependency: 1
          },
            {
            text: "LABORATORIO DE ELECTRONICA A",
            value: 2,
            dependency: 1
          },
           {
            text: "LABORATORIO DE ELECTRONICA B",
            value: 3,
            dependency: 1
          },
           {
            text: "LABORATORIO DE BASICA",
            value: 4,
            dependency: 1
          },
           {
            text: "LABORATORIO DE DIGITALES",
            value: 5,
            dependency: 1
          },   
          {
            text: "LABORATORIO DE COMUNICACIONES",
            value: 6,
            dependency: 1
          },
          {
            text: "LABORATORIO DE CONTROL",
            value: 7,
            dependency: 1
          },
          {
            text: "LABORATORIO DE MAQUINAS",
            value: 8,
            dependency: 1
          },
           {
            text: "LABORATORIO FESTO",
            value: 9,
            dependency: 1
          },
          {
            text: "FISICA 509",
            value: 10,
            dependency: 1
          },
          {
            text: "FISICA 510",
            value: 11,
            dependency: 1
          },
          {
            text: "SALA DE SISTEMAS 500",
            value: 12,
            dependency: 1
          },
          {
            text: "SALA DE SISTEMAS 501",
            value: 13,
            dependency: 1
          },
          {
            text: "SALA DE SISTEMAS 502",
            value: 14,
            dependency: 1
          },
          {
            text: "SALA DE SISTEMAS 503",
            value: 15,
            dependency: 1
          },
          {
            text: "SALA DE SISTEMAS 504",
            value: 16,
            dependency: 1
          },
          {
            text: "SALA DE SISTEMAS 505",
            value: 17,
            dependency: 1
          },
          {
            text: "SALA DE SISTEMAS 506",
            value: 18,
            dependency: 1
          },
          {
            text: "SALA DE SISTEMAS 507",
            value: 19,
            dependency: 1
          },
          {
            text: "SALA DE SISTEMAS 508",
            value: 20,
            dependency: 1
          },
          {
            text: "SALA DE SISTEMAS 601",
            value: 21,
            dependency: 1
          },
          {
            text: "SALA DE SISTEMAS 701",
            value: 22,
            dependency: 1
          },

          {
            text: "SALA DE SISTEMAS 702",
            value: 23,
            dependency: 1
          },

          {
            text: "SALA DE SISTEMAS 703",
            value: 24,
            dependency: 1
          },

          {
            text: "SALA DE SISTEMAS 704",
            value: 25,
            dependency: 1
          },

          {
            text: "SALA DE SISTEMAS 706",
            value: 26,
            dependency: 1
          },

          {
            text: "SALA DE SISTEMAS 707",
            value: 27,
            dependency: 1
          }
        ]
      }
    };
  },
  computed: {
    filteredDatasedes() {
      let options = this.options.opt_idsede;
      return options.filter(o => o.dependency == this.sede);
    },
    filteredDatalabs() {
      let options = this.options.opt_salas;
      return options.filter(o => o.dependency == this.dependencia);
    },
    computedDateFormatted() {
      return this.formatDate(this.date);
    }
  },
  watch: {
    date(val) {
      this.fechaAdquisicion = this.formatDate(this.date);
    }
  },
  methods: {
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${day}/${month}/${year}`;
    },
    formSubmit() {
      this.errors=[]
      if (
        this.placa &&
        this.serial &&
        this.nombreEquipo &&
        this.estado &&
        this.serie &&
        this.modelo &&
        this.marca &&
        this.numeroInterno &&
        this.sede &&
        this.idSede &&
        this.dependencia &&
        this.idUbicacion &&
        this.espacioFisico &&
        this.proveedor &&
        this.valorElemento &&
        this.nit &&
        this.ivaAplicado &&
        this.tipoContrato &&
        this.totalValorelemento &&
        this.cantidadAsignada &&
        this.vigencia &&
        this.fechaAdquisicion &&
        this.numeroContrato &&
        this.numeroFactura &&
        this.tiempoGarantia &&
        this.frecuenciaMantenimiento &&
        this.manual &&
        this.tiempoVidautil &&
        this.tipoUso &&
        this.potenciaElectrica &&
        this.tipoUso_otro &&
        this.paisOrigen &&
        this.impactoEquipo &&
        this.especificacionesTecnicas &&
        this.accesorios &&
        this.documentoFuncionario &&
        this.nombreFuncionario
      ) {
        //let currentObj = this.$refs.form;
        let objeto = this;
        this.axios
          .post(
            "http://" +
              objeto.$serverURI +
              ":" +
              objeto.$serverPort +
              "/Usuario/registrarEquipo",
            {
              placa: this.placa,
              serial: this.serial,
              nombreEquipo: this.nombreEquipo.toUpperCase(),
              estado: this.estado,
              serie: this.serie.toUpperCase(),
              modelo: this.modelo,
              marca: this.marca.toUpperCase(),
              numeroInterno: this.numeroInterno,
              sede: this.sede,
              idSede: this.idSede,
              dependencia: this.dependencia,
              idUbicacion: this.idUbicacion,
              espacioFisico: this.espacioFisico,
              proveedor: this.proveedor,
              valorElemento: this.valorElemento,
              nit: this.nit,
              ivaAplicado: this.ivaAplicado,
              tipoContrato: this.tipoContrato,
              totalValorelemento: this.totalValorelemento,
              cantidadAsignada: this.cantidadAsignada,
              vigencia: this.vigencia,
              fechaAdquisicion: this.fechaAdquisicion,
              numeroContrato: this.numeroContrato,
              numeroFactura: this.numeroFactura,
              tiempoGarantia: this.tiempoGarantia,
              frecuenciaMantenimiento: this.frecuenciaMantenimiento,
              manual: this.manual,
              tiempoVidautil: this.tiempoVidautil,
              tipoUso: this.tipoUso,
              potenciaElectrica: this.potenciaElectrica,
              tipoUso_otro: this.tipoUso_otro.toUpperCase(),
              paisOrigen: this.paisOrigen.toUpperCase(),
              impactoEquipo: this.impactoEquipo,
              especificacionesTecnicas: this.especificacionesTecnicas.toUpperCase(),
              accesorios: this.accesorios.toUpperCase(),
              documentoFuncionario: this.documentoFuncionario,
              nombreFuncionario: this.nombreFuncionario.toUpperCase()
            },
            {
              headers: {
                "Content-Type": "application/json"
              }
            }
          )
          .then(function(response) {
            if (response.data.status == 1) {
              objeto.vista = true;
              objeto.output = response.data.mensaje;
              var respuesta = response.data.mensaje;
              alert(respuesta);
            } else if (response.data.status == 2) {
              objeto.vista = true;
              objeto.output = response.data.status;
            } else {
              objeto.vista = true;
              objeto.output = "Ha ocurrido un error";
            }
          })
          .catch(function(error) {
            objeto.output = error;
          });
      }
      else{
        if (!this.placa) this.errors.push("Placa requerida.")
        if (!this.serial) this.errors.push("Serial requerido.")
        if (!this.nombreEquipo) this.errors.push("Nombre Equipo requerida.")
        if (!this.estado) this.errors.push("Estado requerido.")
        if (!this.serie) this.errors.push("Serie requerido.")
        if (!this.modelo) this.errors.push("Modelo requerido.")
        if (!this.marca) this.errors.push("Marca requerida.")
        if (!this.numeroInterno) this.errors.push("Número interno requerido.")
        if (!this.sede) this.errors.push("Sede requerida.")
        if (!this.idSede) this.errors.push("Id sede requerida.")
        if (!this.dependencia) this.errors.push("Dependencia requerida.")
        if (!this.idUbicacion) this.errors.push("Id ubicación requerido.")
        if (!this.espacioFisico) this.errors.push("Espacio físico requerido.")
        if (!this.proveedor) this.errors.push("Proveedor requerido.")
        if (!this.valorElemento) this.errors.push("Valor elemento requerido.")
        if (!this.nit) this.errors.push("NIT requerido.")
        if (!this.ivaAplicado) this.errors.push("Iva aplicado requerido.")
        if (!this.tipoContrato) this.errors.push("Tipo contrato requerido.")
        if (!this.totalValorelemento) this.errors.push("Total valor elemento requerido.")
        if (!this.cantidadAsignada) this.errors.push("Cantidad asignada requerido.")
        if (!this.vigencia) this.errors.push("Vigencia requerido.")
        if (!this.fechaAdquisicion) this.errors.push("Fecha adquisición requerido.")
        if (!this.numeroContrato) this.errors.push("Número contrato requerida.")
        if (!this.numeroFactura) this.errors.push("Número factura requerido.")
        if (!this.tiempoGarantia) this.errors.push("Tiempo garantía requerida.")
        if (!this.frecuenciaMantenimiento ) this.errors.push("Frecuencia mantenimiento requerida.")
        if (!this.manual) this.errors.push("Manual requerida.")
        if (!this.tiempoVidautil) this.errors.push("Tiempo vida útil requerido.")
        if (!this.tipoUso) this.errors.push("Tipo uso requerido.")
        if (!this.potenciaElectrica) this.errors.push("Potencia eléctrica requerido.")
        if (!this.tipoUso_otro) this.errors.push("Tipo uso Otro requerido.")
        if (!this.paisOrigen) this.errors.push("País origen requerido.")
        if (!this.impactoEquipo) this.errors.push("Impacto equipo requerido.")
        if (!this.especificacionesTecnicas) this.errors.push("Especificaciones téncicas requeridas.")
        if (!this.accesorios) this.errors.push("Accesorios requerido.")
        if (!this.documentoFuncionario) this.errors.push("Documento funcionario requerido.")
        if (!this.nombreFuncionario) this.errors.push("Nombre funcionario requerido.")
        }
    }
  }
};
</script>