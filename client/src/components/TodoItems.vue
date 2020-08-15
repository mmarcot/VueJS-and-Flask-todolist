<template>
    <div>
        <ul>
            <li v-for="item in todoitems" v-bind:key="item.id">{{ item.content }} <span class="badge badge-warning ml-3">{{ item.vote }}</span></li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "TodoItems",
    data() {
        return {
            todoitems: []
        }
    },
    methods: {
        getItems() {
            const path = "http://localhost:5000/items";
            axios.get(path)
                .then((res) => {
                    this.todoitems = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        }
    },
    created() {
        this.getItems();
    },
    mounted() {
        this.$root.$on('refresh', () => {
            this.getItems();
        });
    }
}
</script>

<style lang="scss" scoped>
    ul {
        margin: 0;
        padding: 0;
    }
    ul li {
        list-style-type: none;
    }
</style>