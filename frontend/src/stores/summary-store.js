import { writable } from 'svelte/store'

export const summaryStore = writable({
    summary: "",
    subject: ""
})