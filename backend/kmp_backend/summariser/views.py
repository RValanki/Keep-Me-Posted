from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Create your views here.
def generate_summary(request):
    ## Implement the summarisation logic here

    load_dotenv()

    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    transcript = request.POST.get("transcript")

    if transcript == "" or transcript is None:
        return HttpResponse("Transcript not found", status=404)

    prompt = """The user will give you a meeting transcript.You are an expert in concisely summarising meeting transcripts so that people wanting to review what happened in the meeting can read this summary and understand the key details of what was discussed and any important outcomes. They should be able to understand what tasks have been assigned, when it is due, and the people that have been assigned to it. This should be done in a professional manner, so you must ensure that any profanity or slurs encountered is omitted from the final output. Ensure to NOT include sensitive information such as banking information, passwords, addresses. Quote what someone said with their name if their names are included in the summary.Below is the structure you should follow to generate a summary. Using the following headings take note of the additional information I have included to guide what you include under each heading.1. Start with a suitable title for the summary2. Meeting Agenda: Start with what the meeting’s purpose was and what was the overarching agenda. Include progress on previous tasks if this has been discussed. If the tasks are not completed, state the estimated time it will take to complete if provided and the reason for the delay if provided.3. Key Discussion Points: What were the key things that were debated on or considered, in dot points? Include important information from the meeting relating to the main topic, and if there is information about who said it, include their names as well. List these in full sentences starting with the name of the person (if applicable) and then what was said.4. Final Outcome(s): Summarise the finalised, key decisions that were made during the meeting, in dot points?5. Action items: Summarise what needs to be done and by whom, including deadlines if provided, in dot points. Include the date and time of the next meeting, if it is mentioned."""
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(
        [f"{prompt} Here is the transcript you need to summarise: {transcript}"],
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        }
    )

    prompt_feedback = response.prompt_feedback

    if prompt_feedback:
        if "block_reason" in prompt_feedback:
            return HttpResponse("Unsafe transcript provided", status=400)

    response_data = {
        "summary": response.text
    }

    return JsonResponse(response_data, status=200)
