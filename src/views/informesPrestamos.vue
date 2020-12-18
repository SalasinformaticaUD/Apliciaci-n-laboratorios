<template>
  <v-container fluid>
    <HeaderLaboratorista/>
    <v-row no gutters justify="center">
      <v-col cols="12" sm="4">
        <v-select
          v-model="selectTrim"
          :items="itemsTrim"
          label="Periodo de fechas"
          outlined
          dark
        ></v-select>
      </v-col>
      <v-col cols="12" sm="3">
        <v-menu
          v-model="menuCalendarStart"
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
          dark
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="filterStartDate"
              label="Fecha de inicio"
              hint="DD/MM/YYYY"
              persistent-hint
              prepend-icon="far fa-calendar-plus"
              dark
              @blur="dateCalendarStart = parseDate(filterStartDate)"
              @keyup.enter="dateCalendarStart = parseDate(filterStartDate)"
              v-bind="attrs"
              v-on="on"
            >
            </v-text-field>
          </template>
          <v-date-picker v-model="dateCalendarStart" no-title @input="menuCalendarStart = false"></v-date-picker>
        </v-menu>
      </v-col>
      <v-col cols="12" sm="3">
        <v-menu
          v-model="menuCalendarEnd"
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
          dark
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="filterEndDate"
              label="Fecha final"
              hint="DD/MM/YYYY"
              persistent-hint
              prepend-icon="far fa-calendar-plus"
              dark
              @blur="dateCalendarEnd = parseDate(filterEndDate)"
              @keyup.enter="dateCalendarEnd = parseDate(filterEndDate)"
              v-bind="attrs"
              v-on="on"
            >
            </v-text-field>
          </template>
          <v-date-picker v-model="dateCalendarEnd" no-title @input="menuCalendarEnd = false"></v-date-picker>
        </v-menu>
      </v-col>
    </v-row>
    
    <v-row no gutters justify="center">
      <v-col cols="12" sm="10">
        <v-card dark outlined elevation="3">
          <v-card-title>
            Descargar excel de prueba con todo el contenido
          </v-card-title>
            <v-btn 
              elevation="2" 
              class="ma-2" 
              color="success" 
              @click="excelFiltrarFechas(1)" 
              dark
            >
            Generar Excel
            <v-icon dark right>fas fa-file-csv</v-icon>
            </v-btn>                  
        </v-card>
      </v-col>
    </v-row>

    <v-row no gutters justify="center">
      <v-col cols="12" sm="10">
        <v-card dark outlined elevation="3">
          <v-card-title>
            Descargar la información de la cantidad de adicionales por cada banco de laboratorio según la sala seleccionada
          </v-card-title>
          <v-container fluid>
            <v-row no gutters>
              <v-col cols="12" sm="4">
                <v-select
                v-model="selectSala"
                :items="itemsSala"
                label="Sala de laboratorio"
                outlined
                dark
              ></v-select>
              </v-col>
              <v-col cols="12" sm="4">
                <v-btn 
                  elevation="2" 
                  class="ma-2" 
                  color="success" 
                  @click="excelFiltrarFechas(2)" 
                  dark
                >
                Generar Excel
                <v-icon dark right>fas fa-file-csv</v-icon>
                </v-btn>                  
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import HeaderLaboratorista from "@/components/HeaderLaboratorista.vue";

