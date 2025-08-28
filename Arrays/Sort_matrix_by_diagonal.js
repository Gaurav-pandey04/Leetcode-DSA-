// Sort Matrix by Diagnoal 

grid = [[1,7,3],[9,8,2],[4,5,6]];

const n = grid.length;
const diagonals = {};

// Step 1: collect diagonals
for(let i=0; i<n; i++){
    for(let j=0; j<n; j++){
        const key = i-j;
        if(!diagonals[key]) diagonals[key] = [];
        diagonals[key].push(grid[i][j]);
    }
}

// Step 2: Sort the diagnoals
for(const key in diagonals){
    const k = parseInt(key);
    if(key >=0 ){
        diagonals[key].sort((a,b)=>b-a); // non - increasing
    }else{
        diagonals[key].sort((a,b)=>a-b); // non - decreasing
    }
}

// Step 3: Refil the grid
for(let i=0; i<n; i++){
    for(let j =0; j<n; j++){
        const key = i-j;
        grid[i][j] = diagonals[key].shift();
    }
}

console.log(grid)