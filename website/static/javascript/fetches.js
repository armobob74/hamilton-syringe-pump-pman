async function fetchPOST(endpoint, data) {
  const response = await fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return response.text();
}

async function listen() {
  let data = {
    args: [],
  };
  return await fetchPOST("/pman/listen", data);
}

async function transfer(from_port, to_port, volume) {
  const args = [from_port, to_port, volume];
  const data = { args: args };
  const first_response = await fetchPOST("/pman/transfer", data);
  console.log(first_response);
  const second_response = await listen();
  console.log(second_response)
  return second_response;
}
const example_data = { args: [0, 1, 120] };
