<template>
  <div id="app" :key="reload">
    <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="💚 at First Vue" />
    <Working />
    <Form :reloadIt="reloadIt" postForm="post-form"/>
    <Results/>
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import Working from "./components/Work.vue";
import Form from "./components/Form.vue";
import Results from "./components/Results.vue";

export default {
  name: "App",
  components: {
    HelloWorld,
    Working,
    Form,
    Results,
  },
  data: () => ({
    reload: false,
  }),
  methods: {
    reloadIt: function () {
      this.reload = !this.reload;
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
