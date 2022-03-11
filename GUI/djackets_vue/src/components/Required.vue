<template>
  <div>
    <Navbar />
    <h1>Required Courses</h1>
    <table>
      <tr>
        <th>Selected</th>
        <th>Course Number</th>
        <th>Course Name</th>
        <th>Number of Units</th>
      </tr>
      <tr>
        <td><input type="checkbox"/></td>
        <td>CS 4800</th>
        <td>Software Engineering</th>
        <td>4</th>
      </tr>
    </table>
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
