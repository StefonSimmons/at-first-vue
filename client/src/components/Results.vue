<template>
  <div>
    <h1>Results</h1>
    <section class="countries-container">
      <div v-for="country in countries" :key="country.id" class="country-block">
        <Form
          v-if="editForm === country.id"
          :country="country"
          :reloadIt="reloadIt"
          :exitEditForm="exitEditForm"
        />
        <div v-else class="country-info">
          <span class="delete-icon" v-on:click="deleteCountry(country.id)">X</span>
          <h4><span>Country:</span> {{ country.country_name }}</h4>
          <h4><span>City:</span> {{ country.capital }}</h4>
          <h4><span>People Met:</span> {{ country.population }}</h4>
          <button v-on:click="openEditForm(country.id)">Edit</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { api } from "../services";
import Form from "../components/Form";

export default {
  name: "Results",
  components: {
    Form,
  },
  props: {
    reloadIt: Function,
    openEditForm: Function,
    editForm: Number,
    exitEditForm: Function,
  },
  data: () => {
    return {
      countries: [],
    };
  },
  mounted: async function () {
    const res = await api.get("/countries");
    this.countries = res.data;
  },
  methods:{
    deleteCountry: async function (countryId){
      await api.delete(`/countries/${countryId}/`)
      this.reloadIt()
    }
  }
};
</script>

<style>
.countries-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
.country-block {
  border: black solid 1px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 0 30px;
}
.country-block form {
  display: flex;
  flex-direction: column;
}
.country-block .button-group {
  display: flex;
  justify-content: space-between;
  width: 250px;
}
.country-block button {
  align-self: center;
  width: 100px;
  margin-bottom: 20px;
  padding: 10px 15px;
  background: rgb(91, 184, 132);
  border: rgb(53, 73, 94) 1px solid;
  border-radius: 5px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.25s ease;
}
.country-block button:hover {
  transform: scale(1.05);
  box-shadow: -2px 3px 4px rgb(53, 73, 94);
}
.country-block span {
  font-weight: 900;
}
.button-group .esc-button {
  background: rgb(143, 37, 37);
}
.country-info{
  position: relative;
  width: 100%
}
.delete-icon{
  color: rgb(143, 37, 37);
  position: absolute;
  right: 0px;
  top: 15px;
  cursor: pointer;
  padding: 5px 10px;
  border-radius: 360%;
  transition: all .25s ease-in-out;
}
.delete-icon:hover{
  transform: scale(1.15);
  background: rgba(91, 184, 132, .2);
  box-shadow: 0 0 2px 2px rgba(91, 184, 132,.2);

}
</style>