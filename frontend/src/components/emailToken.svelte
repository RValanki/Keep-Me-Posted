<!--Email Token Component -->

<script>
    import Button from './button.svelte';

    function deleteButtonClick(){
        
    }

</script>

<style>

    @import url("https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0");

    .token-body{
        display: inline-flex;
        align-items: center;
        border-radius: 30px;
        background-color: antiquewhite;
        padding: 5px 10px;
        color:black;
        margin-right: 10px;
    }

    .token-body-span span {
        margin-right:5px;
    }
</style>

<Button>
    
    handleClick = {deleteButtonClick}
    fullWidth={true}

    <span class = "material-symbols-outlined">close</span>

</Button>
