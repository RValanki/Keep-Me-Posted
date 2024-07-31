<!-- Button Component

    Contains modifiable button

    Author: Diya Ramesh, Brenda Dang
    Last modified: 9/05/2024

-->

<script>
    export let type = 'primary';
    export let handleClick = () => {};
    export let icon = ''; // Default empty string for icon URL
    export let text = 'Button';
	export let fullWidth = false; // Default to false for not full width

    // Internal handleClick function that calls the passed handleClick prop
    function internalHandleClick() {
        handleClick();
    }
</script>

<style>
</style>

<div class="flex justify-center sm:justify-start">
    <button 
        class="flex items-center justify-center font-sans border-none rounded-lg px-3 py-2 md:px-4 md:py-3 lg:px-5 lg:py-3.5 transition ease-in-out duration-300 min-h-11
        {type === 'primary' ? 'bg-blue-600 text-white hover:bg-blue-800' : ''}
        {type === 'secondary' ? 'bg-blue-50 text-blue-700 hover:bg-blue-100' : ''}
        {type === 'tertiary' ? 'bg-white text-gray-800 border border-gray-300' : ''}
        {type === 'disabled' ? 'bg-gray-200 text-white cursor-not-allowed' : ''}
        {type === 'error' ? 'bg-red-600 text-white' : ''}
        {fullWidth ? 'w-full text-center' : ''}"
        on:click="{internalHandleClick}">
        {#if icon}
            <!-- svelte-ignore a11y-missing-attribute -->
            <img src="{icon}" class="mr-2 max-w-4 md:max-w-5 lg:max-w-6">
        {/if}

        {text}
        
        <slot></slot>
    </button>
</div>
