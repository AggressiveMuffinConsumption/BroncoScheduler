<template>
  <div>
    <h1>Bronco Scheduler</h1>
      <input v-model="username" placeholder="username" class="textbox" label="username"/><br />
      <input v-model="password" placeholder="password" class="textbox" label="password"/><br />
      <button type="login" variant="primary" class="login">Log In</button><br />
      Create Account &nbsp;|&nbsp; Forgot Password
  </div>
</template>

<script>
export default {
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Outfit&family=Roboto&display=swap');
h1 {
  font-family: Outfit, Helvetica, Arial, sans-serif;
  font-size: 80pt;
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
  color: #42b983;
}
</style>
