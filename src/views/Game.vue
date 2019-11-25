//Todo request game board data and display it or display error
***REMOVED***
	<div>
		<div style="display: flex; flex-direction:row;align-items:center;">
			<avatar/>
			<avatar/>
	***REMOVED***
		<!-- TODO: Display error based on  -->
		<div class="gameBoard">
			<TicTacSquare v-bind:input="item" v-for="(item, index) in testData" v-bind:key="index"></TicTacSquare>
	***REMOVED***
		<p v-if="isConnected">We're connected to the server!</p>
		<p>Room num: "{{room***REMOVED******REMOVED***"</p>
***REMOVED***
***REMOVED***

<script>
import TicTacBoard from '@/components/TicTacBoard';
import TicTacSquare from '@/components/TicTacSquare';
import Avatar from '@/components/Avatar';
export default {
	data() {
		return {
			isConnected: false,
			testData: [],
			room: "",
		***REMOVED***
	***REMOVED***,
	mounted () {
		this.getRoom()
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
		async getRoom() {
			try {
				const req = await fetch(`http://localhost:5000/game/${this.$route.params.roomId***REMOVED***`, {
					method: 'GET',
					headers: {
						contentType: 'application/json',
					***REMOVED***,
				***REMOVED***;
				const data = await req.json();
				this.testData = JSON.parse(data.gameData);
			***REMOVED*** catch (error) {
				console.log('UH OH', error);
			***REMOVED***
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