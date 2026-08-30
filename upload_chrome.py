"""
upload_chrome.py

Upload an unpacked extension zip to Chrome Web Store using a Google Service Account JSON.
This script uses google-auth to build credentials. It expects the service account JSON file path
and the path to the extension zip.

Usage:
  python upload_chrome.py --service-account /path/to/service_account.json --zip dist/shuxiseonzn-extension.zip [--item-id ITEM_ID]

If ITEM_ID is provided, the script will update that item; otherwise it will try to insert a new item
(if your service account has appropriate permissions).

Note: You must enable "Chrome Web Store API" for the service account project and grant the service
account access to the target item or use an account that is owner of the item.

Security: Do NOT paste your service-account JSON here. Use a secure channel to send the file.
"""

import argparse
import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

UPLOAD_URL = 'https://www.googleapis.com/upload/chromewebstore/v1.1/items'
PUBLISH_URL = 'https://www.googleapis.com/chromewebstore/v1.1/items/{itemId}/publish'

SCOPES = ['https://www.googleapis.com/auth/chromewebstore']


def get_authorized_session(service_account_json):
    creds = service_account.Credentials.from_service_account_file(service_account_json, scopes=SCOPES)
    authed_session = AuthorizedSession(creds)
    return authed_session


def upload_item(authed_session, zip_path, item_id=None):
    headers = {
        'x-goog-api-version': '2'
    }
    params = {}
    if item_id:
        url = f"{UPLOAD_URL}/{item_id}"
    else:
        url = UPLOAD_URL
    with open(zip_path, 'rb') as f:
        resp = authed_session.post(url, headers=headers, params=params, data=f)
    resp.raise_for_status()
    return resp.json()


def publish_item(authed_session, item_id, target='default'):
    url = PUBLISH_URL.format(itemId=item_id)
    params = {'publishTarget': target}
    resp = authed_session.post(url, params=params)
    resp.raise_for_status()
    return resp.json()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--service-account', required=True, help='Path to service-account JSON')
    parser.add_argument('--zip', required=True, help='Path to extension zip')
    parser.add_argument('--item-id', required=False, help='Existing Chrome Web Store item id (optional)')
    parser.add_argument('--publish', action='store_true', help='Publish after upload')
    args = parser.parse_args()

    session = get_authorized_session(args.service_account)
    print('Uploading item...')
    res = upload_item(session, args.zip, item_id=args.item_id)
    print('Upload response:', json.dumps(res, indent=2, ensure_ascii=False))
    # If itemId returned, publish optionally
    item_id = args.item_id or res.get('itemId')
    if args.publish and item_id:
        print('Publishing item', item_id)
        pub = publish_item(session, item_id)
        print('Publish response:', json.dumps(pub, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
