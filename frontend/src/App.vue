<template>

  <div id="header">
    <div><img alt="Vue logo" src="./assets/logo.png" style="width: 100px;height: 100px;"></div>
    <div>My Blogs</div>
    </div>
  <hr>
  <div v-for="article in info.results" v-bind:key="article.url" id="articles">
    <div class="article-title">
      {{ article.title }}
    </div>
    <div>{{ formatted_time(article.created) }}</div>
  </div>

</template>

<script>
import axios from "axios";

export default {
  name: 'App',
  data: function () {
    return {
      info: ''
    }
  },
  mounted() {
    axios
        .get('/api/article')
        .then(response => (this.info = response.data))
  },
  methods:{
    formatted_time:function (iso_date_string){
      const date = new Date(iso_date_string)
      return date.toLocaleDateString()
    }
  }
}
</script>

<style>
#app {
  font-family: Georgia, Arial, sans-serif;
  margin-left: 40px;
  margin-right: 40px;
}

#header {
  text-align: center;
  font-size: xx-large;

}

#articles {
  padding: 10px;
  text-align: center;
}

.article-title {
  font-size: large;
  font-weight: bolder;
  color: black;
  text-decoration: none;
  padding: 5px 0 5px 0;
}

</style>
