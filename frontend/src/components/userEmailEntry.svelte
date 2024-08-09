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

{#if $isOpen}
    <!-- Overlay -->
    <div class="fixed inset-0 bg-black bg-opacity-50 z-40" on:click={handleCancel}></div>

    <!-- Popup Content -->
     <div class="fixed inset-0 flex items-center justify-center z-50">
        <div class="p-4 w-full max-w-md bg-white border rounded-xl">
            <div class="h2 text-center text-gray-900 font-semibold p-2">Would you like to recieve a copy of the summary?</div>

      <div class="h3 text-center text-gray-500 text-base p-1">
        Since you are not logged in, we require you to add in your email.
      </div>

      <div class="text-left font-medium text-sm text-gray-700 px-4 py-2">Email address</div>
      <input
        class="border flex ml-5 border-slate-300 p-2 rounded-xl text-left w-11/12 text-sm text-gray-700"
        type="email"
        placeholder="you@kmp.com"
        bind:value={emailString}

      />

      <div class="flex shrink justify-evenly object-cover pb-1 pt-8 items-center">
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
    </div>
{/if}