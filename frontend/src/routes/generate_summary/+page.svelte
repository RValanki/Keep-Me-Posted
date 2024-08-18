<!-- Summary generation page

    Page that shows the summary generated

    Author:Brenda Dang, Diya Ramesh
    Last Modified: 1/08/2024
-->

<script>

  import TopBar from "../../components/topbar.svelte";
  import Button from "../../components/button.svelte";
  import SummaryBox from "../../components/summary-box.svelte";
  import { goto } from "$app/navigation";

  export let title = "Your Summary is Being Generated...";
  export let subTitle = "We are still generating your summary...";
  let summaryBoxRef;

  let backBtn = () => {
    goto("/upload_audio");
  };

  let forwardBtn = () => {
    if (summaryBoxRef && summaryBoxRef.saveSummaryToStore) {
      summaryBoxRef.saveSummaryToStore();
    }
    goto("/email");
  };
  
  $: hasSummaryGenerated = $summaryStore["summary"] && $summaryStore["subject"];
  $: {
      if (hasSummaryGenerated) {
          title = "Summary Generated!";
          subTitle = "Your summary is ready to be sent.";
      } else {
          title = "Your Summary is Being Generated...";
          subTitle = "We are still generating your summary...";
      }
  }
</script>

<body>
  <TopBar />
  
  <div 
       class="text-4xl font-inter font-bold mb-4 text-black flex flex-col justify-center items-center mt-20"
     >
      {hasSummaryGenerated ? "Summary Generated!" : "Your Summary is Being Generated..."}
  </div>
  <div 
       class="text-xl font-inter font-thin text-black flex flex-col justify-center items-center mt-6"
     >
      {hasSummaryGenerated ? "Your summary is ready to be sent." : "We are still generating your summary..."}
  </div>

  <div class="mt-10">
    <SummaryBox bind:this={summaryBoxRef} />
  </div>

  <div class="absolute bottom-8 left-8">
    <Button
      class="primary"
      text="Re-Upload Audio"
      icon="../src/assets/arrow-left.png"
      handleClick={backBtn}
    />
  </div>

  <div class="absolute bottom-8 right-8">
    <Button
      class="primary"
      text="Add Recipients"
      icon="../src/assets/arrow-right.png"
      iconPos="right"
      handleClick={forwardBtn}
    />
  </div>
</body>