<!-- 

    The page where user uploads the audio file for Send Summary ASAP pathway.

    Author: Parul Garg (pgar0011)
    Edited By: Angelina Leung (aleu0007), Maureen Pham (mpha0039), Danny Leung (dleu0007)
    Last Modified: 19/08/24

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

  // Function to navigate to the summary page and update the status to "Viewed"
  let nextPage = () => {
    apiStatusStore.set("Viewed");
    goto("/generate_summary");
  };

  // Function to handle re-upload action and reset the status
  function handleReUpload() {
    apiStatusStore.set("");
    resetStores();
  }
  // Automatically route to the summary generated page when the summary is complete
  $: if ($apiStatusStore === "Complete") {
    nextPage();
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
    <div class="subheading mb-16 mt-4">
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
        icon="../../src/assets/arrow-right.png"
        text="View Summary"
        disabled={ $apiStatusStore == "" }
        type={ $apiStatusStore == "" ? "disabled" : "primary" }
      ></Button>
    </div>
  </body>
</html>