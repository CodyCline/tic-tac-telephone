***REMOVED***
    <div class="gameForm">
        <h1>Welcome to Tic Tac Telephone!</h1>
        <!-- <form @submit="checkForm()"> -->
            <p v-if="this.errors.length">
                <b>Please correct the following error(s):</b>
                <ul>
                    <li v-bind:key="error.index" v-for="error in errors">{{ error ***REMOVED******REMOVED***</li>
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
        <!-- </form> -->
    </div>
***REMOVED***

<script>
***REMOVED***

const e164Format = (input) => {
    //Properly format phone num before checking if valid
***REMOVED***
export default {
    name: 'start-form',
    data () {
        return {
            errors: [],
            name: "",
            phone: "",
            checking: false,
        ***REMOVED***
***REMOVED***
    sockets: {
		connect() {
		***REMOVED***,

		// Fired when the server sends something on the "messageChannel" channel.
		game_created(data) {
			console.log("Something happend", data)
            this.room = data.room; // This needs to go into vuex
            this.$router.push({name : 'game', params: { roomId: data.room ***REMOVED******REMOVED***;
		***REMOVED***,
	***REMOVED***,
    methods:{
        checkForm () {
            this.checking = true;
            //Todo: api call to verify phone number is valid
            if(this.name && this.phone) {
                this.$socket.emit('create');
            ***REMOVED***
            this.errors = [];
            if(!this.name) {
                this.errors.push("Name required");
            ***REMOVED***
            if(!this.phone) {
                this.errors.push("Phone required")
            ***REMOVED***
            
    ***REMOVED***
***REMOVED***
***REMOVED***;
***REMOVED***

***REMOVED***
.gameForm {
    height: 300px; 
    width: 400px;
    background: #5E42B6;
    border-radius: 5px;
***REMOVED***
***REMOVED***