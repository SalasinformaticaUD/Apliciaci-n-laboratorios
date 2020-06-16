<template>
  <v-container class="grey darken-4" dark fluid>
    <HeaderLaboratorista />
    <v-row>
      <v-col>
        <v-col cols="12">
          <v-card color="#424242" dark class="mx-auto">
            <h1 align="center">Políticas Generales</h1>
            <v-card-text class="font-weight-bold">
              <p align="justify">
                El Laboratorio de la Facultad de Ingeniería, es la dependencia
                que se encarga del desarrollo administrativo para el apoyo
                académico a los proyectos curriculares de la facultad
                (Ingeniería Eléctrica, Ingeniería Electrónica, Ingeniería
                Catastral y Geodesia, Ingeniería Industrial e Ingeniería de
                Sistemas) y a los programas de Especialización y Maestrías.
                Diseñamos e implementamos estrategias relacionadas con la
                investigación, la producción y uso de las nuevas tecnologías
                aplicadas a la educación, con el fin de contribuir a que la
                Universidad Distrital Francisco José de Caldas cumpla con su
                función Social a través de la docencia, la investigación y la
                extensión.
              </p>
            </v-card-text>
          </v-card>
          <v-row>
            <v-col cols="4">
              <v-card color="#424242" dark>
                <h1 align="center">Calendario</h1>
                <v-card-text>
                  <v-calendar
                    ref="calendar"
                    v-model="value"
                    :weekdays="weekday"
                    :type="type"
                    :events="events"
                    :event-overlap-mode="mode"
                    :event-overlap-threshold="30"
                    :event-color="getEventColor"
                    @change="getEvents"
                  ></v-calendar>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="4">
              <v-card color="#424242" dark>
                <h1 align="center">Misión</h1>
                <v-card-text class="font-weight-bold">
                  <p align="justify">
                    La misión del Laboratorio de la Facultad de Ingeniería, se
                    proyecta en la planificación y gestión de la Infraestructura
                    tecnológica de la Universidad mediante el apoyo a la gestión
                    educativa para el logro de la excelencia académica de la
                    Facultad de Ingeniería en el desarrollo de la construcción
                    del conocimiento y de los métodos de trabajo investigativo y
                    docente como complemento y aplicación del proceso de
                    enseñanza y aprendizaje guiado por el Docente en el aula de
                    clase y orientado en la práctica en el Laboratorio para la
                    construcción de la identidad en el abordaje de la Ciencia,
                    Cultura y Sociedad.
                  </p>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="4">
              <v-card color="#424242" dark>
                <h1 align="center">Visión</h1>
                <v-card-text class="font-weight-bold">
                  <p align="justify">
                    Contribuir en la formación de integral de los nuevos
                    Ingenieros, articulando el conocimiento teórico y la praxis
                    con la experimentación, en búsqueda de la excelencia,
                    motivando la investigación y contribuyendo al desarrollo
                    científico y tecnológico aportando soluciones a las
                    necesidades actuales y futuras de la comunidad, empresas e
                    industria del País.
                  </p>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-col>
    </v-row>
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
  })
};
</script>
