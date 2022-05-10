<template>
    <div class="page">
        <h1>My Profile</h1>
        <p>Cal Poly Pomona<br>
        {{degree}}<br>
        {{standing}} Year</p>        
        <h2>Information</h2>
        <p>First Name: {{firstname}}<br>
        Last Name: {{lastname}}<br>
        Email: {{email}}</p>
        <button @click="logout()" variant="primary" class="logout">Log Out</button>
    </div>
</template>

<script>
import axios from 'axios'
export default{
  name: 'MyAccount',
  data(){
    return {
        token: '',
        users: [],
        user1: JSON.parse(JSON.stringify(localStorage.getItem('info'))),
        firstname: '',
        lastname: '',
        email: '',
        degree: '',
        standing: '',
        username: localStorage.getItem('user')
    }
  },
  mounted() {
        var users = this;
        document.title = 'My Profile | Bronco Scheduler'
        console.log('App Mounted');
        if (localStorage.getItem('token')) 
          this.token = localStorage.getItem('token');
        console.log(this.token);
        console.log(this.users)
        axios
        .get("/api/v1/studentlist/", {
          params:{
            username: localStorage.getItem('user')
          }
        })
        .then(response => {
          console.log(response)
          users = JSON.stringify(response)
          localStorage.setItem('info',users)
          console.log(users)
          this.users = JSON.parse(JSON.stringify(response))
          this.users = JSON.parse(JSON.stringify(this.users))
          const plain = Object.assign({},this.users)
          this.users = plain
          console.log(this.users)
          console.log(plain.data[0].username)
          console.log(plain.data)

          for (let product of plain.data) {
            if (product.username === this.username) {
              this.firstname = product.firstname;
              this.lastname = product.lastname;
              this.email = product.email;
              if (product.degree === 1){
                this.degree = 'Computer Science UG';
              }
              if (product.standing === 1){
                this.standing = '1st';
              }
              else if (product.standing === 2){
                this.standing = '2nd';
              }
              else if (product.standing === 3){
                this.standing = '3rd';
              }
              else if (product.standing === 4){
                this.standing = '4th';
              }
            }
          }
        
          //console.log(users.data[0])
          console.log(plain.data.Length)
        })
  },
  methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            this.$router.push('/login')
        },
        convertProxyObjectToPojo(proxyObj) {
          return _.cloneDeep(proxyObj);
    }
  },
  created(){
          let token;
          this.token = localStorage.getItem('token');
        }
}
</script>

<style scoped>
.logout {
  background: #00843D;
  color: #ffffff;
  font-size: 15pt;
  padding: 5px 10px;
  border: none;
  border-radius: 3px;
  margin: 5px 0px 20px 0px;
}
.page {
  padding-top: 50px;
}
</style>