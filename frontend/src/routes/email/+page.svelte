<script>
  import Button from "../../components/button.svelte";
  import Topbar from "../../components/topbar.svelte";
  import EmailEntry from "../../components/emailEntry.svelte";
  import EmailList from "../../components/emailList.svelte";
  import { goto } from "$app/navigation";
  import { ContactsStore } from "../../stores/contacts-store";
  import { authStore } from "../../stores/auth-store"
  import { isOpen, isCancelled} from "../../stores/user-email-popup-store";
  import UserEmailEntry from "../../components/userEmailEntry.svelte";
  import { onMount } from "svelte";

  let nextPage = () => {
    if ($authStore.email.length == 0 && !($isCancelled)) {
      isOpen.set(true)
    } else {
      goto("/choose_pathway")
    }
  };

  let previousPage = () => {
    // todo
    console.log("todo go to previous page");
  };
</script>


<UserEmailEntry></UserEmailEntry>

<div class="{$isOpen ? "opacity-50" : ""}">
  <Topbar></Topbar>

  <div class="flex flex-col text-center">
    <div class="flex flex-col p-12 gap-4">
      <h1>Add Recipients</h1>
      <h2 class="font-normal">
        Add the emails you would like to send the summary to.
      </h2>
    </div>

    <EmailEntry></EmailEntry>
    <EmailList></EmailList>
  </div>

  <div class="absolute bottom-8 right-8">
    <Button
      handleClick={nextPage}
      icon="../../src/assets/arrow-right.png"
      text="Choose Pathway"
      disabled={$ContactsStore.length == 0}
    ></Button>
  </div>
</div>

<!-- <div class="absolute bottom-8 left-8">
  <Button
    handleClick={previousPage}
    icon="../../src/assets/arrow-left.png"
    text="View Summary"
  ></Button>
</div> -->
