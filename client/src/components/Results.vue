<template>
  <div>
    <h1>Results</h1>
    <section class="countries-container">
      <div v-for="country in countries" :key="country.id" class="country-block">
        <Form v-if="editForm === country.id" />
        <div v-else>
          <h4><span>Country:</span> {{ country.country_name }}</h4>
          <h4><span>Capital:</span> {{ country.capital }}</h4>
          <h4><span>Population:</span> {{ country.population }}</h4>
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
  data: () => {
    return {
      countries: [],
      editForm: null,
    };
  },
  mounted: async function () {
    const res = await api.get("/countries");
    this.countries = res.data;
  },
  methods: {
    // handleEdit: async function (countryId){
    //   await api.put('countries')
    // }
    openEditForm: function (countryId) {
      this.editForm = countryId;
    },
  },
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
.country-block button {
  align-self: center;
  margin-bottom: 20px;
  padding: 10px 15px;
  background: rgb(91, 184, 132);
  border: rgb(53, 73, 94) 1px solid;
  border-radius: 5px;
  font-weight: 700;
  cursor: pointer;
  transition: all .25s ease;
}
.country-block button:hover {
  transform: scale(1.05);
  box-shadow: -2px 3px 4px rgb(53, 73, 94);
}
.country-block span {
  font-weight: 900;
}
</style>