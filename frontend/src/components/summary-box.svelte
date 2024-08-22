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
    import PopUpModal from "./popUpModal.svelte";
    import { marked } from 'marked';
    import TurndownService from 'turndown';

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
                summaryGenerated = marked(value.summary);
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
            const updatedSummary = document.getElementById("summaryGenerated").innerHTML
            const turndownService = new TurndownService();
            let markdownContent = turndownService.turndown(updatedSummary);
            if (updatedSummary) {
                summaryStore.update(current => {
                    return {
                        ...current,
                        summary: markdownContent
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

    // let displayPopUp = false;

    // function togglePopUp() {
    //     displayPopUp = !displayPopUp;
    // }

    let popUpModalComponent

    function openRegeneratePopUp() {
		// Toggle the popup modal visibility
		popUpModalComponent.togglePopUp();
	}

</script>

<div class="rounded-lg p-4 w-9/12 mx-auto" style="background-color: #F5FAFF;">
    <div class="flex justify-end ml-auto">
        <Button handleClick={openRegeneratePopUp} type="secondary-with-border" text="Regenerate" icon={regenerateIcon}></Button>    
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
                class="w-full p-2 rounded" 
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
            <div
                class="w-full p-2 rounded text-base"
                style="background-color: #F5FAFF;"
                id="summaryGenerated"
                contenteditable=""
                placeholder="Your summary will be generated here..."
            >{@html marked(summaryGenerated)}</div>
        {:else}
            <div class="w-full p-2 rounded text-slate-400 text-base">
                Your subject will be generated here{dots}
            </div>
        {/if}
        
    </div>
</div>

<PopUpModal 
    bind:this={popUpModalComponent}
    header="Regenerating..."
    mainText=""
    type='loading'
    firstHandleClick={openRegeneratePopUp}
    width='96'
/>