// transcribe audio api function. 
// audioFile: .mp3 or .wav file, baseURL = String
// output: String

import { transcribe_audio } from "./transcribe-audio"
import { updateStatus } from "../stores/simple-pathway-store"
import { send_summary } from "./send_summary"
import { send_email } from "./send_email"
import { ContactsStore } from "../stores/contacts-store"


export let simple_pathway = async (audioFile, baseURL) => {
    //Transcribe api to get transcription
    updateStatus("Transcribe")
    const transcript = await transcribe_audio(audioFile, baseURL)
    console.log(transcript)

    //Summary api to get summary
    updateStatus("Summary")
    const summary = await send_summary(transcript, baseURL)
    console.log(summary)

    //Send email api to send email
    updateStatus("Email")
    let contacts = []
    ContactsStore.subscribe(value => {
        contacts = value;
      });    
    console.log(contacts)
    await send_email(summary, "Regular Show", contacts, baseURL)
    
    //Update status to complete
    updateStatus("Complete")
}
