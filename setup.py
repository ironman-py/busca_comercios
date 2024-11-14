from cx_Freeze import setup, Executable


executables = [Executable("main.py")]

setup(
    name="bot-busca",
    version="1.1",
    description="bot para buscas no google e bing",
    executables=executables,
    author='Leandro FB Lima'
)

