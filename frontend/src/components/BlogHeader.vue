<template>
  <div class="header">
    <img alt="Vue logo" src="../assets/logo.png" id="logo">
    <p>A Simple Blog</p>
  </div>

  <hr>
</template>

<script>
export default {
  name: "BlogHeader"
}
</script>

<style scoped>
.header {
  text-align: center;
  font-family: "Ink Free",serif;
  margin: 20px auto;
  font-size: 40px;
  font-weight: bolder;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 60px;

}
#logo{
  width: 60px;
  height: 60px;
  margin-right: 20px;
}
</style>