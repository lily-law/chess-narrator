<template>
    <div class="game">
        <header>
            <home-button />
            <h1>{{ title }}</h1>
            <h2>{{ turn % 2 == 0 ? 'White' : 'Black' }} : Turn {{ turn }}</h2>
            <hamburger-menu />
        </header>
        <aside>
            <ol>
                <li v-for="item in annotation" :key="item.order">
                    <div class="list__move">{{ item.move }}</div>
                    <div v-if="item.comment" class="list__comment">- <span>{{ item.comment }}</span></div>
                </li>
            </ol>
            <button>+</button>
        </aside>
        <main>
            <div class="board"></div>
            <div class="move">
                <h3>{{ annotation[turn].move }}</h3>
                <p class="full-move">{{ fullMove }}</p>
            </div>
            <button class="next">Next</button>
            <div class="commentry">{{ annotation[turn].comment }}</div>
        </main>
    </div>
</template>

<script>
import HomeButton from '@/components/HomeButton.vue'
import HamburgerMenu from '@/components/HamburgerMenu.vue'

export default {
    components: {
        HomeButton,
        HamburgerMenu
    },
    data: function () {
        return {
            id: this.$route.params.id,
            turn: 0,

            // TEMP dummy data
            title: 'Someone vs Someone Else',
            annotation: [
                {
                    order: 0, 
                    move: 'Ke4',
                    comment: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis semper arcu lacus, sit amet porttitor sem vehicula at. In ac turpis lacinia lectus rutrum sagittis. Nulla metus nulla, pellentesque ac magna et, elementum feugiat nisl. Proin bibendum ligula at arcu feugiat hendrerit. In purus turpis, tincidunt id neque accumsan, suscipit ultrices nisi. Maecenas posuere nunc ut efficitur pharetra. Quisque tristique blandit risus ut convallis.

Suspendisse suscipit leo at nunc tincidunt elementum. Donec luctus magna ac augue tristique, commodo pellentesque dui congue. Suspendisse potenti. Ut pulvinar cursus dolor, et efficitur leo congue nec. Fusce turpis urna, convallis sed feugiat id, viverra vel ex. Vestibulum ultricies ipsum in mauris aliquam luctus. Curabitur ut porttitor enim. Mauris et ultricies leo. Donec feugiat augue mauris, sed luctus dolor vestibulum at. Etiam iaculis ligula nec consectetur dictum. Nunc volutpat commodo nulla ac eleifend. Mauris varius dapibus massa non finibus. Vivamus malesuada malesuada ante, in sagittis ex venenatis sed. Suspendisse mattis risus dui, at dapibus enim pretium dapibus. Vivamus consectetur risus augue, eu venenatis lectus malesuada id. Duis sem ante, dapibus non magna eget, mollis porta magna.`
                }
            ]
        }
    },
    computed: {
        fullMove: function () {
            const movesLookup = {
                'K': 'Knight',

            }
            const move = this.annotation[this.turn].move;
            const peice = movesLookup[move[0]]

            return `${peice} to ${move.substr(1)}`
        }
    }
}
</script>

<style scoped>
    .game {
        display: grid;
        grid-template-areas: 
        "header header"
        "aside main";
        grid-template-rows: auto 1fr;
        min-height: 100vh;
        grid-template-columns: 25% auto;
    }
    header {
        grid-area: header;
        display: grid;
        grid-template-columns: 32px 4fr 8fr 2fr;
        align-items: center;
        justify-items: stretch;
        text-align: center;
    }
    .back-icon {
        margin: 12px;
        align-self: center;
    }
    h1 {
        font-size: 1.4em;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        margin: 0 6px;
    }
    h2 {
        font-size: .8em;
        margin: 0;
        background-color: grey;
        align-self: stretch;
        display: grid;
        align-items: center;
    }
    .menu-toggle {
        padding: 4px 12px;
        align-self: stretch;
        display: grid;
        align-items: center;
        justify-items: center;
    }

    aside {
        grid-area: aside;
        background-color: lightgray;
    }
    .list__move {
        font-size: 3vw;
    }
    .list__comment {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 90%;
        font-size: 1.8vw;
    }

    main {
        grid-area: main;
        display: grid;
        align-items: center;
        justify-items: center;
        position: relative;
        grid-template-rows: 15vw auto;
        padding-top: 15%;
    }
    .board {
        position: absolute;
        top: 0;
        left: 0;
        width: 40vw;
        height: 40vw;
        opacity: 0.8;
        z-index: 10;
        background-image: linear-gradient(45deg, #808080 25%, transparent 25%), linear-gradient(-45deg, #808080 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #808080 75%), linear-gradient(-45deg, transparent 75%, #808080 75%);
        background-size: 10vw 10vw;
        background-position: 0 0, 0 5vw, 5vw -5vw, -5vw 0;
        transform: scale(0.9);
    }
    .move {
        z-index: 20;
        display: grid;
        grid-template-areas: 
        "move move"
        ". fullmove";
        align-self: end;
    }
    h3 {
        font-size: 12vw;
        margin: 0;
        grid-area: move;
        align-self: end;
    }
    .full-move {
        align-self: start;
        font-size: 3vw;
        margin: 0;
        grid-area: fullmove;
    }
    .next {
        position: absolute;
        right: 3vw;
        top: 15vw;
        border-radius: 0.6em;
        font-size: 4vw;
        padding: 0.4em;
        font-weight: 600;
    }
    .commentry {
        margin: 5vw;
        padding: 1em;
        padding-top: 0;
        z-index: 20;
        max-height: 32vh;
        overflow-y: auto;
    }
</style>