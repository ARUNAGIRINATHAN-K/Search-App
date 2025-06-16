let executionTime = 0;

function setup() {
    let canvas = createCanvas(400, 200);
    canvas.parent('canvas-container');
    background(255);
    noLoop(); 
}

function draw() {
    background(255);
    
    
    executionTime = window.executionTime || 0;
   
    let maxTime = 0.1; 
    let barHeight = map(executionTime, 0, maxTime, 0, 150);
    barHeight = Math.min(barHeight, 150); 
    barHeight = Math.max(barHeight, 10); 
    
    fill(100, 150, 255); 
    rect(50, 200 - barHeight, 100, barHeight);
    
   
    fill(0);
    textSize(16);
    textAlign(LEFT);
    text('Execution Time (s)', 50, 180);
    text(executionTime.toFixed(4), 50, 160);
}

function updateChart() {
    redraw(); 
}
window.updateChart = updateChart;
