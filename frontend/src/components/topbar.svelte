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
    export let kmpIcon;
    export let gearIcon;
    export let profileIcon;
    export let line;
</script>

<div class = 'TopBar'>
    <nav>
        <ul>
            <li>
                <img class="kmp-icon" src={kmpIcon} alt="KMP Icon" />
            </li>

            <li>
                <div class="gear-container">
                    <img class="gear-icon" src={gearIcon} alt="Gear Icon" />
                </div>
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
