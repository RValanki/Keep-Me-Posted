<script>
    import { onMount } from "svelte";
    import Button from "./button.svelte";
    import { getAuth } from "../stores/auth-store";
    import DriveIcon from "../assets/google-drive.png";
    
    let pickerInited = false;
    let accessToken = null;
    let googleAuth = false;

    const API_KEY = "AIzaSyClx-X-RcNSLj88cdn7Mnnn60KVhnq5hvI";
    const APP_ID = "342252136789";

    function gapiLoaded() {
        console.log("Google API loaded");
        gapi.load("client:picker", initializePicker);
    }

    async function initializePicker() {
        await gapi.client.load(
            "https://www.googleapis.com/discovery/v1/apis/drive/v3/rest",
        );
        pickerInited = true;
    }

    onMount(async () => {
        const queryParams = new URLSearchParams(window.location.search);
        googleAuth = queryParams.get("google_auth") === "true";
        console.log("Google Auth:", googleAuth);

        if (googleAuth) {
            accessToken = getAuth().accessToken;
            console.log("Access Token:", accessToken);
        }

        const gapiScript = document.createElement("script");
        gapiScript.src = "https://apis.google.com/js/api.js";
        gapiScript.async = true;
        gapiScript.defer = true;
        gapiScript.onload = gapiLoaded;
        document.body.appendChild(gapiScript);

    });

    async function handleAuthClick() {
        await createPicker();
    }

    /**
     *  Create and render a Picker object for searching images.
     */
    function createPicker() {
        console.log("Creating picker");
        const view = new google.picker.View(google.picker.ViewId.DOCS);
        view.setMimeTypes("video/mp4,audio/mp3");
        const picker = new google.picker.PickerBuilder()
            .enableFeature(google.picker.Feature.NAV_HIDDEN)
            .enableFeature(google.picker.Feature.MULTISELECT_ENABLED)
            .setDeveloperKey(API_KEY)
            .setAppId(APP_ID)
            .setOAuthToken(accessToken)
            .addView(view)
            .addView(new google.picker.DocsUploadView())
            .setCallback(pickerCallback)
            .build();
        picker.setVisible(true);
    }

    /**
     * Displays the file details of the user's selection.
     * @param {object} data - Containers the user selection from the picker
     */
    async function pickerCallback(data) {
        if (data.action === google.picker.Action.PICKED) {
            let text = `Picker response: \n${JSON.stringify(data, null, 2)}\n`;
            const document = data[google.picker.Response.DOCUMENTS][0];
            const fileId = document[google.picker.Document.ID];
            try {
                const res = await gapi.client.drive.files.get({
                    fileId: fileId,
                    fields: "*",
                });
                text += `Drive API response for first document: \n${JSON.stringify(res.result, null, 2)}\n`;
            } catch (error) {
                text += `Error fetching file: ${error.message}\n`;
                console.error("Error fetching file:", error);
            }
            document.getElementById("content").innerText = text;
        }
    }

</script>


<div class="flex justify-center items-center h-[50px] mb-4">
    {#if googleAuth}
        <Button
            fullWidth={true} 
            fitContainerHeight={true}
            type="secondary" 
            text="Upload from Google Drive"
            icon = {DriveIcon}
            handleClick={handleAuthClick} />
    {:else}
        <form id="google-form" method="post" action="?/OAuth2">
            <Button
                fullWidth={true} 
                fitContainerHeight={true}
                type="secondary" 
                text="Sign in"
                icon = {DriveIcon}
                handleClick={handleAuthClick} />
        </form>
    {/if}

    <p id="content" class="text-center"> </p>
</div>