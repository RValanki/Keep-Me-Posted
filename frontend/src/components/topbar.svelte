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

<div class="TopBar">
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
                        <li><a href={"#"}>View Profile</a></li>
                        <li><a href={"#"}>Settings</a></li>
                        <li><a href={"#"}>Logout</a></li>
                    </ul>
                </div>
                {/if}
            </li>

        </ul>
        <hr class="line">
    </nav>
</div>

<style>
    nav {
        position: relative;
        width: 100%;
        padding-top: 50px;
    }
    .icon-container {
        display: inline-block;
        position: absolute;
        top: 0; 
    }
    .kmp-container {
        left: 3%;
    }
    .gear-container {
        right: 7%; 
        top: 15%;
        padding-right: 25px;
    }
    .gear-icon {
        height: 30px;
    }
    .profile-container {
        right: 3%; 
    }
    img {
        height: 42px; 
    }
    .gear-button, .profile-button {
        background: none;
        border: none;
        cursor: pointer;
        outline: none;
    }
    .dropdown {
        position: absolute;
        background-color: white;
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        z-index: 1;
        right: 0;
    }
    .dropdown ul {
        padding: 10px;
        list-style: none;
        margin: 0;
    }
    .dropdown li a {
        display: block;
        padding: 10px;
        color: black;
        text-decoration: none;
    }
    .dropdown li a:hover {
        background-color: #ddd;
    }
    .line {
        border-top: 1px black;
        position: absolute;
        width: 100%;
    }
</style>