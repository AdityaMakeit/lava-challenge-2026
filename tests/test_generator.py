import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from src.generator import Generator


generator = Generator()

answer = generator.generate(
    query="What is Python?",
    context="""
Python is a programming language.
"""
)

print(answer)