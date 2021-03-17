<template>
  <form v-on:submit.prevent="handleSend()" :class="postForm">
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
    <div class="button-group">
      <button v-if="country" class="esc-button" v-on:click="exitEditForm()">Esc</button>
      <button type="submit">Send</button>
    </div>
  </form>
</template>


<script>
import { api } from "../services";

export default {
  name: "Form",
  props: {
    reloadIt: Function,
    postForm: String,
    country: Object,
    exitEditForm: Function
  },
  data: () => ({
    countryInfo: {
      country_name: "",
      capital: "",
      population: null,
    },
  }),
  mounted: function () {
    if (this.country) {
      const { country_name, capital, population } = this.country;
      this.countryInfo = {
        country_name,
        capital,
        population,
      };
    }
  },
  methods: {
    handleSend: function () {
      if (this.country) {
        this.handleEdit(this.country.id);
      } else {
        this.handleSubmit();
      }
    },
    handleSubmit: async function () {
      await api.post("/countries/", this.countryInfo);
      this.countryInfo.country_name = "";
      this.countryInfo.capital = "";
      this.countryInfo.population = null;
      this.reloadIt();
    },
    handleEdit: async function (countryId) {
      await api.put(`/countries/${countryId}/`, this.countryInfo);
      this.reloadIt();
    },
  },
};
</script>

<style>
form {
  display: flex;
  justify-content: center;
}
input {
  padding: 10px 5px;
  margin: 5px;
  border-radius: 5px;
  box-shadow: -2px 3px 4px rgb(53, 73, 94);
}
input::placeholder {
  font-weight: 700;
}
input:hover {
  background: rgba(53, 73, 94, 0.068);
}
.post-form button {
  height: 20px;
  padding: 20px 5px;
  align-self: center;
  border-radius: 360%;
  display: flex;
  align-items: center;
  font-weight: 700;
  background: rgb(53, 73, 94);
  color: rgb(108, 184, 141);
  cursor: pointer;
  transition: all 0.25s ease;
}
.post-form button:hover {
  box-shadow: -2px 3px 4px rgb(53, 73, 94);
  transform: scale(1.05);
}

</style>