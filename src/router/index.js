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
import Inventarioagregarequipo from "../views/Inventarioagregarequipo.vue";
import pruebaSelect2 from "../views/pruebaSelect2.vue";
import inventarioconsultar from "../views/inventarioconsultar.vue";
import ticketsman from "../views/ticketsman.vue";


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
    component: HomeAdmin,
    meta: {
      requiresAuth: true
    }
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
    }
  },
    {
      path: "/ticketsman",
      name: "ticketsman",
      component: ticketsman,
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
  },
  {
    path: "/addequipo",
    name: "Inventarioagregarequipo",
    component: Inventarioagregarequipo,
    meta: {
      requiresAuth: false
    },
  },
  {
    path: "/busquedainventario",
    name: "inventarioconsultar",
    component: inventarioconsultar,
    meta: {
      requiresAuth: false
    },
  },
    {
      path: "/pruebaBuscar",
      name: "select2",
      component: pruebaSelect2,
      meta: {
        requiresAuth: false
      },
  },
];

const router = new VueRouter({
  routes
});

let objeto = Vue;
router.beforeEach((to, from, next) => {
  let estaAuth = objeto.$cookies.get("user_session");
  let needAuth = to.matched.some(record => record.meta.requiresAuth);
  
  if(needAuth && !estaAuth){
    next('home')
  }else{
    next()
  }
});

export default router;

