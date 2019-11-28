***REMOVED***;
import SocketIO from 'socket.io-client';
import VueSocketIO from 'vue-socket.io';
import VueFlex from '@seregpie/vueflex';
import router from './router';
import store from './store';
import App from './App.vue';

const SocketInstance = new SocketIO(`http://${window.location.hostname***REMOVED***:5000`);


Vue.use(new VueSocketIO({
	debug: true,
	connection: SocketInstance,
	vuex: {
        store,
        actionPrefix: 'SOCKET_',
        mutationPrefix: 'SOCKET_'
***REMOVED***
***REMOVED***);
Vue.use(VueFlex);
Vue.config.productionTip = false;
new Vue({
	router,
	store,
	render: (h) => h(App),
***REMOVED***.$mount('#app');
