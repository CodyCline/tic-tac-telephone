<template>
	<div class="gameSquare">
		<span class="gameLetter gameX" v-if="input == 'X'">X</span>
		<span class="gameLetter gameO" v-else-if="input == 'O'">O</span>
	</div>
</template>

<script lang='ts'>
import Vue from 'vue'
import Component from 'vue-class-component'

@Component({
	props: {
		input: String,
	}
})
export default class TicTacSquare extends Vue {
	
}
</script>

<style scoped>
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
	}
	.gameLetter {
		font-size: 6rem;
	}
	.gameO {
		color: #FFD032;
	}
	.gameX {
		color:#EB1751;
	}
</style>