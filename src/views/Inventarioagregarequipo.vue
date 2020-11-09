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
              <v-btn text @click="volverpag()">Cancel</v-btn>
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

               
                  <v-col class="col-sm-6 col-lg-3">
                   <v-autocomplete :items="options.opt_ubicacion" v-model="TipoUbicacion" label="Tipo de ubicación" solo
                    :rules="[rules.required]"></v-autocomplete>
                  </v-col>
                  <v-col class="col-sm-6 col-lg-3">
                     <v-autocomplete :items="filteredDataubicacion" v-model="numeroidUbicacion" label="Número" solo
                    :rules="[rules.required]"></v-autocomplete>
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
              <v-btn text @click="volverpag()">Cancel</v-btn>
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
              <v-btn text @click="volverpag()">Cancel</v-btn>
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
                    <v-text-field v-model="tiempoVidautil" label="Tiempo de vida útil" solo
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
                      auto-grow
                      rows="1"
                      solo
                      :rules="[rules.required]"
                    ></v-textarea>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-textarea v-model="accesorios" label="Accesorios" auto-grow
                    rows="1" 
                    solo
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
              <v-btn text @click="volverpag()">Cancel</v-btn>
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
      usuario:"",
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
      TipoUbicacion:"",
      numeroidUbicacion:"",
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
      options: {
        opt_sede: [
          {
            text: "ACADEMIA SUPERIOR ARTES-ASAB",
            value: "ACADEMIA SUPERIOR ARTES-ASAB"
          },
          {
            text: "ACADEMICA LUIS A. CALVO",
            value: "ACADEMICA LUIS A. CALVO"
          },
          {
            text: "ADUANILLA DE PAIBA",
            value: "ADUANILLA DE PAIBA"
          },
          {
            text: "CALLE 34",
            value: "CALLE 34"
          },
          {
            text: "CALLE 40",
            value: "CALLE 40"
          },
          {
            text: "CENTRO CULTURAL NUEVA SANTAFE",
            value: "CENTRO CULTURAL NUEVA SANTAFE"
          },
          {
            text: "EMISORA",
            value: "EMISORA"
          },
          {
            text: "GRUPO DESARROLLO FISICO - PIGA",
            value: "GRUPO DESARROLLO FISICO - PIGA"
          },
          {
            text: "IDEXUD",
            value: "IDEXUD"
          },
          {
            text: "MACARENA - A",
            value: "MACARENA - A"
          },
          {
            text: "MACARENA - B",
            value: "MACARENA - B"
          },
          {
            text: "PORVENIR BOSA",
            value: "PORVENIR BOSA"
          },
          {
            text: "POSGRADOS",
            value: "POSGRADOS"
          },
          {
            text: "SECCION DE PUBLICACIONES",
            value: "SECCION DE PUBLICACIONES"
          },
          {
            text: "SOTANOS AVENIDA JIMENEZ",
            value: "SOTANOS AVENIDA JIMENEZ"
          },
          {
            text: "TECNOLOGICA",
            value: "TECNOLOGICA"
          },
          {
            text: "TEUSAQUILLO",
            value: "TEUSAQUILLO"
          },
          {
            text: "THOMAS JEFFERSON",
            value: "THOMAS JEFFERSON"
          },
          {
            text: "UGI ILUD",
            value: "UGI ILUD"
          },
          {
            text: "VIVERO",
            value: "VIVERO"
          }
        ],
        opt_dependencia: [
          {
            text: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA",
            value: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          }
        ],
        opt_ubicacion:[
          {
            text: "PUESTO",
            value: "PUESTO"
          },{
            text: "BANCO",
            value: "BANCO",            
          },{
            text: "STAND",
            value: "STAND",           
          },{
            text: "ARMARIO",
            value: "ARMARIO",        
          }       
        ],
        opt_idsede: [
          {
            text: "FAAS01",
            value: "FAAS01",
            dependency: "ACADEMIA SUPERIOR ARTES-ASAB"
          },
          {
            text: "FALC01",
            value: "FALC01",
            dependency: "ACADEMICA LUIS A. CALVO"
          },
          {
            text: "00AP01",
            value: "00AP01",
            dependency: "ADUANILLA DE PAIBA"
          },
          {
            text: "FMCT01",
            value:"FMCT01",
            dependency: "CALLE 34"
          },
          {
            text: "FICC01",
            value: "FICC01",
            dependency: "CALLE 40"
          },
          {
            text: "#N/A",
            value: "#N/A",
            dependency: "CENTRO CULTURAL NUEVA SANTAFE"
          },
          {
            text: "00EM01",
            value: "00EM01",
            dependency: "EMISORA"
          },
          {
            text: "#N/A",
            value: "#N/A",
            dependency: "GRUPO DESARROLLO FISICO - PIGA"
          },
          {
            text: "#N/A",
            value: "#N/A",
            dependency: "IDEXUD"
          },
          {
            text: "FCMAB3",
            value: "FCMAB3",
            dependency: "MACARENA - A"
          },
          {
            text: "FCMB02",
            value: "FCMB02",
            dependency: "MACARENA - B"
          },
          {
            text: "00POB1",
            value: "00POB1",
            dependency: "PORVENIR BOSA"
          },
          {
            text: "FCPO01",
            value: "FCPO01",
            dependency: "POSGRADOS"
          },
          {
            text: "#N/A",
            value: "#N/A",
            dependency: "SECCION DE PUBLICACIONES"
          },
          {
            text: "FASO01",
            value: "FASO01",
            dependency: "SOTANOS AVENIDA JIMENEZ"
          },
          {
            text: "FTTE10",
            value: "FTTE10",
            dependency:  "TECNOLOGICA"
          },
          {
            text: "#N/A",
            value: "#N/A",
            dependency: "TEUSAQUILLO"
          },
          {
            text: "#N/A",
            value: "#N/A",
            dependency: "THOMAS JEFFERSON"
          },
          {
            text: "#N/A",
            value: "#N/A",
            dependency: "UGI ILUD"
          },
          {
            text: "FMVI04",
            value: "FMVI04",
            dependency: "VIVERO"
          }
        ],
        opt_salas: [
          {
            text: "ALMACEN",
            value: "ALMACEN",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "LABORATORIO DE CIRCUITOS",
            value: "LABORATORIO DE CIRCUITOS",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
            {
            text: "LABORATORIO DE ELECTRONICA A",
            value:  "LABORATORIO DE ELECTRONICA A",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
           {
            text: "LABORATORIO DE ELECTRONICA B",
            value: "LABORATORIO DE ELECTRONICA B",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
           {
            text: "LABORATORIO DE BASICA",
            value: "LABORATORIO DE BASICA",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
           {
            text: "LABORATORIO DE DIGITALES",
            value: "LABORATORIO DE DIGITALES",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },   
          {
            text: "LABORATORIO DE COMUNICACIONES",
            value: "LABORATORIO DE COMUNICACIONES",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "LABORATORIO DE CONTROL",
            value: "LABORATORIO DE CONTROL",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "LABORATORIO DE MAQUINAS",
            value: "LABORATORIO DE MAQUINAS",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
           {
            text: "LABORATORIO FESTO",
            value: "LABORATORIO FESTO",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "FISICA 509",
            value: "FISICA 509",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "FISICA 510",
            value: "FISICA 510",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "SALA DE SISTEMAS 500",
            value:"SALA DE SISTEMAS 500",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "SALA DE SISTEMAS 501",
            value: "SALA DE SISTEMAS 501",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "SALA DE SISTEMAS 502",
            value: "SALA DE SISTEMAS 502",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "SALA DE SISTEMAS 503",
            value:"SALA DE SISTEMAS 503",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "SALA DE SISTEMAS 504",
            value: "SALA DE SISTEMAS 504",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "SALA DE SISTEMAS 505",
            value: "SALA DE SISTEMAS 505",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "SALA DE SISTEMAS 506",
            value: "SALA DE SISTEMAS 506",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "SALA DE SISTEMAS 507",
            value: "SALA DE SISTEMAS 507",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "SALA DE SISTEMAS 508",
            value: "SALA DE SISTEMAS 508",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "SALA DE SISTEMAS 601",
            value: "SALA DE SISTEMAS 601",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },
          {
            text: "SALA DE SISTEMAS 701",
            value: "SALA DE SISTEMAS 701",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },

          {
            text: "SALA DE SISTEMAS 702",
            value: "SALA DE SISTEMAS 702",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },

          {
            text: "SALA DE SISTEMAS 703",
            value: "SALA DE SISTEMAS 703",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },

          {
            text: "SALA DE SISTEMAS 704",
            value: "SALA DE SISTEMAS 704",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },

          {
            text: "SALA DE SISTEMAS 706",
            value: "SALA DE SISTEMAS 706",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          },

          {
            text: "SALA DE SISTEMAS 707",
            value: "SALA DE SISTEMAS 707",
            dependency: "COORDINACIÓN DE LABORATORIOS DE INGENIERÍA"
          }
        ],
        opt_numeroUbicacion: [
          {
            text: "1",
            value: "1",
            dependency: "PUESTO"
          }, {
            text: "2",
            value: "2",
            dependency: "PUESTO"
          }, {
            text: "3",
            value: "3",
            dependency: "PUESTO"
          }, {
            text: "4",
            value: "4",
            dependency: "PUESTO"
          }, {
            text: "5",
            value: "5",
            dependency: "PUESTO"
          },  {
            text: "6",
            value: "6",
            dependency: "PUESTO"
          },  {
            text: "7",
            value: "7",
            dependency: "PUESTO"
          },  {
            text: "8",
            value: "8",
            dependency: "PUESTO"
          },  {
            text: "9",
            value: "9",
            dependency: "PUESTO"
          },  {
            text: "10",
            value: "10",
            dependency: "PUESTO"
          },  {
            text: "11",
            value: "11",
            dependency: "PUESTO"
          },  {
            text: "12",
            value: "12",
            dependency: "PUESTO"
          },  {
            text: "13",
            value: "13",
            dependency: "PUESTO"
          },  {
            text: "14",
            value: "14",
            dependency: "PUESTO"
          },  {
            text: "15",
            value: "15",
            dependency: "PUESTO"
          },  {
            text: "16",
            value: "16",
            dependency: "PUESTO"
          },  {
            text: "17",
            value: "17",
            dependency: "PUESTO"
          },{
            text: "18",
            value: "18",
            dependency: "PUESTO"
          },{
            text: "19",
            value: "19",
            dependency: "PUESTO"
          },{
            text: "20",
            value: "20",
            dependency: "PUESTO"
          },{
            text: "21",
            value: "21",
            dependency: "PUESTO"
          },{
            text: "22",
            value: "22",
            dependency: "PUESTO"
          },{
            text: "23",
            value: "23",
            dependency: "PUESTO"
          },{
            text: "24",
            value: "24",
            dependency: "PUESTO"
          },{
            text: "25",
            value: "25",
            dependency: "PUESTO"
          },{
            text: "26",
            value: "26",
            dependency: "PUESTO"
          },{
            text: "27",
            value: "27",
            dependency: "PUESTO"
          },{
            text: "28",
            value: "28",
            dependency: "PUESTO"
          },{
            text: "29",
            value: "29",
            dependency: "PUESTO"
          },{
            text: "30",
            value: "30",
            dependency: "PUESTO"
          },{
            text: "31",
            value: "31",
            dependency: "PUESTO"
          },{
            text: "32",
            value: "32",
            dependency: "PUESTO"
          },
          {
            text: "1",
            value: "1",
            dependency: "BANCO"
          },{
            text: "2",
            value: "2",
            dependency: "BANCO"
          },{
            text: "2",
            value: "2",
            dependency: "BANCO"
          },{
            text: "3",
            value: "3",
            dependency: "BANCO"
          },{
            text: "4",
            value: "4",
            dependency: "BANCO"
          },{
            text: "5",
            value: "5",
            dependency: "BANCO"
          },{
            text: "6",
            value: "6",
            dependency: "BANCO"
          },{
            text: "7",
            value: "7",
            dependency: "BANCO"
          },{
            text: "8",
            value: "8",
            dependency: "BANCO"
          },{
            text: "9",
            value: "9",
            dependency: "BANCO"
          },{
            text: "10",
            value: "10",
            dependency: "BANCO"
          },{
            text: "11",
            value: "11",
            dependency: "BANCO"
          },{
            text: "12",
            value: "12",
            dependency: "BANCO"
          },     {
            text: "1",
            value: "1",
            dependency: "STAND"
          }, {
            text: "2",
            value: "2",
            dependency: "STAND"
          }, {
            text: "3",
            value: "3",
            dependency: "STAND"
          }, {
            text: "4",
            value: "4",
            dependency: "STAND"
          }, {
            text: "5",
            value: "5",
            dependency: "STAND"
          },  {
            text: "6",
            value: "6",
            dependency: "STAND"
          },  {
            text: "7",
            value: "7",
            dependency: "STAND"
          },  {
            text: "8",
            value: "8",
            dependency: "STAND"
          },  {
            text: "9",
            value: "9",
            dependency: "STAND"
          },  {
            text: "10",
            value: "10",
            dependency: "STAND"
          },  {
            text: "11",
            value: "11",
            dependency: "STAND"
          },  {
            text: "12",
            value: "12",
            dependency: "STAND"
          },  {
            text: "13",
            value: "13",
            dependency: "STAND"
          },  {
            text: "14",
            value: "14",
            dependency: "STAND"
          },  {
            text: "15",
            value: "15",
            dependency: "STAND"
          },  {
            text: "16",
            value: "16",
            dependency: "STAND"
          },  {
            text: "17",
            value: "17",
            dependency: "STAND"
          },  {
            text: "18",
            value: "18",
            dependency: "STAND"
          }, {
            text: "1",
            value: "1",
            dependency: "ARMARIO"
          }, {
            text: "2",
            value: "2",
            dependency: "ARMARIO"
          }, {
            text: "3",
            value: "3",
            dependency: "ARMARIO"
          }, {
            text: "4",
            value: "4",
            dependency: "ARMARIO"
          }, {
            text: "5",
            value: "5",
            dependency: "ARMARIO"
          },  {
            text: "6",
            value: "6",
            dependency: "ARMARIO"
          }
        
        ],
      }
    };
  },
  mounted(){
    this.initialize();
  },
  computed: {
    filteredDatasedes() {
      let options = this.options.opt_idsede;
      return options.filter(o => o.dependency == this.sede);
    },
       filteredDataubicacion() {
      let options = this.options.opt_numeroUbicacion;
      return options.filter(o => o.dependency == this.TipoUbicacion);
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
     initialize() {

      this.usuario=localStorage.usuario
      console.log(this.usuario)
    },
    volverpag(){
      window.history.back()
    },

    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${day}/${month}/${year}`;
    },
    formSubmit() {
      let objeto = this
      objeto.token = localStorage.cdcb0830cc2dd220;
      let encrypted = objeto.$cookies.get("user_session");
      let desen = objeto.$Crypto.AES.decrypt(encrypted, objeto.token);
      let codlab = desen.toString(objeto.$Crypto.enc.Utf8)
      objeto.codigoLab = codlab;
      objeto.idUbicacion= objeto.TipoUbicacion + " " + objeto.numeroidUbicacion;

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
        this.TipoUbicacion &&
        this.numeroidUbicacion &&
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
              nombreFuncionario: this.nombreFuncionario.toUpperCase(),
              laboratorista : this.usuario,
              codigoLaboratorista: this.codlab
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
        if (!this.TipoUbicacion) this.errors.push("Tipo de ubicación requerida.")
        if (!this.numeroidUbicacion) this.errors.push("Número de la ubicación requerida.")
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