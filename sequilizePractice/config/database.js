const Sequelize = require("sequelize");

const sequelize = new Sequelize("sequilizePractice", "root", "", {
  host: "localhost",
  dialect: "mysql",
});

module.exports = sequelize;
