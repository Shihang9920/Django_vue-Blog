<template>
    <div v-for="article in info.results" v-bind:key="article.url" id="articles">
        <div>
      <span v-for="tag in article.tag" v-bind:key="tag" class="tag">
        {{ tag }}
      </span>
        </div>
        <!--        <div class="article-title">-->
        <!--            {{ article.title }}-->
        <!--        </div>-->
        <router-link :to="{name:'ArticleDetail',params:{id:article.id}}" class="article-title">
        {{ article.title}}
        </router-link>
        <div>{{ formatted_time(article.created) }}</div>
    </div>
</template>

<script>
import axios from "axios";
import ArticleDetail from "@/components/ArticleDetail.vue";

export default {
    name: 'ArticleList',
    computed: {
        ArticleDetail() {
            return ArticleDetail
        }
    },
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
    methods: {
        formatted_time: function (iso_date_string) {
            const date = new Date(iso_date_string)
            return date.toLocaleDateString()
        }
    }
}
</script>

<style scoped>
#articles {
    padding: 10px;
    text-align: center;
    /*border: 1px solid #ddd;*/
    margin: 10px auto;
    width: 400px;
    /*box-shadow: 5px 5px 10px #aaaaaa;*/
    /*border-radius: 10px;*/
}

.article-title {
    font-size: large;
    font-weight: bolder;
    color: black;
    text-decoration: none;
    padding: 5px 0 5px 0;
}

.tag {
    padding: 2px 5px 2px 5px;
    margin: 5px 5px 5px 0;
    font-family: Georgia, Arial, sans-serif;
    font-size: small;
    background-color: green;
    color: whitesmoke;
    border-radius: 5px;
}
</style>