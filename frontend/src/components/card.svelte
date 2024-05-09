<script>
    export let cardText;
    export let cardHeadingText;
    export let cardOutlineColor;
    export let cardBackgroundColor;
    export let cardDestination;
    export let cardTextColour;
    export let cardWidth = "30%"; //default dimensions
    export let cardHeight = "60%";
    export let cardImagePath;
    
    const handleClick = () => {
        // window.location.href = cardDestination;
    };
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
        padding: 10px 20px;
        cursor: pointer;
        transition: background-color 0.3s, color 0.3s, border-color 0.3s;
    }
</style>

<!-- The code below can be used to put the cards on the screen, in order for the cards to be size responsive they need
to be in some kind of layout/container/wrapper. If you put the code as it is on a page the cards will initialise
on top of each other -->

<!-- <script>
    import Card from '../components/card.svelte';
</script>

<style>
    .container {
        display: flex;
        flex-direction: column;
        height: 100vh; /* Make ontainer fill the viewport height which is the visible screen pretty much */
    }
    .button-wrapper {
        flex-grow: 1; /* 1 makes the wrapper grow to fill the remaining space */
    }
</style>

<div class="container">
    <div class="button-wrapper">
        <Card
            cardText="We will send the summary to your recipients as soon as it is generated. You can just sit back and relax"
            cardHeadingText="Send Summary Asap"
            cardOutlineColor="#FDDCAB"
            cardBackgroundColor="#FFFAF5"
            cardDestination="/"
            cardTextColour= "#EC4A0A"
            cardImagePath= '/send_asap_lightning.png'
        />
    </div>
</div>

<div class="container">
    <div class="button-wrapper">
        <Card
            cardText="You can customise the email sent to your recipients and the summary will not be sent until you choose."
            cardHeadingText="Customise"
            cardOutlineColor="#FCCEEE"
            cardBackgroundColor="#FAFAFF"
            cardDestination="/"
            cardTextColour= "#C11574"
            cardImagePath= '/customise_pen.png'
        />  
    </div>
</div> -->