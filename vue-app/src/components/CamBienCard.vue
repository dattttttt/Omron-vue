<template>
  <div class="bg-white shadow rounded-xl p-4 text-center">
    <div class="text-4xl">{{ icon }}</div>
    <div class="text-xl font-semibold">{{ name }}</div>
    <div class="text-2xl font-bold">{{ value }}</div>
  </div>
</template>

<script setup>
const props = defineProps({
  name: String,
  value: [String, Number]
})

const iconMap = {
  temperature: '🌡️',
  humidity: '💧',
  illuminance: '☀️',
  atmosphericpressure: '🌬️',
  noise: '🔊',
  etvoc: '🧪',
  eco2: '🌿',
  discomfortindex: '😓'
}

const icon = iconMap[props.name?.toLowerCase()] || '❓'
</script>