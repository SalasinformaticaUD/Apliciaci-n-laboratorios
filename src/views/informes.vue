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
                @click="createExcel" 
                dark
            >
            Generar Excel
            <v-icon dark right>fas fa-file-csv</v-icon>
            </v-btn>
        </v-flex>
    </v-layout>
    <v-layout>
      <v-flex xs6>
          <canvas ref="myChart" v-if=true> </canvas>
      </v-flex>
    </v-layout>
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
    chartToPng: "",
    usuariolab: [],
  }),
  created() {
    this.initialize();
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

  methods: {
    createExcel(){
      let objeto = this;
      this.axios
        .get("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/createExcel", {
          responseType: 'blob',
        })
        .then(function(response) {
          // Para guardar el documento se crea una etiqueta <a> para asociar un href con un URL y agregarle el atributo de descargar
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', 'Informe.xlsx');
          link.click();
        })
        .catch(function(error) {
          objeto.output = error;
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
        let data = this.usuariolab.map(obj => [obj.nombreEquipo, obj.serie, obj.placa, obj.estado,obj.espacioFisico,obj.nombreFuncionario,obj.sede,obj.valorElemento]);

        // A la autotabla se le indican la cabeccera y el contenido (body). .slice es para no mostrar todos os datos sino solo una cantidad. 
        pdf.autoTable({
          head: [['Equipo','Serie','Placa','Estado','Espacio Físico','Nombre Funcionario','Sede','Valor Elemento']],
          body: data.slice(0,4),
          margin:{top:60},
          theme: 'grid',
          styles:{halign: 'center'},
          headStyles: { fillColor: [198,31,31] },
        }) 
        
        // Para obtener la coordenada en Y donde termino la tabla
        let finalY = pdf.previousAutoTable.finalY;

        // Se crea la instancia de la imagen tomada de chart.js y se agrega al documento luego de la tabla
        var grafica = new Image();
        grafica.src = this.chartToPng;
        pdf.addImage(grafica, 'PNG', 10, finalY+8, 130, 70);
        
        pdf.save('NuevoInforme.pdf');
    },
    initialize() {
      (this.usuariolab = []), this.buscar();
    },
    buscar() {
      let objeto = this;
      this.axios
        .get("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/consultarEquipo", {
          headers: {
            "Content-Type": "application/json"
          }
        })
        .then(function(response) {
          objeto.usuariolab = response.data.data;
        })
        .catch(function(error) {
          objeto.output = error;
        });
    }
  }
};
</script>