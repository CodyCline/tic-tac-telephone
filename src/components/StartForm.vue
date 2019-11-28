<template>
    <vue-flex-box
        justify-content="center"
        wrap
    >
        <vue-flex-item>
            <div class="gameForm">
                <h1>Welcome to Tic Tac Telephone!</h1>
                <p v-if="this.errors.length">
                    <b>Please correct the following error(s):</b>
                    <ul>
                        <li v-bind:key="error.index" v-for="error in errors">{{ error }}</li>
                    </ul>
                </p>
                <p>
                    <label for="name">Nickname</label>
                    <input
                        id="name"
                        v-model="name"
                        type="text"
                        name="name"
                    />
                </p>
                <p>
                    <label for="phone">Phone Number</label>
                    <input
                        v-model="phone"
                        type="number"
                        name="phone"
                        min="0"
                    />
                </p>

                <button @click="checkForm()">
                    <span v-if="checking">Loading ...</span>
                    <span v-else>Create!</span>
                </button>
                <span>{{isConnected}}</span>
            </div>
        </vue-flex-item>
    </vue-flex-box>
</template>

<script>
import Vue from 'vue'
import { mapMutations, mapState } from 'vuex';

const e164Format = (input) => {
    //Properly format phone num before checking if valid
}
export default {
    name: 'start-form',
    computed: {
        ...mapState(['isConnected'])
    },
    data () {
        return {
            errors: [],
            name: "",
            phone: "",
            checking: false,
        }
    },
    methods:{
        ...mapMutations(['setNickname', 'setPhone']),
        checkForm () {
            this.checking = true;
            //Todo: api call to verify phone number is valid
            if(this.name && this.phone) {
                this.setNickname(this.name);
                this.setPhone(this.phone);
                this.$socket.emit('create');
            }
            this.errors = [];
            if(!this.name) {
                this.errors.push("Name required");
            }
            if(!this.phone) {
                this.errors.push("Phone required")
            }
            
        },
    },
};
</script>

<style scoped>
.gameForm {
    height: 300px; 
    width: 600px;
    background: #5E42B6;
    border-radius: 5px;
}
</style>