<!-- Top Bar Component

    Contains top bar functionality and styling

    Author: mpha0039
    Edited by: dleu0007
    Last modified: 9/05/2024

 -->
<!-- importing image elements -->
<!-- exporting topbar elements to page -->
<!-- logic to handle click events -->
<script>
    import kmpIcon from '../assets/kmp-icon.png';
    import gearIcon from '../assets/gear-icon.png';
    import profileIcon from '../assets/profile-icon.png';

    function handleGearClick() {
        alert('BOoooooo');
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
                <div>
                    <img class="profile-icon" src={profileIcon} alt="Profile Icon" />
                </div>
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
</style>
