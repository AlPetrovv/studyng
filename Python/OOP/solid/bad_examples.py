import csv
import os
import shutil

############################## FIRST EXAMPLE ##############################


class FeliStatManager:
    def __init__(self, path):
        self.txt_stat = FileStats("txt")
        self.csv_stat = FileStats("csv")

    def read_txt_stats(self, file_path):
        with open(file_path, "r") as f:
            self.txt_stat.increase(lines=len(f.readlines()))
        print("the txt stats were updated")

    def read_csv_stats(self, file_path):
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            self.csv_stat.increase(columns=len(next(reader)), lines=len(list(reader)))
        print("the csv stats were updated")

    def choose_file(self):
        while True:
            file_path = input("Enter a file path: ")
            if os.path.isfile(file_path):
                break
            else:
                print("Invalid file path")
        if file_path.endswith(".txt"):
            self.read_txt_stats(file_path)
        elif file_path.endswith(".csv"):
            self.read_csv_stats(file_path)

    def clean_stats(self):
        while True:
            answers = input("Are you sure you want to clean the stats? (y/n)")
            if answers == "y":
                self.txt_stat = FileStats("txt")
                self.csv_stat = FileStats("csv")
                print("Stats were cleaned")
                break
            elif answers == "n":
                print("Stats were not cleaned")
                break

    def show_stats(self):
        print(self.txt_stat)
        print(self.csv_stat)

    def clean_folder(self):
        while True:
            folder_path = input("Enter a folder path: ")
            if os.path.isdir(folder_path):
                break
            else:
                print("Invalid folder path")
        while True:
            answers = input("Are you sure you want to clean the folder? (y/n)")
            if answers == "y":
                try:
                    shutil.rmtree(folder_path)
                    print("Folder was cleaned")
                    break
                except Exception as exc:
                    print("Folder was not cleaned")
            elif answers == "n":
                print("Folder was not cleaned")
                break


class FileStats:

    def __init__(self, *extensions):
        self.files_num = 0
        self.extensions = extensions
        if "txt" in self.extensions or "csv" in self.extensions:
            self.total_lines = 0
            if "csv" in self.extensions:
                self.total_columns = 0

    def increase(self, **params):
        self.files_num += 1
        if "txt" in self.extensions or "csv" in self.extensions:
            self.total_lines += params["lines"]
            if "csv" in self.extensions:
                self.total_columns += params["columns"]

    def __str__(self):
        res = f"Files number: {self.files_num}\n"
        if "txt" in self.extensions or "csv" in self.extensions:
            res += f"Total lines: {self.total_lines}\n"
            if "csv" in self.extensions:
                res += f"Total columns: {self.total_columns}\n"
        return res


############################ SECOND EXAMPLE ############################
