<!--

	Upload Audio Box Component

	consists of parts
	1. the box itself = blue on initial, green on complete
	2. dropzone + label = container that can be clicked on/drag drop file
	3. description = a text box outline either instruction or completion, 
		includes an icon, a header (bolded line), and subtitle (following lines)
	4. status message = section below confirming status of an upload

	Authors: Parul Garg (pgar0011)
	Editied by: Benjamin Cherian, Zihao Wang, Angelina Leung, Maureen Pham
	Last Modified: 3/08/24

-->
<!-- JavaScript -->
<script>
	import micIcon from "../assets/mic-icon.png";
	import Dropzone from "svelte-file-dropzone";
	import LoadingBar from "./loadingBar.svelte";
	import { simple_pathway } from "../api-functions/simple_pathway";
	import { api_status } from "../stores/simple-pathway-store";
	import { goto } from "$app/navigation";
	export let simple = false;

	let showDropzone = true;
	let loadingBarComponent; // pointer for loading bar
	const dropzoneStyles = "background-color: rgba(255, 0, 0, 0)"; // define custom to style dropzone

	/**
	 * Subscribes to updates from the `api_status` observable
	 * This function also updates the `loadingBar` with the current status value.
	 */
	const unsubscribe = api_status.subscribe((value) => {
		console.log(value.status); // Log the status value
		console.log(typeof updateLoadingBar); // Should log 'function'
		if (loadingBarComponent) {
		loadingBarComponent.updateLoadingBar(value.status);
		}
	});

	// ------------------------------------------ File Handling
	let file;
	let errorMessage = "";
	const MAX_DURATION_SECONDS = 7200; // 7200 seconds = 120 minutes, used to check limit on files

	async function handleFilesSelect(e) {
		const { acceptedFiles } = e.detail;
		file = null; // Reset the file each time new files are selected

		if (acceptedFiles.length > 0) {
			const selectedFile = acceptedFiles[0];

			// Initial file type check before loading it as an audio source
			if (
				!selectedFile.name.endsWith(".mp3") &&
				!selectedFile.name.endsWith(".wav")
			) {
				errorMessage =
				"Invalid audio format! \n Your meeting audio must be in MP3 or WAV format.";
				return; // Exit the function early if file type is incorrect
			}

			const audio = new Audio(URL.createObjectURL(selectedFile)); // Create new Audio HTML object, create URL used as source for audio element

			audio.addEventListener("loadedmetadata", async () => {
				if (audio.duration <= MAX_DURATION_SECONDS) {
				file = selectedFile;
				errorMessage = "";
				console.log("mao");
				const response = await simple_pathway(file, "http://127.0.0.1:8000");
				} else {
				errorMessage =
					"Meeting duration exceeded! \n Your meeting audio should be less than 120 minutes.";
				file = null;
				//TODO: Replace with error message pop-up
				}
			});

			//hide the audio box desc and show the loading bar
			showDropzone = false;
		} else {
		errorMessage =
			"Invalid audio format! Your meeting audio must be in MP3 or WAV format";
		}
  	}
</script>

<!-- COMPONENT -->
<div class= "flex items-center justify-center">
    <!-- upload-audio-box -->
    <div class= "bg-light-blue box-border flex flex-col justify-center p-0 w-7/12 h-48 max-w-2xl max-h-48 border-2 border-medium-blue rounded-md flex-none order-0 flex-grow-0">
		{#if showDropzone}
			<Dropzone on:drop={handleFilesSelect} accept=".mp3, .wav" containerStyles={dropzoneStyles}>

				<!-- The dropzone is on top of custom-input so the grey is covering the lightblue-->
				<div class="text-center flex flex-col items-center text-center">
					<img id="icon" class="w-12 h-20 max-w-12 max-h-12 flex-none order-0 flex-grow-0 mb-3" src={micIcon} alt="Icon" />
					<span class="font-bold w-72 text-xl text-blue-800 order-0 flex-grow-0 mb-1">Upload meeting audio</span>
					<span class="w-64 font-normal text-lg text-gray-400 order-1 flex-grow-0">Must be under 120 minutes. MP3 or WAV formats accepted.</span>
				</div>

			</Dropzone>
		{:else}
			<LoadingBar bind:this={loadingBarComponent} />
		{/if}
	</div>

	<div class="upload-audio-status-message">
      {#if file}
       <!-- <p>File ready: {file.name}</p> -->
      {:else}
        <p>{errorMessage}</p>
      {/if}
  	</div>
</div>



<!-- Styling -->
<style>
    <!-- need to check before deleting-->
	.upload-audio-status-message {
		text-align: center;
		padding: 10px;
		color: #333;
		font-size: 60px;
		margin-top: 100px;
	}
</style>
