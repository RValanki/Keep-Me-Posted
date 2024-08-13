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
	import checkIcon from "../assets/check-icon.png";
	import Dropzone from "svelte-file-dropzone";
	import LoadingBar from "./loadingBar.svelte";
	import { simple_pathway } from "../api-functions/simple_pathway";
	import { api_status } from "../stores/simple-pathway-store";
	import { goto } from "$app/navigation";
	export let simple = false;

	let showDropzone = true;
	let loadingBarComponent; // pointer for loading bar
	const dropzoneStyles = "background-color: rgba(255, 0, 0, 0)"; // define custom to style dropzone

	let isConditionMet = false;
	let firstLine = "Upload meeting audio";
	let secondLine = "Must be under 120 minutes.";
	let thirdLine = "MP3 or WAV formats accepted.";

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
			//TODO
			showDropzone = false;
		} else {
		errorMessage =
			"Invalid audio format! Your meeting audio must be in MP3 or WAV format";
		}
  	}

	// Function to update Tailwind styles based on a condition
	function updateStyles(isConditionMet) {
		const uploadAudioBox = document.getElementById('upload-audio-box');
		const icon = document.getElementById('icon');
		const uploadAudioBoxFirstLine = document.getElementById('upload-audio-box-first-line');
		const uploadAudioBoxSecondLine = document.getElementById('upload-audio-box-second-line');

		if (isConditionMet) {
			// Apply styles for the success state
			uploadAudioBox.classList.remove(
				'bg-light-blue', 'border-medium-blue'); // Remove previous styles
			uploadAudioBox.classList.add(
				'bg-success-25', 'border-success-300'); // Add success styles
			
			icon.src = checkIcon;
			
			uploadAudioBoxFirstLine.classList.remove(
				'text-blue-800');
			uploadAudioBoxFirstLine.classList.add(
				'text-success-700');
			
			uploadAudioBoxSecondLine.classList.remove(
				'text-gray-400');
			uploadAudioBoxSecondLine.classList.add(
				'text-success-700');
			
			firstLine = "Your summary has been generated!";
			secondLine = "View the summary by clicking 'View Summary";
			thirdLine = "";
		} else {
			// Apply styles for the initial state
			uploadAudioBox.classList.remove(
				'bg-success-25', 'border-success-300'); // Remove success styles
			uploadAudioBox.classList.add(
				'bg-light-blue', 'border-medium-blue'); // Add initial styles
			
			icon.src = micIcon;
			
			uploadAudioBoxFirstLine.classList.remove(
				'text-success-700');
			uploadAudioBoxFirstLine.classList.add(
				'text-blue-800');
			
			uploadAudioBoxSecondLine.classList.remove(
				'text-success-700');
			uploadAudioBoxSecondLine.classList.add(
				'text-gray-400');

			firstLine = "Upload meeting audio";
			secondLine = "Must be under 120 minutes.";
			thirdLine = "MP3 or WAV formats accepted.";
		}
	}
</script>

<!-- COMPONENT -->
<div class= "flex items-center justify-center">
    <!-- upload-audio-box -->
    <div id="upload-audio-box" class= "bg-light-blue flex flex-col justify-center w-5/6 h-48 max-w-2xl border-2 border-medium-blue rounded-md">
		{#if showDropzone}
			<Dropzone on:drop={handleFilesSelect} accept=".mp3, .wav" containerStyles={dropzoneStyles}>

				<!-- The dropzone is on top of custom-input so the grey is covering the lightblue-->
				<div class="text-center flex flex-col items-center text-center">
					<img id="icon" class="w-12 h-12 m-3" src={micIcon} alt="Icon" />
					<p id="upload-audio-box-first-line" class="sm:text-xl font-bold text-blue-800 mb-1">{firstLine}</p>
					<p id="upload-audio-box-second-line" class="text-xs sm:text-base text-gray-400">{secondLine}</p>
					<p class="text-xs sm:text-base text-gray-400">{thirdLine}</p>
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