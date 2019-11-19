***REMOVED***
	<div>
		<input type="text" v-model="message"/>
		<button @click="emitEvent">emit</button>
		<div>{{response***REMOVED******REMOVED***</div>
***REMOVED***
***REMOVED***

<script>
***REMOVED***
***REMOVED***
		response:String,
***REMOVED***
    name: 'debug-sockets'
***REMOVED***
export default class DebugSockets extends Vue {
	data () {
		return {
			message: '',
			response: 'Server has not yet replied.'
		***REMOVED***;
	***REMOVED***;
	emitEvent () {
		this.$socket.emit('hello_world', this.message)
	***REMOVED***;
	created () {
		this.$options.sockets.hello_world = (data) => {
			this.response = data;
		***REMOVED***;
	***REMOVED***;
***REMOVED***
***REMOVED***