<!--

    Loading Bar Component

    consists of 5 parts
    1. Progressbar from flowbite-svelte
    2. cancel button = cancels the action that caused the loading bar to trigger
    3. description = a text box that describes what stage the process is at with an accompanying icon

    Authors: Angelina Leung
    Edited by:
    Last Modified: 6/08/24

-->

<script>
  import uploadIcon from "../assets/upload-icon.png";
  import fileIcon from "../assets/file-icon.png";
  import { Progressbar } from "flowbite-svelte";
  import { sineOut } from "svelte/easing";
  import { apiStatusStore } from "../stores/api-status-store";

  export let progress = 0;
  let targetProgress = 0; // Target value for the progress bar, used for animating
  let description = "Uploading Meeting Audio...";
  let iconSrc = uploadIcon;

  $: $apiStatusStore,
    (() => {
      console.log("api changed");
      if ($apiStatusStore == "") {
        targetProgress = 0;
      } else if ($apiStatusStore == "Transcribe") {
        targetProgress = 40;
      } else if ($apiStatusStore == "Summary") {
        targetProgress = 90;
      } else {
        targetProgress = 100;
      }
      updateLoadingBar();
      animateProgress();
    })();

  /**
   * Function to update the progress based on value input
   */
  export function updateLoadingBar() {
    if (progress <= 50) {
      description = "Uploading Meeting Audio...";
      iconSrc = uploadIcon;
    } else {
      description = "Generating Summary...";
      iconSrc = fileIcon;
    }
  }

  /**
   * Smoothly update the progress number
   */
  function animateProgress() {
    const speed = 1; // Speed of animation
    if (progress < targetProgress) {
      progress += speed;
      if (progress >= targetProgress) {
        progress = targetProgress;
        return;
      }
      setTimeout(() => {
        animateProgress();
      }, 50);
    }
  }
</script>

<!-- COMPONENT -->
<div class="flex space-x-5 p-5 h-20">
  <!-- loading-bar -->
  <Progressbar
    {progress}
    animate
    precision={2}
    tweenDuration={1500}
    easing={sineOut}
    size="h-2"
    class="self-center"
    color="blue"
  />
  <span class="text-sm font-medium text-gray-700 w-10 self-center"
    >{Math.round(progress)}%</span
  >
  <!-- progress-number -->
</div>

<div class="flex space-x-5 justify-center">
  <!-- loading-bar-desc -->
  <img class="w-5.5 h-5 self-center" src={iconSrc} alt="Icon" />
  <!-- loading-bar-icon -->
  <span class="text-blue-800 text-base">{description}</span>
</div>
