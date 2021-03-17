<template>
  <div>
    <form v-on:submit.prevent="handleSubmit()">
      <input
        type="text"
        name="countryName"
        placeholder="Country Name"
        v-model="fields.countryName"
      />
      <input
        type="text"
        name="capital"
        placeholder="Capital"
        v-model="fields.capital"
      />
      <input
        type="number"
        name="population"
        placeholder="Population"
        v-model.number="fields.population"
      />
      <button type="submit">Send It</button>
    </form>
  </div>
</template>


<script>
import axios from "axios";
import { baseURL, config } from "../services/airtableConfig";

export default {
  name: "Form",
  props:{
    reloadIt: Function
  },
  data: () => ({
    fields: {
      countryName: "",
      capital: "",
      population: null,
    },
  }),
  methods: {
    handleSubmit: async function () {
      await axios.post(baseURL, { fields: this.fields }, config);
      this.fields.countryName = "";
      this.fields.capital = "";
      this.fields.population = "";
      this.reloadIt()
    },
  },
};
</script>
