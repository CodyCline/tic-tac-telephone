***REMOVED***
  <div class="gameBoard">
		<TicTacSquare />
		<TicTacSquare />
		<TicTacSquare />
		<TicTacSquare />
		<TicTacSquare />
		<TicTacSquare />
		<TicTacSquare />
		<TicTacSquare />
		<TicTacSquare />
  </div>
***REMOVED***

<script>
import TicTacBoard from '@/components/TicTacBoard';
import TicTacSquare from '@/components/TicTacSquare';

export default {
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
***REMOVED***