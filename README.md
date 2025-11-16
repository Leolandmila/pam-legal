# PAM Legal Documents

This repository hosts the Privacy Policy and Terms of Service for the Parent Admin Manager (PAM) mobile application.

## Published URLs

Once deployed to GitHub Pages, these documents are available at:
- **Home:** `https://[your-username].github.io/pam-legal/`
- **Privacy Policy:** `https://[your-username].github.io/pam-legal/privacy-policy.html`
- **Terms of Service:** `https://[your-username].github.io/pam-legal/terms-of-service.html`

## Deployment Instructions

### Initial Setup

1. **Create GitHub repository:**
   ```bash
   # Create new repository on GitHub named "pam-legal"
   # Then push this directory:
   cd pam-legal-docs
   git init
   git add .
   git commit -m "Initial commit: Privacy Policy and Terms of Service"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/pam-legal.git
   git push -u origin main
   ```

2. **Enable GitHub Pages:**
   - Go to repository Settings
   - Navigate to "Pages" section
   - Under "Source", select "main" branch and "/public" folder
   - Click "Save"
   - Your site will be published at: `https://YOUR-USERNAME.github.io/pam-legal/`

### Updating Documents

1. **Edit source files:**
   - Edit `../PRIVACY_POLICY.md` or `../TERMS_OF_SERVICE.md`

2. **Regenerate HTML:**
   ```bash
   python3 convert_to_html.py
   ```

3. **Commit and push:**
   ```bash
   git add public/
   git commit -m "Update legal documents"
   git push
   ```

Changes will be live within 1-2 minutes.

## Files

- `public/` - Hosted files (this is what GitHub Pages serves)
  - `index.html` - Landing page with links to both documents
  - `privacy-policy.html` - Privacy Policy
  - `terms-of-service.html` - Terms of Service
- `convert_to_html.py` - Script to convert Markdown to HTML
- `README.md` - This file

## Local Testing

To test locally before deploying:

```bash
cd public
python3 -m http.server 8000
```

Then visit: `http://localhost:8000`

## Maintenance

- Update the "Last Updated" date when making changes
- Keep source Markdown files in sync with HTML
- Test all links after updates
- Verify mobile responsiveness

## Contact

- **Privacy Questions:** privacy@parentaladminmanager.com
- **Support:** support@parentaladminmanager.com

## License

© 2025 Parent Admin Manager. All rights reserved.
