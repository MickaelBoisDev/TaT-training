<template>
    <div class="sidebar">
        <ul class="sidebar-menu">
            <li>
                <RouterLink to="/history" active-class="active">
                    <i class="fas fa-history"></i> <!-- Icône pour l'historique -->
                </RouterLink>
            </li>
            <li>
                <RouterLink to="/conversion" active-class="active">
                    <i class="fas fa-plus"></i>
                </RouterLink>
            </li>
        </ul>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.sidebar {
    width: 2rem;
    background-color: #4836489d;
    color: #ecf0f1;
    padding: 20px;
    box-shadow: 2px 0px 10px rgba(0, 0, 0, 0.1);
    transition: all 0.1s;
}

.sidebar-menu {
    list-style-type: none;
    padding: 0;
}

.sidebar-menu li {
    cursor: pointer;
    transition: background-color 0.3s, transform 0.3s;
    border-radius: 5px;
    margin-bottom: 10px;
    padding-top: 0.2rem;
    padding-bottom: 0.2rem;
    color: rgb(255, 255, 255);
    font-size: 1rem;
    text-align: center;
}

.active {
    color: #fff;
    transition: box-shadow 0.3s ease;
}

.sidebar-menu li:hover {
    transform: scale(1.02);
}

.fas {
    font-size: 24px;
    transition: color 0.3s ease;
    text-align: center;
    color: black;
    /* met la couleur en noir */

}

.fas:hover {
    color: rgb(225, 172, 237)
}
</style>
