import subprocess

a = input("enter url :- ")
b = ("sqlmap -u {} --dump-all --crawl=2 --batch").format(a)

subprocess.run(b , shell=True)

print("scan done")