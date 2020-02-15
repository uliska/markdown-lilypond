import re
from mkdocs.plugins import BasePlugin

from .syntax import LilyPondSyntax

class LilyPond(BasePlugin):

    fenced_block_re = re.compile(
        '(```lilypond)(.*?)(```)',
        flags=re.DOTALL
    )

    def __init__(self):
        self._syntax = LilyPondSyntax()

    def on_page_markdown(self, markdown, **kwargs):

        return self.fenced_block_re.sub(
            self._syntax.colorize,
            markdown
        )
