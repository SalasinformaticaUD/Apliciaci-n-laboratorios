import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    infoLabs:[
      {name: "Electrónica A",      color: "red darken-2",      bancos:8,    colorLight: "red lighten-2"},
      {name: "Electrónica B",      color: "indigo darken-2",   bancos:6,    colorLight: "indigo lighten-2"},
      {name: "Máquinas",           color: "green darken-3",    bancos:8,    colorLight: "green lighten-2"},
      {name: "Circuitos",          color: "yellow accent-4",   bancos:12,   colorLight: "yellow"},
      {name: "Comunicaciones",     color: "teal darken-2",     bancos:6,    colorLight: "teal lighten-2"},
      {name: "Electrónica básica", color: "orange darken-3",   bancos:8,    colorLight: "orange lighten-2"},
    ],
    date: null,
    banco: null,
    hour: null,
  },
  mutations: {
  },
  actions: {
  },
  getters:{
    infoLabs(state){
      return state.infoLabs;
    }
  },
  modules: {}
});
