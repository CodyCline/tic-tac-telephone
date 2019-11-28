import Vue from 'vue';
import VueRouter, { RouterOptions } from 'vue-router';
import Home from '../views/Home.vue';
import Game from '../views/Game.vue';

Vue.use(VueRouter);

const routes = [
	{
		path: '/',
		name: 'home',
		component: Home,
	},
	{
		path: '/play/:roomId',
		name: 'game',
		component: Game,
	},
	{
		path: '/game',
		name: 'room',
		component: Game,
	},
	{ 
		path: '*', 
		redirect: '/',
	},
];

const router = new VueRouter({
  routes,
  mode: 'history',
});

export default router;
