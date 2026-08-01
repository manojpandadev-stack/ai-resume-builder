from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUTPUT = Path("output/pdf/HR_Interview_Scheduling_Conversations_Natural.pdf")


SCENARIOS = [
    (
        "1. Initial screening call - agreeing a first interview",
        "The recruiter confirms fit for the role and agrees a mutually convenient interview time.",
        [
            ("HR", "Hello, may I speak with Manoj Kumar Panda, please?"),
            ("Manoj", "Speaking. Hello - may I know who is calling?"),
            ("HR", "Hi Manoj. This is Anjali from Bright Software Solutions. I am calling about your application for the Senior Java Developer role. Is now a convenient time for a brief conversation?"),
            ("Manoj", "Yes, absolutely. Thank you for calling."),
            ("HR", "I have reviewed your profile. Your experience with Java, Spring Boot, REST APIs, and microservices at HTC Global Services seems closely aligned with what our team needs."),
            ("Manoj", "Thank you. In my current role, I work mainly on backend services, including API development, data persistence with Hibernate JPA, and service-to-service integration."),
            ("HR", "I also noticed your work on the EBOOKERS travel booking platform. Could you briefly tell me what part of that project you owned?"),
            ("Manoj", "Certainly. I contributed to booking and user-management services, and I worked on payment-related APIs. I was also involved in securing endpoints using JWT-based authentication."),
            ("HR", "That is helpful context. We would like to invite you to an initial technical discussion. Would you be interested in proceeding?"),
            ("Manoj", "Yes, I would be very interested. Please let me know the available slots."),
            ("HR", "We have Thursday at 11:00 a.m. or Thursday at 2:00 p.m. Which would suit you better?"),
            ("Manoj", "Could we please schedule it for 2:00 p.m.? I have a morning commitment at work, but I can be fully available in the afternoon."),
            ("HR", "Of course. I will reserve Thursday at 2:00 p.m. and send a calendar invitation shortly. Please review it once you receive it."),
            ("Manoj", "Thank you, Anjali. I will check the invite and confirm my attendance today."),
        ],
        "Useful phrase: 'Could we please schedule it for ...?' It is polite, clear, and gives a brief professional reason.",
    ),
    (
        "2. Follow-up call - confirming the interview slot",
        "The recruiter verifies the appointment and resolves small practical details before the interview.",
        [
            ("HR", "Hello Manoj, this is Anjali from Bright Software Solutions. I am calling to confirm your interview scheduled for Thursday."),
            ("Manoj", "Hello, Anjali. Yes, thank you for calling. I have the interview marked in my calendar."),
            ("HR", "Wonderful. It is scheduled for Thursday at 2:00 p.m. and should take about forty-five minutes. Does that timing still work for you?"),
            ("Manoj", "Yes, it does. I will be available and can join a few minutes early."),
            ("HR", "I sent the meeting invitation yesterday. Were you able to access the link and the role description?"),
            ("Manoj", "Yes, I received both. The link opens correctly, and I have read through the job description."),
            ("HR", "Excellent. The panel may ask about your recent Spring Boot work, so an updated resume would be useful if anything has changed since you applied."),
            ("Manoj", "My experience and contact details are unchanged, but I can reply to your email with the latest PDF copy for completeness."),
            ("HR", "That would be appreciated. Please also keep a government-issued ID nearby in case the interviewer needs a quick identity check."),
            ("Manoj", "Certainly. I will have it ready."),
            ("HR", "Do you have any questions about the format before we end the call?"),
            ("Manoj", "Just one. Will it be a video call with one interviewer or a panel?"),
            ("HR", "It will be a video call with a technical lead and a senior engineer. They will introduce themselves at the start."),
            ("Manoj", "That is clear. Thank you for the information. I look forward to speaking with them on Thursday."),
        ],
        "Useful phrase: 'For completeness, I can send the latest copy.' This sounds cooperative without implying that something is missing.",
    ),
    (
        "3. Candidate requests to reschedule",
        "The candidate gives timely notice, offers alternatives, and keeps the tone respectful.",
        [
            ("Manoj", "Hello, this is Manoj Panda. May I speak with Anjali from the recruitment team, please?"),
            ("HR", "Speaking, Manoj. How can I help?"),
            ("Manoj", "I am calling about my interview scheduled for Thursday at 2:00 p.m. I am sorry for the short notice, but an urgent production issue has come up in my current project."),
            ("HR", "I understand. Thank you for letting us know before the interview. Would you like to reschedule?"),
            ("Manoj", "Yes, if possible. I remain very interested in the opportunity, and I would prefer a time when I can give the discussion my full attention."),
            ("HR", "That makes sense. Do you have a preferred day next week?"),
            ("Manoj", "Monday or Tuesday afternoon would work well for me. I can be flexible between 1:00 and 4:00 p.m."),
            ("HR", "Let me check the panel's calendar. Monday at 2:00 p.m. is currently available. Would that suit you?"),
            ("Manoj", "Yes, Monday at 2:00 p.m. would be perfect. Thank you for accommodating the change."),
            ("HR", "No problem. I will cancel the existing invitation and send a new one. Please accept the updated invite when it arrives."),
            ("Manoj", "I will do that immediately. Again, I apologize for the inconvenience."),
            ("HR", "There is no need to worry. We appreciate the advance notice. I will speak with you on Monday."),
            ("Manoj", "Thank you, Anjali. Have a good day."),
        ],
        "Useful phrase: 'I would prefer a time when I can give the discussion my full attention.' It explains a rescheduling request positively.",
    ),
    (
        "4. HR offers an alternate slot",
        "The recruiter changes the schedule professionally and reassures the candidate.",
        [
            ("HR", "Hello Manoj, this is Anjali from Bright Software Solutions. I am calling about Monday's interview."),
            ("Manoj", "Hello, Anjali. Yes, I am ready to discuss it."),
            ("HR", "I am afraid the technical lead has been pulled into an urgent client meeting, so we need to move your interview. I apologize for the inconvenience."),
            ("Manoj", "Thank you for informing me. I understand that unexpected commitments can arise. What alternatives do you have?"),
            ("HR", "We can offer Tuesday at 11:00 a.m., Tuesday at 3:00 p.m., or Wednesday at 11:00 a.m."),
            ("Manoj", "Tuesday at 3:00 p.m. would be the most convenient option for me. Would the interview format remain the same?"),
            ("HR", "Yes. It will still be a forty-five-minute Google Meet discussion with the technical lead and senior engineer."),
            ("Manoj", "That works well. I will keep Tuesday at 3:00 p.m. free."),
            ("HR", "Thank you for being flexible. I will send an updated invitation within the next fifteen minutes."),
            ("Manoj", "I will watch for it and accept it as soon as I receive it."),
            ("HR", "Please disregard the earlier calendar invite once the replacement arrives."),
            ("Manoj", "Understood. Thank you for the clear update."),
        ],
        "Useful phrase: 'What alternatives do you have?' It is direct and professional when an employer changes the schedule.",
    ),
    (
        "5. Sharing interview details and required documents",
        "The candidate checks practical requirements without sounding uncertain or unprepared.",
        [
            ("HR", "Hi Manoj. I am sending the final details for your interview on Tuesday at 3:00 p.m."),
            ("Manoj", "Thank you. I have received the invitation. Could you please let me know whether there are any documents I should prepare?"),
            ("HR", "For the interview itself, please keep an updated resume and a government-issued photo ID available. If you proceed to the next stage, we may request academic and employment documents separately."),
            ("Manoj", "Understood. I will have my resume and ID ready. Should I also keep digital copies of my B.Tech certificate and recent salary slips available?"),
            ("HR", "That would be sensible, although you do not need to send them now. Please share only what we request through an official company email."),
            ("Manoj", "Thank you for clarifying. Since this is an online interview, do I need to install any software?"),
            ("HR", "No installation is required. Google Meet will open in your browser, but please test your microphone, camera, and internet connection in advance."),
            ("Manoj", "I will do a quick test this evening. Is there a preferred time to join the meeting?"),
            ("HR", "Please join five minutes early. That gives us time to resolve any connection issue before the panel starts."),
            ("Manoj", "Certainly. I will join at 2:55 p.m. and wait in the meeting room."),
            ("HR", "Perfect. Please use a quiet place with a neutral background if possible."),
            ("Manoj", "I have arranged a quiet room and will make sure there are no interruptions. Thank you for the guidance."),
        ],
        "Useful phrase: 'Could you please let me know whether ...?' It is a polished way to ask for preparation details.",
    ),
    (
        "6. Reminder call - one day before the interview",
        "The recruiter confirms attendance and helps the candidate understand what to expect.",
        [
            ("HR", "Hello Manoj. This is a quick reminder about your interview tomorrow at 3:00 p.m."),
            ("Manoj", "Hello, Anjali. Thank you for the reminder. Yes, I will be available tomorrow."),
            ("HR", "Great. I wanted to make sure the meeting link is working and that you have not had any changes in availability."),
            ("Manoj", "The link works, and my schedule is unchanged. I plan to join about five minutes early."),
            ("HR", "Excellent. There will be two interviewers: a technical lead and a project manager. The discussion will focus on your recent backend work rather than on puzzles alone."),
            ("Manoj", "That is useful to know. May I ask whether they are particularly interested in my EBOOKERS project or in general Java concepts?"),
            ("HR", "Both. Please be ready to explain a service you designed, a technical challenge you faced, and how you collaborated with other teams."),
            ("Manoj", "I will prepare examples around booking workflows, API security, and coordination with the QA team."),
            ("HR", "That sounds appropriate. Please keep your explanations structured: situation, action, and result."),
            ("Manoj", "I will. Thank you for the suggestion."),
            ("HR", "Do you have any final logistical questions?"),
            ("Manoj", "No, everything is clear now. I appreciate your help and look forward to the discussion."),
        ],
        "Useful phrase: 'May I ask whether they are particularly interested in ...?' It makes a focused, relevant question sound courteous.",
    ),
    (
        "7. Scheduling the technical round",
        "After a successful screening, the recruiter sets expectations for a deeper technical conversation.",
        [
            ("HR", "Hello Manoj. I am pleased to let you know that you have cleared the initial discussion."),
            ("Manoj", "That is very good news. Thank you for letting me know."),
            ("HR", "The panel appreciated the way you explained your project responsibilities. We would like to schedule a technical round with our team lead."),
            ("Manoj", "I would be happy to attend. When are you looking to schedule it?"),
            ("HR", "We have availability on Friday at 3:00 p.m. The session may last up to an hour. Would you be able to join then?"),
            ("Manoj", "Yes, Friday at 3:00 p.m. is convenient for me."),
            ("HR", "This round will go deeper into core Java, Spring Boot, database design, REST APIs, microservices, and authentication. There may also be a short problem-solving exercise."),
            ("Manoj", "Thank you for outlining the topics. Should I expect live coding, or will it be mainly a design discussion?"),
            ("HR", "It will be primarily conversational, with perhaps a small coding or debugging question. The lead is more interested in your reasoning than in a perfect answer."),
            ("Manoj", "That is helpful. I will review my project decisions and be prepared to explain the trade-offs I made."),
            ("HR", "Exactly. Please also be ready to discuss performance, error handling, and how your services communicate with one another."),
            ("Manoj", "Certainly. I look forward to the round."),
        ],
        "Useful phrase: 'I will be prepared to explain the trade-offs I made.' This shows maturity and technical judgment.",
    ),
    (
        "8. Scheduling the final HR round",
        "The candidate learns what the final HR conversation covers and prepares factually.",
        [
            ("HR", "Hello Manoj. I hope you are well. I have positive feedback from the technical team."),
            ("Manoj", "I am glad to hear that. Thank you for the update."),
            ("HR", "They would like to move you to the final HR discussion. Are you available next Monday at 11:00 a.m.?"),
            ("Manoj", "Yes, I am available at that time. May I ask what the conversation will cover?"),
            ("HR", "We will discuss your career goals, current responsibilities, notice period, compensation expectations, and any questions you have about the company or role."),
            ("Manoj", "Understood. I will keep the relevant details ready. Will this be the final stage before a decision?"),
            ("HR", "Yes, assuming there are no additional clarifications from the hiring manager, this is the final scheduled round."),
            ("Manoj", "Thank you for clarifying. I will be prepared and will join on time."),
            ("HR", "Please be open about your timelines and expectations. Clear information helps us move quickly if the outcome is positive."),
            ("Manoj", "Absolutely. I will be transparent about my current notice period and any commitments I need to consider."),
            ("HR", "Very good. I will send a calendar invitation for Monday at 11:00 a.m."),
            ("Manoj", "Thank you, Anjali. I look forward to speaking with you then."),
        ],
        "Useful phrase: 'May I ask what the conversation will cover?' It helps you prepare without sounding demanding.",
    ),
    (
        "9. Interview day - confirming readiness",
        "A brief check-in addresses technical setup and gives the candidate calm, practical guidance.",
        [
            ("HR", "Good morning, Manoj. This is Anjali from Bright Software Solutions. I am just checking in before your interview this afternoon."),
            ("Manoj", "Good morning, Anjali. Thank you for calling. I am all set for the 2:00 p.m. interview."),
            ("HR", "Wonderful. Have you been able to test your internet connection, camera, and microphone?"),
            ("Manoj", "Yes. I tested everything this morning, and the meeting link opens correctly."),
            ("HR", "Perfect. Please join by 1:55 p.m. If you face a connection issue, reply to the calendar invitation or call the recruitment number in the email."),
            ("Manoj", "Understood. I have noted both options."),
            ("HR", "The panel may ask you to share your screen for a diagram or a small coding question. Are you comfortable doing that?"),
            ("Manoj", "Yes. I have closed personal windows and prepared a clean workspace in case screen sharing is needed."),
            ("HR", "That is ideal. Keep a notebook nearby, but try not to read directly from prepared notes during the discussion."),
            ("Manoj", "Of course. I will use notes only to remember questions or key points."),
            ("HR", "Excellent. Take a moment before you join, speak at a steady pace, and ask for clarification if a question is unclear."),
            ("Manoj", "Thank you. That is reassuring. I appreciate your support."),
        ],
        "Useful phrase: 'Could you please repeat or rephrase the question?' Asking for clarification is better than guessing.",
    ),
    (
        "10. Post-interview follow-up",
        "The recruiter acknowledges the interview, shares a realistic timeline, and avoids making premature promises.",
        [
            ("HR", "Hello Manoj. Thank you for taking the time to speak with our panel today."),
            ("Manoj", "Thank you for arranging the interview. I enjoyed learning more about the team and the role."),
            ("HR", "I am pleased to hear that. How did you find the discussion?"),
            ("Manoj", "It was a good conversation. I was especially interested in the questions about API design and scaling booking-related services."),
            ("HR", "The panel noted that you explained your JWT authentication work clearly and gave practical examples from EBOOKERS."),
            ("Manoj", "That is encouraging. Please let me know if they need any additional information from my side."),
            ("HR", "At the moment, no further action is needed. The panel will complete their feedback, and we expect to update you within two to three working days."),
            ("Manoj", "Thank you. I appreciate having a clear timeline."),
            ("HR", "If the process takes longer than expected, I will let you know rather than leaving you without an update."),
            ("Manoj", "I appreciate that. I will wait to hear from you."),
            ("HR", "Thank you again for your time and preparation."),
            ("Manoj", "Thank you, Anjali. Have a good day."),
        ],
        "Useful phrase: 'Please let me know if they need any additional information from my side.' It is proactive but not pushy.",
    ),
    (
        "11. Scheduling the managerial round",
        "The candidate prepares for leadership, teamwork, and delivery questions, not only technical questions.",
        [
            ("HR", "Hello Manoj. I have good news: the technical panel has recommended you for a conversation with our engineering manager."),
            ("Manoj", "That is wonderful news. Thank you very much."),
            ("HR", "The manager is available tomorrow at 4:00 p.m. Would you be able to attend a video call at that time?"),
            ("Manoj", "Yes, 4:00 p.m. tomorrow works for me."),
            ("HR", "Great. This round is less about detailed coding and more about how you work with people, handle priorities, and take ownership."),
            ("Manoj", "Thank you for explaining that. Should I prepare examples from my current project?"),
            ("HR", "Yes, please prepare two or three examples: one involving cross-functional collaboration, one involving a delivery challenge, and one showing how you handled feedback or disagreement."),
            ("Manoj", "I can discuss how I coordinated with QA and frontend teams during a booking flow release, as well as an issue we resolved under a tight timeline."),
            ("HR", "Those examples sound relevant. The manager may also ask about Agile ceremonies and how you balance quality with delivery speed."),
            ("Manoj", "Understood. I will prepare concise examples with the context, my contribution, and the result."),
            ("HR", "Excellent. I will send the Google Meet invitation shortly."),
            ("Manoj", "Thank you. I look forward to speaking with the engineering manager."),
        ],
        "Useful phrase: 'I will prepare concise examples with the context, my contribution, and the result.' This signals structured communication.",
    ),
    (
        "12. Offer discussion and joining date",
        "The candidate responds warmly while asking for written details and discussing availability honestly.",
        [
            ("HR", "Hello Manoj. I am delighted to let you know that we would like to offer you the Senior Java Developer position."),
            ("Manoj", "Thank you very much. I am genuinely pleased to hear that and grateful for the opportunity."),
            ("HR", "The team was impressed by your technical background and the way you approached the interviews. I would like to discuss a possible joining date and the next steps."),
            ("Manoj", "Certainly. I would be happy to discuss that."),
            ("HR", "Could you confirm your current notice period at HTC Global Services?"),
            ("Manoj", "My formal notice period is thirty days. I will follow the proper handover process, although I can check whether an earlier release is possible after I receive the written offer."),
            ("HR", "That is reasonable. Based on that timeline, would joining in about four weeks be realistic?"),
            ("Manoj", "Yes, that should be realistic. I can confirm an exact date once I discuss the transition plan with my current manager."),
            ("HR", "Perfect. We will send the formal offer letter by email today, including compensation, benefits, reporting manager, and onboarding documents."),
            ("Manoj", "Thank you. I will read the offer carefully and respond within the stated timeline."),
            ("HR", "Please feel free to send any questions in writing after you review it."),
            ("Manoj", "I appreciate that. I am excited about the role and look forward to reviewing the details."),
        ],
        "Useful phrase: 'I can confirm an exact date once I discuss the transition plan with my current manager.' It is accurate and avoids overpromising.",
    ),
    (
        "13. Salary negotiation",
        "The candidate expresses an expectation with evidence, stays respectful, and leaves room for discussion.",
        [
            ("HR", "Hello Manoj. Before we finalize the offer, I would like to discuss compensation with you."),
            ("Manoj", "Certainly, Anjali. Thank you for arranging the discussion."),
            ("HR", "Based on the role, your experience, and our internal range, we are prepared to offer a total annual package of twelve lakh rupees."),
            ("Manoj", "Thank you for sharing the offer. I appreciate the opportunity and the confidence the team has shown in me."),
            ("HR", "You are welcome. Do you have any questions or concerns about the package?"),
            ("Manoj", "After considering the responsibilities of the role and my experience designing Spring Boot microservices, securing APIs with JWT, and supporting the EBOOKERS platform, I was hoping for something closer to fourteen lakh rupees."),
            ("HR", "I understand. Could you tell me whether that expectation is based on a particular offer or on your understanding of the market?"),
            ("Manoj", "It is based on the scope of the role, my current experience, and the value I believe I can contribute. I am open to a constructive discussion and would be happy to understand the full compensation structure as well."),
            ("HR", "That is a fair explanation. I will speak with the hiring manager and our compensation team to see whether there is flexibility."),
            ("Manoj", "Thank you. I appreciate you considering my request. I remain very interested in joining the team."),
            ("HR", "I should have an update for you within two working days."),
            ("Manoj", "That works for me. Thank you again for the transparent conversation."),
        ],
        "Useful phrase: 'I was hoping for something closer to ...' It is firmer and more diplomatic than demanding a number.",
    ),
    (
        "14. Background verification",
        "The candidate understands the process, shares documents safely, and asks about the timeline.",
        [
            ("HR", "Hello Manoj. This is Anjali from Bright Software Solutions. I am calling to explain the background-verification process."),
            ("Manoj", "Hello, Anjali. Thank you. Please let me know what you need from me."),
            ("HR", "We will verify your education and employment history after you accept the offer. You will receive a secure link from our verification partner rather than a request to send sensitive documents by chat."),
            ("Manoj", "Thank you for clarifying the process. Which documents should I keep ready?"),
            ("HR", "Please keep your B.Tech certificate, identification document, recent address proof if applicable, and employment documents from HTC Global Services. The portal will show the exact list."),
            ("Manoj", "Understood. I have digital copies of those documents and can upload them once I receive the secure link."),
            ("HR", "We may also ask for the contact details of an HR representative or previous manager who can verify your employment dates."),
            ("Manoj", "I can provide the appropriate official contact details. Should I inform the reference in advance?"),
            ("HR", "Yes, that is a good idea. Please tell them that they may receive a standard verification request and that they should respond through their official email address."),
            ("Manoj", "I will do that. How long does the process usually take?"),
            ("HR", "It normally takes five to seven working days, depending on how quickly the institutions and employers respond. We will keep you updated if anything needs clarification."),
            ("Manoj", "Thank you. I will complete the upload promptly once the link arrives."),
        ],
        "Useful phrase: 'Could you please confirm the secure method for sharing these documents?' It protects your privacy and sounds professional.",
    ),
]


