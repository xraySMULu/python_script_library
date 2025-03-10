import os
import zipfile
from boxsdk import Client, OAuth2

def zip_and_upload_to_box(local_folder_path, zip_file_name, box_folder_id, client_id, client_secret, access_token):
    """
    Zips a local folder and uploads it to Box.

    Args:
        local_folder_path (str): Path to the local folder to be zipped.
        zip_file_name (str): Name of the zip file to be created.
        box_folder_id (str): ID of the Box folder to upload the zip file to.
        client_id (str): Your Box application's client ID.
        client_secret (str): Your Box application's client secret.
        access_token (str): Your Box application's access token.
    """

    # Create a zip archive
    zip_file_path = os.path.join(os.getcwd(), zip_file_name)
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(local_folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, local_folder_path))

    # Authenticate with Box
    auth = OAuth2(
        client_id=client_id,
        client_secret=client_secret,
        access_token=access_token
    )
    client = Client(auth)

    # Upload the zip file to Box
    try:
        box_folder = client.folder(box_folder_id)
        box_folder.upload(zip_file_path, file_name=zip_file_name)
        print(f"Successfully uploaded '{zip_file_name}' to Box folder ID '{box_folder_id}'.")
    except Exception as e:
         print(f"Error uploading '{zip_file_name}' to Box: {e}")
    finally:
        # Clean up the local zip file
        os.remove(zip_file_path)


if __name__ == "__main__":
    # Replace with your actual values
    local_folder_to_zip = "/path/to/your/local/folder"
    zip_name = "my_folder.zip"
    box_destination_folder_id = "YOUR_BOX_FOLDER_ID"
    box_client_id = "YOUR_BOX_CLIENT_ID"
    box_client_secret = "YOUR_BOX_CLIENT_SECRET"
    box_access_token = "YOUR_BOX_ACCESS_TOKEN"

    zip_and_upload_to_box(
        local_folder_to_zip,
        zip_name,
        box_destination_folder_id,
        box_client_id,
        box_client_secret,
        box_access_token
    )