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
      <br />
      <!--Planning Semester-->
      <table class="shopping">
        <!--<th>2022 Fall</th>-->
        <th colspan="2"><!--bad practice-->
            <h2>Fall 2022</h2>
        </th>
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
        <tfoot class="foot">
          <tr>
            <td align="right">Total</td>
            <td>&nbsp;</td>
          </tr>
        </tfoot>
      </table>
    </div>
  </div>
</template>

<script>

export default {
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="css">
h1 {
  text-align: left;
}
h2 {
  margin: 0;
  padding: 0;
}
  h2::first-letter {
    text-decoration: underline;
  }
.scheduler{
  float: left;
  width: 60%;
}

.right{
  float: right;
  width: 35%;
}

  .right table {
    width: 100%;
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
</style>
