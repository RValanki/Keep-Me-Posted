<!-- Upload Box Component

    Contains upload box functionaliy and styling

    Author: zwan0318
    Edited by: bche0062
    Last modified: bche0062

 -->

<!--  -->

<script>
  import Dropzone from "svelte-file-dropzone";

  let file;
  let errorMessage = '';

  function handleFilesSelect(e) {
    const { acceptedFiles } = e.detail;
    if (acceptedFiles.length > 0) {
      const selectedFile = acceptedFiles[0];
      if (selectedFile.name.endsWith('.mp3') || selectedFile.name.endsWith('.wav')) {
        const audio = new Audio(URL.createObjectURL(selectedFile));
        audio.addEventListener('loadedmetadata', () => {
          if (audio.duration <= 7200) { // 7200 seconds = 120 minutes
            file = selectedFile;
            errorMessage = '';
          } else {
            //Error message
          }
        });
      } else {
        //Error message
      }
    }
  }
</script>


<Dropzone on:drop={handleFilesSelect} />
{#if file}
  <p>File ready: {file.name} - {Math.floor(file.size / 1024)} KB</p>
{:else}
  <p>{errorMessage}</p>
{/if}
