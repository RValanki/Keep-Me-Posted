<!-- Error Popup Component

    Contains an error pop-up that can have it's text be modified

    Author: Bowen Dong
    Last Modified: 8/08/2024
-->

<script>
    import Button from "./button.svelte";
    export let errorSubHeadingText; // this is the main text of the card (e.g. 'Your meeting audio should be less than 120 minutes')
    export let errorHeadingText; // this is the heading (e.g. 'Meeting duration exceeded!')
    export let errorButtonText; // this is the button text (e.g. 'Re-upload')
    export let isVisible = false; // when error occurs, change to true
    
    function dismissError() {
        isVisible = false;
    }

</script>

{#if isVisible}
<div class="justify-center items-center font-sans h-full transition ease-in-out duration-300">
    <div class="fixed inset-0 flex items-center justify-center w-full h-full bg-black backdrop-blur md:bg-opacity-70">
        <div class="bg-white rounded-lg p-4 w-96 flex flex-col justify-center items-center">
            <img src={'../src/assets/error-icon.svg'} alt="error icon"/>
            <div class="flex items-center justify-center text-gray-900 text-lg font-bold pt-2">
                {errorHeadingText}
            </div>
            <div class="text-gray-500 text-sm pb-3 pt-2">
                {errorSubHeadingText}
            </div>
            <div class="pt-4 w-full">
                <Button
                type='error'
                fullWidth = {true}
                text={errorButtonText} 
                handleClick={dismissError}
                />
            </div>
        </div>
    </div>
</div>
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