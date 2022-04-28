<template>
    <div v-if="active" class="dropdown">
        <slot>
            <ul>
                <li v-for="(semester, id) in semesters" :key="id"><button @click="selectSem(semester)">{{ semester }}</button></li>
            </ul>
        </slot>
    </div>
</template>

<script>
export default {
    name: 'SemDropdownContent',
    inject: ['sharedState'],
    props: {
        semester: String,
    },
    computed: {
        active() {
            return this.sharedState.active
        },
    },
    methods: {
        selectSem(semester) {
            console.log(semester)
            this.sem = semester
        },
        getSemester() {
            console.log("getSemester() " + this.sem)
            if (this.sem == null)
                return "Select Semester"
            return this.sem
            
        }
    },
    data() {
        return {
            semesters:  {
                "1" : "Fall 2020",
                "2" : "Spring 2021",
                "3" : "Summer 2021",
                "4" : "Fall 2021",
                "5" : "Spring 2022",
                "6" : "Summer 2022",
                "7" : "Add semesters here",
            },
        }
    },
}
</script>

<style scoped>
ul {
    margin: 0; padding: 0;
    list-style-type: none;
}

li {
    background: #ffffff;
    border: 1px solid #aaaaaa;
    border-top: none;
}

button {
    background: transparent;
    width: 100%;
    padding: 15px 0px;
    border: none;
    box-sizing: border-box;
}

    button:hover {
        background: #01426A;
        color: #ffffff;
    }

.dropdown {
    width: 32.4%;
    position: absolute;
    box-sizing: border-box;
}
</style>