export default {
  components: {
    HeaderLaboratorista,
  },
  data() {
    return {
      // Los calendarios tienen dos variables. dateCalendarX, asociada al v-model del calendario y filterStartX asociada al v-model del input. El input se maneja en formato dia/mes/año y el calendario con formato año-mes-dia. menuCalendarX es una variable para la visualizacion del calendario en el v-menu

      // Propiedades para el calendario de la fecha inicial
      menuCalendarStart: false,
      dateCalendarStart: null,
      filterStartDate: null,

      // Propiedades para el calendario de la fecha final
      menuCalendarEnd: false,
      dateCalendarEnd: null,
      filterEndDate: null,

      // Para el v-select hay dos propiedades. selectTrim que es el campo seleccionado e itemsTrim que son los posibles valores que puede tomar el v-select
      selectTrim: null,
      itemsTrim: ['Primer trimestre','Segundo trimestre','Tercer trimestre','Cuarto trimestre','Año '+ new Date().toISOString().substr(0, 4),'Otro periodo'],

      // Variables para el seleccionador de la sala. Los nombres de los itemsSala, deben coincidir con los campos encontrados en la base de datos.
      selectSala: null,
      itemsSala: ['Circuitos','Comunicaciones','Digitales','Electronica A','Electronica B','Electronica Básica','Fisica 509','Fisica 510','Maquinas'],      
    }
  },
  mounted() {
    // Se identifica el semestre actual en la funcion actualTrim. Se hace la petición para obtener la base de datos horarios. Cuando se tenga la respuesta, en la promesa se ejecutan las funciones para hacer los graficos
    this.actualTrim();
  },
  watch:{
    dateCalendarStart(val){
      // Identifica cambios en la fecha del calendario startDate modificando el formato de la fecha a dia/mes/año y se revisa en la funcion indetiTrim() si coincide con el rango de fechas de algún periodo del v-select 
      this.filterStartDate = this.formatDate(this.dateCalendarStart);
      this.indentiTrim();
    },
    dateCalendarEnd(val){
      // Identifica cambios en la fecha del calendario endDate modificando el formato de la fecha a dia/mes/año y se revisa en la funcion indetiTrim() si coincide con el rango de fechas de algún periodo del v-select
      this.filterEndDate = this.formatDate(this.dateCalendarEnd);
      this.indentiTrim();
    },
    selectTrim(val){
      // Identifica cambios en el v-select. Para cualquier periodo de tiempo seleccionado cambia los valores de inicio y final en el rango de fechas. 
      let year = new Date().toISOString().substr(0, 4)
      if(this.selectTrim == this.itemsTrim[0]){ //Primer trimestre
        this.dateCalendarStart = year+"-01-01"
        this.dateCalendarEnd = year+"-03-31"
      }
      if(this.selectTrim == this.itemsTrim[1]){ //Segundo trimestre
        this.dateCalendarStart = year+"-04-01"
        this.dateCalendarEnd = year+"-06-30"
      }
      if(this.selectTrim == this.itemsTrim[2]){ //Tercer trimestre
        this.dateCalendarStart = year+"-07-01"
        this.dateCalendarEnd = year+"-09-30"
      }
      if(this.selectTrim == this.itemsTrim[3]){ //Cuarto trimestre
        this.dateCalendarStart = year+"-10-01"
        this.dateCalendarEnd = year+"-12-31"
      }      
      if(this.selectTrim == this.itemsTrim[4]){ //Año completo
        this.dateCalendarStart = year+"-01-01"
        this.dateCalendarEnd = year+"-12-31"
      }      
    }
  },
  methods: {
    actualTrim(){
      // Determina el trisemestre en el v-select a partir del mes para la fecha actual en que se carga la pagina
      let date = new Date().toISOString().substr(0, 10)
      const [year, month, day] = date.split("-");
      if (1 <= month && month <= 3){
        this.selectTrim = this.itemsTrim[0];
      }else if(4 <= month && month <= 6){
        this.selectTrim = this.itemsTrim[1];
      }else if(7 <= month && month <= 9){
        this.selectTrim = this.itemsTrim[2];
      }else if(10 <= month && month <= 12){
        this.selectTrim = this.itemsTrim[3];        
      }      
    },
    indentiTrim(){
      // Identifica, para las dos fechas ingresadas, si coincide con las de un valor de periodo de tiempo del v-select
      let year = new Date().toISOString().substr(0, 4)      
      if(this.filterStartDate == "01/01/"+year && this.filterEndDate == "31/03/"+year){
        this.selectTrim = this.itemsTrim[0]; // Primer trimestre
      }else if (this.filterStartDate == "01/04/"+year && this.filterEndDate == "30/06/"+year){
        this.selectTrim = this.itemsTrim[1]; // Segundo trimestre        
      }else if(this.filterStartDate == "01/07/"+year && this.filterEndDate == "30/09/"+year){
        this.selectTrim = this.itemsTrim[2]; // Tercer trimestre        
      }else if(this.filterStartDate == "01/10/"+year && this.filterEndDate == "31/12/"+year){
        this.selectTrim = this.itemsTrim[3]; // Cuarto trimestre
      }else if(this.filterStartDate == "01/01/"+year && this.filterEndDate == "31/12/"+year){
        this.selectTrim = this.itemsTrim[4]; // Año completo
      }else{
        this.selectTrim = this.itemsTrim[5]; // Otro periodo de tiempo
      }
    },

    excelFiltrarFechas(numButton){
      // Se hace un pre-filtro para asegurar que filterStartDate y filterEndDate no sean las mismas y que la fecha final sea mayor que la fecha inicial. Si las fechas estan correctas, se llama la funcion de axios que crea una base de datos temporal con el filtro de busqueda.       
      // Se agregó un numButton para identificar el buton que fue seleccionado y direccionar a su funcion en especifico. Se puede mejorar esta parte para evitar esto.
      const [dayStart, monthStart, yearStart] = this.filterStartDate.split("/");
      const [dayEnd, monthEnd, yearEnd] = this.filterEndDate.split("/");
      if(this.filterStartDate != this.filterEndDate){
        if(yearStart <= yearEnd && monthStart <= monthEnd && dayStart < dayEnd){
          // Para la peticion es necesario indicar el nombre de la base de datos y el nombre de la llave de los elementos de la base de datos que relacione la fecha
            if(numButton==1){
              this.axiosFilterDate("Prestamo","Fecha_Adicional")
            }else if(numButton == 2){
              this.excelPrestamosBancoPorSala("Prestamo","Fecha_Adicional");          
            }
        }else{
          // Revisar v-alert
          alert("Error, en el rango de las fechas")
        }
      }else{
        alert("Error, misma fecha")
      }
    },

    axiosFilterDate(dataBase, nameKey){
      // Hace la peticion axios y se envìan el nombre de la base de datos, el nombre de la llave fecha y las dos fechas de busqueda. 
      let objeto = this;
      this.axios
        .post(
          "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/excelTemporalFilterDate",{
            dataBase: dataBase,
            nameKeyDate: nameKey,
            startDate: objeto.filterStartDate,
            endDate: objeto.filterEndDate,
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          var mensaje = response.data.mensaje;
          var status = response.data.status;
          // Si status es 1, entonces se creo la base de datos temporal y seguido se hace la peticion get para obtener el documento excel. Si es 3 significa que no hubo elementos que coincidieran con la busqueda
          if(status==1){
            objeto.excelPrestamos();          
          }else if (status==3){
            alert(mensaje)
          }
        })
        .catch(function(error) {
          alert(error);
        });
    },

    excelPrestamos(){
      // Esta funcion hace la peticion para obtener el documento excel generado a partir de la base de datos temporal generada con el filtro de fechas
      let objeto = this;
      objeto.axios
          .get("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/excelPrestamos", {responseType: 'blob'})
          .then(function(response) {
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'InformePrestamos.xlsx');
            link.click();
          })
          .catch(function(error) {
            objeto.output = error;
          });
    },

    excelPrestamosBancoPorSala(dataBase, nameKey){
      // Fue necesario hacer otra funcion que cree una base de datos temporal debido a que se debe enviar el nombre del parametro de la sala en una peticion post, y la funcion que ya se tenía de axiosFilterDate() se volvería más compleja para hacer el fitlrado. Sin embargo se puede combinar las dos funciones en una sola agregando algunas variables adicionales
      // Otra cosa adicional es que se debe tener en cuenta que algunos salas tienen 6 u 8 bancos y de momento solo se está filtrando del banco 1 al banco 6
      if (this.selectSala==null){
        alert("Seleccione una de las salas")
      }else{
        let objeto = this;
        this.axios
          .post(
            "http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/excelTemporalFilterDateBancosSala",{
            dataBase: dataBase,
            nameKeyDate: nameKey,
            startDate: objeto.filterStartDate,
            endDate: objeto.filterEndDate,
            sala: objeto.selectSala
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
        )
        .then(function(response) {
          var mensaje = response.data.mensaje;
          var status = response.data.status;
          // Si status es 1, entonces se creo la base de datos temporal y seguido se hace la peticion get para obtener el documento excel. Si es 3 significa que no hubo elementos que coincidieran con la busqueda
          if(status==1){
            objeto.axios
            .get("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/excelPrestamosBancosSala", {responseType: 'blob'})
            .then(function(response) {
              const url = window.URL.createObjectURL(new Blob([response.data]));
              const link = document.createElement('a');
              link.href = url;
              link.setAttribute('download', 'InformePrestamos.xlsx');
              link.click();
            })
            .catch(function(error) {
              objeto.output = error;
            });
          }else if (status==3){
            alert(mensaje)
          }
        })
        .catch(function(error) {
          alert(error);
        });
      }
      
    },

    formatDate(date){
      // Cambia el formato de la fecha, reemplazando el separador '-' por un '/'. El '-' se utiliza en el v-calendar. El '/' se utiliza en los v-text-input y es el formato generalizado para las fechas en el proyecto
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${day}/${month}/${year}`;
    },

    parseDate (date) {
      // Esta funcion esta asociada a los v-text-input para modificar los v-calendar a partir de fechas ingresados por teclado.
      if (!date) return null
      const [day, month, year] = date.split('/')
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },

    chartDiasVsHoras(dataHorarios){
      // Configuracion del grafico. De momento es un grafico estatico que toma la base de datos Horarios y hace un filtro de cantidad de clases por dia de la semana. En el vector dataChart se guarda en cada posicion las horas por dia
      for (let index in this.diasSemana){
        this.dataChart[index] = dataHorarios.filter(item => item.dia == this.diasSemana[index]).length*2;
      }
      // Si el vector dataChart es mayor a cero (toca cambiar esta validacion) entonces se configuran las propiedades del grafico. dataSets y optionsChart son las configuraciones del grafico (ver chart.js) que utiliza el componente BarChart (ver vue-chart.js).
      if(this.dataChart.length>0){
        this.loaded = true
        this.dataSets = [{
          data: this.dataChart,
          backgroundColor: ['rgba(141, 16, 16, 0.7)', 'rgba(153, 41, 41, 0.7)', 'rgba(184, 42, 42, 0.7)','rgba(231, 32, 32, 0.7)','rgba(255, 3, 3, 0.7)'],
          borderColor: ['rgba(141, 16, 16, 1)', 'rgba(153, 41, 41, 1)', 'rgba(184, 42, 42, 1)','rgba(231, 32, 32, 1)','rgba(255, 3, 3, 1)'],
          borderWidth: 2,
          maxBarThickness: 35,
        }]
        this.optionsChart = {
          scales:{
            xAxes:[{
              ticks: {
                beginAtZero: true
              },
              scaleLabel: {
                display: true,
                labelString: 'Cantidad de horas'
              }
            }],
            yAxes: [{
			    	  ticks: {
				    	  beginAtZero: true
              },
              gridLines: {
					      display: true
					    }
            }],    
          },
          legend: {
				    display: false
          },
          responsive: true,
          maintainAspectRatio: false
        }
      }
    },
  },
};
</script>