from markdown_lilypond.document import AbstractMarkdownDocument
from .block import MkDocsLilyPondBlock

class MkDocsMarkdownDocument(AbstractMarkdownDocument):

    block_class = MkDocsLilyPondBlock
