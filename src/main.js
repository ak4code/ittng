import {createApp} from 'vue'
import store from './store'

const app = createApp({})

app.use(store).mount('#ittng')
