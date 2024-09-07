<!-- Input Field with Validation Component

    Contains Input Field with title and built in validation

    Author: Rohit Valanki
    Last modified: 30/07/2024

-->
<script>
  export let label = "";
  export let value = "";
  export let placeholder = "";
  export let validationMessage = "";
  export let showValidation = false; // Default false state
  export let validationActive = false; // Default false state
  export let isPasswordType = false;
  export let onInput = () => {};
  export let isWithIcon = false; // allows for icon padding

  function handleInput(event) {
    $value = event.target.value;
    if (onInput) {
      onInput(value);
    }
  }

  // Generate a unique ID for the input field
  let inputId = `input-${Math.random().toString(36).substr(2, 9)}`;
</script>

<div id="login-form-container" class="mb-4">
  <label for={inputId} class="block text-gray-700 text-sm mb-1">{label}</label>
  {#if isPasswordType}
    <input
      id={inputId}
      type="password"
      bind:value
      {placeholder}
      on:input={handleInput}
      class="border-gray-300 rounded-lg w-full py-3 px-3 text-gray-700 text-sm placeholder:text-sm leading-tight focus:outline-none focus:shadow-outline"
      style="border-radius: 8px; border-width: 1px;"
    />
  {:else if isWithIcon}
    <input
      id={inputId}
      type="text"
      bind:value
      {placeholder}
      on:input={handleInput}
      class="pl-10 border-gray-300 rounded-lg w-full py-3 px-3 text-gray-700 text-sm placeholder:text-sm leading-tight focus:outline-none focus:shadow-outline"
      style="border-radius: 8px; border-width: 1px;"
    />
  {:else}
    <input
      id={inputId}
      type="text"
      bind:value
      {placeholder}
      on:input={handleInput}
      class="border-gray-300 rounded-lg w-full py-3 px-3 text-gray-700 text-sm placeholder:text-sm leading-tight focus:outline-none focus:shadow-outline"
      style="border-radius: 8px; border-width: 1px;"
    />
  {/if}
  {#if showValidation || validationActive || validationMessage}
    <p
      id="validation-message"
      class={validationActive
        ? "text-red-500 text-xs m-1"
        : "text-[#959595] text-xs m-1"}
    >
      {validationMessage}
    </p>
  {/if}
</div>