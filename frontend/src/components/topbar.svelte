<!-- Top Bar Component

    Contains top bar functionality and styling

    Author: mpha0039
    Edited by: dleu0007
    Last modified: 9/05/2024

 -->

<!--  -->
<script>
    // importing image elements
    import kmpIcon from '../assets/kmp-icon.png';
    import gearIcon from '../assets/gear-icon.png';
    import profileIcon from '../assets/profile-icon.png';

    // logic to handle gear click events
    function handleGearClick() {
        alert('BOoooooo');
    }

    let showDropdown = false;

    function toggleDropdown() {
        showDropdown = !showDropdown;
    }
</script>

<div class = 'TopBar'>
    <nav>
        <ul>
            <li>
                <img class="kmp-icon" src={kmpIcon} alt="KMP Icon" />
            </li>

            <li>
                <button class="gear-button" on:click={handleGearClick}>
                    <img class="gear-icon" src={gearIcon} alt="Gear Icon" />
                </button>
            </li>
            <li>
                <button on:click={toggleDropdown} class="profile-button">
                    <img class="profile-icon" src={profileIcon} alt="Profile Icon" />
                </button>
                {#if showDropdown}
                <div class="dropdown">
                    <ul>
                        <li><a href="#">View Profile</a></li>
                        <li><a href="#">Settings</a></li>
                        <li><a href="#">Logout</a></li>
                    </ul>
                </div>
                {/if}
            </li>

        </ul>
        <hr class="line">
    </nav>
</div>

<!-- make the toolbar permanent -->
<slot />

<!-- styling for the toolbar -->
<style>
    ul {
        display: flex;
        list-style: none;
    }
    li {
        margin-right: 30px;
    }
    .kmp-icon {
        width: 163px;
        height: 48px;
    }
    .gear-container {
        /* added for visualisation purposes */
        /* border: 1px solid red; */
        /* offset padding from the left edge by 70% of the viewport */
        padding-left: calc(73vw);
    }
    .gear-button {
        background: none;
        border: none;
        cursor: pointer;
        padding-left: calc(73vw);
        outline: none;
    }
    .profile-button {
        outline: none;
        background: none;
        border: none;
        cursor: pointer;
    }
    .gear-button:focus {
        outline: none;  /* Removes focus outline */
    }
    .gear-icon {
        width: 45px;
        height: 42px;
    }
    .profile-icon {
        width: 42px;
        height: 42px;
    }

    .line {
        border-top: 1px black;
        width: 100%
    }
    .dropdown {
        position: absolute;
        background-color: white;
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        z-index: 1;
        right: 0;
    }
    .dropdown ul {
        display: block;
        padding: 10px;
        list-style: none;
    }
    .dropdown li a {
        display: block;
        text-decoration: none;
        padding: 10px;
        color: black;
    }
    .dropdown li a:hover {
        background-color: #ddd;
    }
</style>