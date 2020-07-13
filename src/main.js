import Vue from "vue";
import "./plugins/axios";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import "roboto-fontface/css/roboto/roboto-fontface.css";
import "@fortawesome/fontawesome-free/css/all.css";
import Axios from "axios";
import { Row, Column } from 'vue-grid-responsive';

Vue.component("row", Row);
Vue.component("column", Column);

Vue.prototype.$serverURI = " http://127.0.0.1";
Vue.prototype.$serverPort = "5000";

Vue.config.productionTip = false;
// Vue.prototype.$verificarLogin = function(){
//   let objeto = this;
//   let pregunta = localStorage.autorizado
//   if(pregunta=='true'){
//     null
//   }else{
//     alert("Entro en error >;(");
//     objeto.$router.replace({name:'home'});
//   }
// }

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
