<!--

    Loading Bar Component

    consists of 5 parts
    1. loading bar = a solid bar
    2. progress bar = the bar that animates over the loading bar
    3. progress bar progress = a number showing the percentage of which the progress bar covers the loading bar
    4. cancel button = cancels the action that caused the loading bar to trigger
    5. description = a text box that describes what stage the process is at with an accompanying icon

    Authors: Angelina Leung
    Edited by:
    Last Modified: 28/07/24

-->

<script>
    import uploadIcon from "../assets/upload-icon.png";
    import fileIcon from "../assets/file-icon.png";

    let progressBarWidth = 0;
    let progressBarProgress;
    let progressBarDisplay = 0;
    let loadingBarWidth;
    let progressBarMax = 1;
    let currentProgress = 0;

    var ICON_DICT = {
        "Uploading meeting audio": uploadIcon,
        "Generating summary": fileIcon,
    };
    
    /**
     * stop the progress bar from going past 100%
     */
    $: switch (progressBarWidth) {
        case Math.round(loadingBarWidth * progressBarMax):
        clearInterval(progressBarProgress);
    }

    /**
     * increment the progress bar by 1
     */
    const progression = () => {
        if (progressBarWidth < currentProgress * loadingBarWidth) {
            progressBarWidth += 1;
            progressBarDisplay = Math.round(
                (progressBarWidth / loadingBarWidth) * 100,
            );
        }
    };

    /**
     * calls progression (see function above) every 10 milliseconds
     */
    const makeProgression = () => {
        loadingBarWidth = document.getElementById("loadingBar").clientWidth;
        progressBarProgress = setInterval(progression, 10);
    };

    /**
     * increment progress bar depending on which api the process is at
     * @param api_status which api stage the process is in. values include: Transcribe, Summary, Email, Complete
     */
    export function updateLoadingBar(api_status) {
        if (api_status == "Transcribe") {
        currentProgress = 0.4;
        makeProgression();

        setTimeout(() => {
            currentProgress = 0.55;
            makeProgression();
        }, 8000);

        } else if (api_status == "Summary") {
        updateLoadingBarDesc("Generating summary");
        currentProgress = 0.7;
        makeProgression();

        } else if (api_status == "Email") {
        currentProgress = 0.9;
        makeProgression();

        } else if (api_status == "Complete") {
        currentProgress = 0.99;
        makeProgression();
        setTimeout(() => {
            goto("/sent");
        }, 2500);
        }
    }

    /**
     * Update the loading bar desc 
     * @param newText replacement description
     */
    function updateLoadingBarDesc(newText) {
        var firstLine = document.querySelector("loadingBarTextDesc");
        firstLine.textContent = newText + "...";

        // Change icon source
        var icon = document.getElementById("loadingBarIcon");
        icon.src = ICON_DICT[newText];
    }

</script>

<!-- COMPONENT -->
<div class="flex space-x-5 p-5"> <!-- loading-bar -->
    <span class="w-full bg-gray-200 rounded-full h-2.5 self-center"> <!-- progress-bar-base -->
        <span class="bg-blue-600 h-2.5 rounded-full" style="width: {progressBarWidth}px"></span> <!-- progress-bar -->
    </span>
    <span class="text-sm font-medium text-blue-70"><b>{progressBarDisplay}</b>%</span> <!-- progress-number -->
</div>

<div class="flex space-x-5 justify-center p-5"> <!-- loading-bar-desc -->
    <img class="w-5.5 h-5 self-center" src={uploadIcon} alt="Icon" /> <!-- loading-bar-icon -->
    <span class="text-blue-800 text-base">Uploading Meeting Audio...</span>
</div>