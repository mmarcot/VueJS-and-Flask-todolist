<template>
    <div>
        <input type="text" id="todoinput" v-on:keyup.enter="addItem" class="form-control col-sm-6 col-md-5 col-lg-4 col-xl-3 mx-auto">
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "TodoInput",
    methods: {
        addItem() {
            let input_value = document.getElementById('todoinput').value;
            document.getElementById('todoinput').value = '';
            const path = "http://localhost:5000/additem";
            axios.post(path, {'content': input_value})
                .then(() => {
                    // console.log('POST done');
                })
                .catch((error) => {
                    console.error(error);
                })
        }
    }
}
</script>