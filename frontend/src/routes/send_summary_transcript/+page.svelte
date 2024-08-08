<!-- Summary and Transcipt will be sent after generation page

    The end page when user reaches the end before the summary has generated with transcipt attached

    Author: Parul Garg
    Last Modified: 8/08/2024
-->



<script>
    import Button from "../../components/button.svelte";
    import Topbar from "../../components/topbar.svelte";
    import { ContactsStore } from "../../stores/contacts-store";
    import clock from "../../assets/clock.png"
    import { goto } from "$app/navigation";

    
    //the next page in the sequence
    let nextPage = () => {
        console.log("clicked");
        goto("/upload-audio")
    } 
  
</script>
    
<Topbar> </Topbar>

<div class="flex flex-col items-center pt-3 pb-10">
  

  <div class="flex flex-col items-center pt-10">
    <div class="flex justify-center">
      <img class="flex flex-row justify-center items-center p-0 bg-indigo-200 flex-none order-none flex-grow-0 w-24 h-24" src={clock} alt="Clock" />
    </div>
    <h1 class="pt-3">Your Summary and Transcript Will Be Sent..</h1>
    <p class="pt-5">After the summary has been completely generated, it will be sent automatically with the transcript.</p>
  </div>
  
  <div class="flex pt-10 gap-3.125">
    <div class="font-bold">Recipients:</div>

    <div class="flex flex-wrap gap-0.3125">
      
      {#each $ContactsStore as email}
      <div class="flex bg-gray-100 p-1 rounded justify-center items-center gap-3.125">
        <div class="token">{email}</div>
      </div>
    {/each}
    </div>
  </div>
</div>


<div class="absolute bottom-10 left-1/2 transform -translate-x-1/2">
  <div class="button-holder">
    <Button handleClick={nextPage} text="Send Another Summary"></Button>
  </div>
</div>

