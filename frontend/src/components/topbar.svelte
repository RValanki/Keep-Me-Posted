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
  
  $: email = $authStore["email"];

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

  <div class="px-8 flex">
    <div>
      {#if (authStore["loggedIn"])}
      <button on:click={() => toggleDropdown()}>
        <div class="flex justify-center items-center px-8">
          <img class="h-6" src={profileIcons[currentIconIndex]} alt="Profile Icon" />
        </div>
      </button>
      {:else}
        <Button type="secondary" text="Sign In" handleClick={handleSignIn}/>
      {/if}
      {#if showDropdown}
        <div class="w-fit absolute bg-white shadow right-16 py-2 rounded-lg z-50">
          <div class="text-left w-fit py-2 rounded-lg">
            <div class="text-gray-500 text-base px-5 pb-2 w-full">
              {email}
            </div>
            
            <div class="w-full border-t border-gray-100"></div>
            
            <div class="flex w-full float-start items-start justify-start pt-3 pb-1 px-3">
              <button class="hover:bg-gray-100 rounded-lg font-sans justify-center items-center flex w-full h-8" on:click={() => handleLogout()}>
                <div class="justify-start items-center flex flex-row w-full ms-1 px-1">
                  <img class="h-4" src={logOutIcon} alt="Log Out Icon" />
                  <div class="text-gray-700 text-base px-3">Log Out</div>
                </div>
              </button>
            </div>
          </div>
        </div>
      {/if}
    </div>
  </div>
</div>
