<script setup>
import { ref } from 'vue'

defineProps({
  msg: String
})

const serverMsg = ref('REACHING')

const getHelloWorld = async () => {
  fetch('http://localhost:99/api/hello-world').then((r) => {
    return r.json()
  }).then((r) => {
    serverMsg.value = r.msg
  })
}

getHelloWorld()

const count = ref(0)
</script>

<template>
  <div id="b">
    <h1>{{ msg }}</h1>
    <div class="card">
      <button type="button" @click="count++">count is {{ count }}</button>
      <p>
        Edit
        <code>components/HelloWorld.vue</code> to test HMR
      </p>
    </div>

    <p>
      Server message : {{ serverMsg }}
    </p>
    <p>
      Check out
      <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank">create-vue</a>, the official Vue + Vite
      starter
    </p>
    <p>
      Install
      <a href="https://github.com/johnsoncodehk/volar" target="_blank">Volar</a>
      in your IDE for a better DX
    </p>
    <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
  </div>
</template>

<style lang="scss">
@import "../style.scss";

.read-the-docs {
  color: #888;
}
</style>
