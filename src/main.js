import Vue from "vue";
import "./plugins/axios";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import "roboto-fontface/css/roboto/roboto-fontface.css";
import "@fortawesome/fontawesome-free/css/all.css";
import Axios from "axios";
import select2 from "./assets/select2/js/select2.js";

Vue.prototype.$select2="select2";

Vue.prototype.$serverURI = "200.69.103.13";
Vue.prototype.$serverPort = "5000";


Vue.config.productionTip = false;
Vue.prototype.$verificarLogin = function(){
  let objeto = this;
  let pregunta = localStorage.autorizado
  if(pregunta=='true'){
    null
  }else{
    alert("Entro en error >;(");
    objeto.$router.replace({name:'home'});
  }
};
const ignoreWarnMessage = 'The .native modifier for v-on is only valid on components but it was used on <div>.';
Vue.config.warnHandler = function (msg, vm, trace) {
  // `trace` is the component hierarchy trace
  if (msg === ignoreWarnMessage) {
    msg = null;
    vm = null;
    trace = null;
  }
}

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
