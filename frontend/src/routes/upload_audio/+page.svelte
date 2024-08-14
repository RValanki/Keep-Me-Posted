<!-- 

    The page where user uploads the audio file for Send Summary ASAP pathway.

    Author: Parul Garg (pgar0011)
    Edited By: Angelina Leung (aleu0007)
    Last Modified: 13/08/24

-->

<script>
    //required imports
    import Topbar from '../../components/topbar.svelte';
    import UploadBox from "../../components/uploadAudioBox.svelte";
</script>

<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Upload Meeting Audio</title>
    </head>
    <body>
        <Topbar/>
        <h1 class="mt-20 sm:mt-32">Upload Meeting Audio</h1>
        <div class="subheading mb-16 mt-4">Upload your meeting audio for us to summarise.</div>
    
        <UploadBox/>
    </body>
</html>