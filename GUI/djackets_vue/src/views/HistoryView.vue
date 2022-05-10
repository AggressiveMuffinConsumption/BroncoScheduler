<template>
  <div class="about">
    <Navbar />
    <History msg="Hello World" />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"
import History from '@/components/History.vue'
export default {
  name: 'HistoryView',
  components: {
    Navbar,
    History,
  }
}
</script>