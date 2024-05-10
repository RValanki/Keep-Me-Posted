<!-- Upload Box Component

    Contains upload box functionaliy and styling

    Author: zwan0318
    Edited by: bche0062
    Last modified: 10/05/2024

 -->

<!--  -->

<script>
  import Dropzone from "svelte-file-dropzone";

  const MAX_DURATION_SECONDS = 7200; // 7200 seconds = 120 minutes

  let file;
  let errorMessage = '';

  function handleFilesSelect(e) {
    const { acceptedFiles } = e.detail;
    file = null; // Reset the file each time new files are selected

    if (acceptedFiles.length > 0) {
      const selectedFile = acceptedFiles[0];
      // Initial file type check before loading it as an audio source
      if (!selectedFile.name.endsWith('.mp3') && !selectedFile.name.endsWith('.wav')) {
        errorMessage = 'Invalid audio format! \n Your meeting audio must be in MP3 or WAV format.';
        return; // Exit the function early if file type is incorrect
      }

      const audio = new Audio(URL.createObjectURL(selectedFile));
      audio.addEventListener('loadedmetadata', () => {
        if (audio.duration <= MAX_DURATION_SECONDS) {
          file = selectedFile;
          errorMessage = '';
        } else {
          errorMessage = 'Meeting duration exceeded! \n Your meeting audio should be less than 120 minutes.';
          file = null;
          //TODO: Replace with error message pop-up
        }
      });
    } else {
      errorMessage = 'Invalid audio format! Your meeting audio must be in MP3 or WAV format';
    }
  }
</script>

<Dropzone on:drop={handleFilesSelect} accept=".mp3, .wav">
  <div class="dropzone-label">
    <p>Upload meeting audio</p>
    <p>Must be under 120 minutes. MP3 or WAV formats accepted.</p>
  </div>
</Dropzone>

{#if file}
  <p>File ready: {file.name} - {Math.floor(file.size / 1024)} KB</p>
{:else}
  <p>{errorMessage}</p>
{/if}

