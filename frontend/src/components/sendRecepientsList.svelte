<!-- Send Recepients Component

    The list of the recepients displayed on the end pages of the website

    Author: Parul Garg
    Last Modified: 10/08/2024
-->

<script>
    import { ContactsStore } from "../stores/contacts-store"

</script>
  
<div class="flex pb-8 flex-wrap justify-center self-center max-w-xl gap-2">
    {#each $ContactsStore as email}
      <div class="flex align-middle p-2 gap-1 bg-[#F8F9FC] rounded-md">
        <div class="text-xs">{email}</div>
      </div>
    {/each}
</div>
  