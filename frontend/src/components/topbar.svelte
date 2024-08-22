<!-- Top Bar Component

    Contains top bar functionality and styling

    Author: Maureen Pham
    Edited by: Danny Leung, Brenda Dang
    Last modified: 12/08/2024

 -->

<!--  -->
<script>
  // importing image elements and other components
  import kmpIcon from "../assets/kmp-icon.png";
  import profileIcon from "../assets/profile-icon.png";
  import profileHoverIcon from "../assets/profile-icon-dark.png";
  import logOutIcon from "../assets/log-out-icon.png";
  import Button from "../components/button.svelte";
  import { getAuth, authStore, clearAuth } from "../stores/auth-store.js";
  import { goto } from "$app/navigation";
  import { resetStores } from "../stores/reset-store.js";

  let showDropdown = false; // Boolean to dictate whether dropdown is visible
  let profileIcons = [profileIcon, profileHoverIcon]; // Array holding 2 forms of profile picture [default, on:hover]
  let currentIconIndex = 0; // Current profile icon form
  const auth = getAuth(); //
  
  let email = auth.email // Retrieve current email that is logged in
  
  // Function to toggle dropdown
  function toggleDropdown() {
    showDropdown = !showDropdown;
    currentIconIndex = (currentIconIndex + 1) % profileIcons.length;  // Changes profile icon on click (highlighted when dropdown is visible)
  }

  // Function to handle logging out
  function handleLogout() {
    clearAuth();
    resetStores();
    goto("/login");
    console.log("todo - handle logout");
  }

  // Function to handle going to main page (NOT sign in if they are signed in already)
  function handleGoHome () {
    console.log("todo - handle go to home")
  }

  // Function to handle navigating to sign in page
  function handleSignIn () {
    goto("/login")
  }

</script>

<body>
  <!-- Master div -->
  <div class="flex justify-center items-center justify-between border-b h-20">

    <!-- KMP logo -->
    <div class="px-8 m">
      <button on:click={() => handleGoHome()}>
        <img class="h-12" src={kmpIcon} alt="KMP Icon" />
      </button>
    </div>

    <!-- Top right element -->
    <div class="px-8 flex">
      <div>

        <!-- If user is logged in, show the profile icon -->

        {#if (auth.loggedIn)}
        <button on:click={() => toggleDropdown()}>
          <div class="flex justify-center items-center px-8">
            <img class="h-6" src={profileIcons[currentIconIndex]} alt="Profile Icon" />
          </div>
        </button>

        {:else}

        <!-- If user is not logged in, show button to navigate to sign in -->

          <Button type="secondary" text="Sign In" handleClick={handleSignIn}/>
        {/if}

        <!-- Dropdown (only accessible if user is logged in) -->
        {#if showDropdown}

          <!-- Show email that user is logged in with -->

          <div class="w-fit absolute bg-white shadow right-16 py-2 rounded-lg z-50">
            <div class="text-left w-fit py-2 rounded-lg">
              <div class="text-gray-500 text-base px-5 pb-2 w-full">
                {email}
              </div>

              <!-- Divider element -->
              
              <div class="w-full border-t border-gray-100"></div>

              <!-- Log out button -->
              
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
</body>