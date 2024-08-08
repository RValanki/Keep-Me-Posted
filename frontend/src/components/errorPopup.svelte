<!-- Error Popup Component

    Contains an error pop-up that can be modified

    Author: Bowen Dong
    Last Modified: 
-->

<script>
    export let errorSubHeadingText; // this is the main text of the card (e.g. 'Your meeting audio should be less than 120 minutes')
    export let errorHeadingText; // this is the heading (e.g. 'Meeting duration exceeded!')
    export let errorButtonText; // this is the button text (e.g. 'Re-Upload')
    export let handleErrorClick = () => {}; // pass a method here that does what you want to happen when you click the button
    
    function handleClick() {
        handleCardClick();
    }

</script>
  
<div>
    
</div>