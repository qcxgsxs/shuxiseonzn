# Chrome Web Store & Edge Add‑ons Upload Instructions

This directory contains scripts and metadata to package and upload the extension to Chrome Web Store and Microsoft Partner Center (Edge Add‑ons).  

Important: do NOT send credentials (service-account JSON, client secrets) in public chat. Use a secure channel as discussed.

1) Packaging (local)
- Ensure you have assets/icon.png and assets/bg1.png/bg2.png/bg3.png in the repository.
- Generate icon-* variants if needed (see image_utils.py).
- Run the pack script in the repository root:
  ```bash
  chmod +x pack_and_zip.sh
  ./pack_and_zip.sh
  ```
- The output zip will be at `dist/shuxiseonzn-extension.zip`.

2) Chrome Web Store automated upload (service account JSON)
- If you want automatic upload, provide a Google Cloud service account JSON with the Chrome Web Store API enabled.
- Use the `upload_chrome.py` script (requires `google-auth` and `requests` installed). See `upload_chrome.py --help` for options.

3) Microsoft Partner Center (Edge Add‑ons)
- Partner Center requires configuring an app / API keys. The upload process is documented in `upload_edge.md`.

4) Manual upload (recommended if you prefer maximum control)
- Login to the Chrome Web Store Developer Dashboard and create a new item; upload the zip from `dist/` and fill in metadata and screenshots.
- For Edge, login to Partner Center and create a new add-on listing and upload the same zip.

5) Privacy policy
- A public privacy policy URL is required for store submission. We included a template file `privacy_policy.md` in the repo; host it on a public URL (e.g., GitHub Pages) before submission.

If you want me to upload on your behalf, please send the service-account JSON and Partner Center credentials using your chosen secure channel and then tell me "credentials sent via <channel>" so I can start the upload process.
