<!-- HistoryComponent.vue -->
<template>
  <div>
    <!-- ... autres éléments ... -->
    <table>
      <thead>
        <tr>
          <th>Media</th>
          <th>Nom</th>
          <th>Conversion</th>
          <th>Date</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="media in this.medias" :key="media.id">
          <td v-if="media.original_image && !media.isLoading">
            <i class="fas fa-image" title="Original Media"></i>
          </td>
          <td v-else-if="media.isLoading">
            <i class="fa fa-spinner fa-spin"></i>
          </td>
          <td v-else>
            No Image
          </td>

          <td>{{ media.name }}</td>
          <td>{{ media.conversion_type || 'No conversion type' }}</td>
          <td>{{ new Date(media.conversion_date).toLocaleDateString() }}</td>
          <td>
              <!-- Téléchargement de l'image convertie -->
        <i class="fas fa-download" style="margin-right: 10px;" title="Télécharger l'image convertie"
          @click="downloadFile(media.id, 'converted')"></i>

        <!-- Téléchargement de l'image originale -->
        <i class="fas fa-download" style="margin-right: 10px;" title="Télécharger l'image originale"
          @click="downloadFile(media.id, 'original')"></i>

            <!-- Suppression de l'image de l'historique -->
            <i class="fas fa-trash" title="Supprimer de l'historique" @click="deleteMedia(media.id)"></i>
          </td>

        </tr>
      </tbody>
    </table>
    <button @click="deleteAllMedias">Supprimer tous les uploads</button>
  </div>
</template>

<script lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { Media } from '../types/media'
import { MediaRequest } from '../types/mediaRequest'

export default {
  name: 'HistoryComponent',
  setup () {
    const medias = ref<Media[]>([])

    const downloadFile = async (mediaId: number, type: string) => {
      try {
        let apiUrl
        if (type === 'original') {
          apiUrl = `http://localhost:99/api/download_original/?media_id=${mediaId}`
        } else {
          apiUrl = `http://localhost:99/api/download_converted/?media_id=${mediaId}`
        }
        window.location.href = apiUrl
      } catch (error) {
        console.error('Erreur lors du téléchargement:', error)
      }
    }

    const deleteMedia = async (mediaId: number) => {
      try {
        const media = medias.value.find(m => m.id === mediaId)
        if (media) {
          media.isLoading = true
        }

        const response = await fetch(`http://localhost:99/api/delete_media/${mediaId}`, {
          method: 'DELETE'
        })

        if (response.ok) {
          medias.value = medias.value.filter(m => m.id !== mediaId)
        } else {
          console.error('Erreur lors de la suppression du média.')
        }
      } catch (error) {
        console.error('Erreur lors de la suppression du média:', error)
      } finally {
        const media = medias.value.find(m => m.id === mediaId)
        if (media) {
          media.isLoading = false
        }
      }
    }

    const deleteAllMedias = async () => {
      try {
        await axios.delete('http://localhost:99/api/delete_all_medias/')
        fetchMedias()
      } catch (error) {
        console.error('Erreur lors de la suppression de tous les médias:', error)
      }
    }

    const fetchMedias = async () => {
      try {
        const response = await axios.get('http://localhost:99/api/media/')
        medias.value = response.data
      } catch (error) {
        console.error('Erreur lors de la récupération des médias:', error)
      }
    }
    const addMedia = (newMedia: MediaRequest) => {
      console.log(newMedia)
      medias.value.push(newMedia.media)
      // medias = medias[...medias, newMedia];
      console.log(medias)
    }

    onMounted(fetchMedias)

    return {
      medias,
      downloadFile,
      deleteMedia,
      deleteAllMedias,
      addMedia
    }
  }
}
</script>
<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 18px;
  text-align: left;
}

th,
td {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f2f2f2;
}

tr:hover {
  background-color: #f5f5f5;
}

img {
  width: 100px;
}

i:hover {
  transform: scale(1.2);
  transition: all ease-in;
  cursor: pointer;
}
</style>
