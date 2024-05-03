import {createWebHistory, createRouter} from "vue-router";

import Home from './apps/Home.vue';
import Sunrise from "@/apps/Sunrise.vue";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/sunrise',
        name: 'Sunrise',
        component: Sunrise
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

export default router;
