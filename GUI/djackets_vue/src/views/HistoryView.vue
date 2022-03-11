<template>
  <div class="about">
    <History msg="Hello World" />
  </div>
</template>

<script>
import History from '@/components/History.vue'

export default {
  name: 'HistoryView',
  components: {
    History
  }
}
</script>