ADDITIONAL_TURNS = [
    [
        ("HR", "I will also include the role description and the names of the interviewers in the invitation, so you know what to expect."),
        ("Manoj", "That would be very helpful. I will review the description again and prepare examples that are relevant to the role."),
        ("HR", "Excellent. If a conflict arises before Thursday, please let us know as early as possible so we can help."),
    ],
    [
        ("HR", "The invitation will show Indian Standard Time. Please check that the time zone has not changed in your calendar settings."),
        ("Manoj", "I have checked it, and it correctly shows Thursday at 2:00 p.m. IST."),
        ("HR", "Great. A prompt reply to the invitation will complete the confirmation from your side."),
    ],
    [
        ("HR", "Would you like me to note that the change is due to an urgent production responsibility?"),
        ("Manoj", "Yes, please. I want the panel to know that I value their time and that this is an exceptional situation."),
        ("HR", "I will add a brief note and confirm the new appointment by email."),
    ],
    [
        ("HR", "If Tuesday becomes difficult for any reason, Wednesday morning is still being held as a backup for the moment."),
        ("Manoj", "Thank you. Tuesday at 3:00 p.m. is confirmed from my side, so I do not expect to need the backup."),
        ("HR", "Perfect. We will proceed with Tuesday and release the other option."),
    ],
    [
        ("HR", "For your security, please do not send bank information, PAN details, or passwords during the interview process."),
        ("Manoj", "Thank you for mentioning that. I will share documents only through the official process you described."),
        ("HR", "That is exactly right. We want candidates to feel comfortable and informed throughout the process."),
    ],
    [
        ("HR", "Please avoid sharing confidential code or internal documents from your current employer during the interview."),
        ("Manoj", "Of course. I will explain my work at a high level and use anonymized examples where necessary."),
        ("HR", "That is the professional approach. The panel will respect those boundaries."),
    ],
    [
        ("HR", "You do not need to memorize definitions. The lead is interested in how you apply concepts in real projects."),
        ("Manoj", "That suits my working style. I will focus on clear examples and explain why I selected particular approaches."),
        ("HR", "Very good. Practical reasoning will make your answers stronger."),
    ],
    [
        ("HR", "There is no paperwork to complete before this round. Just join from a quiet place and keep the time free."),
        ("Manoj", "Understood. I will make sure I am not interrupted and will keep the entire hour available."),
        ("HR", "Thank you. That will help the conversation run smoothly."),
    ],
    [
        ("HR", "If you are running even a few minutes late, please send a message immediately rather than waiting until the meeting starts."),
        ("Manoj", "Certainly. I have planned to be ready early, but I will notify you straight away if anything unexpected happens."),
        ("HR", "Thank you. Clear communication is always appreciated."),
    ],
    [
        ("HR", "You do not need to send a separate follow-up email today unless you have a specific question or document to share."),
        ("Manoj", "That is helpful. I will wait for the update, and I will respond promptly if you contact me."),
        ("HR", "Perfect. We will be in touch as soon as the feedback is finalized."),
    ],
    [
        ("HR", "The manager is especially interested in how you make decisions when requirements are incomplete or priorities change."),
        ("Manoj", "I can prepare an example where I clarified requirements with stakeholders before committing the team to an implementation."),
        ("HR", "That would be a strong example. Please include how you communicated the decision and its outcome."),
    ],
    [
        ("HR", "The offer letter will specify the date by which we need your written acceptance. Please review that deadline carefully."),
        ("Manoj", "I will. If I need clarification on any point, I will ask before the deadline rather than making assumptions."),
        ("HR", "Excellent. We want you to make a well-informed decision."),
    ],
    [
        ("HR", "You do not need to decide during this call. We want you to have time to review the full offer and benefits."),
        ("Manoj", "I appreciate that. A written breakdown will help me consider the opportunity carefully and respond responsibly."),
        ("HR", "That is completely reasonable. I will return with a clear update after the review."),
    ],
    [
        ("HR", "Please do not upload documents through an unverified link or share passwords with anyone claiming to be from the verification team."),
        ("Manoj", "Understood. I will check that the email and portal are official before uploading any personal documents."),
        ("HR", "Excellent. If anything looks unusual, contact me before taking action."),
    ],
]


