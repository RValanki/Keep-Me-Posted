<!-- Button Component

    Contains modifiable button

    Author: Diya Ramesh, Brenda Dang, Benjamin Cherian
    Last modified: 9/05/2024

-->

<script>
    export let type = 'primary';
    export let handleClick = () => {};
    export let icon = ''; // Default empty string for icon URL
    export let iconSvg = ''; // Default empty string for inline SVG
    export let text = 'Button';
    export let fullWidth = false; // Default to false for not full width
    export let fitContainerHeight = false; // New prop to fit container height

    // Internal handleClick function that calls the passed handleClick prop
    function internalHandleClick() {
        handleClick();
    }
</script>

<div class="flex justify-center sm:justify-start h-full">
    <button 
        class="flex items-center justify-center font-sans rounded-lg px-3 py-2 md:px-4 md:py-3 lg:px-5 lg:py-3.5 transition ease-in-out duration-300 min-h-11
        {type === 'primary' ? 'bg-blue-600 text-white hover:bg-blue-800 border-none' : ''}
        {type === 'secondary' ? 'bg-blue-50 text-blue-700 hover:bg-blue-100 border-none' : ''}
        {type === 'tertiary' ? 'bg-white text-gray-800 border-[1px] border-gray-300 hover:bg-gray-300' : ''}
        {type === 'disabled' ? 'bg-gray-200 text-white cursor-not-allowed border-none' : ''}
        {type === 'error' ? 'bg-red-600 text-white border-none' : ''}
        {fullWidth ? 'w-full text-center' : ''}
        {fitContainerHeight ? 'h-full' : ''}"
        on:click="{internalHandleClick}">
        {#if icon}
            <!-- svelte-ignore a11y-missing-attribute -->
            <img src="{icon}" class="mr-2 max-w-4 md:max-w-5 lg:max-w-6">
        {:else if iconSvg}
            <!-- svelte-ignore a11y-missing-attribute -->
            <div src="{icon}" class="mr-2 sm:mr-2 lg:mr-6 2xl:mr-[2vw] max-w-6">
                {@html iconSvg}
            </div>
            
        {/if}

        {text}
        
        <slot></slot>
    </button>
</div>
