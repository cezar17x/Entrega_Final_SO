import subprocess

def test_suma():
    result = subprocess.run(["dist/calculadora.exe", "sumar", "2", "3"],
    capture_output=True, text=True)
    assert "5" in result.stdout