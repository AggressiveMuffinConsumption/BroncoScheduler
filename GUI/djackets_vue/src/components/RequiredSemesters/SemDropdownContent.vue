<template>
    <div v-if="active">
        <slot />
    </div>
</template>

<script>
export default {
    name: 'SemDropdownContent',
    inject: ['sharedState'],
    computed: {
        active() {
            return this.sharedState.active
        }
    },
}
</script>

<style scoped>

</style>