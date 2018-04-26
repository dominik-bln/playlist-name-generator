<template>
  <div class="track-search">
    <v-select
      ref="selectInput"
      label="Find tracks for playlist"
      hint="Search by artist or track title"
      autocomplete
      return-object
      multiple
      persistent-hint
      browser-autocomplete="off"
      :filter="filterOutAlreadySelected"
      :loading="isLoading"
      :items="optionValues"
      item-text="track_title"
      :value="fakeSelection"
      @input="handleSelection($event)"
      :search-input="query"
      @update:searchInput="handleSearchChange($event)">
      <template slot="item" slot-scope="data">
        <v-list-tile-content v-if="data.item.track_artist && data.item.track_title" v-text="data.item.track_artist + ' | ' + data.item.track_title"></v-list-tile-content>
      </template>
    </v-select>
  </div>
</template>

<script>
/**
 * A typeahead field that can display a set of given options and does not
 * display its current value (but requires another external component to do
 * that e.g. a table).
 *
 * The `value` prop is required to filter out already selected elements.
 *
 * Emits an `input` event with the selected object and a `search-input` event
 * when the user alters the search.
 */
export default {
  name: 'TrackSearch',
  props: {
    value: {
      required: true
    },
    /**
     * An array with option objects. By default the `name` key is used
     * for display purposes (can be replaced via `optionLabel`).
     */
    optionValues: {
      type: Array,
      required: true
    },
    /**
     * Whether the `optionValues` are currently loading.
     */
    isLoading: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      // we need to set an empty value on the select to disable the default
      // v-select displaying because it is expected to be done externally
      fakeSelection: [],
      query: ''
    }
  },
  methods: {
    handleSelection (selection) {
      // Reset the value of the component because we show the data externally.
      // Vuetify seems to copy and watch the selection, otherwise this would
      // not be necessary.
      this.fakeSelection = []
      // we only allow single selection, so the first in the list
      this.$emit('input', selection[0])
    },
    /**
     * Emit a `search-change` event when the user entered a query.
     */
    handleSearchChange (query) {
      // we need to check for null because the queries always expect a string
      if (query) {
        this.$emit('update:searchInput', query)
      }
    },
    /**
     * Ensure that values can only be selected once and are hidden when they are
     * already in the value collection.
     *
     * Using `hide-selected` of v-select does not work here, because of the
     * empty `fakeSelection` being passed to it, to hide the default displaying.
     */
    filterOutAlreadySelected (itemToCheck) {
      return !this.value.find((item) => {
        return item.isrc === itemToCheck.isrc
      })
    }
  }
}
</script>

<style lang="stylus" scoped>
</style>
