// transcribe audio api function. 
// audioFile: .mp3 or .wav file, baseURL = String
// output: String

import { transcribe_audio } from "./transcribe-audio"
import { updateStatus } from "../stores/simple-pathway-store"

export let simple_pathway = async (audioFile, baseURL) => {
    updateStatus("Transcribe")
    await transcribe_audio(audioFile, baseURL)
    updateStatus("Summary")
    await transcribe_audio(audioFile, baseURL) //Placeholder
    updateStatus("Email")
    await transcribe_audio(audioFile, baseURL) //Placeholder
    updateStatus("Complete")
}
