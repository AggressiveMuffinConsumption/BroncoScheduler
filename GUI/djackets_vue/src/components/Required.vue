<template>
  <div id="container">
    <h1>Required Courses</h1>
    <!--Scheduler Table-->
    <div class="scheduler">
      <table>
        <thead>
          <tr>
            <th style="width:10%">Selected</th>
            <th style="width:15%">Course Number</th>
            <th style="width:30%">Course Name</th>
            <th style="width:15%">Number of Units</th>
          </tr>
        </thead>
        <tbody>
          <tr 
          v-for="tester in classList" 
          v-bind:key="tester.id">
            <td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
                <label for="checkbox">{{ checked }}</label></td>
            <td class="slug">{{tester.slug}}</td>
            <td>{{tester.name}}</td>
            <td>{{tester.units}}</td>
          </tr>
        </tbody>
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
        <tr 
          v-for="tester in currentSem" 
          v-bind:key="tester.id">
            <td class="slug" v-if="tester.standing===1">{{tester.slug}}</td>
            <td v-if="tester.standing===1">{{tester.units}}</td>
          </tr>
        <tfoot class="foot">
          <tr>
            <td align="right">Total</td>
            <td>{{totalUnits}}</td>
          </tr>
        </tfoot>
      </table>

      <table class="shopping">
        <!--<th>2022 Fall</th>-->
        <th colspan="2"><!--bad practice-->
            <h2>Spring 2023</h2>
        </th>
        <tr>
          <!--<td></td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
            <label for="checkbox">{{ checked }}</label></td>-->
          <th>Courses</th>
          <th>Units</th>
        </tr>
        <tr 
          v-for="tester in sem2" 
          v-bind:key="tester.id">
            <td class="slug" v-if="tester.standing===2">{{tester.slug}}</td>
            <td v-if="tester.standing===2">{{tester.units}}</td>
          </tr>
        <tfoot class="foot">
          <tr>
            <td align="right">Total</td>
            <td>{{totalUnits2}}</td>
          </tr>
        </tfoot>
      </table>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Required',
  data(){
    return {
      classList: [],
      totalUnits: 0,
      currentSem: [],
      totalUnits2: 0,
      sem2: [],
      totalUnits3: 0,
      sem3: [],
      totalUnits3: 0,
      sem4: [],
    }
  },
  components: {
  },
  mounted() {
    this.getClassList(),
    this.getTotalUnits(),
    document.title = 'Required Courses | Bronco Scheduler'
  },
  methods: {
    getClassList() {
      axios
        .get('/api/v1/classlist/')
        .then(response => {
          this.classList = response.data
          var users = JSON.parse(JSON.stringify(response))
          const plain = Object.assign({},users)
          var count = 0
          var i = 0
          for (let product of plain.data) {
            // if (product.standing === 1) {
            //   this.totalUnits = this.totalUnits + product.units;
            // }
            if(count < 6 && product.standing === 1){
              this.currentSem[count] = product;
              this.totalUnits = this.totalUnits + product.units;
              count ++;
            }
            else if(i < 5 && product.standing === 2){
              this.sem2[i] = product;
              this.totalUnits2 = this.totalUnits2 + product.units;
              i++;
            }

          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    getTotalUnits(){
      console.log("posted");
      for(let i = 0; i < this.classList.Length; i++){
        console.log(this.classList[i].units)
        if(this.classList[i].standing === 1){
          this.totalUnits = this.totalUnits + this.classList[i].units;
          console.log(this.classList[i].units);
        }
      }
    }
  }
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
.shopping {
  margin-bottom: 20px;
}
.shopping:last-child {
  margin-bottom: 0;
}
.slug {
  text-transform: uppercase;
}
</style>