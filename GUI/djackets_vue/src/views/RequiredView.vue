<template>
  <div>
    <Navbar />
    <Required />
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue"
import Required from '@/components/Required.vue'
export default {
  name: 'RequiredView',
  components: {
    Navbar,
    Required,
  },
};
</script>