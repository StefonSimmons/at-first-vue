<template>
  <div>
    <h1>Results</h1>
    <section class="countries-container">
      <div
        v-for="country in countries"
        :key="country.fields.id"
        class="country-block"
      >
        <h4><span>Country:</span> {{ country.fields.countryName }}</h4>
        <h4><span>Capital:</span> {{ country.fields.capital }}</h4>
        <h4><span>Population:</span> {{ country.fields.population }}</h4>
        <button>Edit</button>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import { baseURL, config } from "../services/airtableConfig";

export default {
  name: "Results",
  data: () => {
    return {
      countries: [],
    };
  },
  mounted: async function () {
    const response = await axios.get(baseURL, config);
    this.countries = response.data.records;
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
  align-items: flex-start;
  padding: 0 30px;
}
.country-block button {
  align-self: center;
  margin-bottom: 20px;
  padding: 10px 15px;
  background: rgb(91, 184, 132);
  border: rgb(53, 73, 94);
  border-radius: 5px;
  font-weight: 700;
  cursor: pointer;
}
.country-block button:hover {
  transform: scale(1.05);
}
.country-block span {
  font-weight: 900;
}
</style>