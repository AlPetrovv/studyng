import csv
import os
import shutil
from os import PathLike
import abc

################################## FIRST EXAMPLE ####################################


################# FIRST PRINCIPE (SRP - Single Responsibility Principle) #################
# create additional class for clean folder,
# because another class in bad example had two responsibilities


class FolderCleanerSRP:
    @staticmethod
    def clean_folder(folder_path: str | bytes | PathLike) -> str | bool:
        try:
            shutil.rmtree(folder_path)
            return True
        except Exception as exc:
            return str(exc)


class FileStatUISRP:

    def __init__(self):
        self.stat_mngr = FileStatManagerSRP()
        self.cleaner = FolderCleanerSRP()

    def read_txt_stats(self, file_path):
        with open(file_path, "r") as f:
            self.stat_mngr.txt_stat.increase(lines=len(f.readlines()))
        print("the txt stats were updated")

    def read_csv_stats(self, file_path):
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            self.stat_mngr.csv_stat.increase(
                columns=len(next(reader)), lines=len(list(reader))
            )
        print("the csv stats were updated")

    def choose_file(self):
        while True:
            file_path = input("Enter a file path: ")
            if os.path.isfile(file_path):
                break
            else:
                print("Invalid file path")
        res = self.stat_mngr.choose_file(file_path)
        if res:
            print(res)
        else:
            print("File was updated")

    def clean_stats(self):
        while True:
            answers = input("Are you sure you want to clean the stats? (y/n)")
            if answers == "y":
                self.stat_mngr.clean_stats()
                print("Stats were cleaned")
                break
            elif answers == "n":
                print("Stats were not cleaned")
                break

    def show_stats(self):
        print(self.stat_mngr.get_stats())


class FileStatManagerSRP:
    def __init__(self):
        self.txt_stat = FileStats("txt")
        self.csv_stat = FileStats("csv")

    def read_txt_stats(self, file_path):
        try:
            with open(file_path, "r") as f:
                return self.txt_stat.increase(lines=len(f.readlines()))
        except Exception as exc:
            return str(exc)

    def read_csv_stats(self, file_path) -> str | None:
        try:
            with open(file_path, "r") as f:
                reader = csv.reader(f)
                self.csv_stat.increase(
                    columns=len(next(reader)), lines=len(list(reader))
                )
            return
        except Exception as exc:
            return str(exc)

    def choose_file(self, file_path: str | bytes | PathLike) -> str | None:
        if file_path.endswith(".txt"):
            return self.read_txt_stats(file_path)
        elif file_path.endswith(".csv"):
            return self.read_csv_stats(file_path)

    def clean_stats(self):
        self.txt_stat = FileStats("txt")
        self.csv_stat = FileStats("csv")

    def get_stats(self):
        return self.txt_stat, self.csv_stat


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

    ################# SECOND PRINCIPE (OCP - OPEN/CLOSED PRINCIPLE) #################
    # class can be open for extension, but closed for modification
    # if we need to modify class, we need to create new class from old class and modify it


class FileStatUIOCP:
    def __init__(self):
        self.stat_mngr = FileStatManagerOCP()
        self.cleaner = FolderCleanerSRP()

    def read_txt_stats(self, file_path):
        with open(file_path, "r") as f:
            self.stat_mngr.txt_stat.increase(lines=len(f.readlines()))
        print("the txt stats were updated")

    def read_csv_stats(self, file_path):
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            self.stat_mngr.csv_stat.increase(
                columns=len(next(reader)), lines=len(list(reader))
            )
        print("the csv stats were updated")

    def choose_file(self):
        while True:
            file_path = input("Enter a file path: ")
            if os.path.isfile(file_path):
                break
            else:
                print("Invalid file path")
        res = self.stat_mngr.choose_file(file_path)
        if res:
            print(res)
        else:
            print("File was updated")

    def clean_stats(self):
        while True:
            answers = input("Are you sure you want to clean the stats? (y/n)")
            if answers == "y":
                self.stat_mngr.clean_stats()
                print("Stats were cleaned")
                break
            elif answers == "n":
                print("Stats were not cleaned")
                break

    def show_stats(self):
        print(self.stat_mngr.get_stats())


