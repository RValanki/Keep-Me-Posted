<!-- Card Component

    Contains a card button that can be modified

    Author: Bowen Dong
    Last Modified: 10/05/2024
-->

<script>
    export let cardText;
    export let cardHeadingText;
    export let cardOutlineColour;
    export let cardBackgroundColour;
    export let handleCardClick = () => {};
    export let cardTextColour;
    export let cardWidth = "25%";
    export let cardHeight = "100%";
    export let cardImagePath;
    
    function handleClick() {
        handleCardClick();
    }

</script>
  
<button
    class="Card"
    style="
        background-color: {cardBackgroundColour};
        border: 2px solid {cardOutlineColour};
        border-radius: 10px;
        width: {cardWidth};
        height: {cardHeight};
        --card-outline-colour: {cardOutlineColour};
    "
    on:click={handleClick}
    >
    <div class="card-image-container">
        <img src={cardImagePath} alt="card icon" style="max-width: 100%; max-height: 100%;" />
    </div>
    <div class="card-text-container">
        <h2 style="color: {cardTextColour};">{cardHeadingText}</h2>
        <body style="color: {cardTextColour};">{cardText}</body>
    </div>
</button>
  
<style>
    .Card {
        padding: 2% 2%;
        cursor: pointer;
        transition: box-shadow 0.3s ease-in-out, text-shadow 0.3s ease-in-out;
    }
    .Card:hover {
        box-shadow: 0em 0em 1em 0em var(--card-outline-colour);
        text-shadow: 0.1em 0.1em 0.2em var(--card-outline-colour);
    }
    .Card:hover img{
        filter: drop-shadow(0.2rem 0.2rem 0rem var(--card-outline-colour));
        transition: 0.4s ease-in-out;
    }
    .card-image-container {
        flex: 0 0 auto;
    }
    .card-text-container {
        flex: 1;
    }
</style>



<!-- The code below is the initialised cards and the container you need to put the cards in
Assuming this code will be in the routes directory also need to add handleCardClick -->
<!-- <script>
    import Card from '../components/card.svelte';
</script> -->

<!-- This is a container that will hold the two cards: -->
<!-- <style>
    .CardContainer {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        gap: 1.5%;
    }
</style> -->

<!-- Here i am putting the cards in the container also everything is initialised excpet for handleCardClick -->
<!-- <div class="CardContainer">
    <Card
        cardText="We will send the summary to your recipients as soon as it is generated. You can just sit back and relax."
        cardHeadingText="Send Summary Asap"
        cardOutlineColor="#FDDCAB"
        cardBackgroundColor="#FFFAF5"
        cardTextColour= "#EC4A0A"
        cardImagePath= '/send_asap_lightning.png'
    />
    <Card
        class="card"
        cardText="You can customise the email sent to your recipients and the summary will not be sent until you choose."
        cardHeadingText="Customise"
        cardOutlineColor="#FCCEEE"
        cardBackgroundColor="#FAFAFF"
        cardTextColour= "#C11574"
        cardImagePath= '/customise_pen.png'
    />  
</div> -->
