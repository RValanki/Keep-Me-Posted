<script>
    import Card from "../../components/card.svelte";
    import TopBar from "../../components/topbar.svelte";
    import Button from "../../components/button.svelte";
    import { goto } from "$app/navigation";
    
    let simplePathway = () => {
        let path = '';
        goto(path);
    };
    
    let customisePathway = () => {
        let path = '';
        goto(path);
    };

    let backBtn = () => {
        let path = '';
        goto(path);
    };

</script>

<!-- This is a container that will hold the two cards: -->
<style>
    .card-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 50vh;
        gap: 1.5%;
    }
    .top-text {
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 16px;
        align-items: center;
        margin: 64px;
        margin-top: 3%;
    }
    .bottom-bar {
        margin-left: 3%;
    }
</style>

<body>
    <TopBar />
    <div class="top-text">    
        <h1> Choose Pathway</h1>
        <p class="subheading">We can send your summary ASAP or let you customise your summary</p>
    </div>

    <div class="card-container">
        <Card
            cardText="We will send the summary to your recipients as soon as it is generated. You can just sit back and relax."
            cardHeadingText="Send Summary Asap"
            cardOutlineColour="#FDDCAB"
            cardBackgroundColour="#FFFAF5"
            cardTextColour= "#EC4A0A"
            cardImagePath= '../src/assets/send_asap_lightning.png'
            handleCardClick={simplePathway}
        />
        <Card
            class="card"
            cardText="You can customise the email sent to your recipients and the summary will not be sent until you choose."
            cardHeadingText="Customise"
            cardOutlineColour="#FCCEEE"
            cardBackgroundColour="#FAFAFF"
            cardTextColour= "#C11574"
            cardImagePath= '../src/assets/customise_pen.png'
            handleCardClick={customisePathway}
        />  
    </div>

    <div class="bottom-bar">
        <Button
        class="primary" 
        text="Back"
        icon='../src/assets/arrow-left.png'
        handleClick={backBtn}/>
    </div>
   
</body>