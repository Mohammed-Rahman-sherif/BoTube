#!/usr/bin/python

import httplib2
import os
import sys

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = "C:/Users/User/Desktop/client_secret_app.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube.force-ssl"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the {{ Cloud Console }}
{{ https://cloud.google.com/console }}

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

def get_authenticated_service():
  '''
  credential_path = os.path.join('./', 'E:/BotYT/BoTube/Codes/upload video/thumbnailupload.py-oauth2.json')
  store = Storage(credential_path)
  credentials = store.get()
  if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRETS_FILE, SCOPES)
    credentials = tools.run_flow(flow, store)
  return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=credentials)'''
  
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
    scope=YOUTUBE_READ_WRITE_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

  storage = Storage("%s-oauth2.json" % sys.argv[0])
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage)

  return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    http=credentials.authorize(httplib2.Http()))

# Call the API's thumbnails.set method to upload the thumbnail image and
# associate it with the appropriate video.
def upload_thumbnail(youtube, video_id, file):
  youtube.thumbnails().set(
    videoId=video_id,
    media_body=file
  ).execute()

if __name__ == "__main__":
  # The "videoid" option specifies the YouTube video ID that uniquely
  # identifies the video for which the thumbnail image is being updated.
  '''
  argparser.add_argument("--video-id", required=True,
    help="ID of video whose thumbnail you're updating.")
  # The "file" option specifies the path to the thumbnail image file.
  argparser.add_argument("--file", required=True,
    help="Path to thumbnail image file.")
  args = argparser.parse_args()'''

  video="GIKsEqqoJgo"
  path="C:/Users/User/Downloads/hello.jpg"
  if not os.path.exists(path):
    exit("Please specify a valid file using the --file= parameter.")

  youtube = get_authenticated_service()
  try:
    upload_thumbnail(youtube, video, path)
  except HttpError as e:
    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
  else:
    print("The custom thumbnail was successfully set.")



'''
# -*- coding: utf-8 -*-

# Sample Python code for youtube.thumbnails.set
# NOTES:
# 1. This sample code uploads a file and can't be executed via this interface.
#    To test this code, you must run it locally using your own API credentials.
#    See: https://developers.google.com/explorer-help/code-samples#python
# 2. This example makes a simple upload request. We recommend that you consider
#    using resumable uploads instead, particularly if you are transferring large
#    files or there's a high likelihood of a network interruption or other
#    transmission failure. To learn more about resumable uploads, see:
#    https://developers.google.com/api-client-library/python/guide/media_upload

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.http import MediaFileUpload

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "C:/Users/User/Desktop/client_secrets.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.thumbnails().set(
        
        # TODO: For this request to work, you must replace "YOUR_FILE"
        #       with a pointer to the actual file you are uploading.
        media_body=MediaFileUpload("E:/BotYT/BoTube/Codes/stars.jpg")
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()'''

'''
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.http import MediaFileUpload

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def upload_thumbnail(video_id, thumbnail_file):
    try:
        # Get credentials and create an API client
        client_secrets_file = "C:/Users/User/Desktop/client_secrets2.json"
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            "youtube", "v3", credentials=credentials)

        request = youtube.thumbnails().set(
            videoId=video_id,
            media_body=MediaFileUpload(thumbnail_file)
        )
        response = request.execute()

        print("Thumbnail uploaded.")
    except HttpError as error:
        print(f"An error occurred: {error}")
        response = None

    return response

# Example usage
video_id = "2S1IOevsn7g"
thumbnail_file = "E:/BotYT/BoTube/Codes/stars.jpg"

upload_thumbnail(video_id, thumbnail_file)
'''