import customtkinter as ctk
from .utils import on_generate, save_code_to_file  # Import save_code_to_file

def create_gui():
    app = ctk.CTk()
    app.title("API JS Code Generator")
    app.geometry("600x700")

    # API Name Input
    api_name_label = ctk.CTkLabel(app, text="API Name:")
    api_name_label.pack(pady=10)
    api_name_entry = ctk.CTkEntry(app, width=400)
    api_name_entry.pack(pady=10)

    # Authentication Method Selection
    auth_method_var = ctk.StringVar(value="Client Credentials")
    auth_method_label = ctk.CTkLabel(app, text="Select Authentication Method:")
    auth_method_label.pack(pady=10)
    auth_method_menu = ctk.CTkOptionMenu(app, variable=auth_method_var, values=["Client Credentials", "OAuth2 Authorization Code", "API Key"])
    auth_method_menu.pack(pady=10)

    # API Details Input
    auth_endpoint_label = ctk.CTkLabel(app, text="Authentication Endpoint URL:")
    auth_endpoint_label.pack(pady=10)
    auth_endpoint_entry = ctk.CTkEntry(app, width=400)
    auth_endpoint_entry.pack(pady=10)

    client_id_label = ctk.CTkLabel(app, text="Client ID:")
    client_id_label.pack(pady=10)
    client_id_entry = ctk.CTkEntry(app, width=400)
    client_id_entry.pack(pady=10)

    client_secret_label = ctk.CTkLabel(app, text="Client Secret:")
    client_secret_label.pack(pady=10)
    client_secret_entry = ctk.CTkEntry(app, show="*", width=400)
    client_secret_entry.pack(pady=10)

    # Response Type Selection
    response_type_var = ctk.StringVar(value="JSON")
    response_type_label = ctk.CTkLabel(app, text="Expected Response Type:")
    response_type_label.pack(pady=10)
    response_type_menu = ctk.CTkOptionMenu(app, variable=response_type_var, values=["JSON", "XML"])
    response_type_menu.pack(pady=10)

    # Generate Button
    generate_button = ctk.CTkButton(app, text="Generate JS Code", command=lambda: on_generate(auth_method_var.get(), auth_endpoint_entry.get(), client_id_entry.get(), client_secret_entry.get(), response_type_var.get(), output_text))
    generate_button.pack(pady=20)

    # Output Text Box
    output_text = ctk.CTkTextbox(app, width=500, height=200)
    output_text.pack(pady=10)

    # Save Button
    save_button = ctk.CTkButton(app, text="Save JS Code", command=lambda: save_code_to_file(api_name_entry.get(), output_text.get("1.0", ctk.END)))
    save_button.pack(pady=10)

    return app