class FileStatManagerOCP:
    def __init__(self):
        self.txt_stat = TxtFileStatsOCP()
        self.csv_stat = CsvFileStatsOCP()

    def read_txt_stats(self, file_path):
        try:
            with open(file_path, "r") as f:
                return self.txt_stat.increase(lines=len(f.readlines()))
        except Exception as exc:
            return str(exc)

    def read_csv_stats(self, file_path) -> str | None:
        try:
            with open(file_path, "r") as f:
                reader = csv.reader(f)
                self.csv_stat.increase(
                    columns=len(next(reader)), lines=len(list(reader))
                )
            return
        except Exception as exc:
            return str(exc)

    def choose_file(self, file_path: str | bytes | PathLike) -> str | None:
        if file_path.endswith(".txt"):
            return self.read_txt_stats(file_path)
        elif file_path.endswith(".csv"):
            return self.read_csv_stats(file_path)

    def clean_stats(self):
        self.txt_stat = TxtFileStatsOCP()
        self.csv_stat = CsvFileStatsOCP()

    def get_stats(self):
        return self.txt_stat, self.csv_stat


class FileStatsOCP(abc.ABC):

    def __init__(self, exts) -> None:
        self.files_num = 0
        self.exts = exts

    @abc.abstractmethod
    def increase(self):
        self.files_num += 1

    def __str__(self) -> str:
        return f"Files number: {self.files_num}"


class TxtFileStatsOCP(FileStatsOCP):
    def __init__(self):
        self.total_lines = 0
        super().__init__("txt")

    def increase(self, **params):
        super().increase()
        self.total_lines = 0
        self.total_lines += params["lines"]

    def __str__(self):
        res = f"Files number: {self.files_num}\n"
        res += f"Total lines: {self.total_lines}\n"
        return res


class CsvFileStatsOCP(FileStatsOCP):
    def __init__(self):
        self.total_lines = 0
        self.total_columns = 0
        super().__init__("csv")

    def increase(self, **params):
        super().increase()
        self.total_lines += params["lines"]
        self.total_lines += params["columns"]

    def __str__(self):
        res = f"Files number: {self.files_num}\n"
        res += f"Total lines: {self.total_lines}\n"
        res += f"Total columns: {self.total_columns}\n"
        return res

    #################### THIRD PRINCIPLE (LSR - Liskov Substitution Principle) ####################


class FileStatsLSR(abc.ABC):

    def __init__(self, ext) -> None:
        self.files_num = 0
        self.ext = ext

    @abc.abstractmethod
    def increase(self, **params):
        self.files_num += 1

    def __str__(self) -> str:
        return f"Files number: {self.files_num}"


class TxtFileStatsLSR(FileStatsLSR):
    def __init__(self, ext="txt"):
        self.total_lines = 0
        super().__init__("txt")

    @abc.abstractmethod
    def increase(self, **params):
        super().increase()
        self.total_lines = 0
        self.total_lines += params["lines"]

    def __str__(self):
        res = f"Files number: {self.files_num}\n"
        res += f"Total lines: {self.total_lines}\n"
        return res


class CsvFileStatsLSR(FileStatsLSR):
    def __init__(self, ext="csv"):
        self.total_lines = 0
        self.total_columns = 0
        super().__init__("csv")

    def increase(self, **params):
        super().increase()
        self.total_lines += params["lines"]
        self.total_lines += params["columns"]

    def __str__(self):
        res = f"Files number: {self.files_num}\n"
        res += f"Total lines: {self.total_lines}\n"
        res += f"Total columns: {self.total_columns}\n"
        return res

    ######################## FOURTH PRINCIPLE (ISP - Interface Segregation Principle)  ####################################
    # The ISP states that a class should not be forced to implement an interface that it does not use.
    # Better to create a separate interface for each feature then one for all feature
    # in this example Mixin are present interface


class CsvStatsMixin:
    def __init__(
        self,
    ):
        self.total_columns = 0

    def increase(self, **params):
        self.total_columns += params["columns"]

    def __str__(self):
        return f"Total columns: {self.total_columns}\n"


class TxtStatsMixin:
    def __init__(self):
        self.total_lines = 0

    def __str__(self):
        return f"Total lines: {self.total_lines}\n"

    def increase(self, **params):
        self.total_lines += params["lines"]


class FileStatsISP(abc.ABC):
    def __init__(self, ext) -> None:
        self.files_num = 0
        self.ext = ext

    @abc.abstractmethod
    def increase(self, **params):
        self.files_num += 1

    def __str__(self) -> str:
        return f"Files number: {self.files_num}"


class TxtFileStatsISP(FileStatsISP, TxtStatsMixin):
    def __init__(self, ext="txt"):
        super().__init__(ext)
        TxtStatsMixin.__init__(self)

    @abc.abstractmethod
    def increase(self, **params):
        super().increase()
        TxtStatsMixin.increase(self, **params)

    def __str__(self):
        res = super().__str__()
        res += TxtStatsMixin.__str__(self)
        return res


