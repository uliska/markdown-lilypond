import ly
from ly import document, colorize


class LilyPondSyntax(object):

    def colorize(self, ly_code):
        doc = ly.document.Document(ly_code)
        w = ly.colorize.HtmlWriter()
        w.full_html = False
        w.inline_style = True
        w.set_wrapper_tag('pre')
        w.wrapper_attribute = 'class'
        return w.html(ly.document.Cursor(doc))
