<template>
  <v-data-table
    class="track-listing elevation-1"
    :headers="headers"
    :items="tracks"
    hide-actions
  >
    <template slot="items" slot-scope="props">
      <td>#{{props.index + 1}}</td>
      <td>{{ props.item.track_title }}</td>
      <td>{{ props.item.track_artist }}</td>
      <td>{{ props.item.isrc }}</td>
      <td class="justify-center layout px-0">
        <v-btn icon class="mx-0" @click="$emit('deleteTrack', props.item)">
          <v-icon color="pink">delete</v-icon>
        </v-btn>
      </td>
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
        { text: '#', value: 'track_number' },
        { text: 'Title', value: 'title' },
        { text: 'Artist', value: 'artist' },
        { text: 'ISRC', value: 'isrc' },
        { text: '', value: 'actions' }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
