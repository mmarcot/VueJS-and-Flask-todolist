<template>
    <div>
        <input type="text" id="todoinput" v-on:keyup.enter="addItem" class="form-control col-sm-6 col-md-5 col-lg-4 col-xl-3 mx-auto">
    </div>
</template>

<script>
export default {
    name: "TodoInput",
    methods: {
        addItem() {
            let input_value = document.getElementById('todoinput').value;
            document.getElementById('todoinput').value = '';
            console.log(input_value);
        }
    }
}
</script>