#unzipper
from glob import glob
import sys
import os
import zipfile

password = "infected"

unzipped = "/home/bluepython339/Documents/thesis/unzipped"

def write_csv(vir_name, APT, filename):
	with open(filename, 'a+') as f:
		print("writing: {}, of {}".format(vir_name, APT))
		f.write("{},{}\n".format(vir_name, APT))

def main(fname):
	current = os.getcwd()

	print(current)
	folders = os.listdir()
	for i in folders:
		sub = current+'/'+i
		try:
			inside = os.listdir(sub)
			for f in inside:
					try:
						with zipfile.ZipFile(sub+'/'+f, 'r') as zip_ref:
							zip_ref.setpassword(password.encode())
							zip_ref.extractall(unzipped)
						write_csv(f[:-4]+'.decomp', i, fname)
					except Exception:
						print("file: {} in {} not a zipfile".format(f,i))
		except Exception:
			print("error")

if __name__ == "__main__":
	main(sys.argv[1])