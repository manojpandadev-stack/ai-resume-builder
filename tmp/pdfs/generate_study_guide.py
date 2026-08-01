from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageBreak, PageTemplate, Paragraph,
    Preformatted, Spacer, Table, TableStyle
)

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "output" / "pdf" / "AI_Resume_Builder_Study_Guide.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

NAVY = colors.HexColor("#0B1F3A")
BLUE = colors.HexColor("#1F5A99")
TEAL = colors.HexColor("#0E7490")
GRAY = colors.HexColor("#56616F")
PALE_BLUE = colors.HexColor("#EAF3FB")
PALE_TEAL = colors.HexColor("#E8F6F7")
PALE_ORANGE = colors.HexColor("#FFF7ED")
PALE_RED = colors.HexColor("#FEF2F2")
PALE_GRAY = colors.HexColor("#F3F5F7")


class GuideDocument(BaseDocTemplate):
    def __init__(self, file_name):
        super().__init__(
            file_name, pagesize=A4, leftMargin=1.55 * cm, rightMargin=1.55 * cm,
            topMargin=1.75 * cm, bottomMargin=1.55 * cm,
            title="AI Resume Builder Study Guide", author="Codex"
        )
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="body")
        self.addPageTemplates([PageTemplate(id="guide", frames=[frame], onPage=self.header_footer)])

    @staticmethod
    def header_footer(canvas, doc):
        canvas.saveState()
        width, height = A4
        if doc.page > 1:
            canvas.setStrokeColor(colors.HexColor("#CBD5E1"))
            canvas.line(1.55 * cm, height - 1.15 * cm, width - 1.55 * cm, height - 1.15 * cm)
            canvas.line(1.55 * cm, 1.05 * cm, width - 1.55 * cm, 1.05 * cm)
            canvas.setFillColor(GRAY)
            canvas.setFont("Helvetica", 8.1)
            canvas.drawString(1.55 * cm, height - 0.85 * cm, "AI Resume Builder - Technical Study Guide")
            canvas.drawRightString(width - 1.55 * cm, height - 0.85 * cm, "Project-based learning notes")
            canvas.drawString(1.55 * cm, 0.72 * cm, "React + Spring Boot + MySQL + Spring AI")
            canvas.drawRightString(width - 1.55 * cm, 0.72 * cm, f"Page {doc.page}")
        canvas.restoreState()


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=27, leading=32, alignment=TA_CENTER, textColor=NAVY, spaceAfter=12
))
styles.add(ParagraphStyle(
    name="CoverSub", parent=styles["Normal"], fontName="Helvetica",
    fontSize=12.5, leading=18, alignment=TA_CENTER, textColor=GRAY
))
styles.add(ParagraphStyle(
    name="Heading1X", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=18, leading=23, textColor=NAVY, spaceBefore=12, spaceAfter=9, keepWithNext=True
))
styles.add(ParagraphStyle(
    name="Heading2X", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=12.4, leading=16, textColor=BLUE, spaceBefore=10, spaceAfter=5, keepWithNext=True
))
styles.add(ParagraphStyle(
    name="BodyX", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=9.35, leading=13.9, alignment=TA_JUSTIFY,
    textColor=colors.HexColor("#1F2937"), spaceAfter=7
))
styles.add(ParagraphStyle(
    name="CalloutX", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=9.1, leading=13.2, textColor=colors.HexColor("#1F2937"), spaceAfter=0
))
styles.add(ParagraphStyle(
    name="TableHeadX", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=8.1, leading=10, textColor=colors.white, spaceAfter=0
))
styles.add(ParagraphStyle(
    name="TableCellX", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=7.8, leading=10.15, textColor=colors.HexColor("#1F2937"), spaceAfter=0
))
styles.add(ParagraphStyle(
    name="CodeX", fontName="Courier", fontSize=7.25, leading=9.2,
    textColor=colors.HexColor("#172554"), backColor=colors.HexColor("#F8FAFC"),
    borderColor=colors.HexColor("#CBD5E1"), borderWidth=0.45,
    borderPadding=7, spaceBefore=3, spaceAfter=8
))


def paragraph(text, style="BodyX"):
    return Paragraph(text, styles[style])


def h1(text):
    return paragraph(text, "Heading1X")


def h2(text):
    return paragraph(text, "Heading2X")


