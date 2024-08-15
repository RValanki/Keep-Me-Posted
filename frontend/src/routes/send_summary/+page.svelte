<!-- Summary will be sent after generation page

    The end page when user reaches the end before the summary has generated

    Author: Parul Garg
    Last Modified: 15/08/2024
-->

<script>
    import Button from "../../components/button.svelte";
    import Topbar from "../../components/topbar.svelte";
    import clock from "../../assets/clock.png"
    import { goto } from "$app/navigation";
    import Recipients from "../../components/sendRecipientsList.svelte";

    //the next page in the sequence
    let nextPage = () => {
        console.log("clicked");
        goto("/upload_audio")
    } 
  
</script>
    
<Topbar> </Topbar>

<!-- The div for the content of the page excluding the button -->
<div class="flex flex-col items-center pt-3 pb-10">
  
  <!-- The div for the headings and the clock icon of the page -->
  <div class="flex flex-col items-center pt-10">
    <!-- styling of the clock icon -->
    <div class="flex justify-center">
      <img class="flex flex-row justify-center items-center p-0 bg-indigo-200 flex-none order-none flex-grow-0 w-24 h-24" src={clock} alt="Clock" />
    </div>
    <!-- the heading and subheading of the page -->
    <h1 class="pt-3">Your Summary Will Be Sent..</h1>
    <p class=" text-center pt-5">After the summary has been completely generated, it will be sent automatically.</p>
  </div>
  
  <!-- The div for the recipients section of the page -->
  <div class="flex pt-10 gap-3.125">
    <div class="font-bold pr-8">Recipients:</div>
    <div class="flex flex-wrap">
      <Recipients></Recipients>
    </div>
  </div>
</div>

<!-- The button for sending another summary -->
<div class="absolute bottom-10 left-1/2 transform -translate-x-1/2">
  <div class="button-holder">
    <Button handleClick={nextPage} text="Send Another Summary"></Button>
  </div>
</div>

