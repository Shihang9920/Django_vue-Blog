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
    name: "HomePage",
    components: {
        ArticleList,
        BlogHeader,
        BlogFooter
    }
}
</script>

<style scoped>

</style>