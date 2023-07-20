import Vue from 'vue'
import Router from 'vue-router'
import show from '@/components/show'
import myshopping from '@/components/myshopping'
import login from '@/components/login'
import zhuce from '@/components/zhuce'
import wangji from '@/components/wangji'
import aboutme from '@/components/aboutme'
import realdetail from '@/components/realdetail'
import mysell from '@/components/mysell_page'
import edit from '@/components/edit_page'
import add from '@/components/add_page'
import sellpage from '@/components/sell_page'
Vue.use(Router)



export default new Router({
  // mode: 'history',
  routes: [
    {
      path: '/user',
      name: 'user',
      component: aboutme
    },
    {
      path: '/sell',
      name: 'sell',
      component: sellpage
    },
    {
      path: '/add',
      name: 'add',
      component: add
    },
    {
      path: '/edit',
      name: 'edit',
      component: edit
    },
    {
      path: '/mysell',
      name: 'mysell',
      component: mysell
    },
    {
      path: '/',
      name: 'showpage',
      component: show
    },
    {
      path: '/cart',
      name: 'shoppingcart',
      component: myshopping
    },
    {
      path: '/detail/:productId',
      name: 'detail',
      component: realdetail
    },
    {
      path: '/login',
      component: login
    },
    {
      path: '/signup',
      name: 'signup',
      component: zhuce
    },
    {
      path: '/forget',
      name: 'forget',
      component: wangji
    },
    {
      path: '*',
      component: () => import('../components/404.vue')
    }
  ]
})
