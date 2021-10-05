<template>
    <ol class="chess-board">
        <ol v-for="[rowNumber, row] in Object.entries(rows).reverse()" :key="rowNumber+JSON.stringify(row)" class="row">
            <li v-for="[column, cell] in Object.entries(row)" :key="rowNumber+column+cell.unit"><img v-if="cell.unit.value" :src="`/assets/pieces/standard/${cell.unit.side}/${cell.unit.value}.png`" alt="" /></li>
        </ol>
    </ol>
</template>

<script>


export default {
    name: 'chess-board',
    data() {
        return {
          rows: {
                1: {
                    a: { unit: { value: 'R', side: 'light', moves: 0 } },
                    b: { unit: { value: 'N', side: 'light', moves: 0 } },
                    c: { unit: { value: 'B', side: 'light', moves: 0 } },
                    d: { unit: { value: 'Q', side: 'light', moves: 0 } },
                    e: { unit: { value: 'K', side: 'light', moves: 0 } },
                    f: { unit: { value: 'B', side: 'light', moves: 0 } },
                    g: { unit: { value: 'N', side: 'light', moves: 0 } },
                    h: { unit: { value: 'R', side: 'light', moves: 0 } }
                },
                2: {
                    a: { unit: { value: 'P', side:'light', moves: 0 } },
                    b: { unit: { value: 'P', side:'light', moves: 0 } },
                    c: { unit: { value: 'P', side:'light', moves: 0 } },
                    d: { unit: { value: 'P', side:'light', moves: 0 } },
                    e: { unit: { value: 'P', side:'light', moves: 0 } },
                    f: { unit: { value: 'P', side:'light', moves: 0 } },
                    g: { unit: { value: 'P', side:'light', moves: 0 } },
                    h: { unit: { value: 'P', side:'light', moves: 0 } }
                },
                3: {
                    a: { },
                    b: { },
                    c: { },
                    d: { },
                    e: { },
                    f: { },
                    g: { },
                    h: { }
                },
                4: {
                    a: { },
                    b: { },
                    c: { },
                    d: { },
                    e: { },
                    f: { },
                    g: { },
                    h: { }
                },
                5: {
                    a: { },
                    b: { },
                    c: { },
                    d: { },
                    e: { },
                    f: { },
                    g: { },
                    h: { }
                },
                6: {
                    a: { },
                    b: { },
                    c: { },
                    d: { },
                    e: { },
                    f: { },
                    g: { },
                    h: { }
                },
                7: {
                    a: { unit: { value: 'P', side: 'dark', moves: 0 } },
                    b: { unit: { value: 'P', side: 'dark', moves: 0 } },
                    c: { unit: { value: 'P', side: 'dark', moves: 0 } },
                    d: { unit: { value: 'P', side: 'dark', moves: 0 } },
                    e: { unit: { value: 'P', side: 'dark', moves: 0 } },
                    f: { unit: { value: 'P', side: 'dark', moves: 0 } },
                    g: { unit: { value: 'P', side: 'dark', moves: 0 } },
                    h: { unit: { value: 'P', side: 'dark', moves: 0 } }
                },
                8: {
                    a: { unit: { value: 'R', side: 'dark', moves: 0 } },
                    b: { unit: { value: 'N', side: 'dark', moves: 0 } },
                    c: { unit: { value: 'B', side: 'dark', moves: 0 } },
                    d: { unit: { value: 'Q', side: 'dark', moves: 0 } },
                    e: { unit: { value: 'K', side: 'dark', moves: 0 } },
                    f: { unit: { value: 'B', side: 'dark', moves: 0 } },
                    g: { unit: { value: 'N', side: 'dark', moves: 0 } },
                    h: { unit: { value: 'R', side: 'dark', moves: 0 } }
                }
            },
            bench: {}
        }
    },
    methods: {
        move: function (notation, toPlay) {
            if (!notation[0]) {
                console.warn('Empty move!') // TODO work out if this edge case needs handling
                return false
            }
            else if (notation.length < 2) {
                console.warn('Invalid move notation with length < 2!') 
                return false
            }

            const annotationLookup = {
                '+': 'check',
                '#': 'checkmate',
                '!': 'good move',
                '?': 'poor move'
            }
            // TODO
            // extract annotations
            
            // check if castling
            if (this.notation.includes('0-0-0')) {
                // TODO
                // castle queenside
            }
            else if (this.notation.includes('0-0')) {
                // TODO
                // castle kingside
            }

            const unitToMove = notation[0] === notation[0].toLowerCase() ? 'P' : this.notation[0]
            let unitToTake = this.notation.includes('x') && this.notation[this.notation.indexOf('x') + 1]
            if (unitToTake[0] && unitToTake[0] === unitToTake[0].toPlay) {
                unitToTake = 'P'
            }
            const move = notation.substr(notation.length-2).match(/[a-g]\d/)?.[0]
            const specifiedOrig = notation[notation.length-3].match(/[a-g1-8]/)?.[0] || notation[notation.length-4].match(/[a-g1-8]/)?.[0]

            const colToChar = (col) => String.fromCharCode(col + 96)

            const findPiece = (piece, side, baseRow, baseCol) => {
                let possibleCoords = []
                
                if (!baseRow && baseCol) {
                    // all coords
                    for (let r = 1; r <= 8; r++) {
                        for (let c = 1; c <= 8; c++) {
                            possibleCoords.push([[baseRow+r, baseCol+c]])
                        }
                    }
                }
                else {
                    switch(unitToMove) {
                        case 'B':
                            // search diagonals from move coords
                            for (let i = 1; i <= 8; i++) {
                                possibleCoords.push([[baseRow+i, baseCol+i], [baseRow-i, baseCol-i]])
                            }
                            break
                        case 'K':
                            possibleCoords = [
                                [baseRow+1, baseCol-1], [baseRow+1, baseCol], [baseRow+1, baseCol+1],
                                [baseRow, baseCol-1],                 [baseRow, baseCol+1],
                                [baseRow-1, baseCol-1], [baseRow-1, baseCol], [baseRow-1, baseCol+1]
                            ]
                            break
                        case 'N':
                            // search 1 baseRow + 2 cols and 2 rows + 1 baseCol from move coords
                            possibleCoords = [
                                [baseRow+2, baseCol-1], [baseRow+2, baseCol+1], 
                                [baseRow+1, baseCol-2], [baseRow+1, baseCol+2],  
                                [baseRow-1, baseCol-2], [baseRow-1, baseCol+2], 
                                [baseRow-2, baseCol-1], [baseRow-2, baseCol+1]
                            ]  
                            break
                        case 'P':
                            const orientatedRowDiff = baseRow+(toPlay === 'light' ? 1 : -1)
                            if (unitToTake) {
                                // search +1 and -1 baseCol + 1 baseRow toPlay === 'light' ? foward : backward
                                possibleCoords = [[orientatedRowDiff, baseCol-1], [orientatedRowDiff, baseCol+1]]
                            }
                            else {
                                // search 1 baseRow toPlay === 'light' ? foward : backward
                                possibleCoords = [[baseRow+(toPlay === 'light' ? 1 : -1), baseCol]]
                            }

                            // if first move, include 2 baseRow move
                            var firstMoveConditionalCoord = [baseRow+(toPlay === 'light' ? 2 : -2), baseCol]
                            if (this.rows[firstMoveConditionalCoord[0]]?.[colToChar(firstMoveConditionalCoord[1])]?.unit?.moves === 0) {
                                possibleCoords.push(firstMoveConditionalCoord)
                            }

                            // if opposing pawn is one baseRow above and on it's first move, include En Passant

                            break
                        case 'Q':
                            for (let i = 1; i <= 8; i++) {
                                possibleCoords.push([[baseRow+i, baseCol+i], [baseRow-i, baseCol-i]])
                                possibleCoords.push([
                                        [baseRow+i, baseCol], 
                                    [baseRow, baseCol-i], [baseRow, baseCol+i]
                                        [baseRow-i, baseCol], 
                                ])
                            }
                            break
                        case 'R':
                            // within baseRow and baseCol of move coords
                            for (let i = 1; i <= 8; i++) {
                                possibleCoords.push([
                                        [baseRow+i, baseCol], 
                                    [baseRow, baseCol-i], [baseRow, baseCol+i]
                                        [baseRow-i, baseCol], 
                                ])
                            }
                            break
                    }
                }

                if (specifiedOrig) {
                    possibleCoords = possibleCoords.filter(([row, col]) => Number.isInteger(specifiedOrig) ? row === specifiedOrig : colToChar(col) === specifiedOrig)
                }

                // check each possibleCoord
                let cells = []
                for (let [row, col] of possibleCoords) {
                    const cell = this.rows[row][col]
                    if (cell.side != side || cell.unit != piece) {
                        continue
                    }
                    cells.push({data: cell, location: row+colToChar(col)})
                }
                if (cells.length > 1) {
                    console.warn(`Notation ambigous, multiple possible pieces!: ${JSON.stringify(cells)}`)
                }
                else if (cells.length === 0) {
                    console.warn(`No valid cells found for notation!: ${notation}`)
                }

                return cells[0]
            }

            // if move not in notation find unitToTake
            let pieceToTake;
            if (!move) {
                if (!unitToTake) {
                    console.warn(`Invalid notation!: ${notation}`)
                    return 
                }

                const cell = findPiece(unitToTake, toPlay === 'light' ? 'dark' : 'light')
                pieceToTake = cell?.data
                move = cell?.location
            }

            // convert move char to int
            const [baseRow, baseCol] = [move[0], move.charCodeAt(0)-96]
            
            const cell = findPiece(unitToMove, toPlay, baseRow, baseCol)
            const pieceToMove = cell.data
            pieceToMove.unit.moves++
            this.rows[move[0]][move[1]].unit = { ...pieceToMove }
            this.rows[cell.location[0]][cell.location[1]].unit = {}

            return {
                from: { row: cell.location[0], col: cell.location[1] },
                pieceMoved: pieceToMove,
                pieceTaken: pieceToTake,
                on: { row: move[0], col: move[1] }
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