def add_page_number(canvas, document):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#D7E1EC"))
    canvas.line(18 * mm, 14 * mm, 192 * mm, 14 * mm)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.setFont("Helvetica", 8)
    canvas.drawString(18 * mm, 9 * mm, "HR Interview Scheduling Conversations - Natural Spoken English Practice")
    canvas.drawRightString(192 * mm, 9 * mm, f"Page {document.page}")
    canvas.restoreState()


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=21 * mm,
        title="HR Interview Scheduling Conversations - Natural Spoken English Practice",
        author="Prepared for Manoj Kumar Panda",
    )

    styles = getSampleStyleSheet()
    title = ParagraphStyle("BookTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=25, leading=31, alignment=TA_CENTER, textColor=colors.HexColor("#12355B"), spaceAfter=10)
    subtitle = ParagraphStyle("Subtitle", parent=styles["BodyText"], fontSize=11, leading=16, alignment=TA_CENTER, textColor=colors.HexColor("#475569"), spaceAfter=18)
    heading = ParagraphStyle("ScenarioHeading", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=15, leading=20, textColor=colors.HexColor("#12355B"), spaceBefore=4, spaceAfter=7)
    objective = ParagraphStyle("Objective", parent=styles["BodyText"], fontSize=9.5, leading=13, textColor=colors.HexColor("#475569"), spaceAfter=10)
    speaker = ParagraphStyle("Speaker", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=9.4, leading=13, textColor=colors.HexColor("#12355B"))
    dialogue = ParagraphStyle("Dialogue", parent=styles["BodyText"], fontSize=9.4, leading=13, textColor=colors.HexColor("#1E293B"))
    tip = ParagraphStyle("Tip", parent=styles["BodyText"], fontSize=9.2, leading=13, textColor=colors.HexColor("#334155"), leftIndent=3 * mm, rightIndent=3 * mm, spaceBefore=8, spaceAfter=12)
    toc = ParagraphStyle("Contents", parent=styles["BodyText"], fontSize=10.5, leading=17, textColor=colors.HexColor("#334155"))

    story = [Spacer(1, 35 * mm), Paragraph("HR & Candidate Conversations", title), Paragraph("Interview scheduling and follow-up - realistic spoken English practice", subtitle)]
    total_turns = sum(len(lines) + len(ADDITIONAL_TURNS[index]) for index, (_, _, lines, _) in enumerate(SCENARIOS))
    cover_text = (
        "A polished set of fourteen realistic phone and video-call conversations for interview preparation. "
        f"It includes {total_turns} spoken dialogue turns with natural professional language, clear context, and practical follow-up questions. "
        "The candidate profile reflects a Senior Java Developer with experience in Java, Spring Boot, Hibernate JPA, microservices, REST APIs, and JWT security."
    )
    story.append(Paragraph(cover_text, ParagraphStyle("CoverText", parent=styles["BodyText"], fontSize=11, leading=17, alignment=TA_CENTER, textColor=colors.HexColor("#334155"))))
    story.append(Spacer(1, 15 * mm))
    story.append(Table([[Paragraph("How to practise", speaker), Paragraph("Read each role aloud. Then repeat the conversation without looking, adapting the details to your own experience and availability.", dialogue)]], colWidths=[38 * mm, 128 * mm], style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EAF3FA")), ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#B8D0E8")), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7)])))
    story.append(PageBreak())
    story.extend([Paragraph("Contents", heading), Spacer(1, 3 * mm)])
    for scenario, _, _, _ in SCENARIOS:
        story.append(Paragraph(scenario, toc))
    story.append(PageBreak())

    for index, (scenario, goal, lines, language_tip) in enumerate(SCENARIOS):
        story.append(Paragraph(scenario, heading))
        story.append(Paragraph(goal, objective))
        rows = []
        for person, text in lines + ADDITIONAL_TURNS[index]:
            rows.append([Paragraph(person, speaker), Paragraph(text, dialogue)])
        conversation = Table(rows, colWidths=[24 * mm, 142 * mm], repeatRows=0, hAlign="LEFT")
        conversation.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#DDE7F0")),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#F2F7FB")),
        ]))
        story.append(conversation)
        story.append(Table([[Paragraph("Language focus", speaker), Paragraph(language_tip, tip)]], colWidths=[35 * mm, 131 * mm], style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FFF8E7")), ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#E9D8A6")), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)])))
        if index != len(SCENARIOS) - 1:
            story.append(PageBreak())

    document.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
    print(OUTPUT.resolve())
