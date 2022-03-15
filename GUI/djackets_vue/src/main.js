import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vue from 'vue'
// import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

// // // Make BootstrapVue available throughout your project
// Vue.use(BootstrapVue)
// // // Optionally install the BootstrapVue icon components plugin
// Vue.use(IconsPlugin)

// import { library } from "@fortawesome/fontawesome-svg-core";
// import { fas } from '@fortawesome/free-solid-svg-icons'
// library.add(fas);
// import { dom } from "@fortawesome/fontawesome-svg-core";
// dom.watch();

// app.component("font-awesome-icon", FontAwesomeIcon);


// createApp(App).use(store).use(router).mount('#app')

const app = createApp(App)
// app.use(BootstrapVue)
// app.use(IconsPlugin)
app.use(router)
app.use(store)
app.mount('#app')
