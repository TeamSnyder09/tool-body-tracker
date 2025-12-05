# GitHub Pages Deployment Guide

This project is configured for automatic deployment to GitHub Pages.

## Deployment Status

- **Repository**: https://github.com/TeamSnyder09/tool-body-tracker
- **Website**: https://TeamSnyder09.github.io/tool-body-tracker
- **Documentation**: Built with MkDocs and Material theme

## Setup Instructions

### 1. Add Workflow File to Repository

1. Go to `.github/workflows/` directory in your repository
2. Create a new file named `deploy.yml` with the following content:

```yaml
name: Deploy Documentation to GitHub Pages

on:
  push:
    branches:
      - main
    paths:
      - 'docs/**'
      - 'mkdocs.yml'
      - '.github/workflows/deploy.yml'

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pages: write
      id-token: write

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install mkdocs mkdocs-material pymdown-extensions

      - name: Build documentation
        run: mkdocs build

      - name: Setup Pages
        uses: actions/configure-pages@v3

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: 'site'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

### 2. Enable GitHub Pages

1. Go to your GitHub repository
2. Navigate to **Settings** → **Pages**
3. Under "Build and deployment":
   - **Source**: Select "GitHub Actions"
   - This allows automatic deployment from the workflow

### 3. Configure Repository

Ensure your repository has:
- `mkdocs.yml` - MkDocs configuration (already present)
- `docs/` directory with documentation files (already present)
- `.github/workflows/deploy.yml` - GitHub Actions workflow

### 4. Trigger Deployment

The documentation will be automatically deployed when:
- Changes are pushed to the `main` branch
- Changes affect:
  - `docs/**` (any files in docs directory)
  - `mkdocs.yml`
  - `.github/workflows/deploy.yml`

## Accessing the Documentation

Once deployed, the documentation will be available at:
- **Main Site**: https://TeamSnyder09.github.io/tool-body-tracker/

## Local Documentation Build

To build and preview documentation locally:

### Prerequisites
```bash
pip install mkdocs mkdocs-material pymdown-extensions
```

### Build
```bash
mkdocs build
```

This creates a `site/` directory with the built documentation.

### Preview
```bash
mkdocs serve
```

Open http://localhost:8000 in your browser.

## Documentation Structure

```
docs/
├── index.md           # Home page
├── installation.md    # Installation guide
├── usage.md          # Usage guide
├── api.md            # API reference
└── contributing.md   # Contributing guidelines
```

## Customization

### Update Site Name
Edit `mkdocs.yml`:
```yaml
site_name: Tool Body Tracker
site_description: A program to track tool body time installed on machines
```

### Change Theme Colors
Edit `mkdocs.yml` theme section:
```yaml
theme:
  palette:
    - scheme: default
      primary: blue
      accent: orange
```

### Add New Pages
1. Create a new `.md` file in `docs/`
2. Add it to `mkdocs.yml` under `nav:`

## Troubleshooting

### Documentation Not Updating
- Check GitHub Actions tab for workflow errors
- Verify `.github/workflows/deploy.yml` is in the repository
- Ensure changes are pushed to `main` branch

### Build Failures
- Check Python version (requires 3.11+)
- Verify all dependencies are installed
- Review workflow logs in GitHub Actions

### Pages Not Available
- Verify GitHub Pages is enabled in repository settings
- Check that source is set to "GitHub Actions"
- Allow 1-2 minutes for deployment to complete

## Additional Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
