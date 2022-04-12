<template>
  <div id="container">
    <h1>Required Courses</h1>
    <!--Scheduler Table-->
    <div class="scheduler">
      <table>
        <tr>
          <th style="width:10%">Selected</th>
          <th style="width:15%">Course Number</th>
          <th style="width:30%">Course Name</th>
          <th style="width:15%">Number of Units</th>
        </tr>
        <tr>
          <td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
              <label for="checkbox">{{ checked }}</label></td>
          <td>CS 4800</td>
          <td>Software Engineering</td>
          <td>4.00</td>
        </tr>
        <tr>
          <td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
              <label for="checkbox">{{ checked }}</label></td>
          <td>CS 4630</td>
          <td>Undergrad Seminar</td>
          <td>1.00</td>
        </tr>
        <tr>
            <td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
              <label for="checkbox">{{ checked }}</label></td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
          </tr>
      </table>
    </div>
    <div class="right">
    <!--Filters Selection-->
      <table>
        <th>Course Filters</th>
        <tr>
          <td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
            <label for="checkbox">{{ checked }}</label></td>
          <td>fulfilled/not fulfilled</td>
        </tr>
        <tr>
          <td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
            <label for="checkbox">{{ checked }}</label></td>
          <td>availability</td>
        </tr>
        <tr>
          <td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
            <label for="checkbox">{{ checked }}</label></td>
          <td>section</td>
        </tr>
        <tr>
          <td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
            <label for="checkbox">{{ checked }}</label></td>
          <td>prerequisites</td>
        </tr>
      </table>
      <!--testing dropdown-->
      <SemDropdown>
        <SemDropdownContent>
          <ul>
            <li>Fall 2020</li>
            <li>Spring 2021</li>
            <li>Summer 2021</li>
            <li>Fall 2021</li>
            <li>Spring 2022</li>
            <li>Summer 2022</li>
          </ul>
        </SemDropdownContent>
      </SemDropdown>

      <!--Planning Semester-->
      <table class="shopping">
        <!--<th>2022 Fall</th>-->
        <thead>
            <td colspan="2"><h2>Fall 2022</h2>
            </td>
        </thead>
        <tbody>
        <tr>
          <!--<td></td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
            <label for="checkbox">{{ checked }}</label></td>-->
          <th>Courses</th>
          <th>Units</th>
        </tr>
        <tr style="border-top: 1px solid #aaaaaa">
          <td>CS 4800</td>
          <td>4.00</td>
        </tr>
        <tr>
          <td>&nbsp;</td>
          <td>&nbsp;</td>
        </tr>
        </tbody>
        <tfoot class="foot">
          <tr>
            <td>Total</td>
            <td>&nbsp;</td>
          </tr>
        </tfoot>
      </table>
    </div>
  </div>
</template>

<script>
import App from '../App.vue';
import SemDropdown from './RequiredSemesters/SemDropdown.vue';
import SemDropdownContent from "./RequiredSemesters/SemDropdownContent.vue";
import SemDropdownTable from "./RequiredSemesters/SemDropdownTable.vue";

export default {
  components: {
    SemDropdown,
    SemDropdownContent,
    SemDropdownTable,
    App,
  },
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="css">
h1 {
  text-align: left;
}
.scheduler{
  float: left;
  width: 60%;
  padding: 5px 10px 5px 20px;
}

.right{
  float: right;
  width: 35%;
  padding: 5px 20px 10px 10px;
}

  .right table {
    width: 100%;
  }

h2 {
  margin: 0;
}

  h2:first-letter {
    text-decoration: underline;
  }

th, td, tr {
  padding: 10px;
  border: 1px solid #aaaaaa;
}

table{
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

ul {
  margin: 0; padding: 0;
  list-style-type: none;
}
</style>
