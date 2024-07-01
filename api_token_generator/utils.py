import customtkinter as ctk  # Import customtkinter
from .code_generator import generate_js_code  # Relative import

def save_code_to_file(api_name, js_code):
    if api_name.strip() == "":
        print("API Name cannot be empty")
        return
    with open(f"{api_name}_get_token.js", "w") as file:
        file.write(js_code)
    print(f"\nJavaScript code has been saved to {api_name}_get_token.js")

def on_generate(auth_method, auth_endpoint, client_id, client_secret, response_type, output_text):
    # Logging the input details
    print("Generating JS code with the following details:")
    print(f"Auth Method: {auth_method}")
    print(f"Auth Endpoint: {auth_endpoint}")
    print(f"Client ID: {client_id}")
    print(f"Client Secret: {client_secret}")
    print(f"Response Type: {response_type}")

    api_details = {
        "auth_endpoint": auth_endpoint,
        "client_id": client_id,
        "client_secret": client_secret
    }

    output_text.delete("1.0", ctk.END)

    js_code = generate_js_code(auth_method, api_details, response_type)
    
    if js_code:
        # Find the start and end of the getBearerToken() function
        start_index = js_code.find("async function getBearerToken() {")
        end_index = js_code.find("getBearerToken().then(token => {")
        if start_index != -1 and end_index != -1:
            js_code = js_code[start_index:end_index].strip()

        output_text.insert(ctk.END, js_code)
        print("Generated JS Code:")
        print(js_code)
    else:
        output_text.insert(ctk.END, "Failed to generate JS Code.\n")
        print("Failed to generate JS Code.")
