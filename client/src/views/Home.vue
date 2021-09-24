<template>
    <main>
        <!-- TODO: USER/LOGIN -->
        <game-menu />
        <game-maker />
    </main>
</template>

<script>
import GameMenu from '@/components/GameMenu.vue'
import GameMaker from '@/components/GameMaker.vue'

export default {
    components: {
        GameMenu,
        GameMaker
    }
}
</script>