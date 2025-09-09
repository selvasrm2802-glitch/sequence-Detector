# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

SEQUENCE = [1, 0, 1, 1]  # The sequence we want to detect: 1011

@cocotb.test()
async def test_moore_sequence_detector(dut):
    dut._log.info("Start Moore Sequence Detector Test")

    # Create a clock with 10 ns period
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Applying Reset")
    dut.rst_n.value = 0
    dut.ena.value = 1
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    # Function to apply one input bit per clock
    async def apply_bit(bit):
        dut.ui_in.value = bit
        await ClockCycles(dut.clk, 1)

    # Test 1: Feed some random bits, then the sequence
    dut._log.info("Feeding initial random bits")
    random_stream = [0, 1, 0, 0, 1]
    for bit in random_stream:
        await apply_bit(bit)
        assert dut.uo_out.value == 0, f"Unexpected detection at random stream with bit {bit}"

    # Test 2: Feed the actual sequence 1011
    dut._log.info(f"Feeding target sequence: {SEQUENCE}")
    for i, bit in enumerate(SEQUENCE):
        await apply_bit(bit)

    # Check detection after full sequence is applied
    assert dut.uo_out.value == 1, f"Sequence {SEQUENCE} not detected!"

    # Test 3: Check reset clears detection
    dut._log.info("Testing reset clears detection")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0, "Output not cleared after reset"

    dut._log.info("Moore Sequence Detector Test Passed")
