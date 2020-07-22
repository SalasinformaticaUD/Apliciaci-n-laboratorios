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
                    <v-text-field v-model="placa" label="Placa" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="serial" label="Serial" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="nombreEquipo" label="Nombre del equipo" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="modelo" label="Modelo" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="estado" label="Estado" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="serie" label="Serie" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="marca" label="Marca" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="numeroInterno" label="Número interno" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="nombreFuncionario" label="Nombre del funcionario" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field
                      v-model="documentoFuncionario"
                      label="Documento del funcionario"
                      solo
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
                    <v-text-field v-model="sede" label="Sede" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="idSede" label="Id sede" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="dependencia" label="Dependencia" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="idUbicacion" label="Id ubicación" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="espacioFisico" label="Espacio fisico" solo></v-text-field>
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
                    <v-text-field v-model="proveedor" label="Proveedor" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="valorElemento" label="Valor elemento" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="nit" label="Nit" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="ivaAplicado" label="IVA aplicado" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="tipoContrato" label="Tipo de contrato" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="totalValorelemento" label="Total valor de elemento" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="vigencia" label="Vigencia" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="cantidadAsignada" label="Cantidad asignada" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="fechaAdquisicion" label="Fecha de adquisición" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="numeroContrato" label="Número de contrato" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="numeroFactura" label="Número de factura de compra" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="tiempoGarantia" label="Tiempo de garantía" solo></v-text-field>
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
                    ></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="manual" label="Cuenta con manual" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="tiempoVidautil" label="Tiempo de vida util" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="tipoUso" label="Tipo de uso" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="potenciaElectrica" label="Potencia Eléctrica" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="tipoUso_otro" label="Tipo de uso-otro" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="paisOrigen" label="País de origen" solo></v-text-field>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-text-field v-model="impactoEquipo" label="Impacto del equipo" solo></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-textarea
                      v-model="especificacionesTecnicas"
                      label="Especificaciones técnicas"
                      solo
                    ></v-textarea>
                  </v-col>
                  <v-col class="col-sm-12 col-lg-6">
                    <v-textarea v-model="accesorios" label="Accesorios" solo></v-textarea>
                  </v-col>
                </v-row>
              </v-card>
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
      fechaAdquisicion: "",
      numeroContrato: "",
      numeroFactura: "",
      tiempoGarantia: "",
      frecuenciaMantenimiento: "",
      manual: "",
      tiempoVidautil: "",
      tipoUso: "",
      potenciaElectrica: "",
      tipoUso_otro: "",
      paisOrigen: "",
      impactoEquipo: "",
      especificacionesTecnicas: "",
      accesorios: "",
      documentoFuncionario: "",
      nombreFuncionario: ""
    };
  },
  methods: {
    formSubmit() {
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
              sede: this.sede.toUpperCase(),
              idSede: this.idSede,
              dependencia: this.dependencia.toUpperCase(),
              idUbicacion: this.idUbicacion,
              espacioFisico: this.espacioFisico.toUpperCase(),
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
    }
  }
};
</script>