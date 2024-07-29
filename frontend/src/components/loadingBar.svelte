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
<div class="flex justify-between mb-1"> <!-- loading-bar -->
    <span class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700"> <!-- progress-bar-base -->
        <span class="bg-blue-600 h-2.5 rounded-full" style="width: {progressBarWidth}px"></span> <!-- progress-bar -->
    </span>
    <span class="text-sm font-medium text-blue-70"><b>{progressBarDisplay}</b>%</span> <!-- progress-number -->
</div>

<div class="flex items-center justify-center"> <!-- loading-bar-desc -->
    <img class="w-7.5 7.5" src={uploadIcon} alt="Icon" /> <!-- loading-bar-icon -->
    <span class="loading-bar-text-desc">Uploading Meeting Audio...</span>
</div>

<!-- The following is still being used for reference for tailwind styling -->
<style>
    .loading-bar {
        display: flexbox;
        top: 57%;
        visibility: hidden;
        border: 1px solid;
        position: absolute;
        margin-top: 67px;
        width: 35vw;
        height: 10px;
        background-color: #e9eaec;
        border-radius: 30px 30px 30px 30px;
        border-color: #e9eaec;
    }

    .loading-bar-icon {
        width: 30px;
        height: 30px;

        /* Inside auto layout */
        flex: none;
        order: 0;
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

    .progress-bar {
        position: relative;
        height: 10px;
        background-color: #1570ef;
        border-radius: 30px 30px 30px 30px;
    }

    .progress-number {
        color: rgb(105, 104, 104);
        visibility: hidden;
        font-size: 14px;
        left: 19vw;
        top: 2.8vh;
        position: relative;
    }

</style>