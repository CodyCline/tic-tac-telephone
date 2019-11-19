***REMOVED***
	<div>
		<div style="display: flex; flex-direction:row;align-items:center;">
			<avatar/>
			<avatar/>
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
	***REMOVED***
***REMOVED***
***REMOVED***

<script>
import TicTacBoard from '@/components/TicTacBoard';
import TicTacSquare from '@/components/TicTacSquare';
import Avatar from '@/components/Avatar';

export default {
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