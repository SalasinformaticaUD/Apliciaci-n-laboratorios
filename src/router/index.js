import Vue from "vue";
import VueRouter from "vue-router";
import HomeAdmin from "../views/HomeAdmin.vue";
import HomeLaboratorista from "../views/HomeLaboratorista.vue";
import consultayCancelacion from "../views/consultayCancelacion.vue";
import consultasycancelacionlabo from "../views/consultasycancelacionlabo.vue";
import registroUser from "../views/registroUser.vue";
import prueba from "../views/prueba.vue";
import editUser from "../views/editUser.vue";
import editProfile from "../views/editProfile.vue";
import Home1 from "../views/Home1.vue";
import reservaEstudiante from "../views/reservaEstudiante.vue";


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home1",
    component: Home1
  },
  {
    path: "/homel",
    name: "HomeLaboratorista",
    component: HomeLaboratorista
  },
  {
    path: "/homea",
    name: "HomeAdmin",
    component: HomeAdmin
  },
  {
    path: "/consulta",
    name: "consulta",
    component: consultayCancelacion,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: "/consultalabo",
    name: "consultalabo",
    component: consultasycancelacionlabo,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: "/registrouser",
    name: "registrouser",
    component: registroUser,
    meta: {
      requiresAuth: false
    },
  },
  {
    path: "/prueba",
    name: "prueba",
    component: prueba,
    meta: {
      requiresAuth: false
    },
  },
  {
    path: "/edituser",
    name: "edituser",
    component: editUser,
    meta: {
      requiresAuth: false
    },
  },
  {
    path: "/editprofile",
    name: "editprofile",
    component: editProfile,
    meta: {
      requiresAuth: false
    },
  },
  {
    path: "/home",
    name: "home",
    component: Home1,
    meta: {
      requiresAuth: false
    },
  },
  {
    path: "/consulta2",
    name: "consulta2",
    component: consultasycancelacionlabo,
    meta: {
      requiresAuth: false
    },
  },
  {
    path: "/reservaestudiante",
    name: "reservaestudiante",
    component: reservaEstudiante,
    meta: {
      requiresAuth: false
    },
  }
];

const router = new VueRouter({
  routes
});

export default router;
