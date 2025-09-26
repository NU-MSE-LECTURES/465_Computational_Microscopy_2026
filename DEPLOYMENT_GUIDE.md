# GitHub Pages Deployment Guide

## Deploying the Course Website

Your GitHub Pages site is now ready for deployment! Here's how to activate it:

### 1. Enable GitHub Pages

1. Go to your repository: https://github.com/NU-MSE-LECTURES/465_Computational_Microscopy_2026
2. Click on **Settings** tab
3. Scroll down to **Pages** section in the left sidebar
4. Under **Source**, select:
   - **Deploy from a branch**
   - **Branch**: `dev` (since that's where your website files are)
   - **Folder**: `/ (root)`
5. Click **Save**

### 2. Access Your Site

Once enabled, your site will be available at:
```
https://nu-mse-lectures.github.io/465_Computational_Microscopy_2026/
```

It may take a few minutes for the site to build and become available.

### 3. Site Structure

Your website includes:

- **Homepage** (`index.md`): Course overview and highlights
- **Schedule** (`schedule.md`): Weekly breakdown with topics and deliverables
- **Assignments** (`assignments.md`): Assignment grid with evaluation criteria
- **Resources** (`resources.md`): Software, tools, documentation, and support

### 4. Customization

The site uses Jekyll with:
- Northwestern University branding colors (#4e2a84 purple)
- Responsive design for mobile and desktop
- Professional navigation and layout
- Interactive elements and hover effects

### 5. Updates

To update the website:
1. Make changes to the markdown files in your dev branch
2. Commit and push changes to GitHub
3. GitHub Pages will automatically rebuild the site

### 6. Local Testing (Optional)

To test the site locally before deployment:

```bash
# Install Jekyll (requires Ruby)
gem install bundler jekyll

# Create Gemfile
echo "source 'https://rubygems.org'" > Gemfile
echo "gem 'github-pages', group: :jekyll_plugins" >> Gemfile

# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# View at http://localhost:4000
```

## Next Steps

1. **Deploy the site** following the steps above
2. **Test all pages** to ensure proper functionality
3. **Continue developing** weekly materials (Weeks 3-10)
4. **Share the URL** with students once ready

Your comprehensive course website is now ready to go live!