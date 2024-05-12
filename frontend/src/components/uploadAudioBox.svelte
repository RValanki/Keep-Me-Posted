<!--

    Upload Audio Box Component

    Authors: Parul Garg (pgar0011)
    Editied by: Benjamin Cherian, Zihao Wang, Angelina Leung
    Last Modified: 12/05/24

-->
<!-- JavaScript -->
<script>

  import micIcon from "../assets/mic-icon.png"
  import uploadIcon from "../assets/upload-icon.png"
  import radioIcon from "../assets/radio-icon.png"
  import fileIcon from "../assets/file-icon.png"
  import transparent from "../assets/transparent.png"


  import Dropzone from "svelte-file-dropzone";

  const MAX_DURATION_SECONDS = 7200; // 7200 seconds = 120 minutes

  // ------------------------------------------ File Handling
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

      const audio = new Audio(URL.createObjectURL(selectedFile));  // Create new Audio HTML object, create URL used as source for audio element
      // makeProgression()  // Trigger the loading bar
      updateUploadBoxContents('Uploading Meeting Audio')  // Change box to show 'Uploading Meeting Audio'
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

  // ------------------------------------------ Progress Bar
  let progressBarWidth = 0
  let progressBarProgress
  let progressBarDisplay = 0
  let loadingBarWidth;

  $: if (progressBarWidth === loadingBarWidth) {
    clearInterval(progressBarProgress)
  }

  const progression = () => {
    progressBarWidth += 1
    progressBarDisplay = Math.round(progressBarWidth/loadingBarWidth * 100)
  }

  const makeProgression = () => {
    loadingBarWidth = document.getElementById("loadingBar").clientWidth
    document.getElementById("progressBar").style.display = "block"
    progressBarWidth = 0
    progressBarDisplay = 0
    progressBarProgress = setInterval(progression, 1)
  }

  // ------------------------------------------ Box Contents
  function updateUploadBoxContents() {
    // TODO change text based on Response rather than the loading bar
    const uploadBoxInner = document.getElementById('uploadBoxInner')  // get the span class

    // remove other inner elements
    uploadBoxInner.classList.remove('mic-icon')
    uploadBoxInner.classList.remove('first-line')
    uploadBoxInner.classList.remove('second-line')
    
    // update loading-line text

    const icon = document.createElement('img');
    loadingLine.textContent = 'Uploading Meeting Audio';

    uploadBoxInner.appendChild(loadingLine)   
     
    // when a file is dragged in show the loading bar and 'Uploading meeting audio'

    // when file is sent to assemblyai; show 'Transcribing audio'
    // when file is sent to gemini; show 'Generating Summary'
    // when file is sent to assemblyai; show 'transcribing audio'

    //
  }
</script>

<!-- COMPONENT -->
<div class="upload-box">
  <label for="uploadAudioBox" class="custom-input">
    <Dropzone on:drop={handleFilesSelect} accept=".mp3, .wav">
      <span id = "uploadBoxInner">
        <!-- what the box has initially-->
        <img class="mic-icon" src={micIcon} alt="Mic Icon" />
        <span class="first-line">Upload meeting audio</span>
        <span class="second-line">Must be under 120 minutes. MP3 or WAV formats accepted.</span>
        
        <!-- what the box has after a file is put in it-->
        <span class="loading-line">
          <img class="loading-line-icon" src={} alt="Icon"/>
          <span class="loading-line-text"></span>
        </span>

      </span>
    </Dropzone>
  </label>
</div>

<!-- <div id="loadingBar">
  <div id="progressBar" style="width: {progressBarWidth}px"></div>
  <div id="progressNumber"><b>{progressBarDisplay}</b>%</div>
</div> -->

<div class="status-message">
  {#if file}
    <p>File ready: {file.name}</p>
  {:else}
    <p>{errorMessage}</p>
  {/if}
</div>


<!-- Styling -->
<style>

.upload-box{
  display: flex;
  justify-content: center;
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
  padding: 0px 0px;
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
  font-family: "Inter";
  font-weight: 500;
  font-size: 20px;
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
  font-size: 15px;
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

.loading-line {
  /* 
  /* Auto layout */
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0px;
  gap: 4px;

  width: 256px;
  height: 30px;

  /* Inside auto layout */
  flex: none;
  order: 1;
  flex-grow: 0;
} 

.status-message {
  text-align: center;
  padding: 10px;
  color: #333;
  font-size: 16px;
  margin-top: 100px;
}

#loadingBar {
  border: 1px solid;
  width: 40%;
  height: 40px;
  top: 51%;
  left: 50%;
  transform: translate(-50%, -50%);
  position: absolute;
  background-color: grey;
  border-radius: 30px 30px 30px 30px;
}

#progressBar {
  display: none; 
  height: 40px;
  top: 50%;
  left: 50%;
  position: absolute;
  top: 0%;
  left: 0%;
  background-color: blue;
  border-radius: 30px 30px 30px 30px;
}

#progressNumber {
  position: absolute;
  top: 25%;
  left: 101%;
}

</style>

