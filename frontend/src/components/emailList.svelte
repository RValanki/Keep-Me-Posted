<script>
  import { ContactsStore } from "../stores/contacts-store"

  let remove_email = (email) => {
    ContactsStore.update((prev) => prev.filter((contact) => contact != email));
  };
</script>

<div class="flex py-8 flex-wrap justify-center self-center max-w-xl gap-2">
  {#each $ContactsStore as email}
    <div class="flex align-middle p-2 gap-1 bg-[#F8F9FC] rounded-md">
      <div class="text-xs">{email}</div>
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
