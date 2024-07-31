<script>
    export let type = "text";
    export let label = "";
    export let value = "";
    export let placeholder = "";
    export let validationMessage = "";
    export let showValidation = false; // Default false state
    export let validationActive = false; // Default false state
    export let onInput;
    
    function handleInput(event) {
      value = event.target.value;
      if (onInput) {
        onInput(value);
      }
    }
</script>
  
<div class="mb-4">
    <label class="block text-gray-700 text-sm mb-1">{label}</label>
    <input
      type={type}
      value={value}
      placeholder={placeholder}
      on:input={handleInput}
      class="border-gray-300 rounded-lg w-full py-2 px-3 text-gray-700 text-sm placeholder:text-sm leading-tight focus:outline-none focus:shadow-outline"
      style="border-radius: 8px; border-width: 1px;"
    />
    {#if showValidation| validationActive | validationMessage }
      <p class={validationActive ? "text-red-500 text-xs m-1" : "text-[#959595] text-xs m-1"}>
        {validationMessage}
      </p>
    {/if}
</div>
