<template>
    <div id="navbar">
        <h1>Bronco Scheduler_</h1>
        <div class="options">
            <router-link to="/required"><button>Required Courses</button></router-link>
            <router-link to="/history"><button>Course History</button></router-link>
            <button>Username</button>
            <button>&nbsp;</button>
        </div>
    </div>
</template>
<script>
export default {
    setup() {
        
    },
}
</script>
<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Outfit&family=Roboto&display=swap');

#navbar {
    background: #01426A;
    width: 100%;
    padding: 15px 0px;
    color: #ffffff;
    position: fixed;
    top: 0;
    left: 0;
    text-align: left;
    font-size: 16pt;
}

#navbar h1 {
    font-size: 20pt;
    padding-left: 30px;
    float: left;
}

.options {
    padding-top: 15px;
    float: right;
}

button {
    background: transparent;
    float: left;
    margin-right: 20px;
    border: none;
    padding: 10px 10px;
    color: #ffffff;
    font-size: 15pt;
}

button:hover {
    border-bottom: 3px solid #ffffff;
}

</style>