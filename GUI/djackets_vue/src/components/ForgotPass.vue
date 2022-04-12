<template>
  <div>
    <h1>Bronco Scheduler</h1>
    <h2>Forgot Password?</h2>
      Please enter your email: <br />
      <input v-model="email" placeholder="email" class="textbox" label="email"/><br />
      <router-link to="/forgot-password"><button variant="primary" class="login">Submit</button></router-link><br />
      Have an account? 
      <router-link to="/">Log In</router-link>
  </div>
</template>

<script>
export default {
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
