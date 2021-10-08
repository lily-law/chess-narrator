<template>
    <ol class="chess-board">
        <ol v-for="[rowNumber, row] in Object.entries(rows).reverse()" :key="rowNumber+JSON.stringify(row)" class="row">
            <li v-for="[column, cell] in Object.entries(row)" :key="rowNumber+column+cell.unit+cell.highlight" :class="cell.highlight"><img v-if="cell.unit" :src="`/assets/pieces/standard/${cell.unit.side}/${cell.unit.value}.png`" alt="" /></li>
        </ol>
    </ol>
</template>

<script>

const colToChar = (col) => String.fromCharCode(col + 96)
const charToCol = (char) => char.charCodeAt(0)-96

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
            bench: {dark: {}, light: {}},
            history: []
        }
    },
    methods: {
        move: function (rawNotation, toPlay) {
            if (!rawNotation[0]) {
                console.warn('Empty move!') // TODO work out if this edge case needs handling
                return false
            }
            else if (rawNotation.length < 2) {
                console.warn('Invalid move notation with length < 2!') 
                return false
            }
            else if (!rawNotation.match(/\w\d|\d-d|\w\w\w/)) {
                console.warn(`Invalid move notation! ${rawNotation}`) 
                return false
            }

            const annotationLookup = {
                '+': 'check',
                '#': 'checkmate',
                '!': 'good move',
                '?': 'poor move'
            }

            // extract annotations
            const annoations = []
            const notation = rawNotation.split('').filter(char => {
                if (Object.keys(annotationLookup).includes(char)) {
                    annoations.push(annoationsLookup[char])
                    return false
                }
                return true
            }).join('')

            let changes = []
            let description
            
            // check if castling
            if (notation.includes('0-0')) {
                const r = toPlay === 'light' ? 1 : 8
                const kingCell = kingCell = this.rows[r]['e']
                let kingDest
                let rookCell
                let rookDest
                let freeCell
                if (notation.includes('0-0-0')) {
                    // castle queenside
                    kingDest = this.rows[r]['c']
                    rookCell = this.rows[r]['a']
                    rookDest = this.rows[r]['d']
                    freeCell = this.rows[r]['b']
                    description = 'Castled queenside'
                    changes.push({from: [r, 'e'], to: [r, 'c'] })
                    changes.push({from: [r, 'a'], to: [r, 'd'] })
                }
                else {
                    // castle kingside
                    kingDest = this.rows[r]['f']
                    rookCell = this.rows[r]['h']
                    rookDest = this.rows[r]['g']
                    freeCell = {}
                    description = 'Castled kingside'
                    changes.push({from: [r, 'e'], to: [r, 'f'] })
                    changes.push({from: [r, 'h'], to: [r, 'g'] })
                }

                if (kingCell.unit.moves > 0 || rookCell.unit.moves > 0) {
                    console.warn('Invalid castling, King or Rook has moved previously')
                    return
                }
                if (kingDest.unit || rookDest.unit || freeCell.unit) {
                    console.warn('Invalid castling, units are in the way')
                    return
                }

                kingDest.unit = { ...kingCell.unit }
                rookDest.unit = { ...rookCell.unit }
                delete kingCell.unit
                delete rookCell.unit

                this.history.push({
                    annoations,
                    description,
                    changes
                })

                return {
                    annoations,
                    description
                }
            }

            const unitToMove = notation[0] === notation[0].toLowerCase() ? 'P' : notation[0]
            let unitToTake = notation.includes('x') && notation[notation.indexOf('x') + 1]
            if (unitToTake[0] && unitToTake[0] === unitToTake[0].toLowerCase()) {
                unitToTake = 'P'
            }
            const move = notation.substr(notation.length-2).match(/[a-h]\d/)?.[0]
            const specifiedOrig = notation[notation.length-3]?.match(/[a-h1-8]/)?.[0] || notation[notation.length-4]?.match(/[a-h1-8]/)?.[0]

            const findPiece = (piece, side, baseRow, baseCol) => {
                let possibleCoords = []
                
                if (!baseRow || !baseCol) {
                    // all coords
                    for (let r = 1; r <= 8; r++) {
                        for (let c = 1; c <= 8; c++) {
                            possibleCoords.push(...[[baseRow+r, baseCol+c]])
                        }
                    }
                }
                else {
                    switch(unitToMove) {
                        case 'B':
                            // search diagonals from move coords
                            for (let i = 1; i <= 8; i++) {
                                possibleCoords.push(...[[baseRow+i, baseCol+i], [baseRow-i, baseCol-i]])
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
                            const orientatedRowDiff = baseRow+(toPlay === 'dark' ? 1 : -1)
                            if (unitToTake) {
                                // search +1 and -1 baseCol + 1 baseRow toPlay === 'light' ? foward : backward
                                possibleCoords = [[orientatedRowDiff, baseCol-1], [orientatedRowDiff, baseCol+1]]
                            }
                            else {
                                // search 1 baseRow toPlay === 'light' ? foward : backward
                                possibleCoords = [[orientatedRowDiff, baseCol]]
                            }

                            // if first move, include 2 baseRow move
                            var firstMoveConditionalCoord = [baseRow+(toPlay === 'dark' ? 2 : -2), baseCol]
                            if (this.rows[firstMoveConditionalCoord[0]]?.[colToChar(firstMoveConditionalCoord[1])]?.unit?.moves === 0) {
                                possibleCoords.push(firstMoveConditionalCoord)
                            }

                            break
                        case 'Q':
                            for (let i = 1; i <= 8; i++) {
                                possibleCoords.push(...[[baseRow+i, baseCol+i], [baseRow-i, baseCol-i]])
                                possibleCoords.push(...[
                                        [baseRow+i, baseCol], 
                                    [baseRow, baseCol-i], [baseRow, baseCol+i]
                                        [baseRow-i, baseCol], 
                                ])
                            }
                            break
                        case 'R':
                            // within baseRow and baseCol of move coords
                            for (let i = 1; i <= 8; i++) {
                                possibleCoords.push(...[
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
                
                // Remove any invalid coords
                possibleCoords = possibleCoords.filter(coord => coord && coord[0] > 0 && coord[0] < 9 && coord[1] > 0 && coord[1] < 9)
                for (let [row, col] of possibleCoords) {
                    const colChar = colToChar(col)
                    const cell = this.rows[row][colChar]
                    if (cell?.unit?.side != side || cell?.unit?.value != piece) {
                        continue
                    }
                    cells.push({data: cell, location: colChar+row})
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
            if (!move) {
                if (!unitToTake) {
                    console.warn(`Invalid notation!: ${notation}`)
                    return 
                }
                const cell = findPiece(unitToTake, toPlay === 'light' ? 'dark' : 'light')
                move = cell?.location
            }

            // Put taken piece in bench
            if (unitToTake) {
                // TODO: if opposing pawn is one row above and on it's first move, En Passant, taken piece is one row back
                if (unitToTake === 'P' && !this.rows[move[1]][move[0]].unit && this.rows[move[1] + (toPlay === 'light' ? -1 : 1)][move[0]].unit.value === 'P') {
                    this.bench[toPlay].push({ ...this.rows[move[1] + (toPlay === 'light' ? -1 : 1)][move[0]].unit })
                    this.rows[move[1] + (toPlay === 'light' ? -1 : 1)][move[0]].unit = {}
                }
                else if (this.rows[move[1]][move[0]].unit) {
                    this.bench[toPlay].push({ ...this.rows[move[1]][move[0]].unit })
                    this.rows[move[1]][move[0]].unit = {}
                }
            }

            // convert move char to int
            const [baseRow, baseCol] = [parseInt(move[1]), charToCol(move)]

            // Move piece
            const cell = findPiece(unitToMove, toPlay, baseRow, baseCol)
            const pieceToMove = cell.data
            pieceToMove.unit.moves++
            this.rows[move[1]][move[0]].unit = { ...pieceToMove.unit }
            delete this.rows[cell.location[1]][cell.location[0]].unit

            const getDescription = (moved, from, taken, onto) => {
                const movesLookup = {
                    'B': 'Bishop',
                    'K': 'King',
                    'N': 'Knight',
                    'P': 'Pawn',
                    'Q': 'Queen',
                    'R': 'Rook'
                }
                const movingPeice = movesLookup[moved]
                const takenPeice = taken && movesLookup[taken]
                return `${movingPeice} on ${from} ${takenPeice ? 'takes '+takenPeice+' on' : 'moves to'} ${onto}`
            }

            description = getDescription(unitToMove, cell.location, unitToTake, move)
            changes = [
                { from: [cell.location[1], cell.location[0]], to: [move[1], move[0]] }
            ]

            this.history.push({
                annoations,
                description,
                changes
            })

            this.highlightPath(changes[0])

            return {
                annoations,
                description
            }

        },
        undoMove: function () {
            const { annoations, description, changes } = this.history.pop()
            for (let {from, to} of changes) {
                const fromUnit = this.rows[from[0]][from[1]].unit ? {...this.rows[from[0]][from[1]].unit} : {}
                const toUnit = this.rows[to[0]][to[1]].unit ? {...this.rows[to[0]][to[1]].unit} : {}
                toUnit?.moves && toUnit.moves--
                // TODO handle taken pieces
                this.rows[from[0]][from[1]] = { ...this.rows[from[0]][from[1]], unit: toUnit }
                this.rows[to[0]][to[1]] = { ...this.rows[to[0]][to[1]], unit: fromUnit }
            }
            return {
                annoations,
                description
            }
        },
        highlightPath: function ({from, to}, knightMove) {
            this.clearPathHighlight()
        //    if (!knightMove) {   
                const colFrom = charToCol(from[1])
                const colTo = charToCol(to[1])
                console.log({rowFrom: from[0], colFrom, rowTo: to[0], colTo, })
                for (let r = from[0], c = colFrom; r != to[0] || c != colTo; r != to[0] && (from[0] < to[0] ? r++ : r--), c != colTo && (colFrom < colTo ? c++ : c--)) {
                    this.rows[r][colToChar(c)].highlight = 'trail'
                }
                this.rows[to[0]][to[1]].highlight = 'trail'
        //    }
        //    else {

         //   }
        },
        clearPathHighlight: function() {
            for (let row of Object.values(this.rows)) {
                for (let cell of Object.values(row)) {
                    delete cell.highlight
                }
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
    .trail {
        position: relative;
    }
    .trail::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: blue !important;
        opacity: 0.2;
    }
    
</style>