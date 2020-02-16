import re

from lilypond_plugin.syntax import LilyPondSyntax

class AbstractLilyPondBlock(object):

    """
    Returns a match object segmenting the document by the first
    fenced lilypond block.

    The match will have four groups:
    - Beginning of the document up to the fenced block
    - Remainder of the start line (empty if no options are present)
    - The LilyPond input code
    - Remainder of the document after the closing line of the block

    If no block is found None is returned."
    """

    # Regular expression to find the first/next
    # fenced lilypond block.
    fenced_block_re = re.compile(
        '(.*?)```lilypond(.*?)\n(.*?)```\n(.*)',
        flags=re.DOTALL
    )

    def __init__(self, text):
        self._text = text
        self._start = None
        self._options = None
        self._lilypond_text = None
        self._remainder = None
        self._match = m = self.fenced_block_re.match(text)
        if m:
            self._start = m.group(1)
            self._options = m.group(2)
            self._lilypond_text = m.group(3)
            self._remainder = m.group(4)
        self._syntax = LilyPondSyntax()

    def colorize(self):
        self.set_lilypond(self._syntax.colorize(self.lilypond_text()))

    def has_match(self):
        return self._match is not None

    def lilypond_text(self):
        return self._lilypond_text

    def set_lilypond(self, text):
        self._lilypond_text = text

    def text(self):
        return """{start}
{lilypond}
{remainder}
""".format(
    start=self._start,
    lilypond=self._lilypond_text,
    remainder=self._remainder
)
