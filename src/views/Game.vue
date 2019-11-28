//Todo request game board data and display it or display error
***REMOVED***
	<div>
		<div style="display: flex; flex-direction:row;align-items:center;">
	***REMOVED***
		<!-- TODO: Display error based on  -->
		<div class="gameBoard">
			<TicTacSquare v-bind:input="item" v-for="(item, index) in gameData" v-bind:key="index"></TicTacSquare>
	***REMOVED***
		<p >We're connected to the server! {{isConnected***REMOVED******REMOVED***</p>
		<button @click="startGame">Start Game</button>
		<p>Room num: "{{room***REMOVED******REMOVED***"</p>
		<p>Phone {{phoneNum***REMOVED******REMOVED***</p>
		<footer class="footer">
			<span>Footer</span>
		</footer>
		
***REMOVED***
***REMOVED***

<script>
import TicTacBoard from '@/components/TicTacBoard';
import TicTacSquare from '@/components/TicTacSquare';
import { mapMutations ***REMOVED*** from 'vuex';
<<<<<<< HEAD
import Avatar from '@/components/UI/Avatar';
=======
>>>>>>> 5f18a1e1974ccacf6533818b933d28533efefe6e
import { mapState ***REMOVED*** from 'vuex';
export default {
	computed: {
		...mapState(['phoneNum', 'room', 'gameData', 'isConnected', 'dialButtonText']),
	***REMOVED***,
	data() {
		return {
			buttonText: "Start Game",
		***REMOVED***
	***REMOVED***,
	mounted () {
		this.getRoom()
	***REMOVED***,

	methods: {
		...mapMutations(['setInitialGame', 'startGame']),
		async getRoom() {
			try {
				const req = await fetch(`http://localhost:5000/api/game/${this.$route.params.roomId***REMOVED***`, {
					method: 'GET',
					headers: {
						contentType: 'application/json',
					***REMOVED***,
				***REMOVED***;
				const data = await req.json();
				this.setInitialGame(JSON.parse(data.gameData))
			***REMOVED*** catch (error) {
				//If something happens server-side or the room can't be found redirect home
				return this.$router.push('/')
			***REMOVED***
		***REMOVED***,
		startGame(phone) {
			this.$socket.emit('start_call', {"phone": this.phoneNum, "roomid": this.$route.params.roomId***REMOVED***
		***REMOVED***
	***REMOVED***,

	components: {
		TicTacBoard,
		TicTacSquare,
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
.footer {
	width: 100%;
	background: #FFD500;
	color: #0f0f0f;

***REMOVED***
***REMOVED***