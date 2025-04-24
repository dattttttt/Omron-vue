<template>
  <div class="flex flex-col h-screen">
    <Header />
    <div class="flex flex-1 overflow-hidden">
      <Sidebar />
      <main class="flex-1 overflow-auto bg-gray-50 p-6">
        <SensorDisplay />
      </main>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import Sidebar from './components/Sidebar.vue'
import SensorDisplay from './components/SensorDisplay.vue'
import Footer from './components/Footer.vue'
</script>