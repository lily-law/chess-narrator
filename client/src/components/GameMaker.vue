<template>
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
    </form>
</template>

<script>

export default {
    name: 'game-maker',
    data() {
        return {
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
            // TODO post data
        }
    },
    components: {

    },
    created() {

    },
}
</script>
