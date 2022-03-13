<template>
  <div>
    <Navbar />
    <h1>Required Courses</h1>
    <div class="scheduler">
    <table>
      <tr>
        <th>Selected</th>
        <th>Course Number</th>
        <th>Course Name</th>
        <th>Number of Units</th>
      </tr>
      <tr>
        <td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
            <label for="checkbox">{{ checked }}</label></td>
        <td>CS 4800</td>
        <td>Software Engineering</td>
        <td>4</td>
      </tr>
    </table></div>
    <div class="right">
      <table>
        <th>Course Filters</th>
        <tr>
          <td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
            <label for="checkbox">{{ checked }}</label></td>
          <td>fulfilled/not fulfilled</td>
        </tr>
      </table>
      <table>
        <th>Shopping Cart</th>
        <tr>
          <td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
            <label for="checkbox">{{ checked }}</label></td>
          <td>Course 1</td>
        </tr>
      </table>
    </div>
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
.scheduler{
  float:left;
  padding: 5px 10px;
}
.right{
  float:right;
  padding: 5px 10px;
}
</style>
