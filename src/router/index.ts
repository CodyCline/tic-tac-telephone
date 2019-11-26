***REMOVED***;
import VueRouter, { RouterOptions ***REMOVED*** from 'vue-router';
import Home from '../views/Home.vue';
import Game from '../views/Game.vue';

Vue.use(VueRouter);

const routes = [
	{
		path: '/',
		name: 'home',
		component: Home,
	***REMOVED***,
	{
		path: '/play/:roomId',
		name: 'game',
		component: Game,
	***REMOVED***,
	{
		path: '/game',
		name: 'room',
		component: Game,
	***REMOVED***,
	{ 
		path: '*', 
		redirect: '/',
	***REMOVED***,
];

const router = new VueRouter({
  routes,
  mode: 'history',
***REMOVED***;

export default router;
