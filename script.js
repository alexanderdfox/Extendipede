class ExtendipedeWeb {
    constructor() {
        this.numStates = 100;
        this.frequency = 60;
        this.stepsPerCycle = 40;
        this.sleepTime = 50;
        this.stages = [];
        this.t = 0;
        this.dt = 0;
        this.cycleCount = 0;
        this.isRunning = false;
        this.currentCommand = '';
        this.commandOutput = '';
        this.animationId = null;
        
        this.initializeElements();
        this.setupEventListeners();
        this.updatePipelineDisplay();
    }

    initializeElements() {
        this.numStatesInput = document.getElementById('numStates');
        this.frequencyInput = document.getElementById('frequency');
        this.stepsPerCycleInput = document.getElementById('stepsPerCycle');
        this.sleepTimeInput = document.getElementById('sleepTime');
        this.commandInput = document.getElementById('commandInput');
        this.runButton = document.getElementById('runButton');
        this.acValue = document.getElementById('acValue');
        this.currentCommandDisplay = document.getElementById('currentCommand');
        this.pipelineStages = document.getElementById('pipelineStages');
        this.commandOutput = document.getElementById('commandOutput');
        this.status = document.getElementById('status');
        this.cycleCountDisplay = document.getElementById('cycleCount');
    }

    setupEventListeners() {
        this.runButton.addEventListener('click', () => this.runCommand());
        this.commandInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.runCommand();
            }
        });

        // Update parameters when inputs change
        this.numStatesInput.addEventListener('change', () => {
            this.numStates = parseInt(this.numStatesInput.value);
            this.updatePipelineDisplay();
        });

        this.frequencyInput.addEventListener('change', () => {
            this.frequency = parseFloat(this.frequencyInput.value);
            this.updateDt();
        });

        this.stepsPerCycleInput.addEventListener('change', () => {
            this.stepsPerCycle = parseInt(this.stepsPerCycleInput.value);
            this.updateDt();
        });

        this.sleepTimeInput.addEventListener('change', () => {
            this.sleepTime = parseInt(this.sleepTimeInput.value);
        });
    }

    updateDt() {
        this.dt = 1.0 / (this.frequency * this.stepsPerCycle);
    }

    acSignal(t, freq) {
        return Math.sin(2 * Math.PI * freq * t);
    }

    ledSymbol(state) {
        return state ? "●" : "○";
    }

    async runCommand() {
        const command = this.commandInput.value.trim();
        if (!command || this.isRunning) {
            return;
        }

        this.currentCommand = command;
        this.commandInput.value = '';
        this.isRunning = true;
        this.runButton.disabled = true;
        this.status.textContent = 'Running';
        
        // Initialize pipeline
        this.stages = new Array(this.numStates).fill(false);
        this.t = 0;
        this.cycleCount = 0;
        this.updateDt();

        // Execute command (simulated for now)
        this.commandOutput = await this.executeCommand(command);
        
        // Start animation
        this.animate();
    }

    async executeCommand(command) {
        try {
            const response = await fetch('/api/execute', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ command: command })
            });
            
            const result = await response.json();
            
            if (result.success) {
                return result.output;
            } else {
                return `Error: ${result.output}`;
            }
        } catch (error) {
            console.error('Error executing command:', error);
            return `Network error: ${error.message}`;
        }
    }

    animate() {
        const animateFrame = () => {
            if (!this.isRunning) {
                return;
            }

            const v = this.acSignal(this.t, this.frequency);
            this.acValue.textContent = v.toFixed(2);

            // Positive half cycle = advance command through pipeline
            if (v > 0) {
                // Shift command "through" the stages
                this.stages = [true, ...this.stages.slice(0, -1)];
            } else {
                // Reset LEDs when negative half cycle
                this.stages = new Array(this.numStates).fill(false);
                this.cycleCount++;
                this.cycleCountDisplay.textContent = this.cycleCount;
            }

            this.updatePipelineDisplay();

            // Check if command has exited the last stage
            if (this.stages[this.numStates - 1]) {
                this.commandOutput.textContent = this.commandOutput;
                this.stopAnimation();
                return;
            }

            this.t += this.dt;
            this.animationId = setTimeout(animateFrame, this.sleepTime);
        };

        animateFrame();
    }

    stopAnimation() {
        this.isRunning = false;
        this.runButton.disabled = false;
        this.status.textContent = 'Ready';
        this.currentCommand = '';
        this.currentCommandDisplay.textContent = '-';
        
        if (this.animationId) {
            clearTimeout(this.animationId);
            this.animationId = null;
        }
    }

    updatePipelineDisplay() {
        this.pipelineStages.innerHTML = '';
        
        for (let i = 0; i < this.numStates; i++) {
            const stageElement = document.createElement('div');
            stageElement.className = 'pipeline-stage';
            
            const stageNumber = document.createElement('span');
            stageNumber.className = 'stage-number';
            stageNumber.textContent = `Stage ${i + 1}`;
            
            const stageLed = document.createElement('span');
            stageLed.className = `stage-led ${this.stages[i] ? 'active' : 'inactive'}`;
            stageLed.textContent = this.ledSymbol(this.stages[i]);
            
            stageElement.appendChild(stageNumber);
            stageElement.appendChild(stageLed);
            this.pipelineStages.appendChild(stageElement);
        }
    }
}

// Initialize the application when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new ExtendipedeWeb();
});

// Add some demo commands for testing
document.addEventListener('DOMContentLoaded', () => {
    const demoCommands = [
        'ls',
        'pwd', 
        'date',
        'whoami',
        'echo Hello Extendipede!'
    ];
    
    // Add demo buttons
    const commandSection = document.querySelector('.command-section');
    const demoSection = document.createElement('div');
    demoSection.className = 'demo-section';
    demoSection.innerHTML = `
        <h3>Demo Commands</h3>
        <div class="demo-buttons">
            ${demoCommands.map(cmd => `<button class="demo-btn" data-command="${cmd}">${cmd}</button>`).join('')}
        </div>
    `;
    commandSection.appendChild(demoSection);
    
    // Add demo button styles
    const style = document.createElement('style');
    style.textContent = `
        .demo-section {
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .demo-section h3 {
            color: #00ff88;
            margin-bottom: 15px;
            font-size: 1em;
        }
        
        .demo-buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        
        .demo-btn {
            padding: 8px 15px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 5px;
            color: #e0e0e0;
            cursor: pointer;
            font-family: inherit;
            font-size: 0.9em;
            transition: all 0.3s ease;
        }
        
        .demo-btn:hover {
            background: rgba(0, 255, 136, 0.2);
            border-color: #00ff88;
            color: #00ff88;
        }
    `;
    document.head.appendChild(style);
    
    // Add click handlers for demo buttons
    document.querySelectorAll('.demo-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const command = btn.getAttribute('data-command');
            document.getElementById('commandInput').value = command;
            document.getElementById('runButton').click();
        });
    });
});
