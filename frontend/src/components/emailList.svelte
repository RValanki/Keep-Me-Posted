<script>
  import { ContactsStore } from "../stores/contacts-store"
  import { onMount } from "svelte";

onMount(() => {
    ContactsStore.update((prev) => [])
    for(let i = 0; i < 15; i++) {
        ContactsStore.update((prev) => [...prev, "111" * i + "@gmail.com"]);
    }
})

  let remove_email = (email) => {
    ContactsStore.update((prev) => prev.filter((contact) => contact != email));
  };
</script>

<div class="flex py-8 flex-wrap justify-center self-center max-w-xl gap-2">
  {#each $ContactsStore as email}
    <div class="flex align-middle p-2 bg-[#F8F9FC] rounded-md">
      <div class="token">{email}</div>
      <button on:click={remove_email(email)}
        ><img
          class="h-4"
          src="../../src/assets/remove-icon.png"
          alt="Remove Icon"
        /></button
      >
    </div>
  {/each}
</div>
