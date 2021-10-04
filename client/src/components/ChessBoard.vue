<template>
    <ol class="chess-board">
        <ol v-for="[rowNumber, row] in Object.entries(data).reverse()" :key="rowNumber+JSON.stringify(row)" class="row">
            <li v-for="[column, cell] in Object.entries(row)" :key="rowNumber+column+cell.unit"><img v-if="cell.unit.value" :src="`/assets/pieces/standard/${cell.unit.side}/${cell.unit.value}.png`" alt="" /></li>
        </ol>
    </ol>
</template>

<script>


export default {
    name: 'chess-board',
    data() {
        return {
            
          data: {
                1: {
                    a: { unit: { value: 'R', side: 'light' } },
                    b: { unit: { value: 'N', side: 'light' } },
                    c: { unit: { value: 'B', side: 'light' } },
                    d: { unit: { value: 'Q', side: 'light' } },
                    e: { unit: { value: 'K', side: 'light' } },
                    f: { unit: { value: 'B', side: 'light' } },
                    g: { unit: { value: 'N', side: 'light' } },
                    h: { unit: { value: 'R', side: 'light' } }
                },
                2: {
                    a: { unit: { value: 'P', side:'light' } },
                    b: { unit: { value: 'P', side:'light' } },
                    c: { unit: { value: 'P', side:'light' } },
                    d: { unit: { value: 'P', side:'light' } },
                    e: { unit: { value: 'P', side:'light' } },
                    f: { unit: { value: 'P', side:'light' } },
                    g: { unit: { value: 'P', side:'light' } },
                    h: { unit: { value: 'P', side:'light' } }
                },
                3: {
                    a: { unit: '' },
                    b: { unit: '' },
                    c: { unit: '' },
                    d: { unit: '' },
                    e: { unit: '' },
                    f: { unit: '' },
                    g: { unit: '' },
                    h: { unit: '' }
                },
                4: {
                    a: { unit: '' },
                    b: { unit: '' },
                    c: { unit: '' },
                    d: { unit: '' },
                    e: { unit: '' },
                    f: { unit: '' },
                    g: { unit: '' },
                    h: { unit: '' }
                },
                5: {
                    a: { unit: '' },
                    b: { unit: '' },
                    c: { unit: '' },
                    d: { unit: '' },
                    e: { unit: '' },
                    f: { unit: '' },
                    g: { unit: '' },
                    h: { unit: '' }
                },
                6: {
                    a: { unit: '' },
                    b: { unit: '' },
                    c: { unit: '' },
                    d: { unit: '' },
                    e: { unit: '' },
                    f: { unit: '' },
                    g: { unit: '' },
                    h: { unit: '' }
                },
                7: {
                    a: { unit: { value: 'P', side: 'dark' } },
                    b: { unit: { value: 'P', side: 'dark' } },
                    c: { unit: { value: 'P', side: 'dark' } },
                    d: { unit: { value: 'P', side: 'dark' } },
                    e: { unit: { value: 'P', side: 'dark' } },
                    f: { unit: { value: 'P', side: 'dark' } },
                    g: { unit: { value: 'P', side: 'dark' } },
                    h: { unit: { value: 'P', side: 'dark' } }
                },
                8: {
                    a: { unit: { value: 'R', side: 'dark' } },
                    b: { unit: { value: 'N', side: 'dark' } },
                    c: { unit: { value: 'B', side: 'dark' } },
                    d: { unit: { value: 'Q', side: 'dark' } },
                    e: { unit: { value: 'K', side: 'dark' } },
                    f: { unit: { value: 'B', side: 'dark' } },
                    g: { unit: { value: 'N', side: 'dark' } },
                    h: { unit: { value: 'R', side: 'dark' } }
                }
            }
        }
    },
    methods: {
        move: function (value, toPlay) {
            if (!value[0]) {
                console.warn('Empty move!') // TODO work out if this edge case needs handling
                return false
            }

            const movingPeice = value[0] === value[0].toLowerCase() ? 'P' : this.value[0]
            let takenPeice = this.value.includes('x') && this.value[this.value.indexOf('x') + 1]
            if (takenPeice[0] && takenPeice[0] === takenPeice[0].toPlay) {
                takenPeice = 'P'
            }
            const move = this.move.substr(this.move.length-2)

            const findPeice = (piece, side, baseCoord, validDiffs) => {
                const getCells = () => {
                    const cells = []
                    const [baseRow, baseCol] = baseCoord.split('').reverse()
                    for (let diff of validDiffs) {
                        const potentialCells = Object.values(this.data).reduce((r, c) => r = [r, ...Object.values(c)])
                        if (diff.row) {
                            for (let i = diff.onwardOnly ? baseRow : baseRow - diff.row; i < )
                        }
                    }
                }
                // for each cell
                //      
            }

            switch(movingPeice) {
                case 'B':
                    // search diagonals from move coords
                    break;
                case 'K':
                    
                    break;
                case 'N':
                    // search 1 row + 2 cols and 2 rows + 1 col from move coords
                    findPeice('N', move, [ {rows: 1, cols: 2}, {rows: 2, cols: 1} ])
                    break;
                case 'P':
                    if (takenPeice) {
                        // search +1 and -1 col + 1 row toPlay === 'light' ? foward : backward
                        findPeice('P', move, [ {diagonals: toPlay === 'light' ? 1 : -1, onwardOnly: true} ])
                    }
                    else {
                        // search 1 row toPlay === 'light' ? foward : backward
                        findPeice('P', move, [ {rows: toPlay === 'light' ? 1 : -1, onwardOnly: true} ])
                    }
                    break;
                case 'Q':

                    break;
                case 'R':
                    // within row and col of move coords
                    break;
            }
        }
    }
}
</script>

<style scoped>
    .chess-board {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
    }
    .row {
        margin: 0;
        padding: 0;
        display: flex;
        flex-wrap: nowrap;
        height: 12.5%;
        width: 100%;
    }
    li {
        width: 12.5%;
        height: 100%;
        list-style: none;
    }
    li img {
        max-width: 100%;
    }
    .row:nth-child(1) li:nth-child(2), .row:nth-child(1) li:nth-child(4), .row:nth-child(1) li:nth-child(6), .row:nth-child(1) li:nth-child(8),
    .row:nth-child(2) li:nth-child(1), .row:nth-child(2) li:nth-child(3), .row:nth-child(2) li:nth-child(5), .row:nth-child(2) li:nth-child(7),
    .row:nth-child(3) li:nth-child(2), .row:nth-child(3) li:nth-child(4), .row:nth-child(3) li:nth-child(6), .row:nth-child(3) li:nth-child(8),
    .row:nth-child(4) li:nth-child(1), .row:nth-child(4) li:nth-child(3), .row:nth-child(4) li:nth-child(5), .row:nth-child(4) li:nth-child(7),
    .row:nth-child(5) li:nth-child(2), .row:nth-child(5) li:nth-child(4), .row:nth-child(5) li:nth-child(6), .row:nth-child(5) li:nth-child(8),
    .row:nth-child(6) li:nth-child(1), .row:nth-child(6) li:nth-child(3), .row:nth-child(6) li:nth-child(5), .row:nth-child(6) li:nth-child(7),
    .row:nth-child(7) li:nth-child(2), .row:nth-child(7) li:nth-child(4), .row:nth-child(7) li:nth-child(6), .row:nth-child(7) li:nth-child(8),
    .row:nth-child(8) li:nth-child(1), .row:nth-child(8) li:nth-child(3), .row:nth-child(8) li:nth-child(5), .row:nth-child(8) li:nth-child(7)
    {
        background-color: #808080;
    }
    
</style>