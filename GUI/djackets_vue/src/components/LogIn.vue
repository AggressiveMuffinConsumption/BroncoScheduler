<template>
  <div>
    <h1>Bronco Scheduler</h1>
      <form @submit.prevent="submitForm">
        <input v-model="username" placeholder="username" class="textbox" label="username"/><br />
        <input v-model="password" placeholder="password" class="textbox" label="password" type="password"/><br />
        <div class ="notification is-danger" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>
        <div class = "control">
          <button class ="login" >Log In</button>
        </div>
      </form>
      <router-link to="/create-account">Create Account</router-link> | 
      <router-link to="/forgot-password">Forgot Password</router-link><br />
  </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
export default {
  name: 'LogIn',
  data(){
    return{
      username: '',
      password: '',
      errors: []
    }
  },
  mounted(){
    document.title = 'Log in | Bronco Scheduler'
  },
  methods:{
    async submitForm(){
      axios.defaults.headers.common["Authorization"] = ""

      localStorage.removeItem("token")

      const formData ={
        username: this.username,
        password: this.password
      }

      await axios
        .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token
                    console.log(response)
                    axios.defaults.headers.common["Authorization"] = "Token " + token
                    localStorage.setItem("token", token)
                    localStorage.setItem("user", this.username)
                    const toPath = this.$route.query.to || '/home'
                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        
                        console.log(JSON.stringify(error))
                    }
                })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h1 {
  font-size: 80pt;
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
