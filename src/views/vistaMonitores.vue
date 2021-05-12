<template>
  <v-container fluid>
    <Headerestudiantes />

    <v-form ref="form" v-model="validForm" lazy-validation>
      <v-row class="pt-6" justify="center">     
        <v-col cols="12" sm="3">
          <v-menu
            ref="menu"
            v-model="menu"
            :close-on-content-click="false"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
            dark
          >
            <template v-slot:activator="{ on, attrs }" >
              <v-text-field
                v-model="dateFormatted"
                :rules="[rules.required]"
                label="Fecha"
                persistent-hint
                prepend-icon="far fa-calendar-minus"
                v-bind="attrs"
                v-on="on" 
                readonly
                outlined
                dark
              ></v-text-field>
            </template>
            <v-date-picker v-model="date" no-title @input="menu = false" 
             :max="maxDateCalendar()" :allowed-dates="allowedDates(6)"></v-date-picker>
             <!-- :min=minCalendar -->
          </v-menu>
        </v-col>
        <v-col cols="12" sm="3">
          <v-select
            ref="Laboratorio"
            v-model="laboratorioAdicional"
            :rules="[rules.required]"  
            :items="laboratorios"
            label="Laboratorio"
            placeholder="Seleccionar..."
            required
            dark
            outlined
          ></v-select>
        </v-col>
        <v-col cols="12" sm="3">
          <v-select
            ref="Hora laboratorio"
            v-model="horaAdicional"
            :rules="[rules.required]"  
            :items="horas"
            label="Hora Adicional"
            placeholder="Seleccionar..."
            required
            dark
            outlined
          ></v-select>
        </v-col>
        <v-col cols="12" sm="1" class="mt-3">
          <v-btn rounded color="primary" dark :disabled="!validForm" @click="validarFormulario()">
            Buscar
          </v-btn>
        </v-col>
      </v-row>
    </v-form>

    <v-container fluid v-if="registrosLaboratorio && registrosLaboratorio.length>0">
      <v-row class="px-10 mx-10 text-center" justify="center">
        <v-col cols="12" sm="6" md ="4" lg="4" v-for="(item,index) in infoBancos" :key="index">
          <v-card outlined @click="dialogFicha(item[4])" v-if="item[0]==1" max-height="142px">
            <v-card-title>
              <span class="headline">
                Banco {{item[1]}}
                </span>
                <v-spacer></v-spacer>
              <v-icon color="grey lighten-1">fas fa-external-link-alt</v-icon>
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text class="text-right">
              {{item[2]}}
              <br>
              {{item[3]}}
            </v-card-text>
          </v-card>
          <v-card disabled min-height="142px" v-if="item[0]==0">
            <v-card-title>
              <span class="headline">
                Banco {{index+1}}
                </span>
                <v-spacer></v-spacer>
              <v-icon color="grey lighten-1">fas fa-external-link-alt</v-icon>
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text class="text-right">
            </v-card-text>
          </v-card>        
        </v-col>
      </v-row>    
      <v-row class="px-10 mx-10 mt-10 text-center" justify="center">
        <v-col cols="12" sm="6">
          <v-btn block color="success" dark @click="asistenciaAdicional()" medium>
            Asistencia del laboratorio
          </v-btn>
        </v-col>
      </v-row>
    </v-container>

    <v-dialog v-model="dialogoFicha" max-width="700px">
      <v-card>
        <v-card-title>
          <span class="headline">Ficha de laboratorio</span>
        </v-card-title>
        <v-container fluid v-if="msgInfo.length>0">
          <v-row class="my-n4 mx-5">
            <v-col cols="12" sm="12">
              <v-alert outlined type="warning" color="red" prominent>
                <ul>
                  <li> 
                    {{msgInfo}}
                  </li>
                </ul>
              </v-alert>
            </v-col>
          </v-row>
        </v-container>
        <v-divider></v-divider>
        <v-card-text>
          <v-container>
            <v-row class="mt-n1">
              <v-col cols="12" sm="8">
                <v-text-field
                  v-model="infoItem.usuario"
                  :disabled="true"
                  label="Nombre del estudiante"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="infoItem.codigo"
                  :disabled="true"
                  label="Código del estudiante"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row class="mt-n6">
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="infoItem.fecha_adicional"
                  :disabled="true"
                  label="Fecha del adicional"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="infoItem.sala"
                  :disabled="true"
                  label="Laboratorio adicional"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="2">
                <v-text-field
                  v-model="infoItem.hora"
                  :disabled="true"
                  label="Hora"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="2">                      
                <v-text-field
                  v-model="infoItem.banco"
                  :disabled="true"
                  label="No. Banco"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row class="mt-n6">
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="infoItem.practica"
                  :disabled="true"
                  label="Nombre de la práctica"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="infoItem.estado"
                  :disabled="true"
                  label="Estado del adicional"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="infoItem.asistencia"
                  :disabled="true"
                  label="Asistencia"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row class="pb-2 ma-2 mt-n2" align="center" align-content="center">
              <v-col cols="12" sm="10">
                <v-text-field
                  label="Ingrese un elemento adicional"
                  hide-details="auto"
                  dense
                  @keyup.enter="agregarElementoAdicional()"
                  v-model = "inputElemento"
                  :disabled="!estadoItem"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="2" align-self="center" class="text-right">
                <v-btn :disabled="!estadoItem" color="primary" :dark="estadoItem" small rounded 
                  @click="agregarElementoAdicional()"
                >Agregar</v-btn>
              </v-col>
            </v-row>      
            <v-divider></v-divider>
            <v-row no-gutters class="pa-1" align="center" v-if="infoItem.elemento && infoItem.elemento.length>0">
              <v-col cols="12" sm="1" class="text-sm-center font-weight-black">
                No.
              </v-col>
              <v-col cols="12" sm="5" class="font-weight-black pl-5">
                Elementos
              </v-col>              
              <v-col cols="12" sm="4" class="font-weight-black pl-5">
                Observaciones
              </v-col>                          
              <v-col cols="12" sm="2" class="text-sm-center font-weight-black">
                No. Placa
              </v-col>
            </v-row>
            <v-divider></v-divider>  
            <v-row no-gutters align="center">
              <v-col v-for= "(item,index) in infoItem.elemento" :key="index" cols="12" sm="12">
                <v-row no-gutters class="pa-1" align="center">
                  <v-col cols="12" sm="1" class="text-sm-center">
                    {{index+1}}.
                  </v-col>
                  <v-col></v-col>
                  <v-col cols="12" sm="5" class="pl-5">
                    {{item}}
                  </v-col>
                  <v-col cols="12" sm="4">
                    {{infoItem.estadoElemento[index]}}
                  </v-col>
                  <v-col cols="12" sm="2" class="text-sm-center pl-5 pr-5">
                    <v-text-field
                      dense
                      class="centered-input"
                      hide-details
                      label="# Placa"
                      single-line
                      :disabled="!estadoItem"
                      v-model = "infoItem.placaElemento[index]"
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-divider></v-divider>  
              </v-col>                  
            </v-row>
            <v-row no-gutters align="center" class="mt-5" v-if="infoItem.observacionesGenerales && infoItem.observacionesGenerales.length>0">   
              <v-col cols="12" sm="12">
                <v-text-field
                  v-model="infoItem.observacionesGenerales"
                  :disabled="true"
                  label="Observaciones Generales"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <v-card-actions>
            <v-row class="mt-3 justify-center">
              <v-col cols="12" sm="4">
                <v-btn :disabled="!estadoItem" color="primary" :dark="estadoItem"  block  @click="guardarFichaEdit()" medium>
                  Guardar los cambios
                </v-btn>
              </v-col>
            </v-row>
          </v-card-actions>
        </v-card-text>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogAsistencia" max-width="700px">
      <v-card>
        <v-card-title>
          <span class="headline">Verificación de la asistencia en el laboratorio</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-divider></v-divider>
            <v-row no-gutters align="center">
              <v-col cols="12" sm="2" class="text-sm-center font-weight-black">
                No. Banco                
              </v-col>
              <v-col cols="12" sm="4" class="text-sm-center font-weight-black">
                Estudiante
              </v-col>
              <v-col cols="12" sm="2" class="text-sm-center font-weight-black">
                Código
              </v-col>
              <v-col cols="12" sm="3" offset="1" class="text-sm-center font-weight-black">
                Asistencia
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-row no-gutters align="center">
              <v-col v-for= "(item,index) in infoAsistencia" :key="index" cols="12" sm="12">
                <v-row no-gutters class="py-3" align="center">
                  <v-col cols="12" sm="2" class="text-sm-center">
                    {{item.banco}}
                  </v-col>
                  <v-col cols="12" sm="4" class="text-sm-center">
                    {{item.usuario}}
                  </v-col>
                  <v-col cols="12" sm="2" class="text-sm-center">
                    {{item.codigo}}
                  </v-col>
                  <v-col cols="12" sm="1" offset="1" class="text-sm-center pl-5">
                    <v-btn @click="cambioAsistencia(index,1)" fab x-small :elevation="(item.asistencia == 'SI')? 10 : 0">
                      <v-icon large :color="(item.asistencia == 'SI') ? 'success':'grey lighten-1'">fas fa-check-circle</v-icon>
                    </v-btn>
                  </v-col>
                  <v-col cols="12" sm="1" offset="1" class="text-sm-center ml-9">
                    <v-btn @click="cambioAsistencia(index,2)" fab x-small :elevation="(item.asistencia == 'NO')? 10 : 0">
                    <v-icon large :color="(item.asistencia == 'NO') ? 'error':'grey lighten-1'">fas fa-times-circle</v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
                <v-divider></v-divider>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-row class="mt-n2 ma-3 justify-center">
            <v-col cols="12" sm="5">
              <v-btn block color="primary" dark @click="guardarAsistencia()" medium>
                Guardar Asistencia
              </v-btn>
            </v-col>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>

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
  data() {
    return {
      // Variable para la validacion del formulario
      validForm: true,

      // Variables relacionadas al calendario
      menu: false,                                   // Menu del v-calendar   
      dateFormatted: "",                             // Fecha para el v-model del v-text
      date: "",                                      // Fecha para el v-model del calendar
      minCalendar: "",                               // Fecha mínima permitida en el v-calendar

      // Variable para seleccionar el laboratorio (los nombres deben coincidir con los campos de la base de datos). laboratorioAdicional es el v-model del v-select 
      laboratorios: [
        "Electronica A",
        "Electronica B",
        "Electronica Basica",
        "Maquinas",
        "Comunicaciones",
        "Circuitos"
      ],
      laboratorioAdicional: "",

      // Variable para seleccionar la franja horaria. horaAdicional es el v-model del v-select
      horas: [6,8,10,12,14,16,18],
      horaAdicional: "",

      // Variable que almacena los datos de la peticion
      registrosLaboratorio: [],
      
      // En infoBancos se guarda información si los bancos están ocupados o desocupados; en infoItem se guarda la información temporal del banco seleccionado para ver la Ficha de laboratorio; en infoAsistencia se guarda la información relacionada para firmar la asistencia; en indiceFicha se guarda la posicion de la ficha del vector registrosLaboratorio al hacer clic en alguno de los v-card
      infoBancos: "",
      infoItem: {},
      infoAsistencia: [],
      indiceFicha: 0,

      // Esta variable verifica si el estado del adicional aún se encuentra pendiente para deshabilitar cualquier edicion del mismo (agregar elementos o guardar los cambios)
      estadoItem: false,

      // Esta variable guarda un mensaje informativo en caso de que el adicional no este aprobado o que la asistencia aún no se haya llenado
      msgInfo: "",

      // Variable relacionada al v-dialog de asistencia
      dialogAsistencia: false,

      // Variables relacionadas a la ficha de laboratorio. dialogoFicha es el que permite visualizar la ficha e inputElemento es el text-input para agregar más elementos.
      dialogoFicha: false,
      inputElemento:"",

      // Reglas requeridas para el formulario
      rules:{
        required: value => !!value || "Este espacio es requerido.",
      }, 
    }
  },
  created(){
    // Se evalua si el dia actual es domingo. Si sí, se suma un día para que se tome la fecha del lunes. En caso contrario, se utiliza la fecha actual del sistema. Se le debe indicar las 00:00 para evitar que se corra el día debido a la diferencia horaria que utilizada con el formato ISO.
    let todaydate = this.formatDate(this.conversionDate(new Date()));
    let dateToday = new Date(this.parseDate(todaydate)+" 00:00");
    if (dateToday.getDay() === 0){
      dateToday = dateToday.setDate(dateToday.getDate() + 1); 
    }
    this.dateFormatted = this.formatDate(this.conversionDate(new Date(dateToday)));
    this.date = this.conversionDate(new Date(dateToday))
    this.minCalendar = this.date;
  },

  mounted(){   
  },

  watch:{
    date(val) {
      // Watcher de la variable date (v-model del calendar) para detectar el cambio de día en la fecha y modificar también en el v-text del formulario. 
      this.dateFormatted = this.formatDate(this.date);
    },
  },
  methods:{
    conversionDate(date){
      // Esta función toma una fecha dada la función Date() de JS y retorna una fecha en el formato año-mes-dia. Esto se realiza para evitar utilizar la función Date().toISOString ya que esta última no tiene en cuenta la zona horaria y en horas de la noche toma la fecha como la del dia siguiente. 
      let year = date.getFullYear().toString();
      let month = (date.getMonth()+1).toString();
      let day = date.getDate().toString();
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    parseDate(date) {
      // Esta funcion toma una fecha en el formato dia/mes/año (formato utilizado en el proyecto) y la convierte al formato año-mes-dia (formato v-calendar)
      if (!date) return null
      const [day, month, year] = date.split('/')
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    formatDate(date) {
      // Esta función toma una fecha en el formato año-mes-dia (formato v-calendar) y la convierte al formato dia/mes/año (formato utilizado en el proyecto)
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${day}/${month}/${year}`;
    },
    maxDateCalendar(){
      // Esta función limita la selección máxima de días en el calendario. A la fecha actual se le suman 7 días y se retorna la fecha en formato año-mes-dia (formato v-calendar).
      let date = new Date();
      date = date.setDate(date.getDate() + 7);
      date = this.conversionDate(new Date(date));
      return date;
    },
    allowedDates(n) {
      // Esta función recibe un número entero n para restringir la selección dle día domingo en el v-calendar
      return val => ![n].includes(new Date(val).getDay());
    },
    agregarElementoAdicional(){
      // Esta función toma el text-input que ingresa más elementos en la ficha de laboratorio, determina que la longitud sea mayor a cero para que no sea una cadena vacía y además reemplaza los espacios para evitar que la cadena sean solo espacios vacios. Una vez verificado, se hace un push() al vector de elementos del infoItem, siendo este último la información asociada a uno de los adicionales. Finalmente, vuelve a limpiar el text-input
      if (this.inputElemento.length>0){
        if(this.inputElemento.replace(/ /g, "").length>0){
          this.infoItem.elemento.push(this.inputElemento);
        }
      }      
      this.inputElemento = "";
    },
    dialogFicha(index){
      // Esta función toma con index el valor de uno de los bancos seleccionados. Toma el objeto y lo copia a otro objeto llamado infoItem. Se limpia e inicializa el input de los v-text de las fichas para agregar elementos y se habilita la visualización de la ficha del laboratorio que se encuentra dentro de un v-dialog. Se guarda el indice de la Ficha para sobreescribir el vector en el mismo indice al guardar los cambios.
      this.infoItem = JSON.parse(JSON.stringify(this.registrosLaboratorio[index]));
      this.inputElemento = "";
      this.dialogoFicha = true;
      this.indiceFicha = index;

      // Con la variable estadoItem se habilita la edición de la ficha solo en los casos en que el estudiante tenga el laboratorio aprobado. En caso contrario se muestra un warning. Así mismo, se verifica la asistencia al adicional para agregar el recordatorio.
      this.msgInfo = "";
      if (this.infoItem.estado=="APROBADO"){
        this.estadoItem = true;
        if(this.infoItem.asistencia=="PENDIENTE"){
          this.msgInfo = "La asistencia de estudiante se encuentra " + this.infoItem.asistencia + ".";  
        }
      }else{
        this.estadoItem = false;
        this.msgInfo = "El estado del adicional se encuentra " + this.infoItem.estado + ".";
      } 
    },
    asistenciaAdicional(){      
      // Se hace un filtrado de los bancos que tienen el estado APROBADO y luego se obtiene el número del banco y se orden ascendentemente. Teniendo los bancos ordenados se vuelve a filtrar la información para obtener solo la información de interes para verificar la asistencia. 
      let bancosOcupados = this.registrosLaboratorio.filter(item => item.estado=="APROBADO");
      bancosOcupados = bancosOcupados.map(item => item.banco).sort();

      for (let i=0;i<bancosOcupados.length;i++){
        let infoBanco = this.registrosLaboratorio.filter(item => item.banco==bancosOcupados[i]);
        this.infoAsistencia[i] = {
          banco: infoBanco[0].banco,
          usuario: infoBanco[0].usuario,
          codigo: infoBanco[0].codigo,
          asistencia: infoBanco[0].asistencia,
        }
      }
      if (bancosOcupados.length > 0){
        this.dialogAsistencia = true;
      }
    },
    cambioAsistencia(index,state){
      // De acuerdo al state enviado (1 asistio, 2 no asistio)se modifica el estado de la asistencia. Debido al v-for es necesario recargar el v-dialog. Una manera rapida es con la variable dialogAsistencia.
      if(state==1){
        this.infoAsistencia[index].asistencia = "SI";
      }else{
        this.infoAsistencia[index].asistencia = "NO";        
      }
      this.dialogAsistencia = false;
      this.dialogAsistencia = true;
    },
    guardarAsistencia(){
      // Se recorren los registros de laboratorio y se compara con la información de info asistencia. Si coincide el número de codigo, se modifica la asistencia. En el backend se recibe de nuevo la información de los seis bancos y se actualiza. 
      for(let i = 0;i<this.registrosLaboratorio.length;i++){
        for(let j=0;j<this.infoAsistencia.length;j++){
          if(this.registrosLaboratorio[i].codigo === this.infoAsistencia[j].codigo){
            this.registrosLaboratorio[i].asistencia = this.infoAsistencia[j].asistencia;
          }
        }
      }
      this.editarAdicional();
    },
    guardarFichaEdit(){
      // Se toma la información editada en la ficha de laboratorio (infoItem) y se sobreescribe en la posicion dada de los registros de laboratorio. En el backend se manda de nuevo la información de los seis bancos y se guarda (esto se hace para utilizar la misma función de asistencia)
      this.registrosLaboratorio[this.indiceFicha] = this.infoItem;
      this.indiceFicha = 0;
      this.editarAdicional();
    },
    validarFormulario(){
      // Esta función permite validar los campos del formulario. Unicamente hace la petición al servidor cuando se han llenado los campos. Primero se cierran los v-dialog en caso de hacer una nueva busqueda. 
      if(this.$refs.form.validate()){
        this.dialogAsistencia = false;
        this.dialogoFicha = false;
        this.buscarAdicionales();
      }
    },
    editarAdicional(){
      // Se hace una confirmación. En caso de ser verdadera, se toma la información modificada del infoItem y se envía al servidor. Si el status de la respuesta es 1 significa que se guardaron los cambios correctamente, entonces se cierra el v-dialog de la ficha y se hace nuevamente una busqueda en la base de datos para actualizar la información.
      console.log(this.registrosLaboratorio);
      let confirmacion = confirm("¿Esta seguro de guardar estos cambio?");
      if (confirmacion) {
        let objeto = this;
        this.axios.post("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/editarAdicional",
          {
            datos: objeto.registrosLaboratorio,
          },
          {
            headers: {
              "Content-Type": "application/json"
            }
          })
        .then(function(response){
          var respuesta = response.data.mensaje;
          var status = response.data.status;
          if (status == "1") {
            alert(respuesta);
            objeto.infoItem = {};
            objeto.infoAsistencia = [];
            objeto.dialogAsistencia = false;
            objeto.dialogoFicha = false;
            objeto.buscarAdicionales();
          }
        })
        .catch(function(error) {
          alert(error);
        });
      }
    },
    buscarAdicionales(){
      //Se hace una busqueda en las bases de datos de los adicionales filtrando por fecha, la sala y la hora del laboratorio. Con la respuesta se toma y se crea un nuevo Array (infoBancos) inicializado en ceros con la longitud de la cantidad de bancos que hay en el laboratorio. Luego, se recorre cada banco y si esta ocupado, se cambia el estado a un 1. Además se adjunta información como el usuario y el codigo.
      let objeto = this;
      this.axios.post("http://" + objeto.$serverURI + ":" + objeto.$serverPort + "/Usuario/getReservasLaboratorio",
        {
          fecha_laboratorio: objeto.dateFormatted,
          sala_laboratorio: objeto.laboratorioAdicional,
          hora_laboratorio: objeto.horaAdicional
        },
        {
          headers: {
            "Content-Type": "application/json"
          }
        })
      .then(function(response) {
        objeto.registrosLaboratorio = response.data.data;          
        if (response.data.status==1){
          // El valor del 6 debe ser variable y depender de acuerdo a la cantidad de bancos de la sala
          objeto.infoBancos = new Array(6).fill([0]);
          for(let i=0;i<6;i++){
            if (objeto.registrosLaboratorio[i]){
              let banco = objeto.registrosLaboratorio[i].banco;
              let usuario = objeto.registrosLaboratorio[i].usuario;
              let codigo = objeto.registrosLaboratorio[i].codigo;
              objeto.infoBancos[banco-1] = [1,banco,usuario,codigo,i];
            }          
          }
        }else{
          alert(response.data.mensaje);
        }
      })
      .catch(function(error) {
        objeto.output = error;
      });
    }
  },
};
</script>