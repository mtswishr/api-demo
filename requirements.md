1. Construct a request to the MessageBird API endpoint using a user provided ANI value (example: 14085551212).
2. Utilize the MessageBird API key, which you can obtain from MessageBird Developer Portal, to authenticate your request.
3. Send the request to the appropriate MessageBird API endpoint for performing a lookup operation.
4. Retrieve the response from the API call, and extract the required parameters (countryCode, countryPrefix, e164, and MessageBird) from the response data.
5. Display these parameters as the output of the program.

Ensure your program handles potential issues such as:

- Network errors: Handle situations where the program fails to connect to the MessageBird API due to network issues.
- Authentication errors: Deal with cases where the provided API key is invalid or unauthorized.
- Invalid input: Handle scenarios where the provided ANI value is invalid or improperly formatted.

Your task involves the following steps:

1. Retrieve the album and photo data from the respective endpoints.
2. Filter the albums based on user-provided IDs.
3. Create a folder for each selected album, named in the format album_name_albumid (e.g., sunt qui excepturi placeat culpa_2).
4. Download the images associated with the selected albums using the URLs provided in the photo data.
5. Save each image in the corresponding album folder.

In the parent directory, create a CSV file containing the following columns: id, title, album_id, album_title, remote_path, and local_path.
1. id: The photo ID.
2. title: The title of the photo.
3. album_id: The ID of the album to which the photo belongs.
4. album_title: The title of the album.
5. remote_path: The URL of the photo.
6. local_path: The local path where the photo is saved relative to the parent directory.
