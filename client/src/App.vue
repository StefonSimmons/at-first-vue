<template>
  <div id="app" :key="reload">
    <div class="logo-container">
      <img alt="Vue logo" src="./assets/logo.png" />
      <h4>iews</h4>
    </div>
    <HelloWorld msg="💚" />
    <Working />
    <Form :reloadIt="reloadIt" postForm="post-form" />
    <Results
      :reloadIt="reloadIt"
      :openEditForm="openEditForm"
      :editForm="editForm"
      :exitEditForm="exitEditForm"
    />
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import Working from "./components/Instructions.vue";
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
    editForm: null,
  }),
  methods: {
    reloadIt: function () {
      this.reload = !this.reload;
    },
    openEditForm: function (countryId) {
      this.editForm = countryId;
    },
    exitEditForm: function () {
      this.editForm = null;
    },
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Pattaya&display=swap');
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.logo-container{
  display: flex;
  justify-content: center;
  align-items: flex-end;
}
.logo-container > h4{
  position: relative;
  left: -50px;
  font-weight: 700;
  font-size: 28px;
  margin: 5px;
  letter-spacing: 3px;
  font-family: 'Pattaya', sans-serif;
}
</style>
