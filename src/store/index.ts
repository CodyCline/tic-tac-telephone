***REMOVED***;
import Vuex from 'vuex';

Vue.use(Vuex);
export default new Vuex.Store({
	state: {
		isConnected: false,
		errors: false,
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
		***REMOVED***,
		SOCKET_UPDATE_BOARD(state, data) {
			state.gameData = data;
		***REMOVED***,
		setPhone (state, phone) {
			state.phoneNum = phone;
		***REMOVED***,
		setNickname(state, username) {
			state.nickname = username;
		***REMOVED***,
		setWinner (state, victor) {
			state.winner = victor;
		***REMOVED***

	***REMOVED***,
***REMOVED***;