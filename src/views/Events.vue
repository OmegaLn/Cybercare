<template>
  <div class="events">
    <img alt="Vue logo" src="../assets/logo.png">
    <Events1/>
  </div>
</template>

<script>
// @ is an alias to /src
import Events1 from '@/components/Events_comp.vue';

export default {
  name: 'Events',
  components: {
    Events1,
  },
};
</script>
