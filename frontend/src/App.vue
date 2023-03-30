<template>
  <BlogHeader/>
  <ArticleList/>
  <BlogFooter/>
</template>

<script>
import ArticleList from "@/components/ArticleList.vue";
import BlogHeader from "@/components/BlogHeader.vue";
import BlogFooter from "@/components/BlogFooter.vue";

export default {
  name: 'App',
  components: {ArticleList, BlogHeader, BlogFooter}
}
</script>

<style>
#app {
  font-family: Georgia, Arial, sans-serif;
  margin-left: 40px;
  margin-right: 40px;
}
</style>
