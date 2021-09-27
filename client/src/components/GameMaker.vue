<template>
    <div class="game-maker" v-click-outside="onClickOutside">
        <button class="open-button" v-on:click="open = true">+</button>
        <dialog v-bind:open="open">
            <form>
                <label for="gameMakerTitle">Title: </label>
                <input v-model="title" name="title" id="gameMakerTitle" />
                <label for="gameMakerDescription">Description: </label>
                <textarea v-model="description" name="description" id="gameMakerDescription"></textarea>
                <label for="gameMakerSourceText">Source text: </label>
                <input v-model="source.text" name="source_text" id="gameMakerSourceText" />
                <label for="gameMakerSourceLink">Source link: </label>
                <input v-model="source.link" name="source_link" id="gameMakerSourceLink" />
                
                <label for="gameMakerPlayingWhite">Playing white: </label>
                <input v-model.number="playingWhite" type="number" name="playing_white" id="gameMakerPlayingWhite" />
                <label for="gameMakerPlayingBlack">Playing black: </label>
                <input v-model.number="playingBlack" type="number" name="playing_black" id="gameMakerPlayingBlack" />
            
                <input v-on:click="submit" type="submit" />
                <button v-on:click="cancel">Cancel</button>
            </form>
        </dialog>
    </div>
</template>

<script>
import Vue from 'vue'

Vue.directive('click-outside', {
  bind(el, binding, vnode) {
    el.clickOutsideEvent = (event) => {
      if (!(el === event.target || el.contains(event.target))) {
        vnode.context[binding.expression](event);
      }
    };
    document.body.addEventListener('click', el.clickOutsideEvent);
  },
  unbind(el) {
    document.body.removeEventListener('click', el.clickOutsideEvent);
  },
});

export default {
    name: 'game-maker',
    data() {
        return {
            open: false,
            title: '',
            description: '',
            source: {
                text: '',
                link: ''
            },
            playingWhite: 0,
            playingBlack: 1
        }
    },
    methods: {
        submit(e) {
            e.preventDefault()
            axios.post('/games', {
                title: this.title,
                description: this.description,
                source: this.source,
                playingWhite: this.playingWhite,
                playingBlack: this.playingBlack
            })
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
  });
        },
        onClickOutside() {
            this.open = false
        },
        cancel() {
            this.open = false
            this.title = ''
            this.description = ''
            this.source.text = ''
            this.source.link = ''
            this.playingWhite = 0
            this.playingBlack = 1
        }
    },
}
</script>

<style scoped>
.game-maker {
    width: 50px;
}
dialog {
    min-width: 80%;
    background: rgba(255,255,255,0.9);
}
form {
    padding: 24px;
    display: grid;
    grid-template-columns: 1fr 4fr;
    text-align: right;
}
</style>