# markdown-lilypond

Tools to support LilyPond (code|scores) in Markdown files.

Includes the `markdown_lilypond` Python(3) module and the `lilypond` MkDocs plugin.
The separation into a dedicated plugin and a generic LilyPond package should make
it possible to add other plugins at some later point, first of all a Pandoc filter.

*NOTE:* This is a very preliminary "initial commit"-like repository.

---

This plugin provides support for LilyPond input in Markdown files processed with
[MkDocs](https://www.mkdocs.org). If it is installed and activated fenced code blocks
with the `lilypond` language are highlighted using the
[python-ly](https://github.com/frescobaldi/python-ly) package which powers the
[Frescobaldi](http://frescobaldi.org) IDE.

At this point syntax highlighting without any configuration is all the plugin
provides. There will be further options, and hopefully the possibility to actually 
*use* LilyPond to produce musical scores, but that is out of scope right now.

### Installation

Until we consider uploading this to PyPi the plugin may only be installed from the 
GitHub repository, either by issuing

```
(sudo) pip3 install git+https://github.com/uliska/lilypond-markdown.git
```

or - from within a download directory

```
(sudo) pip3 install -e .
```

The latter is preferable if you want to contribute to the plugin. In this case the
install command has to be repeated after any modification. However, it seems that
dependencies are *not* automatically installed this way, so you'll have to install
the `mkdocs` and `python-ly` packages separately.

Using `sudo` or not is probably a matter of personal taste; however, it is crucial
to stick to one approach across the board to ensure everything works together.

### Usage

In a MkDocs `mkdocs.yml` file, simply add

```yaml
plugins:
  - search
  - lilypond
```

> *NOTE:* Adding a `plugins` section will deactivate the default `search` plugin,
> so you will probably want to add it manually.

Now your rendered site will have highlighted LilyPond input automatically.
