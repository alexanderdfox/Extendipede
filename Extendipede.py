import os
import math
import time
import shlex
import subprocess

DEFAULT_FREQUENCY = 60
DEFAULT_STATES = 100
DEFAULT_STEPS_PER_CYCLE = 40
DEFAULT_SLEEP_TIME = 0.05

def led_symbol(state):
    return "●" if state else "○"

def ac_signal(t, freq):
    return math.sin(2 * math.pi * freq * t)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_command(command):
    """Run a shell command and return its output (string)."""
    try:
        result = subprocess.run(
            shlex.split(command),
            capture_output=True,
            text=True
        )
        return result.stdout.strip() if result.stdout else result.stderr.strip()
    except Exception as e:
        return f"Error: {e}"

def extendipede_shell():
    print("Welcome to Extendipede.\n")
    print("Type commands to run. Type 'exit' to quit.\n")

    # Allow user to set number of states and frequency
    while True:
        try:
            num_states = input(f"Number of pipeline states [{DEFAULT_STATES}]: ").strip()
            num_states = int(num_states) if num_states else DEFAULT_STATES
            if num_states < 1:
                print("Number of states must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            freq = input(f"AC frequency in Hz [{DEFAULT_FREQUENCY}]: ").strip()
            freq = float(freq) if freq else DEFAULT_FREQUENCY
            if freq <= 0:
                print("Frequency must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    steps_per_cycle = DEFAULT_STEPS_PER_CYCLE
    sleep_time = DEFAULT_SLEEP_TIME

    while True:
        command = input("Extendipede> ").strip()
        if command.lower() in ["exit", "quit"]:
            break
        if not command:
            continue

        # Run the command
        output = run_command(command)

        # Simulate Extendipede pipeline
        t = 0
        dt = 1.0 / (freq * steps_per_cycle)

        stages = [False] * num_states

        for step in range(steps_per_cycle * 2):  # simulate 2 cycles
            v = ac_signal(t, freq)

            # Positive half cycle = advance command through pipeline
            if v > 0:
                # shift command "through" the stages
                stages = [True] + stages[:-1]
            else:
                # Reset LEDs when negative half cycle
                stages = [False] * num_states

            clear_screen()
            print(f"AC voltage: {v:.2f}  | Running: {command}\n")
            print(f"Extendipede Pipeline ({num_states} stages)\n")
            for i, s in enumerate(stages):
                print(f"Stage {i+1}: Input {led_symbol(s)} | Output {led_symbol(s)}")

            if stages[-1]:  # once command exits last stage, print result
                print("\nCommand Output:\n" + "-"*30)
                print(output)
                print("-"*30)

            time.sleep(sleep_time)
            t += dt

if __name__ == "__main__":
    extendipede_shell()
