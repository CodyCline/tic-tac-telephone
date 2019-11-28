//Todo request game board data and display it or display error
<template>
	<div>
		<div style="display: flex; flex-direction:row;align-items:center;">
		</div>
		<!-- TODO: Display error based on  -->
		<div class="gameBoard">
			<TicTacSquare v-bind:input="item" v-for="(item, index) in gameData" v-bind:key="index"></TicTacSquare>
		</div>
		<p >We're connected to the server! {{isConnected}}</p>
		<button @click="startGame">Start Game</button>
		<p>Room num: "{{room}}"</p>
		<p>Phone {{phoneNum}}</p>
		<footer class="footer">
			<span>Footer</span>
		</footer>
		
	</div>
</template>

<script>
import TicTacBoard from '@/components/TicTacBoard';
import TicTacSquare from '@/components/TicTacSquare';
import { mapMutations } from 'vuex';
import Avatar from '@/components/UI/Avatar';
import { mapState } from 'vuex';
export default {
	computed: {
		...mapState(['phoneNum', 'room', 'gameData', 'isConnected', 'dialButtonText']),
	},
	data() {
		return {
			buttonText: "Start Game",
		}
	},
	mounted () {
		this.getRoom()
	},

	methods: {
		...mapMutations(['setInitialGame', 'startGame']),
		async getRoom() {
			try {
				const req = await fetch(`http://localhost:5000/api/game/${this.$route.params.roomId}`, {
					method: 'GET',
					headers: {
						contentType: 'application/json',
					},
				});
				const data = await req.json();
				this.setInitialGame(JSON.parse(data.gameData))
			} catch (error) {
				//If something happens server-side or the room can't be found redirect home
				return this.$router.push('/')
			}
		},
		startGame(phone) {
			this.$socket.emit('start_call', {"phone": this.phoneNum, "roomid": this.$route.params.roomId})
		}
	},

	components: {
		TicTacBoard,
		TicTacSquare,
	},
  	name: 'game',
};
</script>


<style scoped>
.gameBoard {
	width: 400px;
	height: 400px;
	margin: 0 auto;
	background-color: #664AC0;
	border-radius: 10px;
	display: grid;
	grid-template: repeat(3, 1fr) / repeat(3, 1fr);
}
.footer {
	width: 100%;
	background: #FFD500;
	color: #0f0f0f;

}
</style>