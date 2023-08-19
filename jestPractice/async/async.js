const axios = require("axios");

const fetchData = async (id) => {
  const results = await axios.get(`https://jsonplaceholder.typicode.com/todos/${id}`);
  const data = results.data
  console.log(data);
  return data;
};

fetchData(3)
module.exports = fetchData