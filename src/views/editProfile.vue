<template>
  <v-container fluid>
    <HeaderLaboratorista />
  </v-container>
</template>

<script>
import HeaderLaboratorista from "@/components/HeaderLaboratorista.vue";
export default {
  components: {
    HeaderLaboratorista
  },
  data: () => ({
    //
  }),
  mounted(){
  this.$verificarLogin();
  },
};
</script>
