<!-- 

    The page where user uploads the audio file for Send Summary ASAP pathway.

    Author: Parul Garg (pgar0011)
    Edited By: Angelina Leung (aleu0007)
    Last Modified: 13/08/24

-->

<script>
  //required imports
  import Button from "../../components/button.svelte";
  import Topbar from "../../components/topbar.svelte";
  import UploadBox from "../../components/uploadAudioBox.svelte";
  import { goto } from "$app/navigation";
  import { apiStatusStore } from "../../stores/api-status-store";

  let nextPage = () => {
    goto("/generate_summary");
  };
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