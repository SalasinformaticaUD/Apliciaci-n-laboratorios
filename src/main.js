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
import VueCookies from 'vue-cookies';
import CryptoJS from 'crypto-js';

import jsPDF from "jspdf";
import 'jspdf-autotable';
import Chart from 'chart.js';
import VueCharts from 'vue-chartjs';

Vue.use(VueCookies);

Vue.use(CryptoJS);


Vue.prototype.$serverURI = "200.69.103.13";
Vue.prototype.$serverPort = "5000";
Vue.prototype.$select2 = select2;
Vue.config.productionTip = false;
Vue.prototype.$usuario="";
Vue.prototype.$cookies = Vue.$cookies;
Vue.prototype.$Crypto = CryptoJS;


new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
