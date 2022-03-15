<template>
    <div class="page">
        <h1>My Profile</h1>
        <p>Cal Poly Pomona<br>
        Computer Science UG<br>
        4th Year</p>        
        <h2>Information</h2>
        <p>First Name: User<br>
        Last Name: Name<br>
        Email: uname@cpp.edu</p>
        <router-link to="/"><button variant="primary" class="logout">Log Out</button></router-link><br />
    </div>
</template>

<script>
export default{

};
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