<template>
  <v-container fluid>
    <HeaderLaboratorista/>
    <v-layout wrap align-center>
        <v-flex text-right>
            <v-btn 
                elevation="2" 
                class="ma-2" 
                @click="createPDF" 
                color="red darken-4" 
                dark
            >
            Generar PDF
            <v-icon dark right>fas fa-file-pdf</v-icon>
            </v-btn>
        </v-flex>
        <v-flex text-left>
            <v-btn 
                elevation="2" 
                class="ma-2" 
                color="success" 
                @click="selectCampos" 
                dark
            >
            Generar Excel
            <v-icon dark right>fas fa-file-csv</v-icon>
            </v-btn>
        </v-flex>
    </v-layout>
    <v-layout>
      <v-flex xs6>
          <canvas ref="myChart" v-if=false> </canvas>
      </v-flex>
    </v-layout>

    <v-dialog
      v-model="dialogSelect"
      scrollable
      max-width="700px"
      dark
    >
      <v-card dark>
          <v-card-text>
            <v-container fluid>
              <v-row>
                <div class="headline"> Seleccione los campos que desea agregar al documento</div>
              </v-row>
              <v-row no-gutters>
                <v-col cols="12" sm="4">
                  <v-checkbox
                  v-model = "selectAllElements"
                  label = "Seleccionar todos los campos"
                  ></v-checkbox>
                </v-col>
              </v-row>
              <v-row no-gutters>
                <v-col v-for="(item, prop, index) in selectedElements" :key="prop" cols="12" sm="4">
                  <v-checkbox
                  v-model = "selectedElements[prop]"
                  :label = "elementsKeys[index]"
                  ></v-checkbox>
                </v-col>
              </v-row>
              <v-row justify="center" no-gutters>
                <v-btn 
                elevation="2" 
                class="ma-2" 
                color="success" 
                @click="createExcel" 
                dark
                >Descargar
                <v-icon dark right>fas fa-file-csv</v-icon>
                </v-btn>
              </v-row>
            </v-container>
          </v-card-text>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import HeaderLaboratorista from "@/components/HeaderLaboratorista.vue";

import jsPDF from "jspdf";
import 'jspdf-autotable';
import Chart from 'chart.js';

