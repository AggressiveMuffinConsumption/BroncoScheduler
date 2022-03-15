<template>
  <div class="about">
    <Navbar />
    <Profile />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"
import Profile from '@/components/Profile.vue'

export default {
  name: 'HistoryView',
  components: {
    Navbar,
    Profile,
  }
}
</script>