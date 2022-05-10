<template>
  <div id="container">
    <h1 msg="unit testing">Course History</h1>
    <div class="semester">
      <h2>Fall 2022</h2>
      <!--TODO: find a way to not have tables be pushed out of position with uneven num of classes-->
      <!--use v-if to render a row in red if credits = 0-->
      <table> <!--use v-for to generate right number of tables-->
        <tr>
          <th>Course #</th>
          <th class="name">Course Name</th>
          <th>Credits</th>
        </tr>
        <tr 
          v-for="tester in currentSem" 
          v-bind:key="tester.id">
            <td class="slug" v-if="tester.standing===1">{{tester.slug}}</td>
            <td v-if="tester.standing ===1">{{tester.name}}</td>
            <td v-if="tester.standing===1">{{tester.units}}</td>
          </tr>
        <tr>
          <th class="total" colspan="2">Total</th>
          <td>{{totalUnits2}}</td>
        </tr>
      </table>
    </div>

    <div class="semester">
      <h2>Spring 2023</h2>
      <table> <!--use v-for to generate right number of tables-->
        <tr>
          <th>Course #</th>
          <th class="name">Course Name</th>
          <th>Credits</th>
        </tr>
        <tr 
          v-for="tester in sem2" 
          v-bind:key="tester.id">
            <td class="slug" v-if="tester.standing===2">{{tester.slug}}</td>
            <td v-if="tester.standing ===2">{{tester.name}}</td>
            <td v-if="tester.standing===2">{{tester.units}}</td>
          </tr>
        <tr>
          <td>&nbsp;</td>
          <td>&nbsp; </td>
          <td>&nbsp;</td>
        </tr>
        <tr>
          <th class="total" colspan="2">Total</th>
          <td>{{totalUnits2}}</td>
        </tr>
      </table>
    </div>

    <!-- <p>{{ msg }}</p> -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Test Message',
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
  props: {
    msg: String
  },
  mounted(){
  document.title = 'History | Bronco Scheduler';
  this.getClassList();
  console.log('App Mounted');
    if (localStorage.getItem('user')) 
        this.user = localStorage.getItem('user');
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
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="css">
h1 {
  text-align: left;
  margin-bottom: 0;
}
h2 {
  width: 100%;
  margin: 0;
  padding: 0px 0px 10px 0px;
  text-align: left;
}
  h2:first-letter {
    text-decoration: underline;
  }
#container {
  margin-top: 50px;
  padding: 0px 50px;
}
.semester {
  width: 50%;
  float: left;
  margin-top: 25px;
}
table {
  background: #ffffff;
  width: 95%;
  padding: 0;
  border-collapse: collapse;
}
  table:nth-child(odd) {
    margin-left: 25px;
  }
th, td {
  border: 1px solid #aaaaaa;
  padding: 10px;
  text-align: left;
}
.name {
  width: 70%;
}
.total {
  text-align: right;
}
</style>