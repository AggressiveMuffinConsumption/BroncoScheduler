<template>
  <div>
    <h1>Bronco Scheduler</h1>
    <h2>Create Account</h2>
    <form @submit.prevent="submitForm">
      <input v-model="email" placeholder="email" class="textbox" label="email" type = "email" /><br />
      <input v-model="username" placeholder="username" class="textbox" label="username" type = "text" /><br />
      <input v-model="first_name" placeholder="first name" class="textbox" label="first_name" type = "text" /><br />
      <input v-model="last_name" placeholder="last name" class="textbox" label="last_name" type = "text" /><br />
      <input v-model="password" placeholder="password" class="textbox" label="password" type = "password" /><br />
      <input v-model="confpassword" placeholder="confirm password" class="textbox" label="confirm password" type = "password"/><br />
      <div class ="notification is-danger" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>
      <div class = "control">
        <button class ="login" >Sign Up</button>
      </div>
    </form>
      Have an account? 
      <router-link to="/login">Log In</router-link>
  </div>
</template>


<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
export default {
  name: 'CreateAcc',
  data(){
    return{
      email: '',
      username: '',
      first_name: '',
      last_name: '',
      password: '',
      confpassword: '',
      errors: []
    }
  },
  mounted(){
    document.title = 'Create Account | Bronco Scheduler'
  },
  methods:{
    submitForm(){
      this.errors = []
      if(this.email === ''){
        this.errors.push('Email is empty')
      }

      if(this.username === ''){
        this.errors.push('Username is empty')
      }

      if(this.first_name === ''){
        this.errors.push('First name is empty')
      }

      if(this.last_name === ''){
        this.errors.push('Last name is empty')
      }

      if(this.password === ''){
        this.errors.push('Password is empty')
      }

      if(this.confpassword !== this.password){
        this.errors.push('Passwords do not match')
      }

      if(!this.errors.length){
        const formData = {
          username: this.username,
          password: this.password,
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email
        }

        const formData2 = {
          firstname: this.first_name,
          lastname: this.last_name,
          username: this.username,
          email: this.email
        }

        axios
            .post("/api/v1/studentlist/", formData2)
            .then(response => {
              console.log(this.last_name)
                return axios 
                          .post("/api/v1/users/", formData)
            .then(response => {
              console.log(this.first_name)
              toast({
                message: 'Account successfully created! Please log in.',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
              })

              this.$router.push('/login')
            })
            .catch(error => {
              if(error.response){
                for(const property in error.response.data){
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
                
                console.log(JSON.stringify(error.response.data))
              }
              else if(error.message){
                this.errors.push('Something went wrong. Please try again')

                console.log(JSON.stringify(error))
              }
            })
            })
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h1 {
  font-size: 50pt;
  font-weight: 600;
}

.textbox {
  background: #EEEEEE;
  width: 25%;
  margin-bottom: 10px;
  padding: 10px 15px;
  border: 1px solid #AAAAAA;
  border-radius: 3px;
  font-size: 15pt;
}

.login {
  background: #00843D;
  color: #ffffff;
  font-size: 15pt;
  padding: 5px 10px;
  border: none;
  border-radius: 3px;
  margin: 5px 0px 20px 0px;
}

  .login:hover {
    background: #FFB400;
    color: #000000;
  }

a {
  color: #00843D;
}
</style>
