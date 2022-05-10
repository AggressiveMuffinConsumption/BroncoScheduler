<template>
    <div id="container">
      <h1>Hello, {{user}}!</h1>
      <h2>Important Dates</h2>
      <table><caption>Overview of Fall 2021 Scheduling and Registration Deadlines</caption>
        <thead>
            <tr>
                <th scope="col" style="width: 430px;">SCHEDULING AND REGISTRATION</th>
                <th scope="col" style="width: 150px;">Fall 2021 Semester <br>15-Week Session</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="width: 430px;">Registration Advising Period</td>
                <td style="width: 150px;">March 22 - June 11</td>
            </tr>
            <tr>
                <td style="width: 430px;">Priority Registration Period</td>
                <td style="width: 150px;">April 19 - 20</td>
            </tr>
            <tr>
                <td style="width: 430px;">General Registration Period</td>
                <td style="width: 150px;">April 21 - June 11</td>
            </tr>
            <tr>
                <td style="width: 430px;">New Student Orientation (tentative)</td>
                <td style="width: 150px;">June 9 - August 6</td>
            </tr>
            <tr>
                <td style="width: 430px;">Fee Bills Posted to BroncoDirect</td>
                <td style="width: 150px;">July 1</td>
            </tr>
            <tr>
                <td style="width: 430px;">Fees Due</td>
                <td style="width: 150px;">July 22</td>
            </tr>
        </tbody>
      </table>
      <h2>To Do</h2>
        <ul>
          <li>Graduate</li>
        </ul>
    </div>
</template>
<script>
import axios from 'axios'
export default {
  data(){
    return{
      user: 'j'
    }
  },
  
  mounted(){
  document.title = 'Home | Bronco Scheduler';
  console.log('App Mounted');
    if (localStorage.getItem('user')) 
        this.user = localStorage.getItem('user');
  },
}

</script>
<style scoped>
h1 {
    font-size: 80pt;
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
ul {
    list-style-type:circle;
}
#container {
  margin-top: 50px;
  padding: 0px 50px;
}
</style>