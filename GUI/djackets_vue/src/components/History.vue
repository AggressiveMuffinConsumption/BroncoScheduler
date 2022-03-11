<template>
  <div>
    <Navbar />
    <h1 msg="unit testing">Course History</h1>
    <p>Unit Testing: {{ msg }}</p>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"

export default {
  components: {
    Navbar,
  },
  name: 'Test Message',
  props: {
    msg: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h1 {
  font-size: 60pt;
}
</style>
