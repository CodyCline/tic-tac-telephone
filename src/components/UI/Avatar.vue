<template>
	<div class="avatarCard">
        <img src="https://clinicforspecialchildren.org/wp-content/uploads/2016/08/avatar-placeholder.gif" class="avatar"/>
        <span>Nickname</span>
        <span>X</span>
	</div>
</template>

<script lang='ts'>
import Vue from 'vue'
import Component from 'vue-class-component'

@Component({
	props: {
		children: Node,
    },
    name: 'tic-tac-board'
})
export default class Avatar extends Vue {
}
</script>

<style scoped>
	.avatarCard {
        width: 120px;
	    height: 200px;
        border: 3px solid #fff;
        border-radius: 10px;
	    margin: 0 auto;
        background-color: #332167;        
        display: flex;
        flex-direction: column;
        align-items:center;
        justify-content: space-evenly;
    }
    .avatar {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background-image: url('https://clinicforspecialchildren.org/wp-content/uploads/2016/08/avatar-placeholder.gif');
    }
</style>