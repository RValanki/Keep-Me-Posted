<!-- Pop-Up Modal Component

    Contains pop-up modal

    Author: Brenda Dang
    Last modified: 8/08/2024

-->

<script>
    import Button from "./button.svelte";

    export let type = 'primary';  // Default type is primary (blue with 1 button)
    export let firstHandleClick = () => {};  // Click function for primary button (dark blue, or red)
    export let secondHandleClick = () => {};  // Click function for secondary button (light blue)
    export let header = 'Pop-Up Modal';  // Header of popup modal
    export let mainText = 'This is a pop-up modal.';  // Main text of popup modal
    export let firstButtonText = 'Button';  // Text for primary button (dark blue, or red)
    export let secondButtonText = 'Button';  // Text for secondary button (light blue)
    export let iconPath = '';
    export let width = '64';
</script>

<div class="justify-center items-center font-sans h-full transition ease-in-out duration-300">
    <div class="fixed inset-0 flex items-center justify-center w-full h-full bg-black backdrop-blur md:bg-opacity-70">
        <div class="bg-white rounded-lg p-4 w-{width}">
            {#if iconPath}
                <div class="flex items-center justify-center pb-2">
                    <img src={iconPath} alt="pop up icon"/>
                </div>  
            {/if}
            <div class="flex items-center justify-center text-gray-900 text-lg font-bold">
                {header}
            </div>
            <div class="flex items-center justify-center text-gray-500 text-sm pb-5 pt-2">
                {mainText}
            </div>
            {#if type === 'secondary'}
                <div class="flex items-center justify-between flex-row">
                    <Button type="secondary" text={secondButtonText} handleClick={secondHandleClick} />
                    <Button type=
                    {type === 'error' ? 'error' : 'primary'}
                    fullWidth= {type === 'primary' || type === 'error' ? true : false}
                    text={firstButtonText} 
                    handleClick={firstHandleClick}
                    />
                </div>
            {:else}
                <div class="w-full">
                    <Button type=
                    {type === 'error' ? 'error' : 'primary'}
                    fullWidth= {type === 'primary' || type === 'error' ? true : false}
                    text={firstButtonText} 
                    handleClick={firstHandleClick}
                    />
                </div>
            {/if}

        </div>
    </div>
</div>