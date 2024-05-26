// src/http.js
import axios from 'axios'

const http = axios.create({
  baseURL: 'https://mma-five.vercel.app/',
  headers: {
    'Content-Type': 'application/json'
  }
})

export default http
