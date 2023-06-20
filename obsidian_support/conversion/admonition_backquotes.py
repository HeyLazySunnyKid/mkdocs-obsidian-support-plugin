from obsidian_support.abstract_conversion import AbstractConversion, SyntaxGroup
from mkdocs.structure.pages import Page

"""
a strategy that convert [obsidian callout](https://help.obsidian.md/Editing+and+formatting/Callouts)
to [mkdocs-material admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
"""

# OBSIDIAN_CALL_OUT_REGEX = "\n ?> ?\\[!(?P<type>[a-z]+)\\](?P<title> .*)?(?P<lines>(\n ?>.*)*)"
#  OBSIDIAN_CALL_OUT_REGEX = "\n```(?P<type>[a-z]+)\\]\n(title: (?P<title> .*))?\n(?P<lines>(.*\n))```"
# OBSIDIAN_CALL_OUT_REGEX = "\n```\\[(?P<type>[a-z]+)\\]```"
OBSIDIAN_CALL_OUT_REGEX = "\n>>>(?P<type>[a-z]+)\\]>>>"
#  OBSIDIAN_CALL_OUT_REGEX_GROUPS = ['type', 'title', 'lines']
OBSIDIAN_CALL_OUT_REGEX_GROUPS = ['type']


class AdmonitionBackquotesConvert(AbstractConversion):
    def __init__(self):
        super().__init__(OBSIDIAN_CALL_OUT_REGEX, OBSIDIAN_CALL_OUT_REGEX_GROUPS)
        with open("log.txt", "w+") as file:
            file.write('DEBUG init DEBUG')

    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        with open("log.txt", "w+") as file:
            file.write('DEBUG convert DEBUG')
        return create_admonition(*syntax_groups)


def create_admonition(ad_type: str) -> str:
    #  if title is None:
    with open("log.txt", "w+") as file:
        file.write('DEBUG on_page_markdown DEBUG')
    title = "adfadsfasd"

    #  if lines is None:
    lines = "test test"

    admonition = "\n!!! " + ad_type + title + "\n" + lines
    return admonition
