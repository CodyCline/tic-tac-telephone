***REMOVED***
	<div>
		<p v-if="isConnected">We're connected to the server!</p>
		<p>Room num: "{{room***REMOVED******REMOVED***"</p>
		<button @click="pingServer()">Ping Server</button>
		<ul id="example-1">
			<li v-bind:key="i" v-for="i in testData">
				{{i***REMOVED******REMOVED***
			</li>
		</ul>
***REMOVED***
***REMOVED***

<script>
export default {

	data() {
		return {
			isConnected: false,
			testData: [],
			room: '',
			testKey: 1,
		***REMOVED***
	***REMOVED***,


	sockets: {
		connect() {
			// Fired when the socket connects.
			this.isConnected = true;
		***REMOVED***,



		disconnect() {
			this.isConnected = false;
		***REMOVED***,

		// Fired when the server sends something on the "messageChannel" channel.
		game_created(data) {
			console.log("Something happend", data)
			this.room = data.room
		***REMOVED***,

		async update_board(data) {
			const boardData = JSON.parse(data.board);
			this.testData = boardData;
			console.log("UPDATED BOARD", boardData);
		***REMOVED***
	***REMOVED***,

	methods: {
		pingServer() {
			console.log("SENDING");
			this.$socket.emit('create', 'PING!')
		***REMOVED***
	***REMOVED***
***REMOVED***
***REMOVED***