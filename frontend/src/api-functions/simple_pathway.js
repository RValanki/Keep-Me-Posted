// transcribe audio api function. 
// audioFile: .mp3 or .wav file, baseURL = String
// output: String

import { transcribe_audio } from "./transcribe-audio"
import { updateStatus } from "../stores/simple-pathway-store"
import { send_summary } from "./send_summary"
import { send_email } from "./send_email"
import { ContactsStore } from "../stores/contacts-store"

let text = " Speaker A: Smoke from hundreds of wildfires in Canada is triggering air quality alerts throughout the US. Skylines from Maine to Maryland to Minnesota are gray and smoggy. And in some places, the air quality warnings include the warning to stay inside. We wanted to better understand what's happening here and why. So he called Peter DiCarlo, an associate professor in the department of Environmental Health and Engineering at Johns Hopkins University. Good morning. Professor. Speaker B: Good morning. g us and sharing this expertise with us. Speaker B: Thank you for having me. "

export let simple_pathway = async (audioFile, baseURL) => {
    updateStatus("Transcribe")
    await transcribe_audio(audioFile, baseURL)

    updateStatus("Summary")
    await send_summary(text, baseURL)

    updateStatus("Email")
    let contacts = []
    const unsubscribe = ContactsStore.subscribe(value => {
        contacts = value;
      });    
    console.log(contacts)
    await send_email(text, "bob", contacts, baseURL)

    updateStatus("Complete")
}
