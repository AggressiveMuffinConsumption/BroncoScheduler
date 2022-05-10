<template>
  <div>
    <LogIn msg="Welcome to Bronco Scheduler"/>
  </div>
</template>

<script>
// @ is an alias to /src
import LogIn from '@/components/LogIn.vue'
export default {
  name: 'LogInView',
  components: {
    LogIn
  }
}
</script>