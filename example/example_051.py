from borb.io.read.types import Name, String, Dictionary
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


def main():
    doc: Document = Document()
    page: Page = Page()
    doc.append_page(page)

    layout: PageLayout = SingleColumnLayout(page)
    layout.add(
        Paragraph(
            """
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                         """
        )
    )

    # set the /Info dictionary
    doc["XRef"]["Trailer"][Name("Info")] = Dictionary()

    # set the /Author
    doc["XRef"]["Trailer"]["Info"][Name("Author")] = String("Joris Schellekens")

    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
