<template>
  <div class="article">
    <img alt="Vue logo" src="../assets/logo.png">
    <Article1/>
  </div>
</template>

<script>
// @ is an alias to /src
import Article1 from '@/components/Article_comp.vue';

export default {
  name: 'Article',
  components: {
    Article1,
  },
};
</script>
