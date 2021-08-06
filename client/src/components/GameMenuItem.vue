<template>
    <li>
        <h2><router-link :to="'/game/' + game.id">{{ game.title }}</router-link></h2>
        <p class="description">{{ game.description }}</p>
        <template v-if="game.source.link">
            <a class="source" :href="game.source.link">{{ game.source.text }}</a>
        </template>
        <p class="source" v-else>{{ game.source.text }}</p>
    </li>
</template>

<script>
    export default {
        name: 'game-menu-item',
        props: {
            game: Object
        }
    }
</script>
