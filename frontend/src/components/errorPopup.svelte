<!-- Error Popup Component

    Contains an error pop-up that can have it's text be modified

    Author: Bowen Dong
    Last Modified: 8/08/2024
-->

<script>
    import PopUpModal from "./popUpModal.svelte";
    export let errorSubHeadingText; // this is the main text of the card (e.g. 'Your meeting audio should be less than 120 minutes')
    export let errorHeadingText; // this is the heading (e.g. 'Meeting duration exceeded!')
    export let errorButtonText; // this is the button text (e.g. 'Re-upload')
    export let isVisible = false; // when error occurs, change to true
    
    function dismissError() {
        isVisible = false;
    }

</script>

{#if isVisible}
    <PopUpModal
    header={errorHeadingText}
    mainText={errorSubHeadingText}
    type='error'
    iconPath='../src/assets/error-icon.svg'
    firstButtonText={errorButtonText}
    firstHandleClick={dismissError}
    width='96'/>
{/if}


<!--
    EXAMPLE USAGE ON A PAGE
-->

<!-- <script>
    import ErrorPopup from "../../components/errorPopup.svelte";

    let ifError = false
</script>


<body>
    <button on:click={() => ifError = !ifError}>click to cause error</button>
   <ErrorPopup errorHeadingText="Invalid audio format!" errorSubHeadingText="Your meeting audio must be in MP3 or WAV format." errorButtonText="Re-upload" isVisible={ifError}/>
</body> -->