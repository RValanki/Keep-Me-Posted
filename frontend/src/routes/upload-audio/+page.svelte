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
</script>

<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&display=swap">
        <title>Send Summary ASAP</title>
    </head>
    <body>
        <Topbar/>

        <div class="center-icon">
            <img class="clock-icon" src={clockIcon} alt="Clock Icon" />
        </div>
        <h1 >Your Summary Will Be Sent..</h1>
        <div class = "subheading">After you upload your meeting audio, your summary will be automatically sent when it is ready.</div>
    
        <UploadBox simple={true} />
    </body>
</html>

<style>
    .center-icon{
        display: flex;
        justify-content: center;
        /* padding-top: 20px; */
        margin-top: 3%;
    }

    .clock-icon{
        /* Frame 23 */

        /* Auto layout */
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        padding: 0px;
        /* gap: 9.3px; */

        width: 7vw;
        height: width;
        max-width: 100px;
        max-height: 100px;

        /* Blue/100 */
        background: #D1E9FF;
        border-radius: 93.0233px;

        /* Inside auto layout */
        flex: none;
        order: 0;
        flex-grow: 0;

        margin-top: 0;
    }

    h1{
        text-align: center;
        margin-top: 2%;
    }

    .subheading{
        text-align: center;
        padding-bottom: 8vh;
        margin-top: 1%;
    }

    body {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

</style>