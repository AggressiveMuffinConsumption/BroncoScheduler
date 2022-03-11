<template>
  <div>
    <Navbar />
    <h1>Required Courses</h1>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"

export default {
  components: {
    Navbar,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h1 {
  font-size: 60pt;
}
</style>
