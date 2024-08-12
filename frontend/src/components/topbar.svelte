<!-- Top Bar Component

    Contains top bar functionality and styling

    Author: mpha0039
    Edited by: dleu0007
    Last modified: 9/05/2024

 -->

<!--  -->
<script>
  // importing image elements
  import kmpIcon from "../assets/kmp-icon.png";
  import profileIcon from "../assets/profile-icon.png";
  import profileHoverIcon from "../assets/profile-icon-dark.png";

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
        <div class="flex justify-center items-center px-8">
          <img class="h-6" src={profileIcons[currentIconIndex]} alt="Profile Icon" />
        </div>
      </button>
      {#if showDropdown}
        <div class="absolute bg-white shadow right-8 px-4 py-2 rounded-lg z-50">
          <ul class="hover:bg-slate-200 px-4 py-1 rounded-lg">
            <li><button on:click={() => handleLogout()}>Logout</button></li>
          </ul>
        </div>
      {/if}
    </div>
  </div>
</div>
