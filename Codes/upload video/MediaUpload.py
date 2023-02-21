from __future__ import print_function

import httplib2
import os
import os.path
import sys
import random
import time
import base64
import google.auth
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from google_auth_oauthlib.flow import InstalledAppFlow
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage 
from oauth2client.tools import argparser, run_flow
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

class UploadInYT:
    def __init__(self, VideoFile, VideoTitle, VideoDescription, VideoKeywords, VideoCategory = 22, VideoPrivacyStatus = "public"):
        self.VideoFile = VideoFile
        self.VideoTitle = VideoTitle
        self.VideoDescription = VideoDescription
        self.VideoKeywords = VideoKeywords
        self.VideoCategory = VideoCategory
        self.VideoPrivacyStatus = VideoPrivacyStatus
    
    def UploadVideoInYT(self):
        tags = None
        if self.VideoKeywords:
            tags = self.VideoKeywords.split(",")
        response = None
        error = None
        retry = 0

        body = dict(
            snippet = dict(
                title = self.VideoTitle,
                description = self.VideoDescription,
                tags = tags,
                categoryId = self.VideoCategory
            ),
            status = dict(
                privacyStatus = self.VideoPrivacyStatus
            )
        )

        insert_request = youtube.videos().insert(
            part = ",".join(body.keys()),
            body = body,
            media_body = MediaFileUpload(self.VideoFile, chunksize=-1, resumable=True)
        )

        while response is None:
            try:
                print("Uploading file...")
                status, response = insert_request.next_chunk()

                if response is not None:
                    if 'id' in response:
                        print("Video id '%s' was successfully uploaded." % response['id'])
                        VideoId = response['id'] ######################################################
                        return VideoId
                    else:
                        exit("The upload failed with an unexpected response: %s" % response)
            except HttpError as e:
                if e.resp.status in RETRIABLE_STATUS_CODES:
                    error = "A retriable HTTP error %d occurred:\n%s" % (e.resp.status,
                                                                    e.content)
                else:
                    raise
            except RETRIABLE_EXCEPTIONS as e:
                error = "A retriable error occurred: %s" % e

            if error is not None:
                print(error)
                retry += 1
                if retry > MAX_RETRIES:
                    exit("No longer attempting to retry.")

            max_sleep = 2 ** retry
            sleep_seconds = random.random() * max_sleep
            print("Sleeping %f seconds and then retrying..." % sleep_seconds)
            time.sleep(sleep_seconds)
    
    def UploadThumnailInYT(VideoId):
        ThumbnailPath = "C:/Users/User/Downloads/hello.jpg"
        try:
            youtube.thumbnails().set(
                videoId = VideoId,
                media_body = MediaFileUpload(ThumbnailPath)
            ).execute()
        except:
            print("Your Youtube channel is unverified so that you cannot upload custom Thumbnails." + "\n" +
                  "You need to verify your account to upload Thumbnail." + "\n" +
                  "You can do this by navigating to YouTube > clicking your profile icon > Settings > Channel status and features > Channel > Feature eligibility > Intermediate features.")
      
    def SendMail(VideoId):
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', GMAIL_SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                gmailflow = InstalledAppFlow.from_client_secrets_file(
                    'C:/Users/User/Desktop/client_secret_new.json', GMAIL_SCOPES)
                creds = gmailflow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            # Call the Gmail API
            service = build('gmail', 'v1', credentials=creds)

            message = EmailMessage()

            message.set_content('Your AI generated video have been successfully uploaded.' + '\n' + 
                                'You can check your video by clicking this link : ' + '\n' +
                                'http://www.youtube.com/watch?v=' + VideoId)

            message['To'] = 'lp8511701@gmail.com'
            message['From'] = 'athisankaranb@gmail.com'
            message['Subject'] = 'Youtube Video Uploaded Successfully'

            # encoded message
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
                .decode()

            create_message = {
                'raw': encoded_message
            }
            # pylint: disable=E1101
            send_message = (service.users().messages().send
                            (userId="me", body=create_message).execute())
            print(F'Message Id: {send_message["id"]}')

        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f'An error occurred: {error}')
            send_message = None
        return send_message

httplib2.RETRIES = 1
MAX_RETRIES = 10
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError)
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

CLIENT_SECRETS_FILE = "C:/Users/User/Desktop/client_secret_new.json"
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
MISSING_CLIENT_SECRETS_MESSAGE = os.path.abspath(os.path.join(os.path.dirname(__file__), CLIENT_SECRETS_FILE))
VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")


flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_UPLOAD_SCOPE, message=MISSING_CLIENT_SECRETS_MESSAGE)
storage = Storage("%s-oauth2.json" % sys.argv[0])
credentials = storage.get()
if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage)

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, http=credentials.authorize(httplib2.Http()))


GMAIL_SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

YouTubeUpload = UploadInYT("C:/Users/User/Desktop/samplevid.mp4", "AN UNBELEIVABLE SKILL", "A world class skill showed by a kid", "skill kid boy fight")
VideoId = YouTubeUpload.UploadVideoInYT()  
UploadInYT.UploadThumnailInYT('STMAqHyk3f8')
UploadInYT.SendMail('STMAqHyk3f8')