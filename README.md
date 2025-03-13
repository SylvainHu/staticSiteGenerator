# Static Site Generator

A flexible static site generator built from scratch using JavaScript that converts Markdown files into a fully-functional website.

## Features

- Converts Markdown files to HTML
- Supports front matter for page metadata
- Handles internal links between pages
- Includes a built-in development server
- Automatically builds navigation based on file structure
- Supports customizable theming via CSS

## How It Works

This generator takes a directory of Markdown files and processes them into HTML pages. It parses front matter, processes Markdown content, and assembles everything into a cohesive site structure.

## Getting Started

```bash
# Clone the repository
git clone https://github.com/SylvainHu/staticSiteGenerator.git

# Navigate to the project
cd static-site-generator

# Install dependencies
npm install

# Run the development server
npm run dev

# Build for production
npm run build