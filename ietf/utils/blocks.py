from wagtail.blocks import (
    CharBlock,
    FloatBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
)
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.contrib.typed_table_block.blocks import TypedTableBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailmarkdown.blocks import MarkdownBlock


class StandardBlock(StreamBlock):
    heading = CharBlock(icon="title")
    paragraph = RichTextBlock(icon="pilcrow")
    image = ImageChooserBlock(icon="image", template="includes/imageblock.html")
    markdown = MarkdownBlock(icon="code")
    embed = EmbedBlock(icon="code")
    raw_html = RawHTMLBlock(icon="placeholder")
    table = TableBlock(
        table_options={"renderer": "html"}, template="includes/tableblock.html"
    )
    typed_table = TypedTableBlock(
        [
            ("text", CharBlock()),
            ("numeric", FloatBlock()),
            ("rich_text", RichTextBlock()),
            ("image", ImageChooserBlock()),
        ]
    )
