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
		path: '/play?g=:roomId',
		name: 'game',
		component: Game,
	***REMOVED***,
	{
		path: '/game',
		name: 'room',
		component: Game,
	***REMOVED***,
];

const router = new VueRouter({
  routes,
  mode: 'history',
***REMOVED***;

export default router;
