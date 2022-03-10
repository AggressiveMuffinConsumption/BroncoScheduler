<template>
    <div id="navbar">
        <h1>Bronco Scheduler</h1>
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
    text-transform: uppercase;
    font-size: 20pt;
    padding-left: 20px;
    float: left;
}

.options {
    float: right;
}

button {
    background: transparent;
    float: left;
    margin-right: 20px;
    border: none;
    padding: 0 20px;
    color: #ffffff;
}

</style>