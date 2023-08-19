const bookController = require('../controllers/book.ctrl')

const express = require('express');
const router = express.Router()

// Create a book
// http://localhost:4000/api/create
router.post('/create', bookController.createBook )

module.exports = router