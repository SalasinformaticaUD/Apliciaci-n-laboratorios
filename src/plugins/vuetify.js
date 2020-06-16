import Vue from "vue";
import Vuetify from "vuetify/lib";
import es from "vuetify/es5/locale/es";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#c9312c",
        secondary: "#424242",
        accent: "#82B1FF",
        error: "#FF5252",
        info: "#2196F3",
        success: "#4CAF50",
        warning: "#FFC107",
        cardtext: "#FFFFFF",
        background: "#212121"
      }
    }
  },
  lang: {
    locales: { es },
    current: "es"
  },
  icons: {
    iconfont: "fa"
  }
});
