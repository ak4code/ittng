import {createStore} from 'vuex'
import { _axios } from "@/plugins/axios"

export default createStore({
    state: {
        storages: null
    },
    getters: {},
    mutations: {
        SET_STORAGES(state, data) {
            state.storages = data
        }
    },
    actions: {
        getStorages({commit}) {
            _axios.get('/api/storages/')
                .then(res => {
                    console.log(res.data)
                    commit('SET_STORAGES', res.data)
                })
                .catch(err => console.error(err))
        }
    },
    modules: {}
})
