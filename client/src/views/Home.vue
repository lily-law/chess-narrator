<template>
    <div>
        <header>
            <h1>Title</h1>
            <!-- TODO: USER/LOGIN -->
        </header>
        <main>
            <div class="tool-bar">
                <div>
                <!-- TODO: search -->
                </div>
                <div>
                <!-- TODO: sortbydate -->
                </div>
                <game-maker />
            </div>
            <game-menu />
        </main>
    </div>
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

<style scoped>
.tool-bar {
    display: flex;
    justify-content: space-between;
}
</style>