class CsvFileStatsISP(FileStatsISP, TxtStatsMixin, CsvStatsMixin):
    def __init__(self, ext="csv"):
        super().__init__(ext)
        TxtStatsMixin.__init__(self)
        CsvStatsMixin.__init__(self)

    def increase(self, **params):
        super().increase()
        TxtStatsMixin.increase(self, **params)
        CsvStatsMixin.increase(self, **params)

    def __str__(self):
        res = super().__str__()
        res += TxtStatsMixin.__str__(self)
        res += CsvStatsMixin.__str__(self)
        return res

    ################## FIFTH PRINCIPLE (DIP - Dependency Inversion Principle)  ####################################
    # The DIP states that a class should depend on abstractions, not on concretions.
    # All must be dependent on abstractions


class FileStatBack(abc.ABC):
    @abc.abstractmethod
    def choose_file(self, file_path: str | bytes | PathLike) -> str | None:
        pass

    @abc.abstractmethod
    def clean_stats(self):
        pass

    @abc.abstractmethod
    def get_stats(self):
        pass


class FileStatUIDIP:
    def __init__(self, back: FileStatBack) -> None:
        self.stat_mngr = back
        self.cleaner = FolderCleanerSRP()

    def read_txt_stats(self, file_path):
        with open(file_path, "r") as f:
            self.stat_mngr.txt_stat.increase(lines=len(f.readlines()))
        print("the txt stats were updated")

    def read_csv_stats(self, file_path):
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            self.stat_mngr.csv_stat.increase(
                columns=len(next(reader)), lines=len(list(reader))
            )
        print("the csv stats were updated")

    def choose_file(self):
        while True:
            file_path = input("Enter a file path: ")
            if os.path.isfile(file_path):
                break
            else:
                print("Invalid file path")
        res = self.stat_mngr.choose_file(file_path)
        if res:
            print(res)
        else:
            print("File was updated")

    def clean_stats(self):
        while True:
            answers = input("Are you sure you want to clean the stats? (y/n)")
            if answers == "y":
                self.stat_mngr.clean_stats()
                print("Stats were cleaned")
                break
            elif answers == "n":
                print("Stats were not cleaned")
                break

    def show_stats(self):
        print(self.stat_mngr.get_stats())


class FileStatManagerDIP(FileStatBack):
    def __init__(self):
        self.txt_stat = TxtFileStatsOCP()
        self.csv_stat = CsvFileStatsOCP()

    def read_txt_stats(self, file_path):
        try:
            with open(file_path, "r") as f:
                return self.txt_stat.increase(lines=len(f.readlines()))
        except Exception as exc:
            return str(exc)

    def read_csv_stats(self, file_path) -> str | None:
        try:
            with open(file_path, "r") as f:
                reader = csv.reader(f)
                self.csv_stat.increase(
                    columns=len(next(reader)), lines=len(list(reader))
                )
            return
        except Exception as exc:
            return str(exc)

    def choose_file(self, file_path: str | bytes | PathLike) -> str | None:
        if file_path.endswith(".txt"):
            return self.read_txt_stats(file_path)
        elif file_path.endswith(".csv"):
            return self.read_csv_stats(file_path)

    def clean_stats(self):
        self.txt_stat = TxtFileStatsOCP()
        self.csv_stat = CsvFileStatsOCP()

    def get_stats(self):
        return self.txt_stat, self.csv_stat


class FileStatsOCP(abc.ABC):

    def __init__(self, exts) -> None:
        self.files_num = 0
        self.exts = exts

    @abc.abstractmethod
    def increase(self):
        self.files_num += 1

    def __str__(self) -> str:
        return f"Files number: {self.files_num}"


class TxtFileStatsOCP(FileStatsOCP):
    def __init__(self):
        self.total_lines = 0
        super().__init__("txt")

    def increase(self, **params):
        super().increase()
        self.total_lines = 0
        self.total_lines += params["lines"]

    def __str__(self):
        res = f"Files number: {self.files_num}\n"
        res += f"Total lines: {self.total_lines}\n"
        return res


class CsvFileStatsOCP(FileStatsOCP):
    def __init__(self):
        self.total_lines = 0
        self.total_columns = 0
        super().__init__("csv")

    def increase(self, **params):
        super().increase()
        self.total_lines += params["lines"]
        self.total_lines += params["columns"]

    def __str__(self):
        res = f"Files number: {self.files_num}\n"
        res += f"Total lines: {self.total_lines}\n"
        res += f"Total columns: {self.total_columns}\n"
        return res


################################## SECOND EXAMPLE ####################################
