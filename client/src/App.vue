<template>
  <div id="app" class="text-center">
    <div class="jumbotron">
      <img src="./assets/todo.png" alt="todo" id="logo">
    </div>
    <TodoInput></TodoInput>
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
#logo {
  width: 35%;
}

.jumbotron {
  background-color: #f5f5f5 !important;
}
</style>
