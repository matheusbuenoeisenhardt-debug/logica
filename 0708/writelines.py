#writelines()
linhas = ["linha1\n"
          "linha2\n"
          "linha3\n"
          "linha4\n"]
with open("0708/saida_lines.txt", "w") as f:
    f.writelines(linhas)