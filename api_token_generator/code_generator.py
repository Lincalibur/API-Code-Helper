def generate_js_code(auth_method, api_details, response_type):
    js_code = ""
    if auth_method == "Client Credentials":
        js_code = f"""
        const fetch = require('node-fetch');

        async function getBearerToken() {{
            const url = '{api_details["auth_endpoint"]}';
            const credentials = new URLSearchParams();
            credentials.append('grant_type', 'client_credentials');
            credentials.append('client_id', '{api_details["client_id"]}');
            credentials.append('client_secret', '{api_details["client_secret"]}');

            const response = await fetch(url, {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/x-www-form-urlencoded'
                }},
                body: credentials
            }});

            if (!response.ok) {{
                throw new Error('Failed to fetch the token');
            }}

            const data = await response.{response_type.lower()}();
            return data.access_token;
        }}

        getBearerToken().then(token => {{
            console.log('Bearer Token:', token);
        }}).catch(error => {{
            console.error('Error:', error);
        }});
        """
    elif auth_method == "OAuth2 Authorization Code":
        # Add the JS code for OAuth2 Authorization Code here
        pass
    elif auth_method == "API Key":
        js_code = f"""
        const fetch = require('node-fetch');

        async function getBearerToken() {{
            const url = '{api_details["auth_endpoint"]}';
            const headers = {{
                'Authorization': 'Bearer {api_details["client_id"]}',
                'Content-Type': 'application/json'
            }};

            const response = await fetch(url, {{
                method: 'GET',
                headers: headers
            }});

            if (!response.ok) {{
                throw new Error('Failed to fetch the token');
            }}

            const data = await response.{response_type.lower()}();
            return data.access_token;
        }}

        getBearerToken().then(token => {{
            console.log('Bearer Token:', token);
        }}).catch(error => {{
            console.error('Error:', error);
        }});
        """
    else:
        print(f"Unsupported authentication method: {auth_method}")
        return ""

    return js_code
