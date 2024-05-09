<!-- Upload Box Component

    Contains upload box functionaliy and styling

    Author: zwan0318
    Edited by: bche0062
    Last modified: bche0062

 -->

<!--  -->

<script>
  import Dropzone from "svelte-file-dropzone";

  const MAX_DURATION_SECONDS = 7200; // 7200 seconds = 120 minutes

  let file;
  let errorMessage = '';

  function handleFilesSelect(e) {
    const { acceptedFiles } = e.detail;
    if (acceptedFiles.length > 0) {
      const selectedFile = acceptedFiles[0];
      if (selectedFile.name.endsWith('.mp3') || selectedFile.name.endsWith('.wav')) {
        const audio = new Audio(URL.createObjectURL(selectedFile));
        audio.addEventListener('loadedmetadata', () => {
          if (audio.duration <= MAX_DURATION_SECONDS) { 
            file = selectedFile;
            errorMessage = '';
          } else {
            errorMessage = 'File is too long. Please uploa  d a file shorter than 120 minutes.';
            file = null;
            //TODO: Replace with error message pop-up
          }
        });
      } else {
        errorMessage = 'Invalid file type. Please upload a .mp3 or .wav file.';
        file = null;
        //TODO: Replace with error message pop-up
      }
    }
  }
</script>


<Dropzone on:drop={handleFilesSelect} accept=".mp3, .wav" let:open>
  <div class="dropzone-label">
    <p>Upload meeting audio</p>
    <p>Must be under 120 minutes. MP3 or WAV formats accepted.</p>
  </div>
</Dropzone>
