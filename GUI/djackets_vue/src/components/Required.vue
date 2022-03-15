<template>
  <div>
    <Navbar />
    <h1>Required Courses</h1>
    <!--Scheduler Table-->
    <div class="scheduler table-format">
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
    </table></div>
    <div class="right">
    <!--Filters Selection-->
      <table style="width:100%">
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
      <table class="shopping" style="width:100%">
        <!--<th>2022 Fall</th>-->
        <thead style="border-bottom:1px solid gray"><!--bad practice-->
            <p align="center">Fall 2022</p>
        </thead>
        <tbody>
        <tr>
          <!--<td></td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
            <label for="checkbox">{{ checked }}</label></td>-->
          <th>Courses</th>
          <th>Units</th>
        </tr>
        <tr style="border-top: 1px solid gray">
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
  width: 70%;
  padding: 5px 10px 5px 30px;
}
.right{
  float:right;
  width: 30%;
  padding: 5px 30px 10px 10px;
}
.table-format{
  th, td{
   border: 1px solid gray;
   border-collapse: collapse; 
   padding: 10px;
  }
}
table{
  border: 1px solid gray;
  th, td{
    padding: 3px 10px 3px 10px;
  }
.foot{
  border: 1px solid gray;
  td{
    border-left:1px solid gray;
    }
  }
}
</style>
