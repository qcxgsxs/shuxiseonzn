# Edge Add-ons upload notes

Microsoft Partner Center upload is more complex and often requires:
- Registering an Azure AD application and granting it access to Partner Center APIs
- Creating a service principal and client secret (tenant id, client id, client secret)
- Making authenticated requests to Partner Center's submission APIs

I will help automate this once you provide the required Partner Center credentials via your secure channel. For now, use Partner Center portal to upload the same zip produced by `pack_and_zip.sh`.

Refer to Microsoft docs: https://learn.microsoft.com/en-us/windows/uwp/packaging/partner-center-api
