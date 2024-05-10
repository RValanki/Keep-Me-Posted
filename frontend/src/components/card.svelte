<!-- Card Component

    Contains a card button that can be modified

    Author: Bowen Dong
    Last Modified: 10/05/2024
-->

<script>
    // declaring variables that will be used
    export let cardText;
    export let cardHeadingText;
    export let cardOutlineColor;
    export let cardBackgroundColor;
    export let handleCardClick = () => {};
    export let cardTextColour;
    export let cardWidth = "25%"; //default dimensions but still exporting JUST IN CASE
    export let cardHeight = "50%";
    export let cardImagePath;
    
    function handleClick() {
        handleCardClick();
    }

</script>
  
<button
    class="Card"
    style="
        background-color: {cardBackgroundColor};
        border: 2px solid {cardOutlineColor};
        border-radius: 10px;
        width: {cardWidth};
        height: {cardHeight};
    "
    on:click={handleClick}
    >
    <img src={cardImagePath} alt="card icon" style="max-width: 100%; max-height: 100%;" />
    <h2 style="color: {cardTextColour};">{cardHeadingText}</h2>
    <p style="color: {cardTextColour};">{cardText}</p>
</button>
  
<style>
    .Card {
        padding: 2% 2%;
        cursor: pointer;
        transition: box-shadow 0.3s ease-in-out;
    }
    .Card:hover {
        box-shadow: 0px 0px 10px 0px #aab4ff;
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
