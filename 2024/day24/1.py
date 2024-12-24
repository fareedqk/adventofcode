from typing import Dict, Set, Tuple
from rich import print

class CircuitSimulator:
    def __init__(self):
        self.wires: Dict[str, int] = {}
        self.gates: Dict[str, Tuple[str, str, str]] = {}  # output -> (op, in1, in2)
        self.processed_gates: Set[str] = set()
        
    def apply_gate(self, op: str, in1: int, in2: int) -> int:
        if op == "AND":
            return 1 if in1 == 1 and in2 == 1 else 0
        elif op == "OR":
            return 1 if in1 == 1 or in2 == 1 else 0
        elif op == "XOR":
            return 1 if in1 != in2 else 0
        raise ValueError(f"Unknown operation: {op}")
    
    def process_gate(self, output: str) -> bool:
        if output in self.processed_gates:
            return True
            
        if output not in self.gates:
            return output in self.wires
            
        op, in1, in2 = self.gates[output]
        
        # Try to process inputs if we don't have their values yet
        if in1 not in self.wires:
            if not self.process_gate(in1):
                return False
        if in2 not in self.wires:
            if not self.process_gate(in2):
                return False
                
        # Now we can process this gate
        self.wires[output] = self.apply_gate(op, self.wires[in1], self.wires[in2])
        self.processed_gates.add(output)
        return True
        
    def parse_input(self, filename: str):
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                    
                # Handle initial wire values
                if ':' in line:
                    wire, value = line.split(':')
                    self.wires[wire.strip()] = int(value.strip())
                    continue
                    
                # Handle gate definitions
                parts = line.split()
                if len(parts) == 5 and parts[3] == "->":
                    in1, op, in2, _, output = parts
                    self.gates[output] = (op, in1, in2)
    
    def simulate(self) -> int:
        # Process all z-wires
        z_wires = sorted([wire for wire in self.gates.keys() if wire.startswith('z')], 
                        key=lambda x: int(x[1:]) if x[1:].isdigit() else -1)
        
        # Process each z-wire
        for wire in z_wires:
            if not self.process_gate(wire):
                print(f"Failed to process wire: {wire}")
        
        # Build binary string
        binary = ""
        for wire in z_wires:
            if wire in self.wires:
                binary = str(self.wires[wire]) + binary  # Prepend the bit
        
        # Convert to decimal
        return int(binary, 2)

    def print_wire_values(self):
        # Print all wire values in sorted order
        z_wires = sorted([wire for wire in self.wires.keys() if wire.startswith('z')],
                        key=lambda x: int(x[1:]) if x[1:].isdigit() else -1)
        print("\nZ-wire values (from z0 to highest):")
        for wire in z_wires:
            print(f"{wire}: {self.wires[wire]}")

def main():
    simulator = CircuitSimulator()
    simulator.parse_input('2024/day24/input.txt')
    result = simulator.simulate()
    print(f"\nZ-wire values:")
    simulator.print_wire_values()
    print(f"\nFinal decimal number: {result}")
    binary = format(result, 'b')
    print(f"Binary representation: {binary}")
    print(f"Number of bits: {len(binary)}")

if __name__ == "__main__":
    main()