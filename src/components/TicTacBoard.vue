<template>
	<div class="gameBoard">
	</div>
</template>

<script lang='ts'>
import Vue from 'vue';
import Component from 'vue-class-component';

@Component({
	props: {
		children: Node,
    },
    name: 'tic-tac-board'
})
export default class TicTacBoard extends Vue {
	
}
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
</style>