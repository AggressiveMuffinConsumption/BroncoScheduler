<template lang="en">
  <div>
    <nav>
      <!--<router-link to="/">Log In</router-link> |
      <router-link to="/history">Course History</router-link> | 
      <router-link to="/required">Required Courses</router-link>-->
    </nav>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Outfit&family=Roboto&display=swap');
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  font-size: 12pt;
}
p {
  font-size: 15pt;
}
nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
h1, h2, h3, h4, h5 {
  font-family: Outfit, Helvetica, Arial, sans-serif;
}
h1 {
  font-size: 40pt;
}
</style>