<template>
  <div class="greating">
    <h1>{{ hello }}</h1>
      <div v-if="storages">
        {{ storages }}
      </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: "greating-page",
  props: ['hello'],
  computed: {
    ...mapState({
      storages: 'storages'
    })
  },
  methods: {}
}
</script>

<style scoped>

</style>