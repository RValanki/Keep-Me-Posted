// transcribe audio api function. 
// audioFile: .mp3 or .wav file, baseURL = String
// output: String

import { transcriptStore } from "../stores/transcript-store";

export let transcribe_audio = async (audioFile, baseURL) => {
    const postRequestString = baseURL + "/api/transcribe"; 

    const formData = new FormData();
    formData.append('audio_file', audioFile);

    try {
        const response = await fetch(postRequestString, { method: "POST", body: formData });
        const jsonResponse = await response.json();
        transcriptStore.set({
            transcript: jsonResponse.transcription
        })

        return jsonResponse.transcription; 

    } catch (error) {
        console.error("Error:", error);
        return null; 
    }
}
