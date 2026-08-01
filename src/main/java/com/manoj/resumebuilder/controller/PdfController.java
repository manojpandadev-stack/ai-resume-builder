package com.manoj.resumebuilder.controller;



import com.lowagie.text.DocumentException;
import com.manoj.resumebuilder.dto.request.AiTextRequest;
import com.manoj.resumebuilder.pdf.PdfService;
import jakarta.validation.Valid;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/pdf")
@CrossOrigin(origins = "http://localhost:3000")
public class PdfController {

    private final PdfService pdfService;

    public PdfController(PdfService pdfService) {
        this.pdfService = pdfService;
    }

    @PostMapping("/download")
    public ResponseEntity<byte[]> downloadPdf(@Valid @RequestBody AiTextRequest request)
            throws DocumentException {

        byte[] pdf = pdfService.generateResumePdf(request.getContent());

        return ResponseEntity.ok()
                .header(HttpHeaders.CONTENT_DISPOSITION,
                        "attachment; filename=resume.pdf")
                .contentType(MediaType.APPLICATION_PDF)
                .body(pdf);
    }
}
