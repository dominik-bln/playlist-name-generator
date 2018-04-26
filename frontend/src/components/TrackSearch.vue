<template>
  <div class="track-search">
    <v-select
      label="Find tracks for playlist"
      cache-items
      persistent-hint
      autocomplete
      type="search"
      :items="tracks"
      item-text="title"
      :loading="loading"
      hint="Search by artist or track title"
      :value="value">
    </v-select>
  </div>
</template>

<script>
export default {
  name: 'TrackSearch',
  props: {
    value: {
      type: String,
      default: ''
    },
    loading: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      tracks: [
        {
          isrc: '12345',
          title: 'Some Title',
          artist: 'The Artist'
        },
        {
          isrc: '34567',
          title: 'Another Title',
          artist: 'Another Artist'
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
