import Vue from "vue";
import VueRouter from "vue-router";
import HomeAdmin from "../views/HomeAdmin.vue";
import HomeLaboratorista from "../views/HomeLaboratorista.vue";
import consultayCancelacion from "../views/consultayCancelacion.vue";
import consultasycancelacionlabo from "../views/consultasycancelacionlabo.vue";
import registroUser from "../views/registroUser.vue";
import editUser from "../views/editUser.vue";
import editProfile from "../views/editProfile.vue";
import Home1 from "../views/Home1.vue";
import reservaEstudiante from "../views/reservaEstudiante.vue";
import Addnewsala from "../views/Addnewsala.vue";
import studentpass from "../views/studentpass.vue";
import editprofilelab from "../views/editprofilelab.vue";
import consultareslabo from "../views/consultareslabo.vue";
import editadmin from "../views/editadmin.vue";
import editpassadmin from "../views/editpassadmin.vue";
import horarios from "../views/horarios.vue";
import labpass from "../views/labpass.vue";

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
    path: "/horarios",
    name: "horarios",
    component: horarios
  },
  {
    path: "/studentpass",
    name: "studentpass",
    component: studentpass
  },
  {
    path: "/editpassadmin",
    name: "editpassadmin",
    component: editpassadmin
  },
  {
    path: "/labpass",
    name: "labpass",
    component: labpass
  },
  {
    path: "/editadmin",
    name: "editadmin",
    component: editadmin,
    meta: {
      requiresAuth: false
    }
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
      requiresAuth: true
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
    }
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
  },
  {
    path: "/consultareslabo",
    name: "consultareslabo",
    component: consultareslabo,
    meta: {
      requiresAuth: false
    }
  },

  {
    path: "/editprofilelab",
    name: "editprofilelab",
    component: editprofilelab,
    meta: {
      requiresAuth: false
    },
  },
  {
    path: "/addnewsala",
    name: "addnewsala",
    component: Addnewsala,
    meta: {
      requiresAuth: false
    },
  }
];

const router = new VueRouter({
  routes
});

export default router;

