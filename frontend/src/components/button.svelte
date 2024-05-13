<!-- Button Component

    Contains modifiable button

    Author: Diya Ramesh, Brenda Dang
    Last modified: 9/05/2024

-->

<!--  -->
<script>
    import '../app.css';
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
    .primary {
        background-color: #1570EF;
        color: #FFFFFF;
    }
    
    .primary:hover {
        background-color: #0C4EAE;
    }

    .secondary {
        background-color: #EFF8FF;
        color: #175CD3;
    }

    .secondary:hover {
        background-color: #CBE3F5;
    }
    
    .tertiary {
        background-color: #FFFFFF;
        color: #344054;
        border: #D0D5DD solid 1px;

    }

    .disabled {
        background-color: #EAECF0;
        color: #FFFFFF;
        cursor: not-allowed;
    }

    .error {
        background-color: #D92D20;
        color: #FFFFFF;
    }


    button {
        display: flex;
        align-items: center;
        justify-content: center;
		font-family: Inter, sans-serif;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        cursor: pointer;
        transition: 0.3s ease-in-out;
		min-height: 44px;
    }

	.full-width {
		width: 100%; /* Set width to 100% when fullWidth prop is true */
		text-align: center;
    }

    img {
        margin-right: 0.5rem;
		max-width: 1.5rem;
    }
    
</style>

<button class="{type}" on:click="{internalHandleClick}" text="{text}" class:full-width="{fullWidth}">
    {#if icon}
        <!-- svelte-ignore a11y-missing-attribute -->
        <img src="{icon}">
    {/if}

    {text}
    
    <slot></slot>
</button>
