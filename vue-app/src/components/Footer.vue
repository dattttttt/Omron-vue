<template>
  <footer class="bg-gray-800 text-white text-lg py-3 px-6 text-center">
    {{ currentTime }}
  </footer>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const currentTime = ref(new Date().toLocaleString())
let timer

onMounted(() => {
  timer = setInterval(() => {
    currentTime.value = new Date().toLocaleString()
  }, 1000)
})

onUnmounted(() => {
  clearInterval(timer)
})
</script>
