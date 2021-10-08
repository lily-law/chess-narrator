<template>
    <div class="game">
        <header>
            <home-button />
            <h1>{{ title }}</h1>
            <h2 :class="`to-play--${toPlay}`"><span v-if="turn > 0">{{ toPlay }} : Turn {{ turn }}</span></h2>
            <hamburger-menu />
        </header>
        <aside>
            <ol>
                <li v-for="item in Object.values(notation)" v-on:click="goto(item.order)"  :key="item.order">
                    <div class="list__move">{{ item.move }}</div>
                    <div v-if="item.comment" class="list__comment">- <span>{{ item.comment }}</span></div>
                </li>
            </ol>
        </aside>
        <main>
            <div v-on:click="() => { boardActive = !boardActive }">
                <chess-board :class="{board: true, 'board--active': boardActive}" ref="board" />
            </div> 
            <div class="move">
                <h3>{{ move }}</h3>
                <p class="full-move">{{ moveDescription }}</p>
            </div>
            <button v-on:click="next" class="next">{{this.turn === 0 ? 'Start' : 'Next'}}</button>
            <div class="commentry">{{ comment }}</div>
        </main>
    </div>
</template>

<script>
import HomeButton from '@/components/HomeButton.vue'
import HamburgerMenu from '@/components/HamburgerMenu.vue'
import ChessBoard from '@/components/ChessBoard.vue'

export default {
    components: {
        HomeButton,
        HamburgerMenu,
        ChessBoard
    },
    data: function () {
        return {
            id: this.$route.params.id,
            turn: 0,
            boardActive: false,
            moveDescription: '',

            // TEMP dummy data
            title: 'Someone vs Someone Else',
            notation: {
                1: {
                    order: 1, 
                    move: 'e4',
                    comment: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis semper arcu lacus, sit amet porttitor sem vehicula at. In ac turpis lacinia lectus rutrum sagittis. Nulla metus nulla, pellentesque ac magna et, elementum feugiat nisl. Proin bibendum ligula at arcu feugiat hendrerit. In purus turpis, tincidunt id neque accumsan, suscipit ultrices nisi. Maecenas posuere nunc ut efficitur pharetra. Quisque tristique blandit risus ut convallis.

Suspendisse suscipit leo at nunc tincidunt elementum. Donec luctus magna ac augue tristique, commodo pellentesque dui congue. Suspendisse potenti. Ut pulvinar cursus dolor, et efficitur leo congue nec. Fusce turpis urna, convallis sed feugiat id, viverra vel ex. Vestibulum ultricies ipsum in mauris aliquam luctus. Curabitur ut porttitor enim. Mauris et ultricies leo. Donec feugiat augue mauris, sed luctus dolor vestibulum at. Etiam iaculis ligula nec consectetur dictum. Nunc volutpat commodo nulla ac eleifend. Mauris varius dapibus massa non finibus. Vivamus malesuada malesuada ante, in sagittis ex venenatis sed. Suspendisse mattis risus dui, at dapibus enim pretium dapibus. Vivamus consectetur risus augue, eu venenatis lectus malesuada id. Duis sem ante, dapibus non magna eget, mollis porta magna.`
                },
                2: {
                    order: 2, 
                    move: 'd5',
                    comment: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis semper arcu lacus, sit amet porttitor sem vehicula at. In ac turpis lacinia lectus rutrum sagittis. Nulla metus nulla, pellentesque ac magna et, elementum feugiat nisl. Proin bibendum ligula at arcu feugiat hendrerit. In purus turpis, tincidunt id neque accumsan, suscipit ultrices nisi. Maecenas posuere nunc ut efficitur pharetra. Quisque tristique blandit risus ut convallis.

Suspendisse suscipit leo at nunc tincidunt elementum. Donec luctus magna ac augue tristique, commodo pellentesque dui congue. Suspendisse potenti. Ut pulvinar cursus dolor, et efficitur leo congue nec. Fusce turpis urna, convallis sed feugiat id, viverra vel ex. Vestibulum ultricies ipsum in mauris aliquam luctus. Curabitur ut porttitor enim. Mauris et ultricies leo. Donec feugiat augue mauris, sed luctus dolor vestibulum at. Etiam iaculis ligula nec consectetur dictum. Nunc volutpat commodo nulla ac eleifend. Mauris varius dapibus massa non finibus. Vivamus malesuada malesuada ante, in sagittis ex venenatis sed. Suspendisse mattis risus dui, at dapibus enim pretium dapibus. Vivamus consectetur risus augue, eu venenatis lectus malesuada id. Duis sem ante, dapibus non magna eget, mollis porta magna.`
                },
                3: {
                    order: 3,
                    move: 'c3'
                },
                4: {
                    order: 4,
                    move: 'c6'
                },
                5: {
                    order: 5,
                    move: 'Qh5'
                }
            }
        }
    },
    methods: {
        next: function() {
            if (!this.finalMove) {
                this.turn++
                const { description } = this.$refs.board.move(this.move, this.toPlay)
                this.moveDescription = description
            }
        },
        prev: function() {
            if (this.turn > 0) {
                this.turn--
                if (this.move) {
                    const { description } = this.$refs.board.undoMove()
                    this.moveDescription = description
                }
            }
        },
        goto: function(t) {
            if (this.turn === t) {
                return
            }
            if (this.turn > t) {
                this.prev()
            }
            else {
                this.next()
            }
            this.goto(t)
        }
    },
    computed: {
        move: function () {
            if (!this.notation[this.turn]?.move) {
                return ''
            }
            return this.notation[this.turn].move
        },
        comment: function () {
            if (!this.notation[this.turn]?.comment) {
                return ''
            }
            return this.notation[this.turn].commnet
        },
        toPlay: function () {
            return this.turn % 2 === 0 ? 'dark' : 'light'
        },
        finalMove: function () {
            return !this.notation[this.turn+1]
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
    .to-play--light {
        background-color: lightgray;
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
        opacity: 0.5;
        z-index: 10;
        transform: scale(0.9);
        background-color: white;
    }
    .board--active {
        position: absolute;
        top: 0;
        left: 0;
        width: 75vw;
        height: 75vw;
        opacity: 0.9;
        z-index: 100;
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
        font-size: 2.6vw;
        padding: 0.8em;
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