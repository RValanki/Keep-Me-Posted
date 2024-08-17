import { writable } from 'svelte/store'

export const transcriptStore = writable({
    transcript: ""
})

export const sendWithTranscriptStore = writable(true)
