<template>
  <v-app id="app">
    <track-search
      :value="queryString"
      @input="searchTrack($event)"/>

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

export default {
  name: 'App',
  components: {
    TrackSearch, TrackListing
  },
  data () {
    return {
      queryString: '',
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
  },
  methods: {
    searchTrack (queryString) {
      this.queryString = queryString
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

.track-listing
  margin-top: 4rem

.submit
  margin-top: 4rem
</style>
