<template>
  <div>
    <div class="left-column">
      <UploadComponent @uploadSuccess="refreshHistory" />
    </div>
    <div class="right-column">
      <HistoryComponent ref="historyComponent" />
    </div>
  </div>
</template>

<script>
import UploadComponent from '../components/Upload.vue'
import HistoryComponent from '../components/History.vue'

export default {
  components: {
    UploadComponent,
    HistoryComponent
  },
  methods: {
    refreshHistory (newMedia) {
      this.$refs.historyComponent.addMedia(newMedia)
      // this.$refs.historyComponent.fetchMedias()
    }
    // ... autres méthodes ...
  }
}
</script>

<style>
.left-column {
  width: 50%;
  float: left;
}

.right-column {
  width: 50%;
  float: right;
}
</style>
