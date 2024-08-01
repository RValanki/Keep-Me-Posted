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

    let backBtn = () => {
        goto("/upload-audio");
    };

    let forwardBtn = () => {
        goto("/email");
    };

</script>

<style>

</style>

<body>
    <TopBar />

    <div class="text-5xl font-inter font-bold mb-4 text-black flex flex-col justify-center items-center">
        {title}
    </div>
    <div class="text-2xl font-inter font-thin text-black flex flex-col justify-center items-center">
        {subTitle}
    </div>

    <SummaryBox />

</body>