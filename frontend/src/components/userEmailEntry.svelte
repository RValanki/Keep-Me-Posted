<script>
  import Button from "./button.svelte";
  import { ContactsStore } from "../stores/contacts-store";
  import { isOpen, isCancelled } from "../stores/user-email-popup-store";

  let emailString = "";
  let emailErrorString = "";

  let handleCancel = () => {
    isCancelled.set(true);
    isOpen.set(false);
  };

  let handleAddEmail = () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailRegex.test(emailString)) {
      ContactsStore.update((prev) => [...prev, emailString]);
      emailString = "";
      isOpen.set(false);
      isCancelled.set(true);
    } else {
      emailErrorString = "Please enter a valid email address.";
      setTimeout(() => {
        emailErrorString = "";
      }, 3000);
    }
  };
</script>

<div
  hidden={!$isOpen}
  class="z-50 w-96 h-80 absolute left-1/2 top-1/4 -translate-x-48 text-center bg-white border rounded-xl"
>
  <div class="text-l p-4">Would you like to recieve a copy of the summary?</div>

  <div class="text-base px-4 text">
    Since you are not logged in, we require you to add your email.
  </div>

  <div class="text-left text-sm px-4 py-2">Email address</div>
  <input
    class="border border-slate-300 p-2 rounded-xl text-left w-11/12 text-sm"
    type="email"
    placeholder="johndoe@email.com"
    bind:value={emailString}
  />

  <div class="flex justify-evenly px-4 pt-8 items-center">
    <Button
      type="secondary"
      text="Cancel"
      fullWidth={true}
      handleClick={handleCancel}
    ></Button>
    <Button
      type="primary"
      text="Add myself"
      fullWidth={true}
      handleClick={handleAddEmail}
    ></Button>
  </div>
</div>
