***REMOVED***
  <div>
    <p v-if="isConnected">We're connected to the server!</p>
    <p>Message from server: "{{socketMessage***REMOVED******REMOVED***"</p>
    <button @click="pingServer()">Ping Server</button>
  </div>
***REMOVED***

<script>
export default {

	data() {
		return {
			isConnected: false,
			socketMessage: ''
		***REMOVED***
	***REMOVED***,

	mounted() {
        this.sockets.subscribe('MESSAGE', (data) => {
			console.log("data")
		***REMOVED***;
***REMOVED***

	sockets: {
		connect() {
			// Fired when the socket connects.
			this.isConnected = true;
		***REMOVED***,



		disconnect() {
			this.isConnected = false;
		***REMOVED***,

		// Fired when the server sends something on the "messageChannel" channel.
		join_room(data) {
			console.log("SOmething happend", data)
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