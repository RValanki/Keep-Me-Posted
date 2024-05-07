<script>
    export let cardText;
    export let cardHeadingText;
    export let cardOutlineColor = "black";
    export let cardBackgroundColor = "white";
    export let onCardClick;
    export let cardDestination = "/";
    
    const handleClick = () => {
        if(onCardClick) onClick();
            // Navigate to another page
            window.location.href = cardDestination;
    };
</script>
  
<button
    class="Card"
    style="
        background-color: {cardBackgroundColor};
        border: 2px solid {cardOutlineColor};
        border-radius: 10px;
    "
    on:click={handleClick}
    >
    <h2>{cardHeadingText}</h2>
    <p>{cardText}</p>
</button>
  
<style>
    .Card {
        padding: 10px 20px;
        cursor: pointer;
        transition: background-color 0.3s, color 0.3s, border-color 0.3s;
    }
</style>