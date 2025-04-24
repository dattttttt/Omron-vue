<template>
  <div class="grid grid-cols-2 gap-4">
    <CamBienCard
      v-for="item in messages"
      :key="item.ID"
      :name="item.NE"
      :value="item.V"
    />
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import mqtt from 'mqtt'
import CamBienCard from './CamBienCard.vue'

const messages = ref([])
let client = null

onMounted(() => {
  client = mqtt.connect('ws://localhost:9001')

  client.on('connect', () => {
    console.log('✅ MQTT connected')
    client.subscribe('CPS/data', (err) => {
      if (err) {
        console.error('❌ Subscription failed:', err)
      } else {
        console.log('📡 Subscribed to CPS/data')
      }
    })
  })

  client.on('message', (topic, payload) => {
    try {
      const data = JSON.parse(payload.toString())
      if (data.DATA && Array.isArray(data.DATA)) {
        messages.value = data.DATA
      }
    } catch (err) {
      console.error('❌ JSON parse error:', err)
    }
  })cd omron-vue

  client.on('error', (err) => {
    console.error('❌ MQTT connection error:', err)
  })
})

onBeforeUnmount(() => {
  if (client) {
    console.log('🧹 Cleaning up MQTT client')
    client.end()
  }
})
</script>
