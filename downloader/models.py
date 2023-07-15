from django.db import models

# Create your models here.
# def download_video(url, output_path):
#   """Downloads a video from the given URL and saves it to the given output path.
#   Args:
#     url: The URL of the video to download.
#     output_path: The path to save the video to.
#   """
#   # Create the output directory if it doesn't exist.
#   if not os.path.exists(os.path.dirname(output_path)):
#     os.makedirs(os.path.dirname(output_path))
#   # Download the video using `requests`.
#   response = requests.get(url, stream=True)
#   # Write the video to the output file.
#   with open(output_path, "wb") as f:
#     for chunk in response.iter_content(chunk_size=1024):
#       if chunk:
#         f.write(chunk)