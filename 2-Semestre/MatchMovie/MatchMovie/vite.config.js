import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  base: "/MatchMovie/",
  plugins: [react()],
  test: {
    globals: true,
    environment: "jsdom",
    setupFiles: "./src/test/setup.js",
    include: ['*/.{test,spec}.{js,mjs,cjs,jsx}']
  
  }
})
