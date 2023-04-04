import {createRouter, createWebHistory} from "vue-router";
import ArticleDetail from "@/components/ArticleDetail.vue";
import HomePage from "@/components/HomePage.vue";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomePage
    },
    {
        path: '/article/:id',
        name: 'ArticleDetail',
        component: ArticleDetail
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});
export default router;