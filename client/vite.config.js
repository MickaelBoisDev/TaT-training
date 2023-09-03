import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'url'
import eslint from 'vite-plugin-eslint'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), eslint()],
  failOnError: true,
  emitError: true,
  emitWarning: true,
  server: {
    host: '127.0.0.1',
    hmr: {
      protocol: 'ws',
      host: '127.0.0.1'
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  build: {
    rollupOptions: {
      output: {
        // Default
        dir: 'dist',
        entryFileNames: 'static/[name]-[hash].js',
        assetFileNames: ({ name }) => {
          if (/\.(gif|jpe?g|png|svg)$/.test(name ?? '')) {
            return 'static/images/[name]-[hash][extname]'
          }
          if (/\.css$/.test(name ?? '')) {
            return 'static/[name]-[hash][extname]'
          }
          if (/\.woff$/.test(name ?? '')) {
            return 'static/[name]-[hash][extname]'
          }
          // default value
          // ref: https://rollupjs.org/guide/en/#outputassetfilenames
          return '[name]-[hash][extname]'
        }
      }
    }
  }
})
