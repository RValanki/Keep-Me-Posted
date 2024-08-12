<!-- Top Bar Component

    Contains top bar functionality and styling

    Author: Maureen Pham
    Edited by: Danny Leung, Brenda Dang
    Last modified: 12/08/2024

 -->

<!--  -->
<script>
  // importing image elements
  import kmpIcon from "../assets/kmp-icon.png";
  import profileIcon from "../assets/profile-icon.png";
  import profileHoverIcon from "../assets/profile-icon-dark.png";
  import logOutIcon from "../assets/log-out-icon.png";
  import Button from "../components/button.svelte";
  import { authStore } from "../stores/auth-store.js";
  import { goto } from "$app/navigation";

  let showDropdown = false;
  let profileIcons = [profileIcon, profileHoverIcon];
  let currentIconIndex = 0;

  function toggleDropdown() {
    showDropdown = !showDropdown;
    currentIconIndex = (currentIconIndex + 1) % profileIcons.length;
  }

  function handleLogout() {
    console.log("todo - handle logout");
  }

  function handleGoHome () {
    console.log("todo - handle go to home")
  }

  function handleSignIn () {
    goto("/login")
  }

</script>

<div class="flex justify-center items-center justify-between border-b h-20">
  <div class="px-8 m">
    <button on:click={() => handleGoHome()}>
      <img class="h-12" src={kmpIcon} alt="KMP Icon" />
    </button>
  </div>

  <div class="px-8">
    <div>
      <button on:click={() => toggleDropdown()}>
        {#if (authStore["loggedIn"])}
        <div class="flex justify-center items-center px-8">
          <img class="h-6" src={profileIcons[currentIconIndex]} alt="Profile Icon" />
        </div>
        {:else}
          <Button type="secondary" text="Sign In" handleClick={handleSignIn}/>
        {/if}
      </button>
      {#if showDropdown}
        <div class="absolute bg-white shadow right-16 px-4 py-2 rounded-lg z-50">
          <div class="text-left w-32 py-2 rounded-lg">
            <div class="text-gray-500 text-base px-1 pb-2 w-full">
              {authStore["email"]}
            </div>
            
            <div class="w-full border-t border-gray-300"></div>
            
            <button on:click={() => handleLogout()}>
              <div class="justify-center items-center flex flex-row px-1 pt-3 w-full">
                <img class="h-4" src={logOutIcon} alt="Log Out Icon" />
                <div class="text-gray-700 text-base px-1">Log Out</div>
              </div>
            </button>
          </div>
        </div>
      {/if}
    </div>
  </div>
</div>
