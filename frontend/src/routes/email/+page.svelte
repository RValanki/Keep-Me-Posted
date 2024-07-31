<script>
  import Button from "../../components/button.svelte";
  import Topbar from "../../components/topbar.svelte";
  import EmailEntry from "../../components/emailEntry.svelte";
  import EmailList from "../../components/emailList.svelte";
  import { goto } from "$app/navigation";
  import { ContactsStore } from "../../stores/contacts-store"

  let nextPage = () => {
    goto("/choose_pathway")
    console.log("todo go to next page");
  };

  let previousPage = () => {
    // todo
    console.log("todo go to previous page");
  };
</script>

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

<!-- <div class="absolute bottom-8 left-8">
  <Button
    handleClick={previousPage}
    icon="../../src/assets/arrow-left.png"
    text="View Summary"
  ></Button>
</div> -->
