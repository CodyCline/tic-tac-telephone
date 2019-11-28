import Vue from 'vue';
import Vuex from 'vuex';
import router from '../router';

Vue.use(Vuex);
export default new Vuex.Store({
	state: {
		isConnected: false,
		errors: false,
		authenticated: false, //2FA Auth
		room: "",
		nickname: "",
		phoneNum: "",
		callStatus: "", //Possible values: call, dialing, connected, retry, failed,
		gameData: [],
		winner: null,
	},
	mutations: {
		SOCKET_CONNECT: (state,  status) => {
            state.isConnected = true;
        },
		SOCKET_DISCONNECT(state) {
			state.isConnected = false;
		},
		SOCKET_ERRORS(state) {
			state.errors = true
		},
		SOCKET_INITIATE_CALL(state, status) {
			state.callStatus = status;
		},
		SOCKET_GAME_CREATED(state, data) {
			state.room = data.room;
            router.push({name : 'game', params: { roomId: data.room }});
		},
		SOCKET_UPDATE_BOARD(state, gameData) {
			const formatted = JSON.parse(gameData.board)
			state.gameData = formatted;
		},
		setPhone (state, phone) {
			state.phoneNum = phone;
		},
		setNickname(state, username) {
			state.nickname = username;
		},
		setInitialGame(state, arr) {
			state.gameData = arr;
		},
		setWinner (state, victor) {
			state.winner = victor;
		}

	},
});