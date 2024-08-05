<!-- 

    The page where user uploads the audio file for Send Summary ASAP pathway.

    Author: Parul Garg (pgar0011)
    Edited By: 
    Last Modified: 10/05/24

-->

<script>
    //required imports
    import Topbar from '../../components/topbar.svelte';
    import UploadBox from "../../components/uploadAudioBox.svelte";
    import clockIcon from "../../assets/clock.png"
    import LoadingBar from '../../components/loadingBar.svelte';
</script>

<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Test loading bar</title>
    </head>
    <body>
        <Topbar/>
        <LoadingBar/>
    
        <!-- <UploadBox simple={true} /> -->
        
    </body>
</html>