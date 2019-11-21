***REMOVED***
	<div class="gameSquare">
		<span class="gameLetter gameX" v-if="input == 'X'">X</span>
		<span class="gameLetter gameO" v-else-if="input == 'O'">O</span>
***REMOVED***
***REMOVED***

***REMOVED***
***REMOVED***
***REMOVED***

***REMOVED***
***REMOVED***
		input: String,
	***REMOVED***
***REMOVED***
export default class TicTacSquare extends Vue {
	
***REMOVED***
***REMOVED***

***REMOVED***
	.gameSquare {
		background: #332167;
		border-radius: 15px;
		border: 6px solid #664AC0;		
		display: flex;
  		justify-content: center;
  		flex-direction: column;
	  	text-align: center;
		font-family: Helvetica;
  		font-weight: bold;
	***REMOVED***
	.gameLetter {
		font-size: 6rem;
	***REMOVED***
	.gameO {
		color: #FFD032;
	***REMOVED***
	.gameX {
		color:#EB1751;
	***REMOVED***
***REMOVED***