import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/views/Home.vue';
import Game from '@/views/Game.vue';
import GameEditor from '@/views/GameEditor.vue';

Vue.use(VueRouter);

const routes = [
  { 
    path: '/', 
    component: Home
  },
  {
    path: '/game/:id',
    component: Game
  },
  {
    path: '/game/:id/edit',
    component: GameEditor
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  // },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
