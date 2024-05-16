// transcribe audio api function. 
// audioFile: .mp3 or .wav file, baseURL = String
// output: String

import { transcribe_audio } from "./transcribe-audio"
import { updateStatus } from "../stores/simple-pathway-store"
import { send_summary } from "./send_summary"
import { send_email } from "./send_email"
import { ContactsStore } from "../stores/contacts-store"


export let simple_pathway = async (audioFile, baseURL) => {
    updateStatus("Transcribe")
    const transcript = await transcribe_audio(audioFile, baseURL)
    console.log(transcript)

    updateStatus("Summary")
    const summary = await send_summary(transcript, baseURL)
    console.log(summary)

    updateStatus("Email")
    let contacts = []
    const unsubscribe = ContactsStore.subscribe(value => {
        contacts = value;
      });    
    console.log(contacts)
    await send_email(summary, "Regular Show", contacts, baseURL)

    updateStatus("Complete")
}
