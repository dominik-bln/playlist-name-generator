<template>
  <v-app id="app">
    <h1 class="main-title display-2">Playlist Name Generator</h1>

    <track-search
      :value="tracks"
      :isLoading="isLoading"
      :optionValues="searchResults"
      @update:searchInput="searchTracks($event)"
      @input="addToPlaylist($event)"/>

    <track-listing
      :tracks="tracks">
    </track-listing>

    <div class="submit text-xs-center">
      <v-btn
        round
        color="primary"
        dark
        large
        @click="requestPlaylistName()">
        Create Playlist Name
      </v-btn>
    </div>

    <v-snackbar
      :timeout="5000"
      top
      vertical
      color="error"
      v-model="showTrackSelectionError"
    >
      Please select some tracks first.
      <v-btn flat @click.native="showTrackSelectionError=false">Close</v-btn>
    </v-snackbar>

    <v-snackbar
      :timeout="5000"
      top
      vertical
      color="error"
      v-model="showTrackSearchError"
    >
      Failed to search for track
      <v-btn flat @click.native="showTrackSearchError=false">Close</v-btn>
    </v-snackbar>

    <v-snackbar
      :timeout="5000"
      top
      vertical
      color="error"
      v-model="showPlaylistNameSearchError"
    >
      Sorry, generating a name for your playlist failed.
      <v-btn flat @click.native="showPlaylistNameSearchError=false">Close</v-btn>
    </v-snackbar>
  </v-app>
</template>

<script>
import TrackSearch from './components/TrackSearch'
import TrackListing from './components/TrackListing'

const API_URL = 'http://localhost:5000'
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
      isLoading: false,
      showTrackSelectionError: false,
      showTrackSearchError: false,
      showPlaylistNameSearchError: false
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
          this.showTrackSearchError = true
        })
    },
    addToPlaylist (track) {
      this.tracks.push(track)
    },
    requestPlaylistName () {
      if (!this.tracks.length) {
        this.showTrackSelectionError = true
        return
      }

      this.isLoading = true
      this.$http.post(API_URL + '/get_title', {
        tracks: this.tracks
      })
        .then((response) => {
          this.isLoading = false
          console.log(response.data)
        })
        .catch((response) => {
          this.isLoading = false
          this.showPlaylistNameSearchError = true
        })
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
