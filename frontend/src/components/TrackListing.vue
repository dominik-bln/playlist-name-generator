<template>
  <v-data-table
    class="track-listing elevation-1"
    :headers="headers"
    :items="tracks"
    hide-actions
  >
    <template slot="items" slot-scope="props">
      <td>{{ props.item.track_title }}</td>
      <td>{{ props.item.track_artist }}</td>
      <td>{{ props.item.isrc }}</td>
    </template>
  </v-data-table>
</template>

<script>
export default {
  name: 'TrackListing',
  props: {
    tracks: {
      type: Array,
      default: () => []
    }
  },
  data () {
    return {
      headers: [
        { text: 'Title', value: 'title' },
        { text: 'Artist', value: 'artist' },
        { text: 'ISRC', value: 'isrc' }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
