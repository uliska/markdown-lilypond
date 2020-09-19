import re
from markdown_lilypond.syntax import LilyPondSyntax

class AbstractMarkdownDocument(object):

    def __init__(self, text):
        self._text = text

    def highlight(self):
        b = self.block_class(self.text())
        while b.has_match():
            b.colorize()
            self.set_text(b.text())
            b = self.block_class(self.text())

    def set_text(self, text):
        self._text = text

    def text(self):
        return self._text
