import re
import os
import sys
from mkdocs.plugins import BasePlugin

# Add the repository root to the Python path, so the global
# modules (that are not specific to a given plugin) can be
# reached from all sources.
sys.path.insert(1, os.path.realpath(os.path.join(os.getcwd(), '..')))
from .markdown_document import MkDocsMarkdownDocument

class LilyPond(BasePlugin):

    def on_page_markdown(self, markdown, **kwargs):

        doc = MkDocsMarkdownDocument(markdown)
        doc.highlight()
        return doc.text()
