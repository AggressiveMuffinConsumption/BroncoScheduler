<template>
  <div class="dropdown" @click="toggle">
    <slot name="toggler">
      <button>
        <h2>
          Semester
        </h2>
        <div class="arrow">
            v
        </div>
      </button>
    </slot>
    <slot />
  </div>
</template>

<script>
export default {
  name: "SemesterDropdown",
  provide() {
    return {
      sharedState: this.sharedState,
    };
  },
  data() {
    return {
      sharedState: {
        active: false,
      },
    };
  },
  methods: {
    toggle() {
      this.sharedState.active = !this.sharedState.active;
    },
  },
};
</script>

<style scoped>
.dropdown {
  margin-top: 20px;
}

button {
  background: #ffffff;
  width: 100%;
  padding: 10px 0px;
  border: 1px solid #aaaaaa;
  border-radius: 0;
  color: #2c3e50;
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
    width: 30px; height: 30px;
    margin-right: 20px;
    margin-top: -30px;
    float: right;
    font-family: Outfit, Helvetica, Arial, sans-serif;
    font-weight: 600;
    font-size: 15pt;
    color: #ffffff;
    border-radius: 100%;
    box-sizing: border-box;
}

    .arrow:hover {
        opacity: 0.5;
    }
</style>
