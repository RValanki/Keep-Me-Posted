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
    import regenerateIcon from "../assets/regenerate-icon.png"

    export let emailSubject = ""
    export let summaryGenerated = ""

    let dots = ""
    setInterval(() => {
        if (dots.length < 3) {
            dots += '.';
        } else {
            dots = '';
        }
    }, 500);

    // Remove internal scrolling in text area and expand outer div instead
    function autoResize(event) {
        const textarea = event.target
        textarea.style.height = `${textarea.scrollHeight}px`
    }

    function loadSummaryContent() {
        const unsubscribe = summaryStore.subscribe(value => {
            if (!summaryGenerated) {
                summaryGenerated = value.summary;
            }
            if (!emailSubject) {
                emailSubject = value.subject;
            }
        });
        if (summaryGenerated && emailSubject) {
            unsubscribe();
        }
    }
    
    onMount(() => {
        loadSummaryContent();
    });

    export const saveSummaryToStore = () => {
        // must do separately in case one hasn't generated yet
        if (emailSubject) {
            // bind not working for some reason so I have to get the content manually
            const updatedSubject = document.getElementById("emailSubject").value         
            // only overwrite store if the edit fields have been populated
            if (updatedSubject) {
                summaryStore.update(current => {
                    return {
                        ...current,
                        subject: updatedSubject
                    };
                });
            }
        }
        if (summaryGenerated) {
            const updatedSummary = document.getElementById("summaryGenerated").value
            if (updatedSummary) {
                summaryStore.update(current => {
                    return {
                        ...current,
                        summary: updatedSummary
                    };
                });
            }
        }

        //for testing
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
        <Button type="secondary-with-border" text="Regenerate" icon={regenerateIcon}></Button>
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
        <div class="w-full p-2 rounded text-slate-400 font-bold">
            Your subject will be generated here{dots}
        </div>
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
            <div class="w-full p-2 rounded text-slate-400 text-base">
                Your subject will be generated here{dots}
            </div>
        {/if}
    </div>
</div>