import '../node_modules/vuetify/src/stylus/app.styl'

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VApp from 'vuetify/es5/components/VApp'
import Vuetify from 'vuetify/es5/components/Vuetify'
import VSelect from 'vuetify/es5/components/VSelect'
import VBtn from 'vuetify/es5/components/VBtn'
import VList from 'vuetify/es5/components/VList'
import VDataTable from 'vuetify/es5/components/VDataTable'
import VSnackbar from 'vuetify/es5/components/VSnackbar'
import transitions from 'vuetify/es5/components/transitions'
import directives from 'vuetify/es5/directives'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

Vue.use(Vuetify, {
  components: {
    VApp,
    Vuetify,
    VBtn,
    VSnackbar,
    VDataTable,
    VList,
    VSelect
  },
  directives,
  transitions
})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
