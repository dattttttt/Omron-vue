<template>
  <div class="bg-white shadow-md rounded-2xl p-4 border border-gray-200 flex flex-col items-center text-center hover:shadow-lg transition">
    <div class="text-4xl mb-2">
      <component :is="iconMap[name.toLowerCase()] || defaultIcon" />
    </div>
    <div class="text-lg font-semibold capitalize text-gray-800">{{ name }}</div>
    <div class="text-2xl font-bold text-blue-600">{{ value }}</div>
  </div>
</template>

<script setup>
import {
  WiThermometer, WiHumidity, WiDaySunny, WiBarometer,
  WiRaindrop, WiSmoke, WiStrongWind, WiAlien, WiHot
} from 'react-icons/wi'

const props = defineProps({
  name: String,
  value: [String, Number],
})

const defaultIcon = WiAlien

const iconMap = {
  temperature: WiThermometer,
  humidity: WiHumidity,
  illuminance: WiDaySunny,
  atmosphericpressure: WiBarometer,
  noise: WiRaindrop,
  etvoc: WiSmoke,
  eco2: WiStrongWind,
  discomfortindex: WiHot,
  heatstrokerisklevel: WiHot,
}
</script>
