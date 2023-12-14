function fetchPOST(endpoint, data){
	// submit a POST request to an endpoint and put the response inside of response-container
	fetch(endpoint, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(data),
	})
		.then(response => response.text())
		.then(html =>{
			updateResponseContainer(html)
		});
}

async function asyncFetchPOST(endpoint, data){
	// same as fetchPOST but returns a promise
	await fetch(endpoint, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(data),
	})
		.then(response => response.text())
		.then(html =>{
			updateResponseContainer(html)
		});
}

async function listen(){
	let active_config = JSON.parse(getCookie('active_config'))
	let data = {
		'com_port': active_config['com_port'],
		'addr':active_config['addr'],
	}
	await asyncFetchPOST('/execute/listen',data) 
}
