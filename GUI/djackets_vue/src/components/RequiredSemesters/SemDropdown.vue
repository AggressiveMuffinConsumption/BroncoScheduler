<template>
  <div class="dropdown" @click="toggle">
    <slot name="toggler">
      <button>
          {{ semester }}
        <div class="arrow">
            v
        </div>
      </button>
    </slot>
    <slot />
    <SemDropdownContent />
    <SemDropdownTable />
  </div>
</template>

<script>
import SemDropdownContent from "./SemDropdownContent.vue";
import SemDropdownTable from "./SemDropdownTable.vue";

export default {
  name: "SemesterDropdown",
  components: {
    SemDropdownContent,
    SemDropdownTable,
  },
  props: {
    
  },
  provide() {
    return {
      sharedState: this.sharedState,
    };
  },
  methods: {
  },
  data() {
    return {
      sharedState: {
        active: false,
      },
      semester: SemDropdownContent.methods.getSemester(),
    };
  },
  methods: {
    toggle() {
      this.sharedState.active = !this.sharedState.active;
    },
    // semester() {
    //   return getSemester()
    // }
  },
};
</script>

<style scoped>

button {
  background: #ffffff;
  width: 100%;
  padding: 10px 0px;
  border: 1px solid #aaaaaa;
  border-radius: 0;
  font-size: 13pt;
  font-weight: 400;
}

h2 {
  margin: 0;
}

h2:first-letter {
  text-decoration: underline;
}

.arrow {
    background: #01426A;
    width: 20px; height: 20px;
    margin-right: 20px;
    float: right;
    font-family: Outfit, Helvetica, Arial, sans-serif;
    font-size: 13pt;
    color: #ffffff;
    border-radius: 100%;
    box-sizing: border-box;
    text-align: center;
}

    .arrow:hover {
        opacity: 0.5;
    }
</style>
