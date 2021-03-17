<template>
  <div>
    <form v-on:submit.prevent="handleSubmit()">
      <input
        type="text"
        name="countryName"
        placeholder="Country Name"
        v-model="countryInfo.country_name"
      />
      <input
        type="text"
        name="capital"
        placeholder="Capital"
        v-model="countryInfo.capital"
      />
      <input
        type="number"
        name="population"
        placeholder="Population"
        v-model.number="countryInfo.population"
      />
      <button type="submit">Send It</button>
    </form>
  </div>
</template>


<script>
import { api } from "../services";

export default {
  name: "Form",
  props: {
    reloadIt: Function,
  },
  data: () => ({
    countryInfo: {
      country_name: "",
      capital: "",
      population: null,
    },
  }),
  methods: {
    handleSubmit: async function () {
      console.log(this.countryInfo);
      await api.post('/countries/', this.countryInfo);
      this.countryInfo.country_name = "";
      this.countryInfo.capital = "";
      this.countryInfo.population = null;
      this.reloadIt()
    },
  },
  // methods: {
  //   handleSubmit: async function () {
  //     await axios.post(baseURL, { fields: this.fields }, config);
  //     this.fields.countryName = "";
  //     this.fields.capital = "";
  //     this.fields.population = "";
  //     this.reloadIt()
  //   },
  // },
};
</script>
