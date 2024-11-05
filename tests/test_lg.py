import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic_gates import *


# Test Binary Gates
def test_and_gate():
    gate = ANDGate("AND Test")
    gate.set_pins(1, 1)
    assert gate.get_output() == 1, "AND Gate failed on input (1,1)"
    
    gate.set_pins(1, 0)
    assert gate.get_output() == 0, "AND Gate failed on input (1,0)"
    
    gate.set_pins(0, 0)
    assert gate.get_output() == 0, "AND Gate failed on input (0,0)"

def test_or_gate():
    gate = ORGate("OR Test")
    gate.set_pins(1, 1)
    assert gate.get_output() == 1, "OR Gate failed on input (1,1)"
    
    gate.set_pins(1, 0)
    assert gate.get_output() == 1, "OR Gate failed on input (1,0)"
    
    gate.set_pins(0, 0)
    assert gate.get_output() == 0, "OR Gate failed on input (0,0)"

def test_xor_gate():
    gate = XORGate("XOR Test")
    gate.set_pins(1, 1)
    assert gate.get_output() == 0, "XOR Gate failed on input (1,1)"
    
    gate.set_pins(1, 0)
    assert gate.get_output() == 1, "XOR Gate failed on input (1,0)"
    
    gate.set_pins(0, 1)
    assert gate.get_output() == 1, "XOR Gate failed on input (0,1)"
    
    gate.set_pins(0, 0)
    assert gate.get_output() == 0, "XOR Gate failed on input (0,0)"

def test_nand_gate():
    gate = NANDGate("NAND Test")
    gate.set_pins(1, 1)
    assert gate.get_output() == 0, "NAND Gate failed on input (1,1)"
    
    gate.set_pins(1, 0)
    assert gate.get_output() == 1, "NAND Gate failed on input (1,0)"
    
    gate.set_pins(0, 0)
    assert gate.get_output() == 1, "NAND Gate failed on input (0,0)"

def test_nor_gate():
    gate = NORGate("NOR Test")
    gate.set_pins(1, 1)
    assert gate.get_output() == 0, "NOR Gate failed on input (1,1)"
    
    gate.set_pins(1, 0)
    assert gate.get_output() == 0, "NOR Gate failed on input (1,0)"
    
    gate.set_pins(0, 0)
    assert gate.get_output() == 1, "NOR Gate failed on input (0,0)"

def test_not_gate():
    gate = NOTGate("NOT Test")
    gate.set_pin(1)
    assert gate.get_output() == 0, "NOT Gate failed on input (1)"
    
    gate.set_pin(0)
    assert gate.get_output() == 1, "NOT Gate failed on input (0)"

# Test Half Adder
def test_half_adder():
    half_adder = HalfAdder()
    
    # Test 0 + 0
    half_adder.set_inputs(0, 0)
    assert half_adder.get_sum() == 0, "Half Adder sum failed on input (0,0)"
    assert half_adder.get_carry() == 0, "Half Adder carry failed on input (0,0)"
    
    # Test 1 + 0
    half_adder.set_inputs(1, 0)
    assert half_adder.get_sum() == 1, "Half Adder sum failed on input (1,0)"
    assert half_adder.get_carry() == 0, "Half Adder carry failed on input (1,0)"
    
    # Test 1 + 1
    half_adder.set_inputs(1, 1)
    assert half_adder.get_sum() == 0, "Half Adder sum failed on input (1,1)"
    assert half_adder.get_carry() == 1, "Half Adder carry failed on input (1,1)"

# Test Full Adder
def test_full_adder():
    full_adder = FullAdder()
    
    # Test 0 + 0 + 0
    full_adder.set_inputs(0, 0, 0)
    assert full_adder.get_sum() == 0, "Full Adder sum failed on input (0,0,0)"
    assert full_adder.get_carry() == 0, "Full Adder carry failed on input (0,0,0)"
    
    # Test 1 + 1 + 0
    full_adder.set_inputs(1, 1, 0)
    assert full_adder.get_sum() == 0, "Full Adder sum failed on input (1,1,0)"
    assert full_adder.get_carry() == 1, "Full Adder carry failed on input (1,1,0)"
    
    # Test 1 + 0 + 1
    full_adder.set_inputs(1, 0, 1)
    assert full_adder.get_sum() == 0, "Full Adder sum failed on input (1,0,1)"
    assert full_adder.get_carry() == 1, "Full Adder carry failed on input (1,0,1)"
    
    # Test 1 + 1 + 1
    full_adder.set_inputs(1, 1, 1)
    assert full_adder.get_sum() == 1, "Full Adder sum failed on input (1,1,1)"
    assert full_adder.get_carry() == 1, "Full Adder carry failed on input (1,1,1)"

# Test 8-bit Adder
def test_eight_bit_adder():
    eight_bit_adder = EightBitAdder()
    
    # Test adding 8-bit numbers [00000001] + [00000001]
    a = [0, 0, 0, 0, 0, 0, 0, 1]
    b = [0, 0, 0, 0, 0, 0, 0, 1]
    result, carry_out = eight_bit_adder.add(a, b)
    assert result == [0, 0, 0, 0, 0, 0, 1, 0], f"8-bit Adder failed on input {a} + {b}"
    assert carry_out == 0, f"8-bit Adder carry failed on input {a} + {b}"
    
    # Test adding [11111111] + [00000001]
    a = [1, 1, 1, 1, 1, 1, 1, 1]
    b = [0, 0, 0, 0, 0, 0, 0, 1]
    result, carry_out = eight_bit_adder.add(a, b)
    assert result == [0, 0, 0, 0, 0, 0, 0, 0], f"8-bit Adder failed on input {a} + {b}"
    assert carry_out == 1, f"8-bit Adder carry failed on input {a} + {b}"
