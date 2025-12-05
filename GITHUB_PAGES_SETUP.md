# GitHub Pages Setup Instructions

## Problem
The GitHub Pages site is not automatically deploying because the source needs to be configured.

## Solution: Enable GitHub Pages Manually

### Step 1: Go to Repository Settings
Visit: https://github.com/TeamSnyder09/tool-body-tracker/settings/pages

### Step 2: Configure Build and Deployment
Under "Build and deployment" section:

1. **Source**: Select **"Deploy from a branch"**
2. **Branch**: Select **"main"**
3. **Folder**: Select **"/ (root)"**
4. Click **Save**

### Step 3: Wait for Deployment
- GitHub will automatically build and deploy the site
- This takes 1-2 minutes
- You'll see the live site URL in the Pages settings once complete

### Expected Result
Once enabled, the site will be available at:
- https://TeamSnyder09.github.io/tool-body-tracker

---

## Alternative: View Documentation Locally

If you want to see the documentation immediately without waiting for GitHub Pages:

```powershell
# Install MkDocs and dependencies
python -m pip install mkdocs mkdocs-material pymdown-extensions

# Navigate to project
cd "c:\Users\ksnyder\OneDrive - Winbro Group Technologies Limited\Desktop\New project"

# Build and serve
mkdocs serve

# Open in browser
# http://localhost:8000
```

---

## Troubleshooting

### Pages Still Not Working After Configuration
1. Verify the branch is set to "main"
2. Check that "Deploy from a branch" is selected
3. Clear your browser cache (Ctrl+Shift+Delete)
4. Wait 5 minutes as GitHub can take time to process

### Getting a 404 Error
- GitHub Pages may still be building
- Wait 2-3 minutes and refresh
- Check the Actions tab to see deployment status

### Need to Rebuild Docs
If you update documentation files:
1. Push changes to main branch
2. GitHub will automatically rebuild (if using workflows)
3. Changes appear on the site within 1-2 minutes

---

## Quick Links

- **Repository**: https://github.com/TeamSnyder09/tool-body-tracker
- **Settings**: https://github.com/TeamSnyder09/tool-body-tracker/settings/pages
- **Actions**: https://github.com/TeamSnyder09/tool-body-tracker/actions
- **Main Branch**: https://github.com/TeamSnyder09/tool-body-tracker/tree/main
