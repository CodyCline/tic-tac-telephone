***REMOVED***;
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
	***REMOVED***,
	mutations: {
		SOCKET_CONNECT(state) {
			state.isConnected = true;
		***REMOVED***,
		SOCKET_DISCONNECT(state) {
			state.isConnected = false;
		***REMOVED***,
		SOCKET_ERRORS(state) {
			state.errors = true
		***REMOVED***,
		SOCKET_INITIATE_CALL(state, status) {
			state.callStatus = status;
		***REMOVED***,
		SOCKET_GAME_CREATED(state, data) {
			state.room = data.room;
            router.push({name : 'game', params: { roomId: data.room ***REMOVED******REMOVED***;
		***REMOVED***,
		SOCKET_UPDATE_BOARD(state, gameData) {
			const formatted = JSON.parse(gameData.board)
			state.gameData = formatted;
		***REMOVED***,
		setPhone (state, phone) {
			state.phoneNum = phone;
		***REMOVED***,
		setNickname(state, username) {
			state.nickname = username;
		***REMOVED***,
		setInitialGame(state, arr) {
			state.gameData = arr;
		***REMOVED***,
		setWinner (state, victor) {
			state.winner = victor;
		***REMOVED***

	***REMOVED***,
***REMOVED***;