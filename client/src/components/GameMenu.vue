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
          games: [
            // temp placeholder data
            {
             'id': 0,
             'title': 'Someone vs Someone Else',
             'description': 'An example game to use as dummy data',
             'date': '2021-07-26T11:37:24.688Z',
             'source': {
                 'text': 'Made up by me',
                 'link': 'http://example.com'
              },
             'playingWhite': 0,
             'playingBlack': 1,
             'user_id': 0
         }
          ],
        }
    },
    methods: {
      getGames() {
        const path = 'http://localhost:5000/games'
        axios.get(path)
          .then((res) => {
            console.log(res.data)
            // this.games = res.data.games
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
