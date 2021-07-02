import Vue from "vue";
import VueRouter from "vue-router";
import jwt_decode from "jwt-decode";
import HomeAdmin from "../views/HomeAdmin.vue";
import HomeLaboratorista from "../views/HomeLaboratorista.vue";
import consultayCancelacion from "../views/consultayCancelacion.vue";
import registroUser from "../views/registroUser.vue";
import editUser from "../views/editUser.vue";
import home from "../views/Home1.vue";
import reservaEstudiante from "../views/reservaEstudiante.vue";
import Addnewsala from "../views/Addnewsala.vue";
import studentpass from "../views/studentpass.vue";
import editprofilelab from "../views/editprofilelab.vue";
import editadmin from "../views/editadmin.vue";
import editpassadmin from "../views/editpassadmin.vue";
import horarios from "../views/horarios.vue";
import labpass from "../views/labpass.vue";
import Inventarioagregarequipo from "../views/Inventarioagregarequipo.vue";
import pruebaSelect2 from "../views/pruebaSelect2.vue";
import inventarioconsultar from "../views/inventarioconsultar.vue";
import ticketsman from "../views/ticketsman.vue";
import consultamantenimiento from "../views/consultamantenimiento.vue";
import mantenimiento from "../views/mantenimiento.vue";
import reservatemp from "../views/reservatemp.vue";
import clasesadd from "../views/clasesadd.vue";
import prestamoequExt from "../views/prestamoequExt.vue";
import prestamoequInt from "../views/prestamoequInt.vue";
import consultareservalabstemp from "../views/consultareservalabstemp.vue";
import informesElementos from "../views/informesElementos.vue";
import informesHorarios from "../views/informesHorarios.vue";
import informesPrestamos from "../views/informesPrestamos.vue";
import LicenciasSoftware from "../views/LicenciasSoftware.vue";
import licenciasEstudiantes from "../views/licenciasEstudiantes.vue";
import Monitores from "../views/vistaMonitores.vue";
import agendaadicionalesL from "../views/agendaAdicionalesLaboratorista.vue";
import agendaadicionalesM from "../views/agendaAdicionalesEstudiantes.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: home,
    meta: {
      requiresAuth: false,
    },
  },
  {
    path: "/homel",
    name: "HomeLaboratorista",
    component: HomeLaboratorista,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista"],
    },
  },
  {
    path: "/horarios",
    name: "horarios",
    component: horarios,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista", "Estudiante", "Administrador"],
    },
  },
  {
    path: "/studentpass",
    name: "studentpass",
    component: studentpass,
    meta: {
      requiresAuth: true,
      role: ["Estudiante"],
    },
  },
  {
    path: "/editpassadmin",
    name: "editpassadmin",
    component: editpassadmin,
    meta: {
      requiresAuth: true,
      role: ["Administrador"],
    },
  },
  {
    path: "/labpass",
    name: "labpass",
    component: labpass,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista"],
    },
  },
  {
    path: "/LicenciasSoftware",
    name: "LicenciasSoftware",
    component: LicenciasSoftware,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista"],
    },
  },  
  {
    path: "/licenciasEstudiantes",
    name: "licenciasEstudiantes",
    component: licenciasEstudiantes,
    meta: {
      requiresAuth: true,
      role: ["Estudiante"],
    },
  },
  {
    path: "/Monitores",
    name: "Monitores",
    component: Monitores,
    meta: {
      requiresAuth: true,
      role: ["Estudiante", "Laboratorista"],
    },
  },
  {
    path: "/editadmin",
    name: "editadmin",
    component: editadmin,
    meta: {
      requiresAuth: true,
      role: ["Administrador"]
    }
  },
  {
    path: "/homea",
    name: "HomeAdmin",
    component: HomeAdmin,
    meta: {
      requiresAuth: true,
      role: ["Administrador"]
    }
  },
  {
    path: "/consulta",
    name: "consulta",
    component: consultayCancelacion,
    meta: {
      requiresAuth: true,
      role: ["Estudiante"]
    }
  },
  {
    path: "/registrouser",
    name: "registrouser",
    component: registroUser,
    meta: {
      requiresAuth: true,
      role: ["Administrador"]
    }
  },
  {
    path: "/edituser",
    name: "edituser",
    component: editUser,
    meta: {
      requiresAuth: true,
      role: ["Administrador"]
    },
  },
  {
    path: "/reservaestudiante",
    name: "reservaestudiante",
    component: reservaEstudiante,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista"]
    },
  },
  {
    path: "/agendaadicionalesL",
    name: "agendaadicionalesL",
    component: agendaadicionalesL,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista"]
    },
  },
  {
    path: "/agendaadicionalesM",
    name: "agendaadicionalesM",
    component: agendaadicionalesM,
    meta: {
      requiresAuth: true,
      role: ["Estudiante"]
    },
  },
  {
    // Vista rara que puede servir para nocturnos
    path: "/reservatemp",
    name: "reservatemp",
    component: reservatemp,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista"]
    },
  },
  {
    // Vista rara que para profesores
    path: "/clasesadd",
    name: "clasesadd",
    component: clasesadd,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista"]
    },
  },
  {
    // Solicitud de prestamo equipos externos (estudiantes)
    path: "/prestamoequext",
    name: "prestamoequext",
    component: prestamoequExt,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista"]
    },
  },
  {
    // Solicitud de prestamo equipos internos (estudiantes)
    path: "/prestamoequint",
    name: "prestamoequint",
    component: prestamoequInt,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista"]
    },
  },
  {
    path: "/editprofilelab",
    name: "editprofilelab",
    component: editprofilelab,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista"]
    }
  },
  {
    // Vista para manejar personas
    path: "/ticketsman",
    name: "ticketsman",
    component: ticketsman,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista"]
    },
  },
  {
    // Vista para agregar nueva sala (No esta vinculada con el toolbar)
    path: "/addnewsala",
    name: "addnewsala",
    component: Addnewsala,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista", "Administrador"],
    },
  },
  {
    path: "/addequipo",
    name: "Inventarioagregarequipo",
    component: Inventarioagregarequipo,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista", "Administrador"],
    },
  },
  {
    path: "/busquedainventario",
    name: "inventarioconsultar",
    component: inventarioconsultar,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista", "Administrador"],
    },
  },
  {
    path: "/mantenimiento",
    name: "mantenimiento",
    component: mantenimiento,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista", "Administrador"]
    },
  },
  {
    path: "/consultamantenimiento",
    name: "consultamantenimiento",
    component: consultamantenimiento,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista", "Administrador"]
    },
  },
  {
    // Buscar usuario con correo interactivo
    path: "/pruebaBuscar",
    name: "select2",
    component: pruebaSelect2,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista"]
    },      
  },
  {
    path: "/consultareservalabstemp",
    name: "consultareservalabstemp",
    component: consultareservalabstemp,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista"]
    },    
  },
  {
    path: "/informesElementos",
    name: "informesElementos",
    component: informesElementos,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista", "Administrador"]
    }
  },
  {
    path: "/informesHorarios",
    name: "informesHorarios",
    component: informesHorarios,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista", "Administrador"]
    }
  },
  {
    path: "/informesPrestamos",
    name: "informesPrestamos",
    component: informesPrestamos,
    meta: {
      requiresAuth: true,
      role: ["Laboratorista", "Administrador"]
    }
  },
];

const router = new VueRouter({
  routes
});

let objeto = Vue;
router.beforeEach((to, from, next) => {

  console.log("%c Desde el router", "font-size: 1rem;");

  if(to.matched.some(record => record.meta.requiresAuth)){
    if(objeto.$cookies.get("jwt") == null){
      console.log("No hay token -> Se va al home");
      next({name: 'home'})
    }else{
      if(to.matched.some(record => record.meta.role)){
        // const role = jwt_decode(objeto.$cookies.get('jwt')).tipo;
        // console.log("JWT: " + role);
        // console.log("META: ");
        // console.log(to.meta.role);
        if (to.meta.role.includes(jwt_decode(objeto.$cookies.get('jwt')).tipo)){
          console.log("Puede continuar, los roles concuerdan");
          next()
        }else{
          console.log("No concuerdan los roles -> aborta la ruta");
          next(false)
        }
      }else{
        console.log("No hay variable role -> Sigue la ruta");
        next()
      }
    } 
  }else{
    console.log("No tiene la variable requiresAuth o es false -> Sigue la ruta");
    next()
  }
});

export default router;