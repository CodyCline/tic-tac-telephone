***REMOVED***;
import VueSocketIO from 'vue-socket.io';
import router from './router';
import store from './store';
import App from './App.vue';


Vue.use(VueSocketIO, `//${window.location.host***REMOVED***`, store);
Vue.config.productionTip = false;
new Vue({
  router,
  store,
  render: (h) => h(App),
***REMOVED***.$mount('#app');
