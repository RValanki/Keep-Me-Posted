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

  let showDropdown = false;

  function toggleDropdown() {
    showDropdown = !showDropdown;
  }

  function handleLogout() {
    console.log("todo - handle logout");
  }

  function handleGoHome () {
    console.log("todo - handle go to home")
  }

</script>

<div class="flex justify-between border-b">
  <div class="py-4 px-8 m">
    <button on:click={() => handleGoHome()}>
      <img class="h-12" src={kmpIcon} alt="KMP Icon" />
    </button>
  </div>

  <div class="py-4 px-8">
    <div>
      <button on:click={() => toggleDropdown()}>
        <div class="py-2 px-8">
          <img class="h-8" src={profileIcon} alt="Profile Icon" />
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
