// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import index2 from './components/index2'
import index1 from './components/index1'
import show from './components/show'
import slideshow from './components/slideshow'
import item from './components/item'
import foot from './components/foot'
import card from './components/card'
import user from './components/user'
import shoppingcart from './components/shoppingcart'
import detail from './components/detail'
import denglu from './components/denglu'
import zhuce from './components/zhuce'
import wangji from './components/wangji'
import aboutme from './components/aboutme'
import realdetail from './components/realdetail'
import mysell from './components/mysell_page'
import sellcard from './components/sellcard'
import editsell from './components/editsell'
import addsell from './components/addsell'
import sell from './components/sell'
import sellpage from './components/sell_page'
import edit from './components/edit_page'
import add from './components/add_page'
import axios from 'axios'
import VueParticles from 'vue-particles'
Vue.prototype.$axios = axios
Vue.use(VueParticles)
Vue.component('index1', index1)
Vue.component('index2', index2)
Vue.component('show', show)
Vue.component('slideshow', slideshow)
Vue.component('item', item)
Vue.component('foot', foot)
Vue.component('card', card)
Vue.component('user', user)
Vue.component('shoppingcart', shoppingcart)
Vue.component('detail', detail)
Vue.component('denglu', denglu)
Vue.component('zhuce', zhuce)
Vue.component('wangji', wangji)
Vue.component('aboutme', aboutme)
Vue.component('realdetail', realdetail)
Vue.component('mysell_page', mysell)
Vue.component('sellcard', sellcard)
Vue.component('editsell', editsell)
Vue.component('edit_page', edit)
Vue.component('addsell', addsell)
Vue.component('add', add)
Vue.component('sell', sell)
Vue.component('sellpage', sellpage)

Vue.config.productionTip = false

router.afterEach((to) => {
  // 根据当前路由名称更改导航选中状态
  App.activeIndex = to.name
})

Vue.use(ElementUI)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
