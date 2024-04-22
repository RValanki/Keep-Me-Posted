from django.shortcuts import render
from django.http import HttpResponse
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Create your views here.
def generate_summary(request):
    ## Implement the summarisation logic here

    load_dotenv()

    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = """The user will give you a meeting transcript.You are an expert in concisely summarising meeting transcripts so that people wanting to review what happened in the meeting can read this summary and understand the key details of what was discussed and any important outcomes. They should be able to understand what tasks have been assigned, when it is due, and the people that have been assigned to it. This should be done in a professional manner, so you must ensure that any profanity or slurs encountered is omitted from the final output. Ensure to NOT include sensitive information such as banking information, passwords, addresses. Quote what someone said with their name if their names are included in the summary.Below is the structure you should follow to generate a summary. Using the following headings take note of the additional information I have included to guide what you include under each heading.1. Start with a suitable title for the summary2. Meeting Agenda: Start with what the meeting’s purpose was and what was the overarching agenda. Include progress on previous tasks if this has been discussed. If the tasks are not completed, state the estimated time it will take to complete if provided and the reason for the delay if provided.3. Key Discussion Points: What were the key things that were debated on or considered, in dot points? Include important information from the meeting relating to the main topic, and if there is information about who said it, include their names as well. List these in full sentences starting with the name of the person (if applicable) and then what was said.4. Final Outcome(s): Summarise the finalised, key decisions that were made during the meeting, in dot points?5. Action items: Summarise what needs to be done and by whom, including deadlines if provided, in dot points. Include the date and time of the next meeting, if it is mentioned."""
    transcript4 = """ good morning everyone lets dive into our agenda for todays meeting starting with a review of our progress on quarter 1 tasks
absolutely overall sarah and i have seen some significant achievements but there have also been delays in certain areas particularly with the rollout of our new software platform
yes unfortunately we encountered unforeseen technical challenges that have impacted our timeline were actively working to address these issues and anticipate an additional two weeks for completion it should be done by 3rd march if we cannot meet this deadline the complexity of integrating the new security features will be the main reason as they require more testing than initially anticipated
thank you for the update michael its crucial that we address these delays promptly while ensuring the quality of our deliverables remains top-notch if any task is expected to go beyond this two week extension i want a comprehensive review of why and how were addressing it
agreed moving on to our next agenda item lets discuss budget allocation for our upcoming projects particularly the marketing campaign for our new product launch
absolutely we need to ensure we have sufficient funds allocated to execute our marketing strategies effectively and drive consumer interest and engagement in terms of budgeting if adjustments are needed it will be due to the increased cost of digital advertising platforms which we are closely monitoring i can look further into these costs this week as well and contact the marketing team thanks for that sarah is there anything you want to add john
and lets not forget about resource allocation we need to make sure we have the right people with the right skills assigned to each project to ensure success should there be any shortfall in skills well look into external training or hiring as necessary
definitely developing a comprehensive marketing plan that incorporates both traditional and digital channels will be essential for reaching our target audience and driving sales if we face delays in launching the campaign it will likely be due to awaiting final product adjustments based on the latest market research would anyone like to get started on this plan yes im happy to thanks michael
agreed additionally we should leverage the valuable insights weve gathered from recent customer surveys to tailor our products and services to better meet their needs and preferences if implementing these insights takes longer its because were ensuring the changes are data-driven and customer-focused
absolutely lets finalize these decisions we approve the budget for quarter 2 projects and allocate resources accordingly well also set revised timelines for the delayed tasks and work diligently to expedite their completion should any project exceed its timeline immediate escalation to the project team for reevaluation will be required
sounds like a plan ill get started on developing the marketing plan right away ensuring it aligns with our strategic objectives and resonates with our target audience any delays in this plan will be communicated early with reasons and proposed solutions would you like to assist me with this michael yes sure thing
and ill coordinate with the relevant departments to ensure we address any operational challenges and streamline our processes to meet our deadlines effectively continuous monitoring will allow us to identify any potential delays early and adjust our plans accordingly
so to reiterate in the coming week michaeel will be starting the marketing plan taking into consideration insight from customer surveys sarah you will be contacting marketing to investigate the costs for our digital marketing campaigns and i will be looking into skill gaps and seeing whether we need additional help through hiring yes sounds good also dont forget to keep working on the rollout of our new software platform
great lets remain proactive and focused as we work towards achieving our goals thank you everyone should we have our next meeting in a weeks time yeah sure when is everyone free im free on monday me too how about you michael im not free on monday but i can do wednesday if thats ok yeah thats fine lets do it next wednesday 22nd february at 12pm
thank you john
thank you"""

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(
        [f"{prompt} Here is the transcript you need to summarise: {transcript4}"],
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        }
    )
    print(response.prompt_feedback)
    print(response.text)

    return HttpResponse("Generated summary goes here" + response.text)
