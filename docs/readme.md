# Documentation

This project uses `mdBook` to generate and host its documentation. `mdBook` is a utility for creating modern books and documentation websites from a collection of Markdown files.

How it works:

- You write content in Markdown files inside the `docs` directory.
- `mdBook` reads the book configuration and chapter structure.
- It converts the Markdown into a static website with navigation, search, and styling.

In this repository, the `mdBook` setup is used specifically for the project documentation. The generated site provides a structured, easy-to-read presentation of the project's methods, results, and supporting materials.

The `SUMMARY.md` file defines the structure and navigation of the book. It lists chapters and sections in Markdown format, and `mdBook` uses it to build the sidebar and page order. Each entry in `SUMMARY.md` points to a Markdown file in the `docs` directory, so organizing or renaming files is reflected automatically in the documentation site.

Basic `mdBook` commands:

- `mdbook init` - initialize a new book in the current directory.
- `mdbook build` - compile the Markdown files into a static website in `book/`.
- `mdbook serve` - start a local web server and preview the book in a browser, default at `:3000`.
- `mdbook test` - check the book for broken links and structural issues.

Use these commands from the `docs` directory to build, preview, and validate the project documentation.
