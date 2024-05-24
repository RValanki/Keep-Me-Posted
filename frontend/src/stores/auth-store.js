import { writable } from 'svelte/store'

export const authStore = writable({
    email: "",
    loggedIn: false
})

export function updateAuth(email, loggedIn) {
    authStore.update(state => ({
        ...state,
        email,
        loggedIn
    }));
}