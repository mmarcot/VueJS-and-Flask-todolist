<template>
    <div id="todoitems" class="p-5">
        <ul>
            <li v-for="item in todoitems" v-bind:key="item.id">
                {{ item.content }} <!-- <span class="badge badge-warning mx-3">{{ item.vote }}</span> -->
                <!-- <button v-on:click='deleteItem(item.id)'>X</button> -->
                <button v-on:click='deleteItem(item.id)' type="button" class="close">&times;</button>
            </li>
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
        },
        deleteItem(item_id) {
            console.log(item_id);
            const path = "http://localhost:5000/deleteitem"
            axios.post(path, {'id': item_id})
                .then(() => {
                    this.getItems();
                })
                .catch((error) => {
                    console.error(error);
                })
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
    #todoitems {
        background-color: #f5f5f5;
        border-radius: 0.3rem;
        margin-top: 30px;
    }
    .close {
        float: none;
    }
</style>