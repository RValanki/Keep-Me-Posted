import { writable } from 'svelte/store';

const initialState = {
  email: "",
  loggedIn: false
};

export const authStore = writable(initialState);

export function updateAuth(email, loggedIn) {
  authStore.update(state => ({
    ...state,
    email,
    loggedIn
  }));
}

export function getAuth() {
  let currentValue;
  
  // Subscribe to the store to get the current value
  const unsubscribe = authStore.subscribe(value => {
    currentValue = value;
  });
  
  // Immediately unsubscribe after getting the value
  unsubscribe();
  
  return currentValue;
}
