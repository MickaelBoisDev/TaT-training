<!-- Upload.vue -->

<template>
  <label for="mediaName">Nom du média:</label>
  <input v-model="mediaName" id="mediaName" placeholder="Entrez le nom du média" />
  <div @click="openFileDialog" @dragover.prevent @drop="fileUpload" class="upload-area">
    <p>Glissez et déposez votre fichier ici, ou cliquez pour sélectionner un fichier.</p>
    <input type="file" @change="fileUpload" ref="fileInput" hidden />
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'UploadComponent',
  data () {
    return {
      mediaName: ''
    }
  },
  emits: ['uploadSuccess'],

  setup (props, { emit }) {
    const fileInput = ref(null)

    const openFileDialog = () => {
      fileInput.value.click()
    }
    const fileUpload = async event => {
      let files
      if (event.type === 'drop') {
        files = event.dataTransfer.files
      } else {
        files = event.target.files
      }

      // Création du formulaire pour envoyer l'image
      const formData = new FormData()
      formData.append('image', files[0])
      // To do
      // formData.append('name', this.mediaName)

      try {
        const response = await fetch('http://localhost:99/api/upload_and_convert/', {
          method: 'POST',
          body: formData
        })

        const data = await response.json()
        if (data) {
          console.log('Le fichier à été converti', data)
          emit('uploadSuccess', data)
        }
      } catch (error) {
        console.error('Erreur lors de l\'envoi de l\'image:', error)
      }
    }

    return {
      fileUpload,
      openFileDialog,
      fileInput
    }
  }
}
</script>

<style scoped>
.upload-area {
  width: 80%;
  margin: 20px auto;
  height: 20rem;
  padding: 10px;
  border: 2px dashed #ccc;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
</style>
