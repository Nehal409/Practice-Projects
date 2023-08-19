const Book = require("../models/book.model");

async function createBook(req, res) {
  const { title, author, subject } = req.body;

  try {
    const newBook = await Book.create({
      title: title,
      author: author,
      subject: subject,
    });

    res.status(201).json(newBook);
  } catch (error) {
    console.log(error);
    res.status(500).json({ error: "An error occurred while creating the book." });
  }
}

module.exports = {
  createBook,
};
