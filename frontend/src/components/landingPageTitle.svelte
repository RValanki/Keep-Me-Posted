<!-- Landing Page Title

    Contains Title and subTitle component for landing page

    Author: Rohit Valanki
    Last modified: 31/07/2024

-->
<script>
    export let title = "Title";
    export let subTitle = "Subtitle!";
</script>

<div
    class=" text-3xl sm:text-4xl md:text-5xl font-inter font-bold mb-0 sm: mb-0 md:mb-4 text-white"
>
    {title}
</div>
<div class="text-xl sm:text-2xl font-inter font-thin italic text-white mr-12">
    {subTitle}
</div>
