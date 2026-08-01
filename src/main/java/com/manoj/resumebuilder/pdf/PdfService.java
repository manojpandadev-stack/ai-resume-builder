package com.manoj.resumebuilder.pdf;


import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfWriter;
import org.springframework.stereotype.Service;

import java.io.ByteArrayOutputStream;

@Service
public class PdfService {

    public byte[] generateResumePdf(String resume) throws DocumentException {

        Document document = new Document();
        ByteArrayOutputStream out = new ByteArrayOutputStream();

        PdfWriter.getInstance(document, out);

        document.open();

        document.add(new Paragraph("AI Generated Resume"));
        document.add(new Paragraph(" "));
        document.add(new Paragraph(resume));

        document.close();

        return out.toByteArray();
    }
}