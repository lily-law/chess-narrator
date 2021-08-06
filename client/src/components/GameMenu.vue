<template>
    <ul role="menu">
        <li is="game-menu-item" v-for="game in games" :key="game.id" :game="game"></li>
    </ul>
</template>

<script>
import axios from 'axios'
import GameMenuItem from './GameMenuItem.vue'

export default {
    name: 'game-menu',
    data() {
        return {
          games: [],
        }
    },
    methods: {
      getGames() {
        const path = 'http://localhost:5000/games'
        axios.get(path)
          .then((res) => {
            console.log(res.data)
            this.games = res.data.games
          })
          .catch((error) => {
            console.error(error)
          })
      },
    },
    components: {
        GameMenuItem
    },
    created() {
      this.getGames()
    },
}
</script>
