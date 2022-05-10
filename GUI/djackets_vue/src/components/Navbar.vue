<template>
    <div id="navbar">
        <router-link to="/home"><button id="title"><h1>Bronco Scheduler_</h1></button></router-link>
        <div class="options">
            <router-link to="/required"><button>Required Courses</button></router-link>
            <router-link to="/history"><button>Course History</button></router-link>
            <router-link to="/profile"><button>Profile</button></router-link>
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
#navbar #title {
    background: transparent;
    font-size: 20pt;
    padding: 0;
    padding-left: 30px;
    float: left;
    border: none;
    color: #ffffff;
}
#title h1 {
    font-size: 25pt;
    padding: 0;
    margin: 0;
}
.options {
    float: right;
}
.options button {
    background: transparent;
    float: left;
    margin-right: 20px;
    border: none;
    padding: 10px 10px 7px 10px;
    color: #ffffff;
    font-size: 15pt;
    border-bottom: 3px solid transparent;
}
button:hover {
    border-bottom: 3px solid #ffffff;
}
</style>