<template>
  <div id="container">
    <h1 msg="unit testing">Course History</h1>
    <div class="semester">
      <h2>Fall 2018</h2>
      <!--TODO: find a way to not have tables be pushed out of position with uneven num of classes-->
      <!--use v-if to render a row in red if credits = 0-->
      <table> <!--use v-for to generate right number of tables-->
        <tr>
          <th>Course #</th>
          <th class="name">Course Name</th>
          <th>Credits</th>
        </tr>
        <tr> <!--use v-for to populate the table-->
          <td>CS4800</td>
          <td>Software Engineering</td>
          <td>3.00</td>
        </tr>
        <tr>
          <td>&nbsp;</td>
          <td>&nbsp;</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
          <th class="total" colspan="2">Total</th>
          <td>&nbsp;</td>
        </tr>
      </table>
    </div>

    <div class="semester">
      <h2>Spring 2019</h2>
      <table> <!--use v-for to generate right number of tables-->
        <tr>
          <th>Course #</th>
          <th class="name">Course Name</th>
          <th>Credits</th>
        </tr>
        <tr> <!--use v-for to populate the table-->
          <td>CS4800</td>
          <td>Software Engineering</td>
          <td>3.00</td>
        </tr>
        <tr>
          <td>&nbsp;</td>
          <td>&nbsp;</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
          <th class="total" colspan="2">Total</th>
          <td>&nbsp;</td>
        </tr>
      </table>
    </div>

    <div class="semester">
      <h2>Summer 2019</h2>
      <table> <!--use v-for to generate right number of tables-->
        <tr>
          <th>Course #</th>
          <th class="name">Course Name</th>
          <th>Credits</th>
        </tr>
        <tr> <!--use v-for to populate the table-->
          <td>CS4800</td>
          <td>Software Engineering</td>
          <td>3.00</td>
        </tr>
        <tr>
          <td>&nbsp;</td>
          <td>&nbsp;</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
          <th class="total" colspan="2">Total</th>
          <td>&nbsp;</td>
        </tr>
      </table>
    </div>
    <!-- <p>{{ msg }}</p> -->
  </div>
</template>

<script>
export default {
  name: 'Test Message',
  props: {
    msg: String
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
