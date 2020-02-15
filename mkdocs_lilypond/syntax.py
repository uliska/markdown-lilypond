from mkdocs.plugins import BasePlugin

class LilyPondSyntax(BasePlugin):

    def on_page_markdown(self, markdown, **kwargs):
        return "LilyPond\n\n" + markdown