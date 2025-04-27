<template>
  <div class="grid grid-cols-2 gap-4">
    <CamBienCard
      v-for="(item, index) in parsedData"
      :key="index"
      :name="item[0]"
      :value="item[1]"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import CamBienCard from './CamBienCard.vue'

const rawData = ref([])
const parsedData = ref([])

const fetchData = async () => {
  try {
    console.log("📡 Đang gọi API:", import.meta.env.VITE_API_URL)
    const res = await fetch(`${import.meta.env.VITE_API_URL}/api/data`)
    const data = await res.json()
    rawData.value = data

    parsedData.value = data
      .map(line => line.trim())
      .filter(line => line && !line.startsWith("Tên cảm biến"))
      .map(line => line.split(','))
      .reverse()
  } catch (e) {
    console.error('❌ Lỗi khi fetch dữ liệu:', e)
  }
}

onMounted(() => {
  fetchData()
  setInterval(fetchData, 5000)
})
</script>
