<template>
  <v-app id="app">
    <h1 class="main-title display-2">Playlist Name Generator</h1>

    <track-search
      :value="[]"
      :isLoading="isLoading"
      :optionValues="searchResults"
      @update:searchInput="searchTracks($event)"
      @input="addToPlaylist($event)"/>

    <track-listing
      :tracks="tracks">
    </track-listing>

    <div class="submit text-xs-center">
      <v-btn round color="primary" dark large>
        Create Playlist Name
      </v-btn>
    </div>
  </v-app>
</template>

<script>
import TrackSearch from './components/TrackSearch'
import TrackListing from './components/TrackListing'

// const API_URL = 'http://localhost:5000'
const ELASTICSEARCH_URL = 'http://localhost:9200'

export default {
  name: 'App',
  components: {
    TrackSearch, TrackListing
  },
  data () {
    return {
      tracks: [],
      searchResults: [],
      isLoading: false
    }
  },
  methods: {
    searchTracks (queryString) {
      console.debug('[Sending Query:]' + queryString)
      this.isLoading = true
      this.$http.get(ELASTICSEARCH_URL + '/isrcs/_search?size=40&q=' + queryString)
        .then((response) => {
          if (response.data.hits.hits.length) {
            this.searchResults = response.data.hits.hits.map((item) => {
              return item._source
            })
          } else {
            this.searchResults = []
          }
          this.isLoading = false
        })
        .catch((response) => {
          this.isLoading = false
          alert('Failed to search for track')
        })
    },
    addToPlaylist (track) {
      this.tracks.push(track)
    }
  }
}
</script>

<style lang="stylus">
html
  box-sizing: border-box
  background-color: $body-background-color

*, *:before, *:after
  box-sizing: inherit

*:focus, *:active
  outline: none

body
  margin: 0
  // ensure we can add global mousevent listeners to
  // the body that will fire on all parts of the page
  min-height: 100vh

#app
  font-family: 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  padding: 8rem 5rem 2rem

.track-search,
.track-listing
.submit
  margin-top: 4rem

.main-title
  text-align: center
</style>
