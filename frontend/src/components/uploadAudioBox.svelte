<!--

    Upload Audio Box Component

    Authors: Parul Garg (pgar0011)
    Editied by:
    Last Modified: 10/05/24

-->

<script>

    import micIcon from "../assets/mic.png"

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

<div class="upload-box">

    <label for="uploadAudioBox" class="custom-input">
        <img class="mic-icon" src={micIcon} alt="Mic Icon" />
        <span class="first-line">Upload meeting audio</span>
        <span class="second-line">Must be under 120 minutes. MP3 or WAV formats accepted.</span>
    
    </label>

    <input type="file" class = "hidden-box" id="uploadAudioBox" name="uploadAudioBox" accept="audio/mp3, audio/wav">
</div>


<Dropzone on:drop={handleFilesSelect} accept=".mp3, .wav" class="uploadDropZone"></Dropzone>

{#if file}
  <p>File ready: {file.name} - {Math.floor(file.size / 1024)} KB</p>
{:else}
  <p>{errorMessage}</p>
{/if}


<style>

.upload-box{
    display: flex;
    justify-content: center;
    
}

.hidden-box{
    display: none;
}

.mic-icon{
    /* mic */

    width: 49px;
    height: 55px;


    /* Inside auto layout */
    flex: none;
    order: 0;
    flex-grow: 0;

}

.custom-input{

    /* Upload Audio Box */

    box-sizing: border-box;
    

    /* Auto layout */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 24px 0px;
    gap: 16px;

    width: 800px;
    height: 195px;

    /* Blue/25 */
    background: #F5FAFF;
    /* Blue/300 */
    border: 3px solid #84CAFF;
    border-radius: 5px;

    /* Inside auto layout */
    flex: none;
    order: 0;
    flex-grow: 0;

}

.first-line{

    /* Upload meeting audio */

    width: 250px;
    height: 30px;

    /* Text xl/Medium */
    font-style: normal;
    //font-family: "Inter";
    font-weight: 500;
    font-size: 24px;
    line-height: 30px;
    /* identical to box height, or 150% */
    text-align: center;

    /* Blue/800 */
    color: #1849A9;


    /* Inside auto layout */
    flex: none;
    order: 0;
    flex-grow: 0;


}

.second-line{
    /* Must be under 120 minutes. MP3 or WAV formats accepted. */

    width: 230px;
    height: 24px;

    /* Text md/Regular */
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 24px;
    /* or 150% */
    text-align: center;

    /* Gray/400 */
    color: #98A2B3;


    /* Inside auto layout */
    flex: none;
    order: 1;
    flex-grow: 0;

}

</style>