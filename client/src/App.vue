<template>
  <div id="app" class="text-center">
    <h1 class="jumbotron">TODO list</h1>
    <TodoInput></TodoInput>
    <hr>
    <TodoItems></TodoItems>
  </div>
</template>

<script>
import TodoInput from './components/TodoInput.vue'
import TodoItems from './components/TodoItems.vue'

export default {
  name: 'App',
  components: {
    TodoInput,
    TodoItems
  }
}
</script>

<style lang="scss">
#app {

}
</style>
