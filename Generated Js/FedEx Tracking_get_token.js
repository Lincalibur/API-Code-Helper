
    const fetch = require('node-fetch');

    async function getBearerToken() {
        const url = 'https://apis.fedex.com/track/v1/trackingnumbers';
        const credentials = new URLSearchParams();
        credentials.append('grant_type', 'bearer');
        credentials.append('client_id', 'TestClientId');
        credentials.append('client_secret', 'TestClientSecret');

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: credentials
        });

        if (!response.ok) {
            throw new Error('Failed to fetch the token');
        }

        const data = await response.json();
        return data.access_token;
    }

    getBearerToken().then(token => {
        console.log('Bearer Token:', token);
    }).catch(error => {
        console.error('Error:', error);
    });
    