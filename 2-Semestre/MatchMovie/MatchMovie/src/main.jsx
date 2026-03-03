import { StrictMode } from 'react'
import RouterApp from './routes/index.jsx'
import { createRoot } from 'react-dom/client'
import './index.css'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterApp />
  </StrictMode>,
)

