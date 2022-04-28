<template>
  <div id="container">
    <h1>Required Courses</h1>
    <!--Scheduler Table-->
    <div class="scheduler">
      <!--Filters Selection-->
      <h2>Course Filters

      </h2>
      <table width="100%">
        <tr>
          <td>
            <input
              type="checkbox"
              id="checkbox"
              v-model="unchecked"
              v-on:click="selectTest"
            />
            <label for="checkbox">{{ checked }}</label>
          </td>
          <td>fulfilled/not fulfilled</td>
          <td>
            <input
              type="checkbox"
              id="checkbox"
              v-model="unchecked"
              v-on:click="selectTest"
            />
            <label for="checkbox">{{ checked }}</label>
          </td>
          <td>availability</td>
        </tr>
        <tr>
          <td>
            <input
              type="checkbox"
              id="checkbox"
              v-model="unchecked"
              v-on:click="selectTest"
            />
            <label for="checkbox">{{ checked }}</label>
          </td>
          <td>section</td>
          <td>
            <input
              type="checkbox"
              id="checkbox"
              v-model="unchecked"
              v-on:click="selectTest"
            />
            <label for="checkbox">{{ checked }}</label>
          </td>
          <td>prerequisites</td>
        </tr>
      </table>

      <h2>Available Courses</h2>
      <table>
        <tr>
          <th style="width: 10%">Selected</th>
          <th style="width: 15%">Course Number</th>
          <th style="width: 30%">Course Name</th>
          <th style="width: 15%">Number of Units</th>
        </tr>
        <tr>
          <td>
            <input
              type="checkbox"
              id="checkbox"
              v-model="unchecked"
              v-on:click="selectTest"
            />
            <label for="checkbox">{{ checked }}</label>
          </td>
          <td>CS 4800</td>
          <td>Software Engineering</td>
          <td>4.00</td>
        </tr>
        <tr>
          <td>
            <input
              type="checkbox"
              id="checkbox"
              v-model="unchecked"
              v-on:click="selectTest"
            />
            <label for="checkbox">{{ checked }}</label>
          </td>
          <td>CS 4630</td>
          <td>Undergrad Seminar</td>
          <td>1.00</td>
        </tr>
        <tr>
          <td>
            <input
              type="checkbox"
              id="checkbox"
              v-model="unchecked"
              v-on:click="selectTest"
            />
            <label for="checkbox">{{ checked }}</label>
          </td>
          <td>&nbsp;</td>
          <td>&nbsp;</td>
        </tr>
      </table>
    </div>
    <div class="right">
      <!--dropdown-->
      <SemDropdown />
    </div>
  </div>
</template>

<script>
import App from "../App.vue";
import SemDropdown from "./RequiredSemesters/SemDropdown.vue";

export default {
  components: {
    SemDropdown,
    App,
  },
  props: {
    unchecked: Boolean,
    checked: Boolean
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="css">
h1 {
  text-align: left;
}
.scheduler {
  float: left;
  width: 60%;
}

.right {
  float: right;
  width: 35%;
}

.right table {
  width: 100%;
}

h2 {
  text-align: left;
  margin-top: 25px;
  margin-bottom: 10px;
}

  h2:first-child {
    margin-top: 0;
  }

  td h2 {
    text-align: center;
    margin: 0;
  }

  h2:first-letter {
    text-decoration: underline;
  }

th,
td,
tr {
  padding: 10px;
  border: 1px solid #aaaaaa;
}

table {
  background: #ffffff;
  border: 1px solid #aaaaaa;
  border-collapse: collapse;
}

#container {
  margin-top: 50px;
  padding: 0px 50px;
}

.shopping {
  margin-top: 20px;
}
</style>
