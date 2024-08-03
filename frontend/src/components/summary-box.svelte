<!-- Summary box component

    Contains the summary generated and the subject

    Author: Diya Ramesh, Brenda Dang
    Last modified: 1/08/2024

-->

<!--  -->
<script>
    import Button from "./button.svelte"
    import { summaryStore } from "../stores/summary-store"
    import { onMount, onDestroy } from "svelte"

    export let emailSubject = ""
    export let summaryGenerated = ""

    // Remove internal scrolling in text area and expand outer div instead
    function autoResize(event) {
        const textarea = event.target
        textarea.style.height = `${textarea.scrollHeight}px`
    }

    function loadSummaryContent() {
        const unsubscribe = summaryStore.subscribe(value => {
            summaryGenerated = value.summary;
            emailSubject = value.subject;
        });
        if (summaryGenerated && emailSubject) {
            unsubscribe();
        }
    }
    
    onMount(() => {
        loadSummaryContent();
    });

    export const saveSummaryToStore = () => {
        // bind not working for some reason so I have to get the content manually
        const updatedSubject = document.getElementById("emailSubject").value
        const updatedSummary = document.getElementById("summaryGenerated").value
        
        // only overwrite store if the edit fields have been populated
        if (updatedSubject && updatedSummary) {
            summaryStore.set({
            summary: updatedSubject,
            subject: updatedSummary,
        });
        }

        // for testing
        // summaryStore.subscribe(value => {
        //     console.log(value.summary);
        //     console.log(value.subject)
        // })
    }

</script>

<style>
    .subject-placeholder::placeholder {
        color: #98A2B3;
        opacity: 1;
        font-weight: 600;
        font-size: 20px;
    }

    .summary-placeholder::placeholder {
        color: #98A2B3;
        opacity: 1;
        font-size: 16px;
    }

    textarea {
        overflow: hidden; /* Remove scrollbars */
        resize: none; /* Prevent manual resizing */
    }
</style>

<div class="rounded-lg p-4 w-9/12 mx-auto" style="background-color: #F5FAFF;">
    <div class="flex justify-end ml-auto">
        <Button type="secondary"></Button>
    </div>
    <div class="flex flex-col gap-0	 mb-4">
        <label 
            class="block text-dark font-semibold pl-2 text-base mb-2" 
            style="color:#667085" 
            for="emailSubject">
            Email Subject
        </label>
        {#if emailSubject}
            <input 
                class="w-full p-2 rounded subject-placeholder" 
                style="background-color: #F5FAFF;" 
                type="text" 
                id="emailSubject" 
                bind:value={emailSubject} 
                placeholder="Your subject will be generated here..." />
        {:else}
            <input 
                class="w-full p-2 rounded subject-placeholder" 
                style="background-color: #F5FAFF;" 
                type="text" 
                id="emailSubject" 
                placeholder="Your subject will be generated here..." />
        {/if}
    </div>
    <div class="flex flex-col gap-0 mb-4">
        <label 
            class="lock text-dark font-semibold pl-2 text-base mb-2" 
            style="color:#667085" 
            for="summaryGenerated">
            Summary
        </label>
        {#if summaryGenerated}
            <textarea
                class="w-full p-2 rounded text-base summary-placeholder"
                style="background-color: #F5FAFF;"
                id="summaryGenerated"
                bind:value={summaryGenerated}
                placeholder="Your summary will be generated here..."
                on:input={autoResize}
            ></textarea>
        {:else}
            <textarea
                class="w-full p-2 rounded text-base summary-placeholder"
                style="background-color: #F5FAFF;"
                id="summaryGenerated"
                placeholder="Your summary will be generated here..."
                on:input={autoResize}
            ></textarea>
        {/if}
    </div>
</div>