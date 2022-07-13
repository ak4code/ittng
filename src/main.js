import axios from "./plugins/axios"
import {createApp} from 'vue'
import store from './store'
import GreatingPage from "@/components/home/GreatingPage"

const app = createApp({
    components: {
        GreatingPage,
    }
})

app.use(axios).use(store).mount('#ittng')
store.dispatch('getStorages')