def bullet(text):
    return paragraph("&bull; " + text)


def code(text):
    return Preformatted(text.strip(), styles["CodeX"])


def note(label, text, tone="blue"):
    palette = {
        "blue": (PALE_BLUE, BLUE), "teal": (PALE_TEAL, TEAL),
        "warn": (PALE_ORANGE, colors.HexColor("#C2410C")),
        "red": (PALE_RED, colors.HexColor("#B91C1C")),
    }
    background, border = palette[tone]
    cell = paragraph("<b>" + escape(label) + ":</b> " + escape(text), "CalloutX")
    table = Table([[cell]], colWidths=[17.8 * cm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), background),
        ("BOX", (0, 0), (-1, -1), 0.7, border),
        ("LINEBEFORE", (0, 0), (0, 0), 3.0, border),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return table


def grid(headers, rows, widths):
    data = [[paragraph(escape(header), "TableHeadX") for header in headers]]
    for row in rows:
        data.append([paragraph(escape(str(value)), "TableCellX") for value in row])
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#CBD5E1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE_GRAY]),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return table


def add_bullets(story, items):
    story.extend(bullet(item) for item in items)


def build_story():
    s = []

    # Cover and study map
    s += [
        Spacer(1, 3.1 * cm),
        paragraph("AI Resume Builder", "CoverTitle"),
        paragraph(
            "A rigorous technical study guide for interviews, demonstrations, and deeper software-engineering understanding",
            "CoverSub"
        ),
        Spacer(1, 1.2 * cm),
        note(
            "System in one sentence",
            "A React application sends candidate information to a Spring Boot API that generates resumes, ATS feedback, cover letters, stored resume records, and PDF downloads.",
            "teal"
        ),
        Spacer(1, 0.5 * cm),
        grid(
            ["Layer", "Technology", "Reason it exists"],
            [
                ["Presentation", "React 19, Bootstrap, Axios", "Captures inputs, manages UI state, calls APIs, and downloads files."],
                ["Application", "Spring Boot 3, Java 21", "Exposes REST endpoints and organizes use cases."],
                ["Persistence", "Spring Data JPA, MySQL", "Maps resume data to relational records and supports CRUD."],
                ["AI", "Spring AI, Groq OpenAI-compatible API, Llama model", "Creates resume text, feedback, and cover letters."],
                ["Export", "OpenPDF", "Creates PDF bytes delivered to the browser."],
            ],
            [2.7 * cm, 5.4 * cm, 9.7 * cm]
        ),
        Spacer(1, 0.9 * cm),
        paragraph("Prepared from the project source. No credentials are reproduced in this guide.", "CoverSub"),
        PageBreak(),

        h1("How to use this guide"),
        paragraph(
            "This guide explains what the current project does, why its parts exist, and how to describe it at an advanced level. Study it once in order. Then revisit the architecture, risks, and interview sections until you can trace any user action from the browser to the backend and back."
        ),
        h2("Learning outcomes"),
    ]
    add_bullets(s, [
        "Explain the complete request flow from a React form submission to an AI response or a downloaded PDF.",
        "Distinguish controller, service, repository, entity, and DTO responsibilities in Spring Boot.",
        "Describe prompts, model integration, CORS, HTTP file delivery, and database persistence.",
        "Identify limitations in the code without overstating features that do not yet exist.",
        "Propose security, reliability, and product improvements appropriate for production.",
    ])
    s += [
        h2("Guide map"),
        grid(
            ["Part", "Focus", "Core question"],
            [
                ["1", "System model", "What does the application do and how do the pieces communicate?"],
                ["2", "React frontend", "How are inputs, asynchronous calls, and downloads handled?"],
                ["3", "Spring Boot", "How are endpoints and application layers structured?"],
                ["4", "Data and AI", "How are data models, persistence, prompts, and LLM output handled?"],
                ["5", "Documents and integration", "How do PDF export, CORS, validation, and errors work?"],
                ["6", "Production thinking", "How would you secure, test, deploy, and improve the project?"],
                ["7", "Interview preparation", "How should you present the project with technical confidence?"],
            ],
            [1.1 * cm, 4.6 * cm, 12.1 * cm]
        ),
        Spacer(1, 0.3 * cm),
        note(
            "Important mindset",
            "A strong answer explains the existing implementation and then identifies a precise improvement. Do not claim that a planned feature is already present.",
            "warn"
        ),
    ]

    # Architecture
    s += [
        h1("1. System model and request lifecycle"),
        paragraph(
            "The application is a client-server system. The browser hosts a React single-page interface. React sends HTTP requests to a Java Spring Boot API. The backend handles deterministic operations such as persistence and PDF generation, and probabilistic operations such as drafting a resume with a language model. MySQL is used to persist structured resume records."
        ),
        h2("End-to-end flow"),
        grid(
            ["Step", "Component", "Action", "Output"],
            [
                ["1", "Candidate", "Completes name, contact, education, skills, experience, and projects.", "Structured input."],
                ["2", "React App", "Stores input in state and sends Axios requests.", "HTTP request to port 8080."],
                ["3", "Controller", "Maps endpoint and request body to a use case.", "Service call."],
                ["4", "Service", "Builds prompt, uses repository, or creates PDF.", "Text, record, or byte array."],
                ["5", "Provider or database", "LLM writes content; MySQL stores data; OpenPDF renders document.", "Response payload."],
                ["6", "React App", "Updates screen state or downloads a Blob.", "Visible text or resume.pdf."],
            ],
            [1.0 * cm, 3.1 * cm, 8.2 * cm, 5.5 * cm]
        ),
        h2("Main user journeys"),
    ]
    add_bullets(s, [
        "Generate resume: form data -> POST /ai/generate -> prompt -> model -> generated text in the resume panel.",
        "Analyze resume: generated text -> POST /ai/analyze as text/plain -> analysis prompt -> model -> ATS report panel.",
        "Generate cover letter: form data -> POST /ai/cover-letter -> focused prompt -> model -> cover-letter panel.",
        "Download PDF: generated text -> POST /pdf/download as text/plain -> OpenPDF -> binary response -> browser download.",
    ])
    s += [
        note(
            "Key distinction",
            "AI endpoints produce non-deterministic text. The PDF endpoint does not call the model; it deterministically turns supplied text into a document.",
            "blue"
        ),
    ]

    # Frontend
    s += [
        h1("2. Frontend engineering: React state and HTTP"),
        paragraph(
            "The frontend uses a React functional component with hooks. Form data lives in one state object, and each AI output has its own state variable. This is a practical shape for a compact form because the complete data object can be sent in one request."
        ),
        h2("State model"),
        code("""
const [form, setForm] = useState({
  name: "", email: "", phone: "", education: "",
  skills: "", experience: "", projects: ""
});
const [resume, setResume] = useState("");
const [analysis, setAnalysis] = useState("");
const [coverLetter, setCoverLetter] = useState("");
const [loading, setLoading] = useState(false);
        """),
        paragraph(
            "The form state represents what the candidate enters. Resume, analysis, and coverLetter represent results from separate API use cases. The loading flag prevents repeated actions while a call is in progress. This matters because language-model requests are slower and less predictable than a local calculation."
        ),
        h2("Generic change handler"),
        code("""
const handleChange = (e) => {
  setForm({
    ...form,
    [e.target.name]: e.target.value,
  });
};
        """),
        paragraph(
            "The spread operator makes a new object and the computed property name updates only the field identified by the input name. This avoids mutating existing state and enables React to rerender reliably."
        ),
        h2("Controlled input observation"),
        paragraph(
            "The email field is explicitly controlled with value={form.email}, whereas several other inputs only provide onChange. Both can capture values, but a consistent controlled approach is easier to reset, validate, prefill, and test. A refinement should bind every input's value to its corresponding form property."
        ),
        h1("2.1 Async calls and browser file downloads"),
        h2("Generating a resume"),
        code("""
const response = await axios.post(
  "http://localhost:8080/ai/generate",
  form
);
setResume(response.data);
        """),
        paragraph(
            "Axios serializes the form object as JSON. Spring Boot deserializes it into ResumeRequest. The model returns plain text, so the frontend receives it in response.data and stores it in resume state. The try/catch/finally pattern should always reset loading, regardless of success or failure."
        ),
        h2("Why plain text endpoints set Content-Type"),
        paragraph(
            "The analysis and PDF endpoints receive the generated resume itself, not a JSON object. The browser therefore sends Content-Type: text/plain. This communicates the body format to Spring's request handling layer and prevents accidental JSON parsing assumptions."
        ),
        h2("Binary PDF workflow"),
        code("""
const response = await axios.post(
  "http://localhost:8080/pdf/download",
  resume,
  { headers: { "Content-Type": "text/plain" }, responseType: "blob" }
);
const url = window.URL.createObjectURL(response.data);
        """),
        paragraph(
            "A PDF is binary data. responseType: blob stops Axios from parsing it as text or JSON. The application creates an in-memory object URL, gives it to a temporary anchor element, triggers a click, removes the element, and revokes the URL to release browser memory."
        ),
        note(
            "Interview phrasing",
            "The application handles AI output as normal text state, but handles a PDF as binary data. That difference is why the client uses a Blob response type for file downloads.",
            "teal"
        ),
    ]

    # Backend layers
    s += [
        h1("3. Backend engineering: layered Spring Boot design"),
        paragraph(
            "Spring Boot is organized into layers because HTTP concerns, business rules, database access, and data representation evolve differently. Controllers define the web contract. Services implement application use cases. Repositories abstract persistence. Entities describe stored domain data. DTOs describe API payloads."
        ),
        grid(
            ["Layer", "Project classes", "Primary responsibility", "Avoid putting here"],
            [
                ["Controller", "AIController, ResumeController, PdfController", "Map paths and methods; parse input; return HTTP responses.", "Complex business or database logic."],
                ["Service", "AIService, ResumeService, PdfService", "Run use cases and coordinate dependencies.", "Frontend-specific rendering state."],
                ["Repository", "ResumeRepository", "Read and write Resume entities via JPA.", "Prompts or document formatting."],
                ["Entity", "Resume", "Map persisted resume fields to a database table.", "A general-purpose API contract."],
                ["DTO", "ResumeRequest", "Carry AI-generation input including projects.", "Persistence identity and database rules."],
            ],
            [2.1 * cm, 4.1 * cm, 6.2 * cm, 5.4 * cm]
        ),
        h2("REST mappings"),
        paragraph(
            "AIController is rooted at /ai, making its generation method POST /ai/generate. Its analysis and cover-letter methods become POST /ai/analyze and POST /ai/cover-letter. PdfController exposes POST /pdf/download. ResumeController exposes POST /resume, GET /resume, PUT /resume/{id}, and DELETE /resume/{id}."
        ),
        h2("Dependency injection"),
        paragraph(
            "Spring creates application objects, known as beans, and injects required dependencies. The project uses @Autowired field injection in several classes. AIService uses constructor injection, which is preferable because its dependencies are explicit, can be final, and are easier to provide in tests."
        ),
        note(
            "Preferred refactor",
            "Use constructor injection consistently. It makes a class's requirements visible and avoids mutable injection fields.",
            "blue"
        ),
    ]

    # Data model
    s += [
        h1("4. Data model, DTOs, and MySQL persistence"),
        h2("The Resume entity"),
        paragraph(
            "Resume is marked with @Entity and mapped to the resume table. Its id uses GenerationType.IDENTITY, so the database creates unique primary-key values. The current persisted attributes are name, email, phone, skills, education, and experience."
        ),
        code("""
@Entity
@Table(name = "resume")
public class Resume {
  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;
  private String name;
  private String email;
  private String phone;
  private String skills;
  private String education;
  private String experience;
}
        """),
        h2("Why ResumeRequest is valuable"),
        paragraph(
            "The generation request contains a projects field, but the database entity does not. This is a concrete reason to separate API DTOs from entities: the contract required to generate a document is not necessarily identical to the data currently persisted in a table."
        ),
        h2("CRUD flow"),
        paragraph(
            "ResumeService calls repository.save to insert or update records and repository.findAll to list them. updateResume first loads an existing object with findById, copies selected properties, and saves it. deleteResume calls deleteById. JPA translates these operations into SQL."
        ),
        h2("Current data-model gaps"),
    ]
    add_bullets(s, [
        "Projects are used in AI prompts but are not stored on Resume or copied during update.",
        "There is no GET /resume/{id} endpoint for fetching one record.",
        "There are no validation constraints for required fields, email syntax, or input length.",
        "Missing ids are not converted into clear 404 responses.",
        "A future product may model repeated employment, education, and project records as ordered child entities.",
    ])
    s += [
        note(
            "Design principle",
            "Do not normalize a database just for formality. Use structured child tables when they enable better queries, consistency, revisions, or user-facing features.",
            "teal"
        ),
    ]

    # AI
    s += [
        h1("5. AI integration and prompt engineering"),
        paragraph(
            "AIService wraps Spring AI's ChatClient. It receives a prompt, sends it to the configured chat model, performs a synchronous call, and returns the content. The configuration points Spring AI at a Groq OpenAI-compatible endpoint using a Llama-family model."
        ),
        code("""
public String generateResume(String prompt) {
  return chatClient.prompt(prompt)
      .call()
      .content();
}
        """),
        h2("Prompt construction"),
        paragraph(
            "The controller combines a task instruction with labeled candidate details. Resume generation asks for an ATS-friendly resume. Resume analysis asks for an ATS score, missing skills, grammar suggestions, improvements, and overall feedback. Cover-letter generation currently targets a Java Spring Boot Developer position."
        ),
        grid(
            ["Prompt element", "Current purpose", "Stronger version"],
            [
                ["Task instruction", "Tells the model to generate or analyze.", "Specify seniority, tone, output sections, and constraints."],
                ["Candidate fields", "Gives facts to base output on.", "Validate fields and show omitted values clearly."],
                ["ATS direction", "Guides screening-focused language.", "Include a target job description and requested keywords."],
                ["Analysis list", "Encourages separate feedback topics.", "Require JSON for reliable interface rendering."],
                ["Fixed role", "Makes the cover-letter demo focused.", "Accept title, company, and job description dynamically."],
            ],
            [3.6 * cm, 6.4 * cm, 7.8 * cm]
        ),
        h2("Hallucination and factual accuracy"),
        paragraph(
            "A language model predicts plausible text, not verified facts. It may invent metrics, credentials, employers, or skills. The system should treat generation as a draft based on user-supplied facts. Users must review every claim before submitting the resume."
        ),
        note(
            "Strong engineering statement",
            "The AI should improve phrasing, organization, and relevance. It should not invent a candidate's employment history, qualifications, achievements, or technical skills.",
            "warn"
        ),
        h1("5.1 Production-grade AI design"),
        h2("Structured output"),
        paragraph(
            "Free-form text is easy to demonstrate but difficult for a user interface to interpret reliably. For ATS analysis, the better contract is a JSON object with a numeric score and arrays for missing skills, grammar suggestions, and improvements. The backend can validate the response before returning it."
        ),
        code("""
{
  "score": 78,
  "missingSkills": ["Docker", "AWS"],
  "grammarSuggestions": ["Replace passive wording in experience item 2"],
  "improvements": ["Add measurable outcome metrics"],
  "overallFeedback": "Strong entry-level backend profile."
}
        """),
        h2("Reliability controls"),
    ]
    add_bullets(s, [
        "Set connection and read timeouts so an unavailable model cannot block the application indefinitely.",
        "Rate-limit requests to manage AI cost and prevent abuse.",
        "Map upstream provider failures to safe application errors such as 502 or 503.",
        "Log model version, prompt version, latency, and error category without logging sensitive resume content by default.",
        "Use asynchronous jobs for expensive generation flows as traffic increases.",
    ])
    s += [
        h2("Privacy and prompt injection"),
        paragraph(
            "A resume contains personal data, and future job descriptions or uploads may contain adversarial instructions. Treat all user-supplied content as data inside a clear prompt boundary. Minimize retention, disclose external AI processing, and never allow user text to override the system's safety and formatting rules."
        ),
    ]

    # PDF and web integration
    s += [
        h1("6. PDF generation and HTTP delivery"),
        paragraph(
            "PdfService uses OpenPDF to create a Document, attach a writer to a ByteArrayOutputStream, add paragraphs, close the document, and return a byte array. PdfController sets the HTTP headers and body. The browser receives the bytes as a Blob and downloads resume.pdf."
        ),
        code("""
return ResponseEntity.ok()
  .header(HttpHeaders.CONTENT_DISPOSITION,
          "attachment; filename=resume.pdf")
  .contentType(MediaType.APPLICATION_PDF)
  .body(pdf);
        """),
        grid(
            ["Element", "Meaning", "Browser impact"],
            [
                ["Content-Type: application/pdf", "Identifies the response MIME type.", "The response is treated as a PDF binary file."],
                ["Content-Disposition: attachment", "Requests a download and suggests a filename.", "The browser downloads resume.pdf."],
                ["ResponseEntity<byte[]>", "Carries status, headers, and binary body.", "Spring writes a complete PDF response."],
                ["Axios Blob response", "Preserves binary data on the client.", "JavaScript can create a temporary download URL."],
            ],
            [4.3 * cm, 7.2 * cm, 6.3 * cm]
        ),
        h2("Current and improved rendering"),
        paragraph(
            "The current PDF has a title and raw resume text. This demonstrates a correct transport pipeline, but it is not yet a sophisticated resume renderer. A better design returns structured resume data from the AI layer and renders headings, bullets, contact details, experience entries, and page-aware layout with a selected template."
        ),
    ]
    add_bullets(s, [
        "Keep content text-based and use conventional headings so applicant-tracking systems can read the PDF.",
        "Use a registered Unicode font if the application accepts names or content outside ASCII.",
        "Control margins, typography, bullet indenting, and page breaks for professional presentation.",
        "Stream large document output rather than creating one large byte array in memory.",
    ])
    s += [
        h1("7. CORS, validation, and error handling"),
        h2("CORS"),
        paragraph(
            "React normally runs at http://localhost:3000 in development while Spring Boot runs at http://localhost:8080. The different ports make them different origins. @CrossOrigin on AIController and PdfController permits the React origin to call the API. CORS is a browser rule; it is not authentication."
        ),
        paragraph(
            "In production, replace the local development origin with the exact deployed frontend domain. Do not use broad wildcard origins for sensitive authenticated applications."
        ),
        h2("Validation"),
        paragraph(
            "Current request bodies are accepted without validation. Add jakarta.validation constraints to ResumeRequest and use @Valid on @RequestBody arguments. This rejects blank names, malformed emails, and oversized inputs before the application calls a paid AI service or writes the database."
        ),
        code("""
public class ResumeRequest {
  @NotBlank @Size(max = 100) private String name;
  @NotBlank @Email private String email;
  @Size(max = 4000) private String experience;
}

public String generateResume(@Valid @RequestBody ResumeRequest request) { ... }
        """),
        h2("Exception handling"),
        paragraph(
            "updateResume currently calls orElseThrow without a domain-specific exception. A missing id can become an unclear server error. A @RestControllerAdvice should translate expected failures into useful responses."
        ),
        grid(
            ["Failure", "Recommended status", "Response idea"],
            [
                ["Resume id absent", "404 Not Found", "Resume with id 42 does not exist."],
                ["Invalid request", "400 Bad Request", "email must be a valid email address."],
                ["Model provider timeout", "503 Service Unavailable", "Generation service is temporarily unavailable."],
                ["PDF rendering failure", "500 Internal Server Error", "Could not create PDF; try again."],
            ],
            [5.0 * cm, 4.1 * cm, 8.7 * cm]
        ),
    ]

    # Security
    config_example = (
        "spring.datasource.url=$" + "{DB_URL}\n"
        "spring.datasource.username=$" + "{DB_USERNAME}\n"
        "spring.datasource.password=$" + "{DB_PASSWORD}\n"
        "spring.ai.openai.api-key=$" + "{GROQ_API_KEY}"
    )
    s += [
        h1("8. Security and privacy review"),
        paragraph(
            "The application processes names, contact information, education, and work history. It also uses a database and an external AI provider. A learning prototype can demonstrate integration, but a deployable application must protect secrets, establish record ownership, limit access, and disclose data processing."
        ),
        note(
            "Immediate action",
            "The project configuration contains secrets directly in source configuration. Treat them as exposed: rotate the database password and AI key, remove them from source control, and replace them with environment variables or a managed secret store.",
            "red"
        ),
        h2("Safe configuration pattern"),
        code(config_example),
        h2("Security checklist"),
    ]
    add_bullets(s, [
        "Use .gitignore and an example configuration file containing placeholders only.",
        "Use profiles or deployment variables for development, test, and production configuration.",
        "Add authentication before storing or retrieving real user records.",
        "Authorize by ownership: a user must not access a resume by guessing its id.",
        "Use HTTPS in production and apply safe headers.",
        "Set request-size limits, rate limits, and quotas for AI endpoints.",
        "Minimize transfer and retention of personal data; document how the AI provider processes it.",
        "Keep dependencies current and scan for vulnerabilities.",
    ])
    s += [
        paragraph(
            "Deleting a secret from the current file is not enough if the project was committed or shared. Source history, archives, build logs, and forks may retain it. Rotation invalidates the old secret and is the correct remediation."
        ),
    ]

    # Testing and roadmap
    s += [
        h1("9. Testing, operations, and deployment"),
        h2("Test strategy"),
        grid(
            ["Test level", "Target", "Example assertion"],
            [
                ["Unit", "ResumeService", "Updating a record copies all intended fields and missing ids become domain errors."],
                ["Web slice", "AIController", "POST /ai/generate maps JSON to ResumeRequest and calls the service."],
                ["Repository", "ResumeRepository", "Entity mappings and CRUD work with a test database."],
                ["Integration", "Whole API", "Endpoints return correct status, headers, bodies, and errors."],
                ["Frontend", "React components", "Mock Axios, fill form, click button, and assert loading, result, and errors."],
            ],
            [3.0 * cm, 4.7 * cm, 10.1 * cm]
        ),
        h2("Operational concerns"),
    ]
    add_bullets(s, [
        "Expose health checks using Spring Boot Actuator for deployment monitoring.",
        "Log endpoint, latency, status, and upstream failure category while redacting PII and secrets.",
        "Measure generation latency, error rate, model cost, request volume, and PDF failures.",
        "Use Flyway or Liquibase for schema migrations rather than relying on ddl-auto=update in production.",
        "Deploy React as static assets, Spring Boot as an API service, and MySQL as a managed database with environment-specific configuration.",
    ])
    s += [
        note(
            "Production principle",
            "A working demo proves functionality. A production service additionally proves security, resilience, ownership, observability, testing, and repeatable deployment.",
            "teal"
        ),
        h1("10. Technical roadmap and code-review findings"),
        paragraph(
            "The existing project is a readable and valuable prototype. The roadmap below addresses the most important gaps first, preserving the simple learning-oriented structure while moving toward a real product."
        ),
        grid(
            ["Priority", "Finding", "Impact", "Suggested change"],
            [
                ["P0", "Secrets in configuration", "Provider and database compromise risk.", "Rotate secrets and use environment variables."],
                ["P1", "No validation or error advice", "Bad inputs and absent ids yield unclear failures.", "Use @Valid and @RestControllerAdvice."],
                ["P1", "No authentication or ownership", "Records could be exposed or modified by other callers.", "Add users, authentication, and per-user authorization."],
                ["P1", "Projects not persisted", "AI input is not fully saved or updated.", "Add projects field or normalized project records."],
                ["P2", "Free-form AI analysis", "Interface cannot reliably render individual findings.", "Use validated structured JSON output."],
                ["P2", "Simple PDF layout", "Document is functional but not portfolio-ready.", "Render structured sections from a template."],
                ["P2", "Field injection", "Dependencies are less explicit and testable.", "Adopt constructor injection."],
                ["P3", "Hardcoded frontend URLs", "Deployment needs code edits.", "Use environment-specific frontend configuration."],
            ],
            [1.2 * cm, 4.0 * cm, 5.5 * cm, 7.1 * cm]
        ),
        h2("Feature sequence"),
    ]
    add_bullets(s, [
        "Phase 1: credential rotation, validation, exception handling, constructor injection, and action-specific loading states.",
        "Phase 2: job-description input, keyword matching, editable output, and professional ATS-safe PDF templates.",
        "Phase 3: user accounts, saved dashboards, revision history, secure ownership, and export history.",
        "Phase 4: structured AI output, configurable roles and tones, provider fallback, and cost observability.",
    ])
    # Interview
    s += [
        h1("11. Interview preparation"),
        h2("A 60-second project explanation"),
        note(
            "Suggested answer",
            "I built an AI Resume Builder with a React frontend and Spring Boot backend. A candidate enters profile, education, skills, experience, and projects. React sends that information to REST endpoints. The backend uses Spring AI with an OpenAI-compatible language-model provider to generate an ATS-friendly resume, analyze it, and create a cover letter. I also added JPA and MySQL CRUD support plus PDF export with OpenPDF. The main engineering topics are asynchronous UI state, REST design, prompt engineering, CORS, binary file downloads, database persistence, and secure handling of personal data.",
            "blue"
        ),
        h2("Core interview questions"),
        grid(
            ["Question", "Strong answer direction"],
            [
                ["Why React and Spring Boot?", "React is effective for interactive form workflows. Spring Boot provides REST, DI, JPA, validation, test support, and AI integration."],
                ["How does data flow?", "Form state -> Axios -> controller -> service -> model, database, or PDF renderer -> response -> React state or Blob download."],
                ["Why use a DTO?", "ResumeRequest represents API needs, including projects, independently of the persisted Resume entity."],
                ["Why use Blob for PDFs?", "A PDF is binary. Blob preserves raw bytes and enables a browser object URL download."],
                ["What does CORS do?", "It permits the development React origin to call a backend on a different port. It does not authenticate callers."],
                ["How would you improve AI quality?", "Use job descriptions, schema-constrained output, factual-claim checks, prompt versioning, and an editable review step."],
                ["Most urgent security fix?", "Rotate exposed configuration secrets, then use environment variables and add authenticated record ownership."],
            ],
            [5.1 * cm, 12.7 * cm]
        ),
        h1("11.1 Advanced discussion answers"),
        h2("Why not call a repository directly from a controller?"),
        paragraph(
            "A controller should be a transport adapter: it maps HTTP to a use case and results back to HTTP. Business rules commonly grow to include authorization, auditing, retries, provider fallback, and transactions. The service layer owns such rules and can be reused by HTTP, scheduled, or message-driven entry points."
        ),
        h2("How would you make an LLM product more predictable?"),
        paragraph(
            "The exact wording remains probabilistic, but the system can be predictable around it: fixed prompt versions, controlled generation settings, JSON schema output, input validation, factual constraints, content review, editable user drafts, and telemetry that records model and prompt versions."
        ),
        h2("How would the database evolve?"),
        paragraph(
            "Introduce a User entity and an ownership relationship to Resume. Retain resume metadata and version history, then decide whether experience, education, and projects belong in ordered child tables or validated JSON based on future queries. Use Flyway for migrations."
        ),
        h2("What happens when the model provider fails?"),
        paragraph(
            "Map the provider exception to an application-level failure, apply timeouts, retry only transient failures, log internal details safely, and return a clear temporary-unavailable response. Optionally offer a retry path or carefully controlled fallback provider."
        ),
        h2("What makes an ATS-friendly PDF?"),
        paragraph(
            "It should preserve selectable text, use clear conventional headings, avoid important content inside images or complex graphics, use standard fonts, maintain simple structure, and prioritize semantic readability over decorative layout."
        ),
    ]

    # Checklist
    s += [
        h1("12. Demonstration and revision checklist"),
        h2("Demonstration sequence"),
    ]
    add_bullets(s, [
        "Start MySQL and confirm the configured schema is available.",
        "Start Spring Boot with non-secret local configuration and confirm the AI provider is reachable.",
        "Start React, enter a realistic candidate profile, and generate a resume.",
        "Review generated statements for factual accuracy before analysis or export.",
        "Run ATS analysis and explain its five feedback categories.",
        "Generate a cover letter and note that the current prompt targets a Java Spring Boot Developer role.",
        "Download the PDF and confirm it opens as a valid file.",
        "If demonstrating CRUD endpoints, create, list, update, and delete a safe test record.",
    ])
    s += [h2("Before publishing or deploying")]
    add_bullets(s, [
        "Rotate exposed keys and passwords, and remove secrets from configuration and repository history.",
        "Commit an example configuration file with placeholders only.",
        "Add validation, standardized exception responses, and tests.",
        "Set production CORS origins and enable authentication before handling real personal data.",
        "Move database schema management to migrations and configure safe production settings.",
        "State clearly that every AI-generated claim requires user review.",
    ])
    s += [
        Spacer(1, 0.5 * cm),
        note(
            "Final takeaway",
            "This project is a strong learning foundation because it combines modern frontend work, a layered Java backend, relational persistence, AI integration, and document generation. Moving from prototype to production mainly requires secure configuration, structured data, validation, ownership, resilience, and polished user experience.",
            "teal"
        ),
        Spacer(1, 0.55 * cm),
        paragraph("End of study guide", "CoverSub"),
    ]
    return s


if __name__ == "__main__":
    GuideDocument(str(OUTPUT)).build(build_story())
    print(OUTPUT)
