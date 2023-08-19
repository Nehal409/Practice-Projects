const { DataTypes } = require("sequelize");
const sequelize = require("../config/database");

const Book = sequelize.define("books", {
  title: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  author: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  subject: {
    type: DataTypes.STRING
  },
});

module.exports = Book;


