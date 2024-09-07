<!-- 

    The page where user uploads the audio file for Send Summary ASAP pathway.

    Author: Parul Garg (pgar0011)
    Edited By: Angelina Leung (aleu0007), Maureen Pham (mpha0039), Danny Leung (dleu0007), Rohit Valanki (rval0008)
    Last Modified: 07/09/24

-->

<script>
  //required imports
  import Button from "../../components/button.svelte";
  import Topbar from "../../components/topbar.svelte";
  import Toggle from '../../components/toggle.svelte';
  import UploadBox from "../../components/uploadAudioBox.svelte";
  import { goto } from "$app/navigation";
  import { apiStatusStore } from "../../stores/api-status-store";
  import { resetStores } from "../../stores/reset-store";
  import RightArrow from "../../assets/arrow-right.png"
  import { onMount } from 'svelte';
  import { updateAuth } from '../../stores/auth-store.js';

  onMount(() => {
    // Get the current URL
    const currentUrl = window.location.href;
    
    // Create a URL object
    const url = new URL(currentUrl);
    
    // Extract the email from the query parameters
    const email = url.searchParams.get('email');
    
    if (email) {
      updateAuth(email, true);
      
    } 
  });

  // Function to navigate to the summary page and update the status to "Viewed"
  let nextPage = () => {
    goto("/generate_summary");
  };

  // Function to handle re-upload action and reset the status
  function handleReUpload() {
    apiStatusStore.set("");
    resetStores();
  }
</script>

<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Upload Meeting Audio</title>
  </head>
  <body>
    <Topbar />
    <h1 class="mt-12">Upload Meeting Audio</h1>
    <div class="subheading mb-16 mt-4 px-2">
      Upload your meeting audio for us to summarise.
    </div>

    <UploadBox />
  
    <Toggle/>
    
    {#if ($apiStatusStore == "Complete")}
      <div class="flex justify-center items-center p-3">
        <Button 
          type="secondary"
          text="Re-Upload Audio"
          handleClick={handleReUpload}
        />
      </div>
    {/if}
  
    <div class="absolute bottom-8 right-8">
      <Button
        handleClick={nextPage}
        icon={RightArrow}
        text="View Summary"
        disabled={ $apiStatusStore == "" }
        type={ $apiStatusStore == "" ? "disabled" : "primary" }
      ></Button>
    </div>
  </body>
</html>