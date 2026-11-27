from main_funct import process_tape, validate_inputs, main
import pytest

def test_1():
    tape, data = process_tape("unary.json", "11-1=")
    validate_inputs(tape,data)

def test_2():
    tape, data = process_tape("unary_wrong.json", "11-1=")
    with pytest.raises(ValueError):
        validate_inputs(tape,data)

def test_3():
    tape, data = process_tape("unary.json", "11-1=")
    validate_inputs(tape,data)

def test_4():
    assert(main(["unary.json", "11-1="])) == 0
    assert(main(["unary_wrong.json", "11-1="])) == 1