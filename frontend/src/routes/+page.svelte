<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<script>
    import Card from '../components/card.svelte';
    
    const navigateTo = () => {
      // go to send asap page or the other one i forgot when user clicks
    };
  </script>
  
<Card
    cardText="We will send the summary to your recipients as soon as it is generated. You can just sit back and relax"
    cardHeadingText="Send Summary Asap"
    cardOutlineColor="orange"
    cardBackgroundColor="lightyellow"
    onCardClick={navigateTo}
    cardDestination="/another-page"
/>
