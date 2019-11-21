***REMOVED***
	<div>
		<div style="display: flex; flex-direction:row;align-items:center;">
			<avatar/>
			<avatar/>
	***REMOVED***
		<div class="gameBoard">
			<TicTacSquare v-bind:input="item" v-for="item in testData" v-bind:key="item"></TicTacSquare>
	***REMOVED***
		<p v-if="isConnected">We're connected to the server!</p>
		<p>Room num: "{{room***REMOVED******REMOVED***"</p>
		<button @click="pingServer()">Ping Server</button>
***REMOVED***
***REMOVED***

<script>
import TicTacBoard from '@/components/TicTacBoard';
import TicTacSquare from '@/components/TicTacSquare';
import Avatar from '@/components/Avatar';
const arr = " " * 9

export default {
	data() {
		return {
			isConnected: false,
			testData: [" "," "," "," "," "," "," "," "," ",],
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

		update_board(data) {
			const boardData = JSON.parse(data.board);
			this.testData = boardData;
			console.log("UPDATED BOARD", boardData);
		***REMOVED***,
	***REMOVED***,

	methods: {
		pingServer() {
			console.log("SENDING");
			this.$socket.emit('create', 'room')
		***REMOVED***
	***REMOVED***,

	components: {
		TicTacBoard,
		TicTacSquare,
		Avatar,
	***REMOVED***,
  	name: 'game',
***REMOVED***;
***REMOVED***


***REMOVED***
.gameBoard {
	width: 400px;
	height: 400px;
	margin: 0 auto;
	background-color: #664AC0;
	border-radius: 10px;
	display: grid;
	grid-template: repeat(3, 1fr) / repeat(3, 1fr);
***REMOVED***
***REMOVED***