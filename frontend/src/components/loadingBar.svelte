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
    import {Progressbar} from 'flowbite-svelte';
    import { sineOut } from 'svelte/easing';

    let progress = 0;
    let description = "Uploading Meeting Audio...";
    let iconSrc = uploadIcon;

    /**
     * Function to update the progress based on value input
    */ 
    function updateLoadingBar(value) {
        if (value > progress){
            progress = value
        }
        if (progress < 50) {
            description = "Uploading Meeting Audio...";
            iconSrc = uploadIcon;
        }
        if (progress > 50) {
            description = "Generating Summary...";
            iconSrc = fileIcon;
        }
    }
</script>

<!-- COMPONENT -->
<div class="flex space-x-5 p-5 pb-0"> <!-- loading-bar -->
    <Progressbar
        {progress}
        animate
        precision={2}
        tweenDuration={1500}
        easing={sineOut}
        size="h-6"
        class="mb-8"
        color="blue"
    />
    <span class="text-sm font-medium text-gray-700">{progress}%</span> <!-- progress-number -->
</div>

<div class="flex space-x-5 justify-center"> <!-- loading-bar-desc -->
    <img class="w-5.5 h-5 self-center" src={iconSrc} alt="Icon" /> <!-- loading-bar-icon -->
    <span class="text-blue-800 text-base">{description}</span>
</div>