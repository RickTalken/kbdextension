# KBD Extension for Python-Markdown

This [Python-Markdown](https://python-markdown.github.io/) extension adds markdown syntax for the HTML `<kbd>` tag.  The `<kbd>` tag is typically used to indicate user input.  This extension provides markdown syntax for up to three different styled `<kbd>` tags.  For example, the author of a guide to using a UI might want to style `<kbd>` tags to indicate user input via keyboard keys, buttons, and menu choices.  The KBD Extension makes it possible for the author to create css specific for each type of user input and use markdown syntax to style their guide accordingly.

See [Usage](#usage) for more information.

## Installation
```
pip install git+git://github.com/ricktalken/kbdextension.git
```

## Usage
The KBD Extension is an inline processor for adding markdown syntax for inline `<kbd>` tags.  Text wrapped in double brackets, double braces, or double parenthesis will be wrapped with an HTML `<kbd>` tag.  The KBD extension was designed to work with Python-Markdown default extensions. The KBD Extension markdown indicators can be individually enabled or disabled if conflicts are encountered when paired with other 3rd party extensions.  Brackets are enabled by default (but can be disabled).  Braces and parenthesis are disabled by default (but can be individually enabled).  By default, the page's default css implementation will be applied to the `<kbd>` tag(s).  The KBD extension can be confugured to use custom css for each of the KBD markdown indicators.

### Brackets Markdown
```python
markdown.markdown("Press the [[Enter]] key!", extensions=[KbdExtension()])
```
The bracket syntax is enabled by default.  This will produce the following HTML:
```html
<p>Press the <kbd>Enter</kbd> key!</p>
```
Custom css classes can be applied to `<kbd>` tags produced by brackets markdown.
```python
markdown.markdown(
    "Press the [[Enter]] key!", 
    extensions=[KbdExtension(brackets_css="bracket_css")]
)
```
This will produce the following HTML:
```html
<p>Press the <kbd class="bracket_css">Enter</kbd> key!</p>
```
### Braces Markdown
Braces markdown is disabled by default.  It can be enabled by setting `enable_braces` to `True` in the constructor.
```python
markdown.markdown(
    "Click the {{Search}} button!", 
    extensions=[KbdExtension(enable_braces=True)]
)
```
This will produce the following HTML:
```html
<p>Click the <kbd>Search</kbd> button!</p>
```
As with bracket syntax, custom css classes can be applied to `<kbd>` tags produced by braces markdown.
```python
markdown.markdown(
    "Click the {{Search}} button!",
    extensions=[KbdExtension(enable_braces=True, braces_css="braces-css")],
)
```
This will produce the following HTML:
```html
<p>Click the <kbd class="braces-css">Search</kbd> button!</p>
```
### Parenthesis Markdown
Parenthesis markdown is disabled by default.  It can be enabled by setting `enable_parens` to `True` in the constructor.
```python
markdown.markdown(
    "Click the ((File)) menu!", 
    extensions=[KbdExtension(enable_parens=True)]
)
```
This will produce the following HTML:
```html
<p>Click the <kbd>File</kbd> menu!</p>
```
As with bracket syntax, custom css classes can be applied to `<kbd>` tags produced by parenthesis markdown.
```python
markdown.markdown(
    "Click the ((File)) menu!",
    extensions=[KbdExtension(enable_parens=True, parens_css="parens-css")],
)
```
This will produce the following HTML:
```html
<p>Click the <kbd class="parens-css">File</kbd> menu!</p>
```

## MkDocs Configuration
The KBD Extension can be configured for use with [MkDocs](https://www.mkdocs.org/).  This extension provides configuration options of its own as described in the [usage notes](#usage) above. Configuration options are nested in a key/value mapping in the `markdown_extensions:` section of the `mkdocs.yml` configuration file.  Example configurations for this extension are provided below.  For more on configuring markdown extensions in MkDocs, refer to [MkDocs configuration documentation](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions).

### Default Configuration
The default configuration enables bracket syntax only.
```yaml
markdown_extensions:
    - kbdextension
```
### Partial Configuration
This partial configuration disables the brackets markdown indicator and enables the braces markdown indicator with a custom css class for the `<kbd>` tag that it renders.
```yaml
extra_css:
    - css/extra.css
markdown_extensions:
    - kbdextension
        enable_brackets: false
        enable_braces: true
        braces_css: braces_kbd_css
```
### Full Configuration
A full configuration enables brackets, braces, and parenthesis markdown indicators along with custom css for each.  Note that brackets are enabled by default so it is not necessary to set the `enable_brackets` configuration to `true`.
```yaml
extra_css:
    - css/extra.css
markdown_extensions:
    - kbdextension
        brackets_css: brackets_kbd_css
        enable_braces: true
        braces_css: braces_kbd_css
        enable_parens: true
        parens_css: parens_kbd_css
```
For more on configuring custom css in MkDocs, refer to [MkDocs configuration documentation](https://www.mkdocs.org/user-guide/configuration/#extra_css).

## License
This software is provided under the MIT License. See [LICENSE](LICENSE.md) for details.