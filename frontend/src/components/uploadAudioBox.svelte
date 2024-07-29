<!--

	Upload Audio Box Component

	consists of parts
	1. the box itself = blue on initial, green on complete
	2. dropzone + label = container that can be clicked on/drag drop file
	3. description = a text box outline either instruction or completion, 
		includes an icon, a header (bolded line), and subtitle (following lines)
	4. status message = section below confirming status of an upload

	Authors: Parul Garg (pgar0011)
	Editied by: Benjamin Cherian, Zihao Wang, Angelina Leung
	Last Modified: 28/07/24

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
			document.querySelector('.audio-box-desc').style.visibility = "hidden";
		} else {
		errorMessage =
			"Invalid audio format! Your meeting audio must be in MP3 or WAV format";
		}
  	}
</script>

<!-- COMPONENT -->
<div class="upload-audio-container">
	<div class="upload-audio-box">
		<Dropzone on:drop={handleFilesSelect} accept=".mp3, .wav" containerStyles={dropzoneStyles}>

			<!-- The dropzone is on top of custom-input so the grey is covering the lightblue-->
			<div class="upload-audio-box-desc">
				<img id="icon" class="audio-box-icon" src={micIcon} alt="Icon" />
				<span class="upload-audio-box-header">Upload meeting audio</span>
				<span class="upload-audio-box-subtitle">Must be under 120 minutes. MP3 or WAV formats accepted.</span>
			</div>
		
		</Dropzone>
		<LoadingBar bind:this={loadingBarComponent} />
	</div>

	<div class="upload-audio-status-message">
      {#if file}
        <p>File ready: {file.name}</p>
      {:else}
        <p>{errorMessage}</p>
      {/if}
  	</div>
</div>



<!-- Styling -->
<style>
	.upload-audio-box{
		box-sizing: border-box;

		display: flex;
		flex-direction: column;
		justify-content: center;
		padding: 0px 0px;
		gap: 16px;

		width: 55vw;
		height: 27vh;
		max-width: 700px;
		max-height: 233px;

		/* Blue/25 */
		background: #f5faff;
		/* Blue/300 */
		border: 3px solid #84caff;
		border-radius: 5px;

		/* Inside auto layout */
		flex: none;
		order: 0;
		flex-grow: 0;
	}

	.upload-audio-box-desc {
		text-align: center;
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.audio-box-icon {
		/* large icon */

		width: 3.5vw;
		height: calc(2 * width);

		max-width: 46px;
		max-height: 52px;

		/* Inside auto layout */
		flex: none;
		order: 0;
		flex-grow: 0;
	}

	.upload-audio-box-header {
		/* Upload meeting audio */
		width: 25vw;
		height: 5vh;

		/* Text xl/Medium */
		font-style: normal;
		font-family: "Inter";
		font-weight: 500;
		font-size: 1.45vw;
		line-height: 5vh;
		/* identical to box height, or 150% */
		text-align: center;

		/* Blue/800 */
		color: #1849a9;

		/* Inside auto layout */
		flex: none;
		order: 0;
		flex-grow: 0;
	}

	.upload-audio-box-subtitle {
		/* Must be under 120 minutes. MP3 or WAV formats accepted. */

		width: 16.5vw;
		height: 5vh;

		/* Text md/Regular */
		font-style: normal;
		font-weight: 400;
		font-size: 1.1vw;
		line-height: 4vh;
		/* or 150% */
		text-align: center;

		/* Gray/400 */
		color: #98a2b3;

		/* Inside auto layout */
		flex: none;
		order: 1;
		flex-grow: 0;
	}

	.upload-audio-status-message {
		text-align: center;
		padding: 10px;
		color: #333;
		font-size: 16px;
		margin-top: 100px;
	}
</style>
