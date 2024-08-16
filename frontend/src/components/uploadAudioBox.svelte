<!--

	Upload Audio Box Component

	consists of parts
	1. the box itself = blue on initial, green on complete
	2. dropzone = container that can be clicked on/drag drop file
	3. description = a text box with either instruction or completion, 
		includes an icon, a header (bolded line), second and third line

	Authors: Parul Garg (pgar0011)
	Editied by: Benjamin Cherian, Zihao Wang, Angelina Leung, Maureen Pham, Danny Leung
	Last Modified: 14/08/24

-->
<!-- JavaScript -->
<script>
	import micIcon from "../assets/mic-icon.png";
	import checkIcon from "../assets/check-icon.png";
	import Dropzone from "svelte-file-dropzone";
	import LoadingBar from "./loadingBar.svelte";
	import { transcribe_audio } from "../api-functions/transcribe_audio";
	// import { send_summary } from "../api-functions/send_summary";
	import PopUpModal from "./popUpModal.svelte"; // Import the PopUpModal component
	import errorIcon from "../assets/error-icon.png"; // Import the error icon

	// content
	let fileUploaded = false;
	let uploadComplete = false;
	let loadingBarComponent; // pointer for loading bar
	const dropzoneStyles = "background-color: rgba(255, 0, 0, 0)"; // define custom to style dropzone

	// File Handling
	const MAX_DURATION_SECONDS = 7200; // 7200 seconds = 120 minutes, used to check limit on files
	const errorMessage = {
		DURATION_EXCEEDED: ["Meeting duration exceeded", "Your meeting audio should be less than 120 minutes.", "Re-upload"],
		INVALID_FORMAT: ["Invalid audio format!", "Your meeting audio must be in MP3 or WAV format.", "Re-upload"],
		ASSEMBLYAI_ERROR: ["AssemblyAI Error name", "Some description of the error. Please try again later", "Close"],	
	};

	let showError = false; // State for showing the error popup
	let popupHeader = ''; // Header for the popup
	let popupMainText = ''; // Main text for the popup

	async function handleFilesSelect(e) {
		const { acceptedFiles } = e.detail;
		// console.log(e.detail)

		if (acceptedFiles.length > 0) {
			const selectedFile = acceptedFiles[0];
			// console.log(selectedFile);

			// Initial file type check before loading it as an audio source
			if (
				!selectedFile.name.endsWith(".mp3") &&
				!selectedFile.name.endsWith(".wav")
			) {
				raiseError(errorMessage.INVALID_FORMAT);
				return; // Exit the function early if file type is incorrect
			}
			
			// check duration of audio file
			const audio = new Audio(URL.createObjectURL(selectedFile)); // Create new Audio HTML object, create URL used as source for audio element

			audio.addEventListener("loadedmetadata", async () => {
				if (audio.duration >= MAX_DURATION_SECONDS) {
					raiseError(errorMessage.DURATION_EXCEEDED);
				}
			});
			// File has passed all checks
			startUpload(selectedFile);
  		}
	}

	// Function that calls transcribe_audio API
	async function startUpload(file) {
		console.log('start upload');
		const transcript = await transcribe_audio(file, "http://127.0.0.1:8000"); //
		console.log(transcript);

		// TODO
		// loadingBarComponent.updateLoadingBar(50);
		// sent_summary api
		// loadingBarComponent.updateLoadingBar(99);
		// fileUploaded = true;
		// uploadComplete = true;
	}

	// Function to give popup correct messages
	function raiseError(errorType) {
		popupHeader = errorType[0];
		popupMainText = errorType[1];
		showError = true;
  	}

	function dismissError() {
		showError = false;
	}
</script>

<!-- COMPONENT -->
<div class= "flex items-center justify-center">
    <!-- upload-audio-box -->
	 {#if !fileUploaded}
	 	<!-- BLUE with dropzone -->
	 	<div id="upload-audio-box" class= "bg-light-blue flex flex-col justify-center w-5/6 h-48 max-w-2xl border-2  border-medium-blue rounded-md">
			<Dropzone on:drop={handleFilesSelect} accept=".mp3, .wav, .pdf" containerStyles={dropzoneStyles}>

				<!-- The dropzone is on top of custom-input so the grey is covering the lightblue-->
				<div class="text-center flex flex-col items-center text-center">
					<img id="icon" class="w-12 h-12 m-3" src={micIcon} alt="Icon" />
					<p id="upload-audio-box-first-line" class="sm:text-xl font-bold text-blue-800 mb-1">Upload meeting audio</p>
					<p id="upload-audio-box-second-line" class="text-xs sm:text-base text-gray-400">Must be under 120 minutes.</p>
					<p class="text-xs sm:text-base text-gray-400">MP3 or WAV formats accepted.</p>
				</div>
			</Dropzone>
		</div>
	 {:else if fileUploaded && uploadComplete}
		<!-- GREEN no dropzone -->
		 <div id="upload-audio-box" class= "bg-success-25 flex flex-col justify-center w-5/6 h-48 max-w-2xl border-2 border-success-300 rounded-md">
			<div class="text-center flex flex-col items-center text-center">
				<img id="icon" class="w-12 h-12 m-3" src={checkIcon} alt="Icon" />
				<p id="upload-audio-box-first-line" class="sm:text-xl font-bold text-success-700 mb-1">Your summary has been generated!</p>
				<p id="upload-audio-box-second-line" class="text-xs sm:text-base text-success-700">View the summary by clicking 'View Summary'</p>
			</div>
		</div>
	 {:else} <!--file has been uploaded awaiting api-->
	 	<div id="upload-audio-box" class= "bg-light-blue flex flex-col justify-center w-5/6 h-48 max-w-2xl border-2  border-medium-blue rounded-md">
	 		<LoadingBar bind:this={loadingBarComponent}/>
		</div>
	 {/if}
</div>

<!-- Error Pop-Up Modal -->
{#if showError}
	<PopUpModal 
		type="error"
		header={popupHeader}
		mainText={popupMainText}
		iconPath={errorIcon}
		firstButtonText="Re-upload"
		firstHandleClick={dismissError}
		width="96"
		visible={showError}
	/>
{/if}
