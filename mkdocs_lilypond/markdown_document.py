from lilypond_plugin.markdown_document import AbstractMarkdownDocument
from .block import MkDocsLilyPondBlock

class MkDocsMarkdownDocument(AbstractMarkdownDocument):

    block_class = MkDocsLilyPondBlock