export default {
  components: {
    HeaderLaboratorista
  },
  data: () => ({
    chartToPng: "", // Almacena la imagen del canvas
    elementos: [], // Toma los elementos de la base de datos. Se llena en el created

    // elementsKeys son los label de los checkbox y debe coincidir en el mismo orden que selectedElements, ya que este ultimo es para el proceso de validacion en Python. El nombre de las propiedades de selectedElements debe ser exactamente el mismo que se tiene en la base de datos
    elementsKeys: ["Nombre del equipo","Referencia/Modelo","Serie","Marca","Placa","Estado","Sede","Id Sede","Dependencia","Espacio Físico","Id Ubicación","Cantidad asignada","Código Interno","Frecuencia de mantenimiento","Tiempo de vida útil","Potencia eléctrica","Especificaciones técnicas","Cuenta con manual","Accesorios","Tipo de uso","Otro tipo de uso","Impacto del uso del equipo","País de origen","Proveedor","Nit","Tipo de contrato","Vigencia","Fecha de adquisición","Número de contrato","Valor del elemento","Iva aplicado","Valor total del elemento","Número de la factura de compra","Tiempo de garantía","Nombre del funcionario","Documento del funcionario"],
    selectedElements:{
      Nombre_Del_Equipo: false,
      "Referencia/Modelo": false,
      Serie: false,
      Marca: false,
      Placa: false,
      Estado: false,
      Sede: false,
      Id_Sede: false,
      Dependencia: false,
      Espacio_Fisico: false,
      Id_Ubicacion: false,
      Cantidad_Asignada: false,
      Codigo_Interno: false,
      Frecuencia_De_Mantenimiento: false,
      Tiempo_De_Vida_Util: false,
      Potencia_Electrica: false,
      Especificaciones_Tecnicas: false,
      Cuenta_Con_Manual: false,
      Accesorios: false,
      Tipo_De_Uso: false,
      Tipo_De_Uso_Otro: false,
      Impacto_Uso_Del_Equipo: false,
      Pais_De_Origen: false,
      Proveedor: false,
      Nit: false,
      Tipo_De_Contrato: false,
      Vigencia: false,
      Fecha_De_Adquisicion: false,
      Numero_De_Contrato: false,
      Valor_Elemento: false,
      Iva_Aplicado: false,
      Total_Valor_Elemento: false,
      "#_De_Factura_Compra": false,
      Tiempo_De_Garantia: false,
      Nombre_Del_Funcionario: false,
      Documento_Funcionario: false,
    },
    dialogSelect: false, // Para activar o desactivar el v-dialog
    selectAllElements: false, // Para el checkbox de seleccionar todos los elementos. Esta asociado a un watcher
  }),
  created() {
    this.buscar();
  },
  mounted(){
    // Se crea la instancia de chart.js. En el atributo type se le indica que la grafica es tipo pie. En el atributo data se le indica los parametros de las graficas incuyendo colores. En el atributo options se le indican parametros adicionales como animaciones, eventos, ubicacion del legend. 
    let chartPie = new Chart(this.$refs.myChart, {
      type: 'pie',
      data: {
        labels: ['Total Conectados', 'Total Equipos', 'Confiabilidad'],
        datasets:[{
          data: [35, 35, 30],
          backgroundColor: ["#FFFA24", "#ff9900", "#4d4dff"],
          // borderColor: ["#FFFA24", "#ff9900", "#4d4dff"]
        }]
      },
      options:{
        animation: false,
        legend: {labels:{fontSize:14},
                position:'right'}

        }
    });
    // Luego de haber renderizado la imagen se puede convertir a imagen y se guarda en una variable global. Se debe ajustar la funcion para que se renderice luego de la animacion. Sale un warning en la consola
    this.chartToPng = chartPie.toBase64Image();
  },
  watch:{
    // Revisa la variable de seleccionar todos los campos para conmutarlos entre true y false
    selectAllElements: function(val){
      for (let item in this.selectedElements){
        if(this.selectAllElements==true){
          this.selectedElements[item] = true
        }else{
          this.selectedElements[item] = false
        }
      }
    }
  },
  methods: {
    selectCampos(){ // Metodo para abrir el v-dialog con todos los checkbox en false
      for (let item in this.selectedElements){
        this.selectedElements[item] = false
      }      
      this.selectAllElements = false;
      this.dialogSelect = true;
    },
    createExcel(){
      // Se hace primero una peticion post para validar los campos en python y crear una coleccion temporal en mongo. En la promesa del post se hace la peticion get para descargar el documento excel
      let objeto = this;
      this.axios
        .post(
          "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/excelTemporalElementos",JSON.stringify(this.selectedElements),
          {
            headers: {
              "Content-Type": "application/json",
              "Authorization": this.$cookies.get("jwt") ? "Bearer " + this.$cookies.get("jwt") : "",
            }
          }
        )
        .then(function(response) {
          var respuesta = response.data.mensaje;
          var status = response.data.status;
          if (status==1){
            objeto.axios
            .get("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/createExcel", {responseType: 'blob'})
            .then(function(response) {
            if (response.data.status == 401) {                                
              objeto.$router.push('/');
              alert("Error de sesion");                
            }else{
              // Para guardar el documento se crea una etiqueta <a> para asociar un href con un URL y agregarle el atributo de descargar
              const url = window.URL.createObjectURL(new Blob([response.data]));
              const link = document.createElement('a');
              link.href = url;
              link.setAttribute('download', 'Informe.xlsx');
              link.click();
              objeto.dialogSelect = false; //Cierra el v-dialog luego de descargar
            }
            })
            .catch(function(error) {
              objeto.output = error;
            });
          }
        })
        .catch(function(error) {
          alert(error);
        });
      },

    createPDF () { 
        // Para jsPDF se trabaja con coordenadas de la hoja con formato A4, (x,y) donde x varia entre 0 mm y 210 (mm) y y varia entre 0 mm y 297 mm. La coordenada (0,0) es la esquina superior izquierda del documento. 

        // Se crea la instancia de jsPDF
        var pdf = new jsPDF();

        // Se indica el ancho de linea y el tamaño de letra para jsPDF
        pdf.setLineWidth(0.4);          
        pdf.setFontSize(9);        

        // Se hace el rectangulo que contiene la cabecera y luego se asocian las tres lineas de texto
        pdf.rect(20, 20, 170, 22);
        pdf.text("MANTENIMIENTOS LABORATORIOS DE INGENIERIA", 105, 27,'center');
        pdf.text("SALAS DE INFORMATICA TRIMESTRE II", 105, 32,'center');
        pdf.text("PERIODO COMPRENDIDO ENTRE EL 1 DE ABRL HASTA EL 30 DE ABRIL DEL 2020", 105, 37,'center');

        // Se hace la instancia de la imagen y se le referencia la fuente. Se agrega al pdf y se indica el tamaño
        var imgLab = new Image();
        imgLab.src = '../logo.png';
        pdf.addImage(imgLab, 'PNG', 171, 21, 15, 20);

        var imgUD = new Image();
        imgUD.src = '../preloader.png';
        pdf.addImage(imgUD, 'PNG', 25, 21, 15, 20);

        // Se toma la información de la base de datos y se crea un arreglo con la informacion de los objetos. Cada objeto es una fila.
        let data = this.elementos.map(obj => [obj.Nombre_Del_Equipo, obj.Serie, obj.Placa, obj.Estado,obj.Espacio_Fisico,obj.Nombre_Del_Funcionario,obj.Sede,obj.Valor_Elemento]);

        // A la autotabla se le indican la cabeccera y el contenido (body). .slice es para no mostrar todos os datos sino solo una cantidad. 
        pdf.autoTable({
          head: [['Equipo','Serie','Placa','Estado','Espacio Físico','Nombre Funcionario','Sede','Valor Elemento']],
          body: data.slice(0,6),
          margin:{top:60},
          theme: 'grid',
          styles:{halign: 'center'},
          headStyles: { fillColor: [198,31,31] },
        }) 
        
        // Para obtener la coordenada en Y donde termino la tabla
        let finalY = pdf.previousAutoTable.finalY;


        // Se tiene en comentarios la adicion del grafico hasta no estudiar bien como convertir el canvas en imagen

        // Se crea la instancia de la imagen tomada de chart.js y se agrega al documento luego de la tabla
        // var grafica = new Image();
        // grafica.src = this.chartToPng;
        // pdf.addImage(grafica, 'PNG', 10, finalY+8, 130, 70);
        
        pdf.save('NuevoInforme.pdf');
    },
    buscar() {
      let objeto = this;
      objeto.axios
        .get("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/obtenerElementosExcel", {
          headers: {
            "Content-Type": "application/json",
            "Authorization": this.$cookies.get("jwt") ? "Bearer " + this.$cookies.get("jwt") : "",
          }
        })
        .then(function(response) {
          
          if (response.data.status == 401) {                                
            objeto.$router.push('/');
            alert("Error de sesion");                
          }
          objeto.elementos = response.data.data;
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>