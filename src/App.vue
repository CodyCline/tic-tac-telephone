<template>
	<div id="app">
		<router-view></router-view>
	</div>
</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';
export default class App extends Vue {}
</script>

<style>
body {
  background: #412EA2;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
  margin-top: 60px;
}
</style>
