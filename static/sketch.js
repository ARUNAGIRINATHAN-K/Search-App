let executionTime = 0;

function setup() {
    let canvas = createCanvas(400, 200);
    canvas.parent('canvas-container');
    background(255); // White background for better contrast
    noLoop(); // Draw only once unless updated
}

function draw() {
    background(255);
    
    // Ensure executionTime is a number and handle small values
    executionTime = window.executionTime || 0;
    
    // Scale execution time for better visibility
    // Map times between 0 and 0.1 seconds to 0-150 pixels
    // Times larger than 0.1s will be capped at 150 pixels
    let maxTime = 0.1; // Adjust this based on typical execution times
    let barHeight = map(executionTime, 0, maxTime, 0, 150);
    barHeight = Math.min(barHeight, 150); // Cap at 150 pixels
    
    // Ensure a minimum bar height for visibility
    barHeight = Math.max(barHeight, 10); // Minimum height of 10 pixels
    
    // Draw the bar
    fill(100, 150, 255); // Blue bar
    rect(50, 200 - barHeight, 100, barHeight);
    
    // Draw text labels
    fill(0);
    textSize(16);
    textAlign(LEFT);
    text('Execution Time (s)', 50, 180);
    text(executionTime.toFixed(4), 50, 160);
}

// Function to update the chart when new data is available
function updateChart() {
    redraw(); // Redraw the canvas with the new executionTime
}

// Listen for changes in executionTime
window.updateChart = updateChart;