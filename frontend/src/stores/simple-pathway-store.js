import { writable } from 'svelte/store'

export const api_status = writable({
    api_status: ""
})

// Function to update the status in the store
export function updateStatus(newStatus) {
    api_status.update(oldStatus => {
        return { ...oldStatus, status: newStatus };
    });
}

