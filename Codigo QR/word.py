from docx import Document

def create_word_document_with_qr_code(qr_code_image_path, output_docx_path):
    # Create a new Word document
    doc = Document()

    # Add a title to the document
    doc.add_heading('Imagen QR de Tecmilenio', level=1)

    # Add the QR code image to the document
    doc.add_picture(qr_code_image_path)  # Adjust the width as needed

    # Save the document to the specified output path
    doc.save(output_docx_path)

create_word_document_with_qr_code('codigo_qr.png', 'ejemplo2.docx')
print("Word document created successfully with the QR code image.")
