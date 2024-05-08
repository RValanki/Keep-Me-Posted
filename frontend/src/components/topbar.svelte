import kmpIcon from '../assets/kmp-icon';

<!-- Top Bar Navigation Component

    Enables settings and profile on-click

    Author: mpha0039
    Edited by:
    Last modified: 9/05/2024

 -->

<nav>
    <h2> KMP </h2>
    <ul>
        <li>
            <img src={kmpIcon}</>
        </li>
        <li>
            <a href="/">Profile</a>
        </li>
    </ul>
</nav>

<!-- make the toolbar permanent -->
<slot />

<!-- styling for the toolbar -->
<style>
    ul {
        display: flex;
        list-style: none;
    }
    li {
        margin-right: 20px;
    }
</style>
